# bible_verse-cli

<h1 align="center">Bible verses on the command line,scrapes biblegateway.com</h1>

### Dependencies
``` pip install opencv-python ```

Dependency above is only for image feature, with pure CLI you dont need it

### Versions

See the list of versions here
https://www.biblegateway.com/versions/

### Usage

```
For a plain output on the terminal 

./bible_verse book_name chapter verse [version]

Example: 
	./bible_verse John 3 16 KJV
	./bible_verse John 3 16-21 VULGATE
	
For books with numbers infront of them, ex: 1 Peter

Example:
	./bible_verse 1Peter 1 1-2 SBLGNT
```

```
For an output to image

./bible_verse book_name chapter verse [version] | python3 versetoimage.py

Example:
	./bible_verse John 3 16 KJV | python3 versetoimage.py
	./bible_verse John 3 16-21 NIV | python3 versetoimage.py
	./bible_verse John 3 16-21 NKJV | python3 versetoimage.py <your image.png>

```
