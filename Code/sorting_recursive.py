#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # empty array to add items too
    merged_arr = []
    i, j = 0, 0 # inital indicies to increase

    # loop until we no longer can for 1 array
    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            # add the item from the first array and go to next index
            merged_arr.append(items1[i])
            i += 1
        else:
            # add the item from the second array and go to the next index
            merged_arr.append(items2[j])
            j += 1
    # sometimes, we will not get all the items of the "second" loop so we need to add them after looping
    merged_arr = merged_arr + items1[i:] + items2[j:]

    # return the merged array :)
    return merged_arr

def split(items):
    """Split a list into two equal halves."""
    half = len(items) // 2
    return items[half:], items[:half]


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # split into two halves
    list1, list2 = split(items)
    
    # sort both halves
    list1.sort()
    list2.sort()
    
    # merge the two sorted halves
    return merge(list1, list2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # base case, we have a single item array
    if len(items) == 1:
        return items
    # split the list into two halves
    list1, list2 = split(items)

    # merge sort both halves recursively
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)

    # merge the two halves :)
    return merge(list1, list2)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == "__main__":
    #  list1 = [1, 2, 3, 4, 5]
    #  list2 = [1, 3, 4, 6, 7]
    #
    #  print(merge(list1, list2))

    to_sort = [3, 7, 4, 3, 2, 1, 6, 7, 123, 9, 4, 12, 6]
    print(merge_sort(to_sort))

