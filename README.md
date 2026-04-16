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
- Ruff

## How To Start

### 1. Install dependencies

Install `uv` if it is not already installed, then install the project dependencies:

```bash
uv sync
```

### 2. Configure environment variables

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Fill in the required values:

```env
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
CORS_ORIGINS=http://localhost:5173
JWT_SECRET_KEY=replace-with-a-secure-secret
```

`DATABASE_URL`, `CORS_ORIGINS`, and `JWT_SECRET_KEY` are required by the application.

### 3. Prepare the database

Make sure PostgreSQL is running and the database from `DATABASE_URL` exists.

Apply database migrations:

```bash
uv run flask --app run.py db upgrade
```

### 4. Run the application

Start the Flask development server:

```bash
uv run python run.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Useful Commands

Run migrations:

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
