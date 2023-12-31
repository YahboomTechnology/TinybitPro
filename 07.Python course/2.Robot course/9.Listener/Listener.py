# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, pin12, sleep
import tinybit
import neopixel

np = neopixel.NeoPixel(pin12, 2)
np.clear()
tinybit.car_HeadRGB(0, 0, 0)
display.show(Image.HAPPY)
delay = 80

level_0 = Image("00000:00000:00000:00000:00000")
level_1 = Image("00000:00000:00000:00000:09990")
level_2 = Image("00000:00000:00000:00900:99999")
level_3 = Image("00000:00000:00000:09990:99999")
level_4 = Image("00000:00000:00900:99999:99999")
level_5 = Image("00000:00000:99999:99999:99999")
level_6 = Image("00000:09990:99999:99999:99999")
level_7 = Image("00900:99999:99999:99999:99999")
level_8 = Image("99999:99999:99999:99999:99999")


while True:
    voice = tinybit.getVoicedata()
    if voice < 10:
        tinybit.car_stop()
        np.clear()
        tinybit.car_HeadRGB(0, 0, 0)
        display.show(level_0)
    elif voice >= 10 and voice < 40:
        display.show(level_1)
        tinybit.car_HeadRGB(0, 0, 50)
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np.show()
        tinybit.car_spinleft(50)
        sleep(delay)
        tinybit.car_spinright(50)
        sleep(delay)
    elif voice >= 40 and voice < 70:
        display.show(level_2)
        tinybit.car_HeadRGB(50, 50, 50)
        np[0] = (0, 255, 255)
        np[1] = (0, 255, 255)
        np.show()
        tinybit.car_spinleft(60)
        sleep(delay)
        tinybit.car_spinright(60)
        sleep(delay)
    elif voice >= 70 and voice < 110:
        display.show(level_3)
        tinybit.car_HeadRGB(0, 100, 0)
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np.show()
        tinybit.car_spinleft(70)
        sleep(delay)
        tinybit.car_spinright(70)
        sleep(delay)
    elif voice >= 110 and voice < 160:
        display.show(level_4)
        tinybit.car_HeadRGB(0, 0, 200)
        np[0] = (0, 0, 255)
        np[1] = (0, 0, 255)
        np.show()
        tinybit.car_spinleft(80)
        sleep(delay)
        tinybit.car_spinright(80)
        sleep(delay)
    elif voice >= 160 and voice < 170:
        display.show(level_5)
        tinybit.car_HeadRGB(255, 255, 0)
        np[0] = (255, 255, 0)
        np[1] = (255, 255, 0)
        np.show()
        tinybit.car_spinleft(90)
        sleep(delay)
        tinybit.car_spinright(90)
        sleep(delay)
    elif voice >= 170 and voice < 200:
        display.show(level_6)
        tinybit.car_HeadRGB(0, 255, 255)
        np[0] = (0, 255, 255)
        np[1] = (0, 255, 255)
        np.show()
        tinybit.car_spinleft(100)
        sleep(delay)
        tinybit.car_spinright(100)
        sleep(delay)
    elif voice >= 200 and voice < 240:
        display.show(level_7)
        tinybit.car_HeadRGB(255, 255, 255)
        np[0] = (255, 255, 255)
        np[1] = (255, 255, 255)
        np.show()
        tinybit.car_spinleft(110)
        sleep(delay)
        tinybit.car_spinright(110)
        sleep(delay)
    elif voice >= 240:
        display.show(level_8)
        tinybit.car_HeadRGB(255, 255, 0)
        np[0] = (255, 255, 0)
        np[1] = (255, 255, 0)
        np.show()
        tinybit.car_spinleft(120)
        sleep(delay)
        tinybit.car_spinright(120)
        sleep(delay)
