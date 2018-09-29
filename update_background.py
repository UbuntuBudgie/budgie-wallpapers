#!/usr/bin/env python3

import glob

PREAMBLE = """<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->
"""

ENTRY = """  <static>
    <duration>1795.0</duration>
    <file>{image_filename}</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>{image_filename}</from>
    <to>{next_image_filename}</to>
  </transition>
"""

FOOTER = """</background>
"""

PATH = '/usr/share/backgrounds/budgie/'


def get_output():
    images = glob.glob('*.jpg')
    n = len(images)

    output = PREAMBLE
    for i in range(n):
        output += ENTRY.format(
            image_filename=PATH + images[i],
            # Using modulo to show the first wallpaper after the last one.
            next_image_filename=PATH + images[(i + 1) % n],
        )
    output += FOOTER

    return output


if __name__ == '__main__':
    print(get_output())
