#!/usr/bin/with-contenv bashio

cd /bin/resol-vbus/examples/json-live-data-server
cp /config/addons/config.js .
echo "--- VERSIONS ---"
echo "add-on version: 0.0.7"
echo -n "nodejs version: " && node --version
echo -n "npm version: " && npm --version
echo "--- DEVICES ---"
ls /dev/ttyUSB* || true
ls /dev/ttyACM* || true
echo "--- json-live-data-server ---"
node index.js
