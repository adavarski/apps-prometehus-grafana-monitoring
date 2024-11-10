import express from "express";
import promClient from "prom-client";

const app = express();

// Create a Registry to register the metrics
const register = new promClient.Registry();

// Enable the collection of default metrics
promClient.collectDefaultMetrics({ register });

// Create a custom metric
const httpRequestsTotal = new promClient.Counter({
  name: "http_requests_total",
  help: "Total number of HTTP requests",
  labelNames: ["method", "path", "status_code"],
});

// Register the custom metric
register.registerMetric(httpRequestsTotal);

// Middleware to increment the counter for each request
app.use((req, res, next) => {
  res.on("finish", () => {
    httpRequestsTotal.inc({
      method: req.method,
      path: req.path,
      status_code: res.statusCode,
    });
  });
  next();
});

app.get("/", (req, res) => {
  res.send("Hello from Node.js Express!");
});

// Expose the metrics endpoint
app.get("/metrics", async (req, res) => {
  res.set("Content-Type", register.contentType);
  res.end(await register.metrics());
});

app.listen(3000, () => console.log("Server is running on port 3000"));
