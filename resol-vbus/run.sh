#!/usr/bin/with-contenv bashio

cd /bin/resol-vbus/examples/json-live-data-server
cp /config/addons/config.js .
node --version
node index.js
