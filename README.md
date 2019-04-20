## Online Video Converter Selenium Automator

Automates video conversion via [Online Video Converter](https://www.onlinevideoconverter.com/youtube-converter) using Selenium.

## Notes:
* This uses Chrome Web Driver.

## Features:
* Consecutive downloads.
* Downloads one video at a time. Checks for pending downloads at your downloads directory and prevents multiple active downloads.

## Installation

* Clone the project to any location on your machine.
* Set your Chrome's Downloads directory at the `config.json` file.
* Place a **videos.csv** file in the project's root containing all the video links you wanna download.
* Open a terminal and start the script by running: `$ python app.py`
