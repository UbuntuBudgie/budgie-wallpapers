#!/usr/bin/env python

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
    <file>%(a)s</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>%(a)s</from>
    <to>%(b)s</to>
  </transition>
"""

FOOTER = """</background>
"""

PATH='/usr/share/backgrounds/budgie/'

def main():
    images = glob.glob('*.jpg')
    m = len(images)

    output = ''
    output += PREAMBLE 
    for i in xrange(m):
        output += ENTRY % {'a': PATH + images[i], 'b': PATH + images[(i+1) % m]}
    output += FOOTER
    print output,

if __name__ == '__main__':
    main()
