[![buy_me_a_coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20me%20a%20coffee-yellow.svg?style=for-the-badge)](https://www.buymeacoffee.com/dirkmaucher)

# Neolink

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

## About

This add-on allows you to run Neolink directly on your HAOS instance. If you don't know Neolink you might not need this add-on. Details can be found [here](https://github.com/QuantumEntangledAndy/neolink). This add-on uses the Neolink fork of @QuantumEntangledAndy which also supports MQTT.

## Installation & Configuration

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fdm82m%2Fhassio-addons)

1. Install this add-on in your HAOS instance.
2. The operating mode of Neolink defaults to `RTSP`. If you prefer `MQTT`, please change it within the add-on configuration. Or select `DUAL` if you want to use RTSP and MQTT in parallel.
3. Create the configuration file named `neolink.toml` in your HAOS `/config/addons/` folder.
   - For configuration please follow [these](https://github.com/QuantumEntangledAndy/neolink#configuration) instructions.
   - Sample config file can be found [here](https://raw.githubusercontent.com/QuantumEntangledAndy/neolink/master/sample_config.toml).
4. Start the add-on and check the log output.
5. The log level defaults to `INFO`. You can set it to error, warn, info, or debug. Most users can leave it at info, but debug can be helpful if you have issues.

<!--

Notes to developers after forking or using the github template feature:
- While developing comment out the 'image' key from 'example/config.yaml' to make the supervisor build the addon
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
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg?style=for-the-badge
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg?style=for-the-badge
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg?style=for-the-badge
