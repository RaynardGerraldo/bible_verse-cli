import sys
import textwrap

import cv2
from PIL import Image,ImageDraw,ImageFont

def create_bible():
	width,height = (1280,720)
	contents = sys.stdin.read().split('"')

	book_chapter = contents[0].replace("\n","")
	verse = contents[1].replace("\n","")
	verse = textwrap.wrap(verse, width=15)

	bible = Image.new("RGBA",(width,height),"#FFE5B4")
	write = ImageDraw.Draw(bible)
	font_T = ImageFont.truetype('FreeMono.ttf', 30)
		
	# Write Chapter
	header = 15
	w, h = write.textsize(book_chapter, font=font_T)
	write.text(((width - w) / 2, header),book_chapter,font=font_T,fill="black")

	# Write Verse
	body,pad = 50,10
	for lines in verse:
		w, h = write.textsize(lines, font=font_T)
		write.text(((width - w) / 2, body),lines,font=font_T,fill="black")
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
