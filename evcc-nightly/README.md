[![buy_me_a_coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20me%20a%20coffee-yellow.svg?style=for-the-badge)](https://www.buymeacoffee.com/dirkmaucher)
[![paypal](https://img.shields.io/badge/If%20you%20like%20it-PayPal%20Me-blue.svg?style=for-the-badge)](https://paypal.me/dirkmaucher)

[![GitHub Repo stars](https://img.shields.io/github/stars/dm82m/hassio-addons?style=flat)](https://github.com/dm82m/hassio-addons/stargazers) _Thanks to everyone having starred my repo! To star it click [here](https://github.com/dm82m/hassio-addons), then click on the star on the top right. Thanks!_

# :tada: Good news!
I have implemented an official evcc nightly support for Home Assistant in the evcc project itself. Please migrate to it!

# Why should I migrate?

:rocket: First an easily: the old App is gone. And more importantly: The new App has update notficiations included, that means: whenever there is an new nightly, Home Assistant will tell you and you can run the upgrade! :)

# How can I migrate?
1. Remember the paths you used in the old nightly App for your configuration and db file, you need them in the new nightly App.
   1. In case that you had your db file in `/data/` (default), you need to manually extract the db file from this old App and put it into the new nightly App. A guide how to do that, can be found [here](https://docs.evcc.io/en/docs/installation/home-assistant#how-do-i-access-the-evcc-database).
2. Stop this old nightly App here.
3. Install the new nightly App [here](https://docs.evcc.io/en/docs/installation/home-assistant#installation).
4. Configure the paths for your configuration file and potentially aswell the one of the db file in the new nightly App.
   1. Remember to put back the db file if you extracted it like described in 1.i.
5. Start the new nightly App and check if everything is working. If not open an issue [here](https://github.com/evcc-io/hassio-addon/issues/new).
6. Uninstall the old nightly App and remove my App repository, if you do not use any other App I provide.

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
