# A4 — Docker Compose + PostgreSQL

A self-contained ETL pipeline running two Docker containers together — one for Python, one for PostgreSQL — communicating over a Docker Compose network.

## What it does

Fetches 7 days of EUR exchange rates from the [Frankfurter API](https://www.frankfurter.app/) and loads them into a PostgreSQL database — all inside Docker, with no local setup required.

Pipeline steps:
1. Waits until PostgreSQL is ready (retry logic for the startup race condition)
2. Creates the `exchange_rates` table if it doesn't exist
3. Fetches 7 days of rates from Frankfurter (EUR → USD, HUF, AUD)
4. Inserts the results into PostgreSQL (`ON CONFLICT DO NOTHING` prevents duplicates on re-runs)

## Project structure

```
a4-docker-compose-postgresql/
├── docker-compose.yml   # defines the app and db services
├── Dockerfile           # builds the Python container
├── main.py              # ETL pipeline script
├── requirements.txt     # Python dependencies
└── .env                 # database credentials (not committed)
```

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Setup

Create a `.env` file in the project root:

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=exchange_rates
DB_USER=user
DB_PASSWORD=pass123
```

## How to run

Build and run both containers:

```bash
docker compose up --build
```

The script runs automatically and exits when done. Exit code 0 means success.

## Verify the data

Start the database container on its own:

```bash
docker compose up -d db
```

Connect to it:

```bash
docker compose exec db psql -U user -d exchange_rates
```

Query the results:

```sql
SELECT * FROM exchange_rates;
```

## Key concepts

- **Docker Compose networking** — containers communicate using service names (`db`) instead of `localhost`
- **Startup race condition** — `depends_on` doesn't guarantee PostgreSQL is ready; retry logic handles the gap
- **ETL pattern** — fetch, transform, and load are separate functions with clear responsibilities
- **Idempotency** — running the script multiple times produces the same result, no duplicate rows