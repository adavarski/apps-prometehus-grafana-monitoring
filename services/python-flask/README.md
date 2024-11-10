# Python Flask Microservice

This is a Python Flask microservice that exposes metrics for Prometheus.

## Features

- Flask web server
- Prometheus metrics endpoint
- Default metrics collection
- Custom HTTP request counter

## Getting Started

1. Make sure you have Python and pip installed.
2. Run `pip install -r requirements.txt` to install dependencies.
3. Run `python app.py` to start the server.

The server will be available at `http://localhost:8000`.

## Endpoints

- `/`: Returns "Hello World!"
- `/metrics`: Exposes Prometheus metrics

## Docker

This service can be built and run as a Docker container. Use the provided Dockerfile to build the image.

## Metrics

- Default Flask metrics are collected automatically.
- A custom `http_requests_total` counter tracks HTTP requests with labels for method, endpoint, and status code.

For more information on available metrics, check the `/metrics` endpoint when the server is running.
