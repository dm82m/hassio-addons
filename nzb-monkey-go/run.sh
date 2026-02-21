#!/usr/bin/env bashio

echo "App version: 0.0.2"

export HOME=/root

streamlit run /app.py --server.port 8501 --server.address 0.0.0.0
