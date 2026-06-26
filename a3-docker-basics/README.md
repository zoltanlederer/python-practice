# A3 — Docker

A small script that fetches data from a public API, processes it slightly, and prints the result to the terminal. Nothing goes to a database.

## What it does

- Load the city name from .env
- Look it up in the CITIES dictionary to get coordinates
- Build the API URL with those coordinates
- Call the API with requests
- Parse the JSON response
- Print the temperature

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

## How to run it

1. Copy the example env file
```
cp .env.example .env
```

2. Build the Docker image
```
docker build -t a3-weather .    
```

3. Pass environment variable at run time
```
docker run -e CITY=budapest a3-weather
```

## Available cities

- `budapest`
- `london`

If an unknown city is provided, it defaults to `london`.