import subprocess
import unittest
from unittest import mock

import update_background
import update_properties


class TestUpdateBackground(unittest.TestCase):
    @mock.patch('update_background.glob.glob')
    def test_get_output(self, mock_glob):
        mock_glob.return_value = [
            'Xplo_by_Hugo_Cliff.png',
            'ubuntu_budgie_wallpaper1.jpg',
            'silent_sunrise_in_the_rainforest_by_eric_li.jpg',
        ]
        expected_output = """<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->
  <static>
    <duration>1795.0</duration>
    <file>/usr/share/backgrounds/budgie/Xplo_by_Hugo_Cliff.png</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>/usr/share/backgrounds/budgie/Xplo_by_Hugo_Cliff.png</from>
    <to>/usr/share/backgrounds/budgie/ubuntu_budgie_wallpaper1.jpg</to>
  </transition>
  <static>
    <duration>1795.0</duration>
    <file>/usr/share/backgrounds/budgie/ubuntu_budgie_wallpaper1.jpg</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>/usr/share/backgrounds/budgie/ubuntu_budgie_wallpaper1.jpg</from>
    <to>/usr/share/backgrounds/budgie/silent_sunrise_in_the_rainforest_by_eric_li.jpg</to>
  </transition>
  <static>
    <duration>1795.0</duration>
    <file>/usr/share/backgrounds/budgie/silent_sunrise_in_the_rainforest_by_eric_li.jpg</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>/usr/share/backgrounds/budgie/silent_sunrise_in_the_rainforest_by_eric_li.jpg</from>
    <to>/usr/share/backgrounds/budgie/Xplo_by_Hugo_Cliff.png</to>
  </transition>
</background>
"""
        self.assertEqual(update_background.get_output(), expected_output)

    def test_output(self):
        output = subprocess.getoutput('python3 update_background.py')
        self.assertEqual(output, update_background.get_output())


class TestUpdateProperties(unittest.TestCase):
    @mock.patch('update_properties.glob.glob')
    def test_get_output(self, mock_glob):
        mock_glob.return_value = [
            'Xplo_by_Hugo_Cliff.png',
            'ubuntu_budgie_wallpaper1.jpg',
            'silent_sunrise_in_the_rainforest_by_eric_li.jpg',
        ]
        expected_output = """<?xml version="1.0"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>
  <wallpaper>
    <_name>Xplo</_name>
    <filename>/usr/share/backgrounds/budgie/Xplo_by_Hugo_Cliff.png</filename>
    <options>zoom</options>
    <pcolor>#000000</pcolor>
    <scolor>#000000</scolor>
    <shade_type>solid</shade_type>
  </wallpaper>
  <wallpaper>
    <_name>Ubuntu</_name>
    <filename>/usr/share/backgrounds/budgie/ubuntu_budgie_wallpaper1.jpg</filename>
    <options>zoom</options>
    <pcolor>#000000</pcolor>
    <scolor>#000000</scolor>
    <shade_type>solid</shade_type>
  </wallpaper>
  <wallpaper>
    <_name>Silent</_name>
    <filename>/usr/share/backgrounds/budgie/silent_sunrise_in_the_rainforest_by_eric_li.jpg</filename>
    <options>zoom</options>
    <pcolor>#000000</pcolor>
    <scolor>#000000</scolor>
    <shade_type>solid</shade_type>
  </wallpaper>
</wallpapers>
"""
        self.assertEqual(update_properties.get_output(), expected_output)

    def test_output(self):
        output = subprocess.getoutput('python3 update_properties.py')
        self.assertEqual(output, update_properties.get_output())


if __name__ == '__main__':
    unittest.main()
