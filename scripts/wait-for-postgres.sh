#!/usr/bin/env bash
set -euo pipefail
until pg_isready -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB"; do
  sleep 1
done
