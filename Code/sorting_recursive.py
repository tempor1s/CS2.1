#!python

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
     Running time: O(m) where m is the list with a lower higher value element
     Memory usage: O(m + n) The length of the two lists."""

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
    return items[:half], items[half:]


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n logn) Sorting both sides take O(logn), and merging is O(n)
    Memory usage: O(n^2) Merging requires us to make another variable after merging"""
    # split into two halves
    list1, list2 = split(items)
    
    # sort both halves using any sort :)
    list1.sort()
    list2.sort()
    
    # merge the two sorted halves - mutate the passed array 
    merged = merge(list1, list2)
    items[:] = merged

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n logn) because merge takes O(n) and we split a bunch
    Memory usage: O(n logn) because of merging creating a new variable every time"""
    # modify the original array
    if len(items) > 1:
        left, right = split(items)

        merge_sort(left)
        merge_sort(right)

        merged = merge(left, right)
        items[:] = merged

    #  this version does not modify the passed array
    #  if len(items) <= 1:
    #      return items
    #  else:
    #      left, right = split(items)
    #      return merge_sort(merge(left), merge(right))


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

