# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 15:47:58 2019

@author: Aryan Singh
"""

#dictionaries in python

## stored as key value pair, key - left
## similar to the Hash map in Java


# the keys have to be unique
monthConversion = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
}

print(monthConversion["Jan"]) # prints the value of this

print(monthConversion.get("Feb"))

# this is like the getOrDefault in Hash map Java
# prints the default thing if it doesn't find the word
print(monthConversion.get("Mine","This is default version"))

