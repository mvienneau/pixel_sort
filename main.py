from PIL import Image
from collections import defaultdict

from group import group_columns, compare_bands
from sort import flatten, sort_groupings

THRESHOLD = 25

SORT_RED = lambda x: x[0]
SORT_GREEN = lambda x: x[1]
SORT_BLUE = lambda x: x[2]

SORT_INTENSITY = lambda x: x[0] + x[1] + x[2]

def create_columns(img):
    columns = []
    for x in range(img.width):
        column = []
        for y in range(img.height):
            pixel = img.getpixel((x,y)) # get each pixel COLUMN wise (?)
            column.append(pixel)
        columns.append(column)
    return columns
        

if __name__ == "__main__":
    fp = "test.jpg"
    img = Image.open(fp)

    img.show()

    columns = create_columns(img)
    
    col_groupings = group_columns(columns, compare_bands)
    sorted_col_groupings = []
    for groupings in col_groupings:
        sorted_col_groupings.append(sort_groupings(groupings, SORT_INTENSITY))
    
    sorted_cols = [flatten(groupings) for groupings in sorted_col_groupings]
    for x in range(img.width):
        for y in range(img.height):
            sort_pixel = sorted_cols[x][y]
            img.putpixel((x,y), sort_pixel)
    

    img.show()


    




        