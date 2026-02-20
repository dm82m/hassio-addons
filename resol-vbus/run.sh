#!/usr/bin/with-contenv bashio

if [ -f "/homeassistant/addons/config.js" ]; then
    echo "Migrating '/homeassistant/addons/config.js' to '/addon_configs/a14d3924_resol-vbus/config.js'"
    cp /homeassistant/addons/config.js /config/
    mv /homeassistant/addons/config.js /homeassistant/addons/config.js.migrated
fi

cd /bin/resol-vbus/examples/json-live-data-server
cp /config/config.js .
echo "--- VERSIONS ---"
echo "App version: 0.0.9"
echo -n "nodejs version: " && node --version
echo -n "npm version: " && npm --version
echo "--- DEVICES ---"
ls /dev/ttyUSB* || true
ls /dev/ttyACM* || true
echo "--- json-live-data-server ---"
node index.js
