#!/usr/bin/env python3

import glob

ENTRY = """  <wallpaper>
    <_name>{name}</_name>
    <filename>{filename}</filename>
    <options>zoom</options>
    <pcolor>#000000</pcolor>
    <scolor>#000000</scolor>
    <shade_type>solid</shade_type>
  </wallpaper>"""

PATH = '/usr/share/backgrounds/budgie/'

# Print a preamble.
print(
    """<?xml version="1.0"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>""",
)

# Print entries.
for image_filename in glob.glob('*.jpg'):
    print(
        ENTRY.format(
            filename=PATH + image_filename,
            # Example: 'ubuntu_budgie_wallpaper1.jpg' -> 'Ubuntu'.
            name=image_filename.split('_', maxsplit=1)[0].capitalize(),
        ),
    )

# Print a footer.
print('</wallpapers>')
