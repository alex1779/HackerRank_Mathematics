#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:32:51 2022

@author: rafa
"""

import math
import os
import random
import re
import sys

#
# Complete the 'maximumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def maximumDraws(n):
    # Write your code here
    return n+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()
