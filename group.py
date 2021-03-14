
from collections import defaultdict

# Terminology
# group: subset of pixels for a column
#           ex: d[0] for d = {0: [p1, p2, p3], 1: [p5, p6, p7]}
#               [p1, p2, p3] <--- group
# grouped_column / bucket: a column of an image that has been grouped_by some metric
#           ex: d for d = {0: [p1, p2, p3], 1: [p5, p6, p7]}
# 



THRESHOLD = 25
'''
compare_bands takes two pixels, and compares them bassed strictly on a difference in color bands (RGB)
:param p1: first pixel
:param p2: second pixel
'''
def compare_bands(p1, p2, threshold=THRESHOLD):
    r1, g1, b1 = p1
    r2, g2, b2 = p2
    if abs(r1 -  r2) > threshold: # check for a ~10% dif in pixel bands
        return 1
    if abs(g1 - g2) > threshold:
        return 1
    if abs(b1 - b2) > threshold:
        return 1
    return 0


'''
group_column takes a column and a function and returns the groups of pixels specifyed by the function
:param column: a list of pixels
:param fn: a function that takes two pixels, and returns 1 if they differ, 0 if they are 'similar'
:return: a dictionary of {group: [pixels]}
'''
def group_column(column, fn):
    buckets = defaultdict(list)
    group = 0
    for pixel in column:
        # if there is a previous pixel in the group, and they differ
        if buckets[group] and fn(pixel, buckets[group][-1]):
            group = group + 1 # create a new group
        buckets[group].append(pixel)
    return buckets

'''
group_columns takes a list of columns and a function and returns the groups of pixels specifyed by the function
:param column: a list of a list of pixels
:param fn: a function that takes two pixels, and returns 1 if they differ, 0 if they are 'similar'
:return: a list of a dictionary of [{group: [pixels]}]
'''
def group_columns(columns, fn):
    grouped_cols = []
    for column in columns:
        grouped_cols.append(group_column(column, fn))
    
    return grouped_cols

