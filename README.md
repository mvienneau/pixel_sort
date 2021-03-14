# pixel_sort
**NOTE: This is very unfinished and very much a sloppy WIP**


Python Implementation of After Effects Pixel Sort Plugin
https://aescripts.com/ae-pixel-sorter/

A scrappy attempt at creating something that sorts pixels in a certain 'interval' based on intensity, color band, etc. 

## Use
To use, simply edit the code to change the `img = Image.open("YOURFILE_HERE.jpg")` to point to any photo. Then run `python main.py`. Requires the python package `Pillow`

## Testing
This project uses `pytest` for tests, to run them, just run `pytest` in the root of this directory

## Benchmarks
A simple benchamarking file is included for perf purposes. The breakdown is as follows;
```sh
Creating Columns:     0.723
Grouping Columns:     0.473
Sort Grouped Columns: 0.331
Flatten Groups:       0.053
Recreating Picture:   0.833
```
Most of the time is spent breaking down the image into an array of pixels, and rebuilding that.


## TODO
- ~~Unit tests to ensure the code is actually doing what I think~~
- ~~Break out more of the functions into separate files~~
- ~~Re-write the sorting/bucketing code to be cleaner and clearer~~
- Add more ways to sort and bucket 
