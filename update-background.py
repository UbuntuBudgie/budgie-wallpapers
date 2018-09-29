#!/usr/bin/env python3

import glob

ENTRY = """  <static>
    <duration>1795.0</duration>
    <file>{image_filename}</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>{image_filename}</from>
    <to>{next_image_filename}</to>
  </transition>"""

PATH = '/usr/share/backgrounds/budgie/'


images = glob.glob('*.jpg')
m = len(images)

# Print a preamble.
print(
    """<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->""",
)

# Print entries.
for i in range(m):
    print(
        ENTRY.format(
            image_filename=PATH + images[i],
            # Using modulo to show the first wallpaper after the last one.
            next_image_filename=PATH + images[(i + 1) % m],
        ),
    )

# Print a footer.
print('</background>')
