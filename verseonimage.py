import sys
import textwrap
from io import BytesIO
from urllib.request import urlopen

import cv2,numpy as np
from PIL import Image,ImageDraw,ImageFont

contents = sys.stdin.read().split('"')
contents = [x for x in contents if x != "\n" and x]
book_chapter = contents[0].replace("\n","")
verse = contents[1].replace("\n","")

def create_bible(book_chapter,verse):
    width,height = (1280,720)
    verse = textwrap.wrap(verse, width=15)

    bible = Image.new("RGBA",(width,height),"#FFE5B4")
    write = ImageDraw.Draw(bible)
    freemono = 'https://github.com/RaynardGerraldo/bible_verse-cli/raw/master/fonts/FreeMono.ttf'
    font_T = ImageFont.truetype(urlopen(freemono), 30)
   
    # Write Chapter
    header = 15
    w, h = write.textsize(book_chapter, font=font_T)
    write.text((
        (width - w) / 2, header),
        book_chapter,
        font=font_T,
        fill="black",
    )

    # Write Verse
    body,pad = 50,10
    for lines in verse:
        w, h = write.textsize(lines, font=font_T)
        write.text((
            (width - w) / 2, body),
            lines,
            font=font_T,
            fill="black",
        )
        body += h + pad

    # Save image
    bible_file = BytesIO()
    bible.save(bible_file,format='PNG')
    return bible

def create_border(f_stream):
    img = cv2.cvtColor(np.array(f_stream),cv2.COLOR_BGR2RGB)
    color = [19, 69, 139]
    top, bottom, left, right = [20]*4

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
bible_file_stream = create_bible(book_chapter,verse)
create_border(bible_file_stream)
