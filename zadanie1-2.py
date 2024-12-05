#!usr/bin/python
#
# 2. Given a list of integers. Remove duplicates from the list and create a tuple.
# Find the minimum and maximum number.


n = input("Give a list of integers:")
n = n.split(" ")
i = set(n)
n = tuple(i)
print(n)
print(min(n))
print(max(n))
