#!/bin/bash
echo "[HOOK] Running Django migrations inside container..."
python manage.py migrate --noinput
