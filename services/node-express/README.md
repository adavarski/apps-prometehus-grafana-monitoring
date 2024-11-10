# Node.js Express Microservice

This is a Node.js Express microservice that exposes metrics for Prometheus.

## Features

- Express web server
- Prometheus metrics endpoint
- Default metrics collection
- Custom HTTP request counter

## Getting Started

1. Make sure you have Node.js and npm installed.
2. Run `npm install` to install dependencies.
3. Run `npm start` to start the server.

The server will be available at `http://localhost:3000`.

## Endpoints

- `/`: Returns "Hello World!"
- `/metrics`: Exposes Prometheus metrics

## Docker

This service can be built and run as a Docker container. Use the provided Dockerfile to build the image.

## Metrics

- Default Node.js metrics are collected automatically.
- A custom `http_requests_total` counter tracks HTTP requests with labels for method, route, and status code.

For more information on available metrics, check the `/metrics` endpoint when the server is running.
