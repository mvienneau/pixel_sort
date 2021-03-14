# Sorting Constants
SORT_RED = lambda x: x[0]
SORT_GREEN = lambda x: x[1]
SORT_BLUE = lambda x: x[2]
SORT_INTENSITY = lambda x: x[0] + x[1] + x[2]

def sort_groupings(groupings, fn):
    return {k: sorted(v, key=fn) for k, v in groupings.items()}


'''
flatten takes in a {group: [...pixels]} object, and flattens it into an array
:param group_dict: dictionary holding group # and list of pixels
:return: a list of pixels 
'''
def flatten(group_dict):
    return [
        item 
        for sublist in group_dict.values() # get the grouped list
        for item in sublist # iterate through to flatten
    ]

