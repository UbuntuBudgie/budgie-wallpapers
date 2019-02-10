#!/usr/bin/env python

import glob

PREAMBLE = """<?xml version="1.0"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>
"""

ENTRY = """  <wallpaper>
    <_name>%(b)s</_name>
    <filename>%(a)s</filename>
    <options>zoom</options>
    <pcolor>#000000</pcolor>
    <scolor>#000000</scolor>
    <shade_type>solid</shade_type>
  </wallpaper>
"""


FOOTER = """</wallpapers>
"""

PATH='/usr/share/backgrounds/budgie/'

def main():
    images = glob.glob('*.jpg')
    m = len(images)

    output = ''
    output += PREAMBLE 
    for i in xrange(m):
        output += ENTRY % {'a': PATH + images[i], 'b': images[(i)].split('_')[0].capitalize()}
    output += FOOTER
    print output,

if __name__ == '__main__':
    main()
