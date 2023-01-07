import sys
import textwrap
from io import BytesIO
from urllib.request import urlopen

import cv2,numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_bible(book_chapter, verse, img=None):
	if img is None:
		# Set default image size if no image is provided
		width, height = (1280, 720)
		bible = Image.new("RGBA", (width, height), "#FFE5B4")
		write = ImageDraw.Draw(bible)
	else:
		# Use size of provided image
		width, height = img.size
		bible = img.copy()
		write = ImageDraw.Draw(bible)

	# Calculate maximum width and height for the text block
	max_width = width - 40
	max_height = height - 40

	font_url = 'https://github.com/RaynardGerraldo/bibleverse-cli/raw/master/fonts/FreeMono.ttf'
	try:
		font = ImageFont.truetype(urlopen(font_url), 30)
	except:
		print("Error: Could not load font from URL. Using default font.")
		font = ImageFont.load_default()

	# Calculate padding based on font size
	padding = font.getbbox('A')[3] // 3

	# Wrap text to fit within the maximum width
	verse_lines = textwrap.wrap(verse, width=max_width // font.getbbox('A')[2])

	# Calculate text block height based on number of lines and font size
	text_height = len(verse_lines) * (font.getbbox('A')[3] + padding)

	# Calculate top and left margins for the verse text
	top_margin = 20
	left_margin = (width - max_width) // 2

	# Write Chapter
	chapter_box = write.textbbox((0,0),book_chapter, font=font)
	w,h = chapter_box[2], chapter_box[3]
	write.text((
		(width - w) // 2, top_margin),
		book_chapter,
		font=font,
		fill="black",
	)

	# Write Verse
	y = top_margin + h + padding
	for line in verse_lines:
		line_box = write.textbbox((0,0),line,font=font)
		w,h = line_box[2], line_box[3]
		write.text((
			left_margin, y),
			line,
			font=font,
			fill="black",
		)
		y += h + padding

	# Save image
	bible_file = BytesIO()
	bible.save(bible_file, format='PNG')
	return bible

def create_border(f_stream):
	img = cv2.cvtColor(np.array(f_stream),cv2.COLOR_BGR2RGB)
	color = [19, 69, 139]
	top, bottom, left, right = [20] * 4

	bible_final = cv2.copyMakeBorder(
		img,
		top,
		bottom,
		left,
		right,
		cv2.BORDER_CONSTANT,
		value=color
	)
	cv2.imshow("{}".format(book_chapter), bible_final)
	while True:
		keyCode = cv2.waitKey(1)
		if cv2.getWindowProperty("{}".format(book_chapter), cv2.WND_PROP_VISIBLE) <1:
			break
	cv2.destroyAllWindows()

# Check if the user provided an image file name as a command line argument
if len(sys.argv) > 1:
	# Open the image file
	try:
		img = Image.open(sys.argv[1])
	except OSError:
		print("Error: Could not open image file. Using default image size.")
		img = None
else:
	img = None

# Read input
contents = sys.stdin.read().split('\n')
book_chapter = contents[0]
verse = contents[1]

# Create the Bible image
bible_file_stream = create_bible(book_chapter,verse,img)

# Add a border to the image
create_border(bible_file_stream)

