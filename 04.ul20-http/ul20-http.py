#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import signal
import datetime
import time
import requests 
from bme280 import BME280

try:
  from smbus2 import SMBus
except ImportError:
  from smbus import SMBus

EXIT = False

def handler(signum, frame):
  global EXIT
  EXIT = True

def main():
  signal.signal(signal.SIGTERM, handler)
  signal.signal(signal.SIGINT, handler)

  iotagent = 'http://' + os.environ.get('IOTA_IP', 'iot-agent').rstrip('/') + ':7896/iot/d'
  key = os.environ.get('IOTA_KEY', '4jggokgpepnvsb2uv4s40d59ov')
  device = os.environ.get('DEVICE_ID', 'sensor004')
  debug = not not os.environ.get('DEBUG_FLAG', '')

  if (debug):
    print(iotagent)
    print(key)
    print(device)

  bus = SMBus(1)
  bme280 = BME280(i2c_dev=bus)

  url = '{}?k={}&i={}'.format(iotagent, key, device)
  headers = {'Content-Type': 'text/plain'}
  if (debug):
    print (url)

  while True:
    date = datetime.datetime.utcnow().isoformat(timespec='seconds')
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    measures = 'd|{}|t|{:05.2f}|h|{:05.2f}|p|{:05.2f}'.format(date, temperature, humidity, pressure)
    print(measures)

    r = requests.post(url, data=measures, headers=headers)
    if r.status_code != 200:
      print(r.status_code)
      print(r.text)
      break

    time.sleep(1)

    if (EXIT):
      break

if __name__ == '__main__':
  main()
