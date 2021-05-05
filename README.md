# KivyMapview for Android

The goal of this app is to use Python and Python packages to work with the map on Android.
You can use this as a starting point if you want to do something similar or improve the app.

# App Screenshot

![image](https://user-images.githubusercontent.com/55840190/117187123-3f3c5780-ade4-11eb-8586-3a12658d9df8.png)

# Features

* using [Kivy](https://github.com/kivy/kivy) and [KivyMD](https://github.com/kivymd/KivyMD) for interface
* using [Kivy-Garden Mapview](https://github.com/kivy-garden/mapview) for drawing and processing the map
* using [plyer.gps](https://github.com/kivy/plyer) for gps tracking on Android
* using mapview generates a cache, which is cleared every time when the application is closed 


# Requirements

Described in [requirements.txt](requirements.txt)

# Building with [Buildozer](https://github.com/kivy/buildozer) for Android
Just build:
```
    buildozer android debug 
```
Build & Deploy on device:
```
    buildozer android debug deploy
```
See the logcat:
```
    buildozer android logcat | grep python
```

# Using on PC
Impossible while using plyer.gps, so if you want to see the map - comment gps.start/stop in code like:
```
    ...
        # gps.start()
    ...
```
