#!/usr/bin/env python3

import glob

PREAMBLE = """<?xml version="1.0"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>
"""

ENTRY = """  <wallpaper>
    <_name>{name}</_name>
    <filename>{filename}</filename>
    <options>zoom</options>
    <pcolor>#000000</pcolor>
    <scolor>#000000</scolor>
    <shade_type>solid</shade_type>
  </wallpaper>
"""

FOOTER = """</wallpapers>
"""

PATH = '/usr/share/backgrounds/budgie/'


def get_output():
    output = PREAMBLE
    for image_filename in glob.glob('*.jpg'):
        output += ENTRY.format(
            filename=PATH + image_filename,
            # Example: 'ubuntu_budgie_wallpaper1.jpg' -> 'Ubuntu'.
            name=image_filename.split('_', maxsplit=1)[0].capitalize(),
        )
    output += FOOTER

    return output


if __name__ == '__main__':
    print(get_output())
