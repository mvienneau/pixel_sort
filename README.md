# pixel_sort
*NOTE* This is very unfinished and very much a sloppy WIP
Python Implementation of After Effects Pixel Sort Plugin
https://aescripts.com/ae-pixel-sorter/

A scrappy attempt at creating something that sorts pixels in a certain 'interval' based on intensity, color band, etc. 

## Use
To use, simply edit the code to change the `img = Image.open("YOURFILE_HERE.jpg")` to point to any photo. Then run `python main.py`. Requires the python package `Pillow`

## TODO
- Unit tests to ensure the code is actually doing what I think
- Break out more of the functions into separate files
- Add more waays to sort and bucket 
