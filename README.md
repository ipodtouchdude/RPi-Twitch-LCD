# RPi-Twitch-LCD
Control a 16x2 LCD using a Raspberry Pi to display Twitch stream info.

This script will show channel name, stream title, categorie and current viewers watching. 

# Install

### Requiements:
Pip, Adafruit CharLCD

### Pip
```sh
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip
```
### Adafruit CharLCD
```sh
sudo pip install adafruit-charlcd
```

# Running

You will need to setup a Twitch Developer Application for a Client ID at https://www.twitch.tv/kraken/oauth2/clients/new.

Edit the `Twitch_LCD.py` and insert Client ID at `client_id=''`. After set your GPIO output `lcd = Adafruit_CharLCD...` and you're ready to start the script.

```sh
sudo ./Twitch_LCD.py
```
