# Async-Weather-API
 Asyncronic weather API on grequests. This application helps to determine the weather by coordinates almost anywhere in the world.

# Contents
- [How it works](#how-it-works)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Structure](#structure)
- [Overview](#overview)

# How it works
This project works on Python 3 with grequests and tkinter.

# Requirements
```
requests
```
```
grequests
```
```
emoji
```
All requirements contains in requirements.txt.

Also, project use unique WeatherApi token.

# Quick Start
To run the project, run the following commands:
```bash
cd Async-Weather-API
```
```
pip install -r requirements.txt
```
```
python async_weather_api.py
```

# Structure
Project have one folder with weather data in Queenstown, NZ and Ceske Budejovice, CZ.
And next files:
* 🎉 async_wether_api.py - main logic and GUI
* 🎈 connections.py - set connections and get data
* 🏗 constants.py - constants
* 🖼 log_decorator.py - log decorator
* 🐱‍👤messages.py - GUI messages
* 🎨rec_data.py - recording data
* 🎪places.txt - places coordinates

# Overview

The main window:

![main](https://github.com/xmzboy/Async-Weather-API/blob/main/readme_images/main.PNG)
___

The settings window and manual:

![main](https://github.com/xmzboy/Async-Weather-API/blob/main/readme_images/settings.PNG)
___

The messages:

![main](https://github.com/xmzboy/Async-Weather-API/blob/main/readme_images/messages.PNG)
___
