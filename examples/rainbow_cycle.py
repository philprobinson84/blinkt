#!/usr/bin/env python

import colorsys
import time

from blinkt import set_clear_on_exit, set_brightness, set_all, show


spacing = 360.0 / 16.0
hue = 0

set_clear_on_exit()
set_brightness(1)

while True:
    hue = int(time.time() * 2) % 360
    h = (hue % 360) / 360.0
    r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
    set_all(r,g,b)
    show()
    time.sleep(0.001)
