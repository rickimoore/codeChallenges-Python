# coding: utf-8
"""
You'll be given a string of characters as an input.

Create a function reverse_slice that returns a list of strings: (a) in the reverse order of the original string, and (b) with each successive string starting one character further in from the end of the original string.

For example:

'123'  becomes  ['321','21','1']
"""
def reverse_slice(s):
    reversed = s[::-1]
    increment = 0
    count  = len(list(reversed))
    slices = []
    
    while count > 0:
        slices.append(reversed[increment::])
        increment += 1
        count -= 1
    
    return slices
