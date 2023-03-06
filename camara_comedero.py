#!/usr/bin/python3


import requests
from picamera import PiCamera
from time import sleep
from subprocess import call
from datetime import datetime
from fractions import Fraction

def telegram_bot_sendfoto(bot_message, ruta):
   bot_token = ''
   bot_chatID = ''
   
   message = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto'

   response = requests.post(message,
              files={'photo': (ruta, open(ruta, 'rb'))},
              data={'chat_id': bot_chatID, 'caption': bot_message})
   return response.json()


def main():
   now = datetime.now()
   dt_string = now.strftime("%d%m%Y_%H%M%S")
   ruta_foto = '/home/pi/fotos/foto_'+dt_string+'.jpg'
   camera = PiCamera()
  
   #camera.start_preview()
   camera.resolution = (1280,720)
   #camera.framerate = Fraction(1,6)
   #camera.shutter_speed = 6000000
   #camera.sensor_mode = 3
   sleep(5)
   camera.capture(ruta_foto)
   #camera.exposure_mode = 'off'
   mensaje = 'Ha comido el gato?'
   telegram_bot_sendfoto(mensaje,ruta_foto)
   

if __name__ == '__main__':
   main()
