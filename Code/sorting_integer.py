#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n + max(numbers)) Loop through inital array, and then loop through created
    array that is the size of the max integer in the array.
    Memory usage: O(max(numbers)) We have to create a new array the size of max integer in the array"""
    m = max(numbers) + 1
    count = [0] * m # generate max(numbers) amount of 0's
    
    for num in numbers:
        count[num] += 1 # increment occurance
    
    i = 0
    for count_index in range(m): # loop until our largest number (+1 because range does not include the max value :))
        for _ in range(count[count_index]): # add the item x amount of times (will ignore 0)
            numbers[i] = count_index
            i += 1

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

if __name__ == '__main__':
    a = [1, 4, 5, 6, 1, 2, 4, 5, 8, 1, 4, 8]
    counting_sort(a)
    print(a)