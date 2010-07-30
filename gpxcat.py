#!/usr/bin/env python
"""
Script to concatenate two or more GPX files.
Author: Alexander Artemenko <svetlyak.40wt@gmail.com>
URL: http://github.com/svetlyak40wt/gpxcat/
License: New BSD License
"""

import re
import sys

#from xml.etree import cElementTree as ET
from lxml import etree as ET

def main(filenames):
    assert(len(filenames) > 0)

    root_xml = ET.parse(filenames[0])
    root = root_xml.getroot()
    namespace = re.match(r'{(.*)}.*', root.tag).group(1)

    for filename in filenames[1:]:
        xml = ET.parse(filename)
        tracks = xml.findall('{%s}trk' % namespace)
        for track in tracks:
            root.append(track)

    sys.stdout.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    root_xml.write(sys.stdout)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Usage:\n%s file1.gpx file2.gpx file3.gpx > output.gpx' % sys.argv[0]
        sys.exit(1)

    main(sys.argv[1:])

