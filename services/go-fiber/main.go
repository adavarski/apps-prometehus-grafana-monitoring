package main

import (
	"strconv"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/adaptor"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	httpRequestsTotal = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "http_requests_total",
			Help: "Total number of HTTP requests",
		},
		[]string{"method", "endpoint", "status_code"},
	)
)

func init() {
	prometheus.MustRegister(httpRequestsTotal)
}

func main() {
	app := fiber.New()

	app.Use(func(c *fiber.Ctx) error {
		err := c.Next()
		httpRequestsTotal.WithLabelValues(c.Method(), c.Path(), strconv.Itoa(c.Response().StatusCode())).Inc()
		return err
	})

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello from Go Fiber!")
	})

	app.Get("/metrics", adaptor.HTTPHandler(promhttp.Handler()))

	app.Listen(":9000")
}