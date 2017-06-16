from __future__ import unicode_literals
import logging
from optparse import OptionParser
from moviepy.editor import *
import moviepy.video.fx.rotate as rotate

# Needs ipython : pip install ipython

logging.basicConfig(filename='videorotate.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filemode='w')
logging.info('VideoRotate.py logs')

parser = OptionParser()
parser.add_option("-f", "--file", dest="file",
                  help="movie file")
parser.add_option("-d", "--degrees", dest="degrees",
                  help="rotate degrees")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="print status messages to stdout")
(options, args) = parser.parse_args()

print("file = " + str(options.file))
print("degrees = " + str(options.degrees))

file = "IMG_2206.MOV"
degrees = 90
if options.file is not None:
    file = str(options.file)
if options.degrees is not None:
    degrees = options.degrees

print("file is " + file)
logging.info("file is " + file)
print("degrees is " + str(degrees))
logging.info("degrees is " + str(degrees))

clip = VideoFileClip(file)
print("clip rotation is " + str(clip.rotation))
clip.fx(rotate, -90)
clip.write_videofile('new_video.mp4', fps=25, codec='mpeg4')

