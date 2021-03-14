import argparse
from PIL import Image
from collections import defaultdict

import group, sort

SORT_FUNCS = {
    'RED': lambda x: x[0],
    'GREEN': lambda x: x[1],
    'BLUE': lambda x: x[2],
    'INTENSITY': lambda x: sum(x)
}

INTERVAL_FUNCS = {
    'BANDS': group.compare_bands,
    'INTENSITY': group.compare_intensity
}

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="filepath of the image")
    parser.add_argument("--sort_func", default="INTENSITY", help="sort type [RED | GREEN | BLUE | INTENSITY]")
    parser.add_argument("--threshold", default="75", type=int, help="threshold level for comparing two pixels when making intervals")
    parser.add_argument("--interval_func", default="INTENSITY", help="which kernel to decide intervals [BANDS | INTENSITY]")
    args = parser.parse_args()

    fp = args.image
    img = Image.open(fp)
    img.show()

    columns = create_columns(img)

    interval_func = INTERVAL_FUNCS[args.interval_func]
    threshold = args.threshold
    
    sort_func = SORT_FUNCS[args.sort_func]
    
    col_groupings = group.group_columns(columns, interval_func, threshold)
    sorted_col_groupings = []
    for groupings in col_groupings:
        sorted_col_groupings.append(sort.sort_groupings(groupings, sort_func))
    
    sorted_cols = [sort.flatten(groupings) for groupings in sorted_col_groupings]
    for x in range(img.width):
        for y in range(img.height):
            sort_pixel = sorted_cols[x][y]
            img.putpixel((x,y), sort_pixel)
    

    img.show()
    