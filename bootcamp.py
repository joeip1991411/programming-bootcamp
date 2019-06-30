# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:36:24 2019

@author: Joe

The following function reads a list of integers from user input.
Find all pairs of numbers in the list whose product is even and whose sum is odd.
It then print out a formatted list of the pairs.
"""

def even_product_odd_sum(integer_list):
    
    # empty list to store result
    result_list = []
    
    # outer loop (1st item to the second last item)
    for i in range(len(integer_list)-1):
        # inner loop (next item to the last item)
        for j in range(i+1, len(integer_list)):
            # check condition:
            # product is even
            if (((integer_list[i] * integer_list[j])%2 == 0) and 
                # sum is odd
                ((integer_list[i] + integer_list[j])%2 == 1)):
                # append to result list if requirements are satisfied
                result_list.append((integer_list[i], integer_list[j]))
    
    return result_list