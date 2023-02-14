from setuptools import *
import glob
import re
import os

# look/set what version we have
changelog = "debian/changelog"
if os.path.exists(changelog):
    head=open(changelog).readline()
    match = re.compile(".*\((.*)\).*").match(head)
    if match:
        version = match.group(1)

setup(
    name = 'budgie-wallpapers',
    version = version,
    data_files=[('share/backgrounds/budgie', glob.glob('*.png')+glob.glob('*.jpg')),
		('share/gnome-background-properties', glob.glob('*.xml')),
               ],
    cmdclass = {},
    py_modules=[]
)

