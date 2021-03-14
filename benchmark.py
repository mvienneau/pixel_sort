import time
from PIL import Image
import group, sort, main

img = Image.open("test.jpg")

t1 = time.time()
columns = main.create_columns(img)
t2 = time.time()

print ("Creating Columns: %05.3f" % (t2-t1))


t1 = time.time()
col_groupings = group.group_columns(columns, group.compare_bands)
t2 = time.time()

print ("Grouping Columns: %05.3f" % (t2-t1))


t1 = time.time()
sorted_col_groupings = []
for groupings in col_groupings:
    sorted_col_groupings.append(sort.sort_groupings(groupings, sort.SORT_INTENSITY))
t2 = time.time()

print ("Sort Grouped Columns: %05.3f" % (t2-t1))

t1 = time.time()
sorted_cols = [sort.flatten(groupings) for groupings in sorted_col_groupings]
t2 = time.time()

print ("Flatten Groups: %05.3f" % (t2-t1))

t1 = time.time()
for x in range(img.width):
    for y in range(img.height):
        sort_pixel = sorted_cols[x][y]
        img.putpixel((x,y), sort_pixel)
t2 = time.time()


print ("Recreating Picture: %05.3f" % (t2-t1))