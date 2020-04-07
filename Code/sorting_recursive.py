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
        if items1[i] <= items2[j]:
            # add the item from the first array and go to next index
            merged_arr.append(items1[i])
            i += 1
        else:
            # add the item from the second array and go to the next index
            merged_arr.append(items2[j])
            j += 1

    # sometimes, we will not get all the items of the "second" loop so we need to add them after looping
    # (we use merge here because it is more efficent, but only one of them will always be empty)
    merged_arr.extend(items1[i:])
    merged_arr.extend(items2[j:])

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
    items[:] = merge(list1, list2)

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

        items[:] = merge(left, right)

    #  this version does not modify the passed array
    #  if len(items) <= 1:
    #      return items
    #  else:
    #      left, right = split(items)
    #      return merge_sort(merge(left), merge(right))


def partition(items, start, end):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # start pivot at first item
    pivot = items[start]
    low = start + 1
    high = end

    while True:
        # if current value we are on is larger than the pivot, it means it is in the correct
        # place and we can move to the next element
        # also have to make sure we have not passed or low value, because that means we have already moved
        # all values to the correct side of the pivot
        while low <= high and items[high] >= pivot:
            high -= 1
        # opposite of above
        while low <= high and items[low] <= pivot:
            low += 1
        # value is either found a value for low and high that are out of order so we swap,
        # or high and low is out of order so we exit
        if low <= high:
            # swap the values at low and high
            items[low], items[high] = items[high], items[low]
        else:
            break
    
    items[start], items[high] = items[high], items[start]

    return high

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # if no low or high is passed in, calculate them outselves because it is most likely the first call.
    if low is None or high is None:
        low = 0
        high = len(items) - 1

    # base case
    if low >= high:
        return

    # partition the items
    p = partition(items, low, high)
    # sort both half of the partition recursively
    quick_sort(items, low, p-1)
    quick_sort(items, p+1, high)


if __name__ == "__main__":
    #  list1 = [1, 2, 3, 4, 5]
    #  list2 = [1, 3, 4, 6, 7]
    #
    #  print(merge(list1, list2))
    
    list1 = [1, 2]
    list2 = [3, 4]
    print(list1)
    print(list2)
    print(list1 + list2)
    print(list1)
    print(list2)
    print()
    list1 = list1 + list2
    print(list1)
    print(list2)
