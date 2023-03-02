# VALIDATE Subsequence

# Given two non-empty arrays of integers, write a function that determines wether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjancet in the array but that are in the same order as they appear in the array.
# For instance, the numbers [1, 3, 5] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.


# Sample Input
#   array = [5, 1, 22, 25, 6, -1, 8, 10],
#   sequence = [1, 6, -1, 10]

# sample output
# True

# O(n) time | O(1) space
def validateSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


# O(n) time | O(1) space
def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)