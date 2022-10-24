#!/usr/bin/with-contenv bashio
ARCH="$(bashio::info.arch)"

if [[ "aarch64" = *"${ARCH}"* ]]; then
    neolink_aarch64 rtsp --config /config/addons/neolink.toml
fi

if [[ "amd64" = *"${ARCH}"* ]]; then
    neolink_amd64 rtsp --config /config/addons/neolink.toml
fi

if [[ "armhf" = *"${ARCH}"* ]]; then
    neolink_armhf rtsp --config /config/addons/neolink.toml
fi

if [[ "i386" = *"${ARCH}"* ]]; then
    neolink_i386 rtsp --config /config/addons/neolink.toml
fi
