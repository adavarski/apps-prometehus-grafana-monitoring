import os
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor


def get_services_from_env():
    services_env = os.getenv('SERVICE_URLS')
    if not services_env:
        raise ValueError(
            "SERVICE_URLS environment variable is not set or is empty")

    services = [url.strip() for url in services_env.split(',') if url.strip()]
    if not services:
        raise ValueError(
            "No valid URLs found in SERVICE_URLS environment variable")

    return services


def make_request(url):
    try:
        response = requests.get(url)
        print(f"Request to {url}: Status {response.status_code}")
    except requests.RequestException as e:
        print(f"Request to {url} failed: {str(e)}")


def generate_traffic(services):
    while True:
        with ThreadPoolExecutor(max_workers=5) as executor:
            for _ in range(random.randint(1, 10)):
                url = random.choice(services)
                executor.submit(make_request, url)
        time.sleep(random.uniform(0.1, 1))


if __name__ == "__main__":
    try:
        services = get_services_from_env()
        print(f"Traffic generator started for services: {services}")
        generate_traffic(services)
    except ValueError as e:
        print(f"Error: {str(e)}")
        exit(1)
