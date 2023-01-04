#!/usr/bin/with-contenv bashio

cd /bin/resol-vbus/examples/json-live-data-server
cp /config/addons/config.js .
echo "--- VERSIONS ---"
echo -n "nodejs version: " && node --version
echo -n "npm version: " && npm --version
echo "--- DEVICES ---"
ls /dev/tty*
echo "--- json-live-data-server ---"
node index.js
