#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Psuedo Code
    # Loop from the beginning given n, and check to see if n value > n + 1 value
    # if n value > n + 1 value, return false because it is not sorted
    # otherwise continue
    # if we reach the end without returning False, it is sorted so we can just return true
    
    # Not bad, but we could one line!
    #  for i in range(len(items) - 1):
    #      if items[i] > items[i + 1]:
    #          return False
    #  return True
    return True if all([items[i] <= items[i + 1] for i in range((len(items) - 1))]) else False

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # for item list:
    # check if current item value is less than i + 1
    # if it is, swap them, otherwise continue

    # pretty good solution, but we can go a bit faster!
    #  for _ in range(len(items)):
    #      for i in range(len(items) - 1):
    #          if items[i] > items[i + 1]:
    #              items[i], items[i + 1] = items[i + 1], items[i]
   
    # slightly faster because we ignore already sorted elements
    # traverse though all elements n times
    len_of_items = len(items)
    for i in range(len_of_items):
        # last elements are already in place :) 
        for j in range(0, len_of_items-i-1):
            # traverse array swapping elements
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(N^2) Because we have to loop through every item n times to sort
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items) - 1):
        smallest_index = i
        for j in range(i, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
        items[i], items[smallest_index] = items[smallest_index], items[i]

    return items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # loop from 1 to len of items, we start at one because we are assuming 1 is already sorted
    for i in range(1, len(items)):
        # extract the element we are currently on
        extracted_item = items[i]
        
        # the index of the item we are going to potenially swap with
        j = i -1
        # while we are not at 0, and our extracted item is less than j - the goal is to decrease all the way down to zero 
        while j >=0 and extracted_item < items[j]:
            # swap j+1 with the current item since it is greater than our target
            items[j+1] = items[j]
            # decreate j again to keep going backwards
            j -= 1
        # finally, swap our extracted item with the element one above
        items[j+1] = extracted_item
        
    # return the sorted items
    return items
