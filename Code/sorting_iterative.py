#!python


def is_sorted(items, ascending=True):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) Worse case because we have to check all the way to the end
    Memory usage: O(n) It just needs the items passed in, it does not allocate any new memory."""
    for i in range(len(items) - 1):
        if ascending:
            if items[i] > items[i + 1]:
                return False
        else:
            if items[i] < items[i + 1]:
                return False
    return True

    # one line :)
    #  return True if all([items[i] <= items[i + 1] for i in range((len(items) - 1))]) else False

def bubble_sort(items, ascending=True):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) We use a nested for loop :)
    Memory usage: O(n) - We do not store any data, just move things around. It scales with the amount of items."""

    # slightly faster because we ignore already sorted elements
    # traverse though all elements n times
    len_of_items = len(items)
    for i in range(len_of_items):
        # last elements are already in place :)
        for j in range(0, len_of_items-i-1):
            # Sort in ascending order (0-9) etc
            if ascending:
                # traverse array swapping elements
                if items[j] > items[j + 1]:
                    # swap the current and next element, yat python!
                    items[j], items[j + 1] = items[j + 1], items[j]
            # Sort in descending order
            else:
                # traverse array swapping elements
                if items[j] < items[j + 1]:
                    # swap the current and next element, yat python!
                    items[j], items[j + 1] = items[j + 1], items[j]

    # return the sorted items
    return items


def selection_sort(items, ascending=True):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(N^2) Because we have to loop through every item n times to sort
    Memory usage: O(n) - It does not store anything, just moves things around!"""
    # loop from 0 to len(items - 1)
    for i in range(len(items) - 1):
        # keep a reference of the smallest index we have found ever iteration (current index to start)
        smallest_index = i
        # loop from that index 
        for j in range(i, len(items)):
            if ascending:
                if items[j] < items[smallest_index]:
                    smallest_index = j
            else:
                if items[j] > items[smallest_index]:
                    smallest_index = j

        items[i], items[smallest_index] = items[smallest_index], items[i]
    
    return items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Average: O(n^2) It uses a nested loop that loops for every element in the array.
    Memory usage: Best: O(n) It does not make any copies, it just moves data around. It scales with the size of the items."""
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
