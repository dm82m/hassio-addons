#!/bin/bash
set -e

CONFIG_PATH=/data/options.json

MODE=$(jq --raw-output '.mode // empty' $CONFIG_PATH)
LOG=$(jq --raw-output '.log // empty' $CONFIG_PATH)

echo "--- VERSIONS ---"
echo "add-on version: 0.0.7"
echo -n "neolink version: " && neolink --version
echo "neolink mode: ${MODE}"
echo "ATTENTION: if you expected a newer Neolink version, please reinstall this Add-on!"
echo "--- Neolink ---"

case $LOG in
  debug)
    export RUST_LOG="neolink=debug"
    ;;
  info)
    export RUST_LOG="neolink=debug"
    ;;
  warn)
    export RUST_LOG="neolink=warn"
    ;;
  error)
    export RUST_LOG="neolink=error"
    ;;
  *)
    echo "Unknown log level"
    ;;
esac

case $MODE in
  rtsp)
    neolink rtsp --config /config/addons/neolink.toml
    ;;

  mqtt)
    neolink mqtt --config /config/addons/neolink.toml
    ;;

  dual)
    neolink mqtt-rtsp --config /config/addons/neolink.toml
    ;;

  *)
    echo -n "Unknown mode option"
    ;;
esac
