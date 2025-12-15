#!/bin/sh
set -e

if [ "${RUN_MIGRATION:-true}" = "true" ]; then
  echo "Running alembic migrations..."
  alembic upgrade head
else
  echo "Skipping alembic migrations"
fi

uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
