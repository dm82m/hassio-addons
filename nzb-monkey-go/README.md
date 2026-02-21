[![buy_me_a_coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20me%20a%20coffee-yellow.svg?style=for-the-badge)](https://www.buymeacoffee.com/dirkmaucher)
[![paypal](https://img.shields.io/badge/If%20you%20like%20it-PayPal%20Me-blue.svg?style=for-the-badge)](https://paypal.me/dirkmaucher)

[![GitHub Repo stars](https://img.shields.io/github/stars/dm82m/hassio-addons?style=flat)](https://github.com/dm82m/hassio-addons/stargazers) _Thanks to everyone having starred my repo! To star it click [here](https://github.com/dm82m/hassio-addons), then click on the star on the top right. Thanks!_

# NZB-Monkey-Go

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]

## About

Ever wanted to have nzb-monkey-go directly accessible in your Home Assistant? Instead of finding your laptop that has it installed? And even better, so no need to use the command line but beeing able to use a lean and smart web interface? You found it! This app is exactly what you were searching for!

You can copy your NZBLINKs into the input field and start processing and all the rest is done automatically.
Also you are able to live edit your NZB-Monkey-Go configuration files. Yes we know, it is usually one file but we are providing two processing modes. One is called the 'normal' one. This one just has all the search engines. The other mode 'Direct Search' has its own configuration file and you can set all other search engines expcept the direct search to '0'. With that you are forcing NZB-Monkey-Go to use the direct search. 

## Installation & Configuration

[![Open your Home Assistant instance and show the add App repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fdm82m%2Fhassio-addons)

1. Install this App in your HAOS instance.
2. Enable to show it in your HAOS sidebar.
3. Start the App.
4. Open the App and go to the 'Configuration' and place your 'nzb-monkey-go.conf' and alternatively the 'nzb-monkey-go_direct.conf'.
5. Switch back to the 'Process Links' tab, put in your NZBLINKs and hit 'Start Processing'.

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
