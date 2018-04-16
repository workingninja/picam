# picamir

A simple live stream Web cam with IR for the Raspberry Pi.

## Requirements

1. Python 2.7
2. Raspberry Pi with Raspbian
3. [Pi NoIR Camera v2](https://www.raspberrypi.org/products/pi-noir-camera-v2/)
4. [BrightPi](https://uk.pi-supply.com/products/bright-pi-bright-white-ir-camera-light-raspberry-pi)

## Installation

### picamir

```bash
git clone https://github.com/workingninja/picamir.git
cd picamir
```

### Bright-Pi

#### Install brightpi

```bash
cd ir
git clone https://github.com/PiSupply/Bright-Pi.git
mkdir brightpi
cp Bright-Pi/brightpi/brightpilib.py brightpi/
```

#### Enable I2C Autoloading

```bash
sudo raspi-config
```

Interfacing Options > I2C > Yes

#### SMBus for Bright-Pi

```bash
sudo apt-get install i2c-tools
sudo apt-get install python-smbus
```

```bash
python -m virtualenv --system-site-packages env
```

### Install packages via pip

```bash
source env/bin/activate
pip install -r requirements.txt
```

### Yarn

```bash
yarn install
ln -s node_modules static
```

## Running picamir

### Temporarily

```bash
(env)$ ./app.py
```

### Persistent (across reboots)

Add the following to your users crontab (`crontab -e`):

```bash
@reboot /path/to/picamir/env/bin/python /path/to/picamir/app.py
```

## Special Thanks

This project would not be possible without the camera module from [Miguel Grinberg](https://github.com/miguelgrinberg/flask-video-streaming) and IR LEDs and code developed by [Pi Supply](https://uk.pi-supply.com/products/bright-pi-bright-white-ir-camera-light-raspberry-pi).
