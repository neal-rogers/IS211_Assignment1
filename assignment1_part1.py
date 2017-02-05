#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program processes a list of numbers and determines how many."""


def listDivide(numbers, divide=2):
    """
    Args:
        numbers (list): List of numbers to divide.
        divide (int): Integer to divide each number in list by.
        divisible (int): Count of numbers divisible.

    Returns:
        divisible (int): 

    Example:
        >>> listDivide([1,2,3,4,5])
        >>> 2
    """
    divisible = []
    for n in numbers:
        if n % divide == 0:
            divisible.append(n)
    return len(divisible)


class ListDivideException(Exception):
    """
    Attributes:
        None
    """
    pass


def testListDivide():
    """
    Args:
        None

    Returns:
        None

    Example:
        >>> testListDivide()
        >>> 
    """
    try:
        
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide=10)
        listDivide([1,2,3,4,5])
        listDivide([])
        listDivide([1,2,3,4,5], 1)
    except:
        raise ListDivideException()
