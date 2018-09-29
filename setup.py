from distutils.core import setup
import glob
import os.path
import re

from DistUtilsExtra.command import build_extra, build_i18n

# Try to get a current version from changelog.
version = None
changelog_file_path = 'debian/changelog'
if os.path.exists(changelog_file_path):
    with open(changelog_file_path) as changelog_file:
        head = changelog_file.readline()
    match = re.match(r'.*\((.*)\).*', head)
    if match:
        version = match.group(1)

setup(
    name='budgie-wallpapers',
    description='Wallpapers for Ubuntu Budgie',
    version=version,
    url='https://github.com/UbuntuBudgie/budgie-wallpapers',
    data_files=[
        ('share/backgrounds/budgie', glob.glob('*.png') + glob.glob('*.jpg')),
        ('share/backgrounds/budgie', glob.glob('contest/*.xml')),
    ],
    cmdclass={
        'build': build_extra.build_extra,
        'build_i18n': build_i18n.build_i18n,
    },
)
