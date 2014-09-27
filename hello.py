#!/usr/bin/env python

def what_is_a_good_name_for_a_function():
    print "depends on how verbose you are"

def my_two_cents():
    print "write short names that tell a long story"


def main():
    print 3 + 8, "a"*10

    #Hella is more politically correct than hello! 
    print "Hella World!"
    print "Hella Berkeley!"

    nums = range(10)
    for n in nums:
        print n

    p = range(30,40)
    myd = dict(zip(nums, p))



if __name__ == '__main__':
    main()
