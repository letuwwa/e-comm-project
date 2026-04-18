# E-Commerce Project Backend

Backend API for an e-commerce study project.

## Technologies

- Python 3.13+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate / Alembic
- PostgreSQL
- Flask-JWT-Extended
- Flask-CORS
- python-dotenv
- uv
- Docker / Docker Compose
- Gunicorn
- Ruff

## How To Start

### 1. Configure environment variables

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Default Docker values:

```env
FLASK_ENV=development
POSTGRES_DB=e-comm
POSTGRES_USER=admin
POSTGRES_PASSWORD=change_me
DATABASE_URL=postgresql://admin:change_me@postgres:5432/e-comm
CORS_ORIGINS=http://localhost:5173
JWT_SECRET_KEY=change_me
```

Change `POSTGRES_PASSWORD` and `JWT_SECRET_KEY` for real use.

Inside Docker Compose, the database host is `postgres` and the port is `5432`.

### 2. Start with Docker Compose

Build and start the API and PostgreSQL:

```bash
docker compose up -d --build
```

The API will be available at:

```text
http://127.0.0.1:5000
```

PostgreSQL is exposed on the host at:

```text
localhost:5433
```

The app container waits for PostgreSQL to become healthy, then runs database migrations automatically before starting Gunicorn.

## Useful Commands

Start containers:

```bash
docker compose up -d
```

Rebuild the app image:

```bash
docker compose build app
```

View running containers:

```bash
docker compose ps
```

View app logs:

```bash
docker compose logs -f app
```

Stop containers and keep database data:

```bash
docker compose down
```

Stop containers and delete the local database volume:

```bash
docker compose down -v
```

Run migrations manually inside the app container:

```bash
docker compose exec app flask --app run.py db upgrade
```

Create a new migration after model changes:

```bash
docker compose exec app flask --app run.py db migrate -m "describe changes"
```

Run Ruff inside the app container:

```bash
docker compose exec app ruff check .
```

## Local Development Without Docker

Install `uv` if it is not already installed, then install dependencies:

```bash
uv sync
```

If running the app on the host while PostgreSQL is running in Docker, use this `DATABASE_URL` in `.env`:

```env
DATABASE_URL=postgresql://admin:change_me@localhost:5433/e-comm
```

Apply database migrations:

```bash
uv run flask --app run.py db upgrade
```

Create a new migration after model changes:

```bash
uv run flask --app run.py db migrate -m "describe changes"
```

Run Ruff:

```bash
uv run ruff check .
```
