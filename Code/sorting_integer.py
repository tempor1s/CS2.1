#!python
from collections import defaultdict
from sorting_iterative import insertion_sort
import math


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
    
    write_pos = 0
    for write_val in range(m): # loop until our largest number (+1 because range does not include the max value :))
        for _ in range(count[write_val]): # add the item x amount of times (will ignore 0)
            numbers[write_pos] = write_val # write to that index thge valui 
            wirte_pos += 1

# def counting_sort(numbers):
#     max_val = max(numbers)
#     min_val = min(numbers)
#     count = defaultdict(int)
    
#     for i in numbers:
#         count[i] += 1
#     result = []
#     for j in range(min_val, max_val + 1):
#         result.extend([j] * count[j])
#     return result


def bucket_sort(numbers, num_buckets=None):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(??)
    TODO: Memory usage: O(??)"""
    # get hash codes (max value, bucket count)
    code = hashing(numbers)
    # create our empty buckets (if they specify a 
    # value we use that many buckets otherwise we do it dynamically)
    if num_buckets is None:
        buckets = [[] for _ in range(code[1])]
    else:
        buckets = [[] for _ in range(num_buckets)]

    # disperse our data into the buckets - O(n)
    for num in numbers:
        # rehash the value into one of the buckets (similar to hash(num))
        rehashed_value = num // code[0] * (code[1] - 1)
        # find the bucket based off of the index (after 'hash')
        bucket = buckets[rehashed_value]
        # append the value to said bucket
        bucket.append(num)
    
    # sort the elements in each bucket using insertion sort - O(n)
    for bucket in buckets:
        insertion_sort(bucket)
    
    # keep track of the value to write to
    write_index = 0
    # merge all the buckets back together in sorted order - O(n)
    for bucket in range(len(buckets)):
        # loop through every value in the bucket
        for value in buckets[bucket]:
            # write the value (sorted) into our input array
            numbers[write_index] = value
            # increase the element of the place we are going to write to
            write_index += 1

def hashing(numbers):
    return [max(numbers), int(math.sqrt(len(numbers)))]

if __name__ == '__main__':
    a = [1, 4, 5, 6, 1, 2, 4, 5, 8, 1, 4, 8]
    bucket_sort(a)
    print(a)