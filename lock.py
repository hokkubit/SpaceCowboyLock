#!/bin/env python

import os, sys
import random
import subprocess
from PIL import Image, ImageFilter 


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def get_random_img():
    pic = random.choice(os.listdir(get_script_path() + '/img' ))
    return pic

def take_screen():
    command='scrot /tmp/screen.png'
    subprocess.call(command.split())

def prepare(*args):
    command='convert -gamma 0.3 /tmp/screen.png /tmp/screen_dark.png'
    subprocess.call(command.split())
    path = get_script_path()
    random_img = get_random_img()
    im = Image.open('/tmp/screen_dark.png')
    im_out = im.filter(ImageFilter.GaussianBlur(radius=5))
    try:
        logo = Image.open('{0}/img/{1}'.format(path, random_img))
        source_x, source_y = im_out.size
        logo_x, logo_y = logo.size 
        im_out.paste(logo,
                     (int(source_x*0.8 - logo_x/2),
                      int(source_y*0.9 - logo_y/2)),
                      logo)
        im_out.save('/tmp/screen_dark.png')
    except:
        im_out.save('/tmp/screen.png')

def lock():
    try:
        command='i3lock -i /tmp/screen_dark.png'
        subprocess.call(command.split())
        os.remove('/tmp/screen_img.png')
    except:
        command='i3lock -i /tmp/screen.png'
        os.remove('/tmp/screen.png')

if __name__ =='__main__':
    take_screen()
    prepare()
    lock()
