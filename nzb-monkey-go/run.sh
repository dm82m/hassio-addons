#!/usr/bin/env bashio

echo "App version: 0.0.3"

export HOME=/root

streamlit run /usr/src/app/nmg-web.py --server.port 8501 --server.address 0.0.0.0
