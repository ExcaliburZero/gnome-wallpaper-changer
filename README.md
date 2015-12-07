# gnome-wallpaper-changer
A python script which changes the GNOME wallpaper at specific time intervals.

## Usage
In order to setup this script one first needs to change the time intervals and wallpaper locations in `wallpaper_changer.py` to fit their needs. That script will change the wallpaper based on the current time.

Then one should enable the script to be run at a regular interval using `cron`. This can be done by running `crontab -e` and adding the following line, with the location of the wallpaper_changer folder substituted in:
```
1 * * * * python WALLPAPER_CHANGER_FOLDER_LOCATION/wallpaper_changer.py
```
