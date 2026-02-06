[![buy_me_a_coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20me%20a%20coffee-yellow.svg?style=for-the-badge)](https://www.buymeacoffee.com/dirkmaucher)
[![paypal](https://img.shields.io/badge/If%20you%20like%20it-PayPal%20Me-blue.svg?style=for-the-badge)](https://paypal.me/dirkmaucher)

[![GitHub Repo stars](https://img.shields.io/github/stars/dm82m/hassio-addons?style=flat)](https://github.com/dm82m/hassio-addons/stargazers) _Thanks to everyone having starred my repo! To star it click [here](https://github.com/dm82m/hassio-addons), then click on the star on the top right. Thanks!_

# Resol-VBus

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]

## About

This App allows you to run resol-vbus [json-live-data-server](https://github.com/danielwippermann/resol-vbus/tree/master/examples/json-live-data-server) directly on your HAOS instance. This is needed if you are using a Resol KM1, VBus/LAN or VBus/USB device and want to use the [hass-Deltasol-KM2](https://github.com/dm82m/hass-Deltasol-KM2) component to get your Resol data into Home Assistant.

## Installation & Configuration

[![Open your Home Assistant instance and show the add App repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fdm82m%2Fhassio-addons)

1. Install this App in your HAOS instance.
2. Create the configuration file named `config.js` in your HAOS `/addon_configs/a14d3924_resol-vbus/` folder.
   - For configuration please follow [these](https://github.com/danielwippermann/resol-vbus/tree/master/examples/json-live-data-server#configuration) instructions.
   - Sample config file can be found [here](https://raw.githubusercontent.com/danielwippermann/resol-vbus/master/examples/json-live-data-server/config.js.example).
3. Start the add-on and check the log output.

<!--

Notes to developers after forking or using the github template feature:
- While developing comment out the 'image' key from 'example/config.yaml' to make the supervisor build the App
  - Remember to put this back when pushing up your changes.
- When you merge to the 'main' branch of your repository a new build will be triggered.
  - Make sure you adjust the 'version' key in 'example/config.yaml' when you do that.
  - Make sure you update 'example/CHANGELOG.md' when you do that.
  - The first time this runs you might need to adjust the image configuration on github container registry to make it public
- Adjust the 'image' key in 'example/config.yaml' so it points to your username instead of 'home-assistant'.
  - This is where the build images will be published to.
- Rename the example directory.
  - The 'slug' key in 'example/config.yaml' should match the directory name.
- Adjust all keys/url's that points to 'home-assistant' to now point to your user/fork.
- Share your repository on the forums https://community.home-assistant.io/c/projects/9
- Do awesome stuff!
 -->

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg?style=for-the-badge
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg?style=for-the-badge
