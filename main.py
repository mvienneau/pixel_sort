from PIL import Image
from collections import defaultdict

THRESHOLD = 25

SORT_RED = lambda x: x[0]
SORT_GREEN = lambda x: x[1]
SORT_BLUE = lambda x: x[2]

SORT_INTENSITY = lambda x: x[0] + x[1] + x[2]

def compare_bands(p1, p2):
    r1, g1, b1 = p1
    r2, g2, b2 = p2
    if abs(r1 -  r2) > THRESHOLD: # check for a ~10% dif in pixel bands
        return 1
    if abs(g1 - g2) > THRESHOLD:
        return 1
    if abs(b1 - b2) > THRESHOLD:
        return 1
    return 0


def bucket_column(column):
    buckets = []
    start_idx = 0
    for i in range(len(column) - 1):
        cur_pixel = column[i]
        next_pixel = column[i+1]
        if compare_bands(cur_pixel, next_pixel):
            buckets.append((start_idx, i+1))
            start_idx = i+1
    buckets.append((start_idx, len(column)))
    return buckets

def sort_columns(columns):
    new_cols = []
    for column in columns:
        new_cols.append(sort_bucket_columns(column))
    return new_cols

def sort_bucket_columns(column):
    bucketed_sort_cols = []
    buckets = bucket_column(column)
    for b_range in buckets:
        sort_arr = column[b_range[0]: b_range[1]]
        sort_arr.sort(key=SORT_INTENSITY)
        bucketed_sort_cols.append(sort_arr)
    ret_col = [item for sublist in bucketed_sort_cols for item in sublist]
    return ret_col

        

if __name__ == "__main__":
    fp = "test.py"
    img = Image.open("flower.webp")

    img.show()

    columns = []
    for x in range(img.width):
        column = []
        for y in range(img.height):
            pixel = img.getpixel((x,y)) # get each pixel COLUMN wise (?)
            column.append(pixel)
        columns.append(column)
    
    sorted_cols = sort_columns(columns)
    for x in range(img.width):
        for y in range(img.height):
            sort_pixel = sorted_cols[x][y]
            img.putpixel((x,y), sort_pixel)

    print ("hi")
    img.show()


    




        