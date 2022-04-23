import sys
import textwrap

import cv2
from PIL import Image,ImageDraw,ImageFont,ImageOps

def create_bible():
	# Init
	width,height = (640,480)
	verse = '''Climb any old mountain.'''
	verse = textwrap.wrap(verse, width=15)
	bible = Image.new("RGBA",(width,height),"#FFE5B4")
	write = ImageDraw.Draw(bible)
	myFont = ImageFont.truetype('FreeMono.ttf', 30)
	
	
	# Write Chapter
	header = 20
	w, h = write.textsize("Test", font=myFont)
	write.text(((width - w) / 2, header),"Test",font=myFont,fill="black")

	# Write Verse
	body,pad = 50,10
	for lines in verse:
		w, h = write.textsize(lines, font=myFont)
		write.text(((width - w) / 2, body),lines,font=myFont,fill="black")
		body += h + pad
	bible.save("bible.png")

def create_border():
	img = cv2.imread("bible.png")
	color = [19, 69, 139]
	top, bottom, left, right = [20]*4

	bible_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
	cv2.imshow("img", bible_border)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

create_bible()
create_border()
