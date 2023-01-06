# bible_verse-cli

<h1 align="center">Bible verses on the command line,scrapes biblegateway.com</h1>

### Dependencies
``` pip install opencv-python ```

### Usage

```
For a plain output on the terminal 

./bible_verse book_name chapter verse [version]

Example: 
	./bible_verse John 3 16 KJV
	./bible_verse John 3 16-21 NIV

```

```
For an output to image

./bible_verse book_name chapter verse [version] | python3 versetoimage.py

Example:
	./bible_verse John 3 16 KJV | python3 versetoimage.py
	./bible_verse John 3 16-21 NIV | python3 versetoimage.py

```

### PLANS
* Generate better verse images
