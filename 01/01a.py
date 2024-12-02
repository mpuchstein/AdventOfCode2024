#!/usr/bin/python

import sys

class ListElement:

    def __init__(self, value, nxt):
        self.value=value
        self.nxt=nxt

    def insert_sorted(self, value):
        if value < self.value:
            return ListElement(value, self)
        elif self.nxt is not None:
            self.nxt = self.nxt.insert_sorted(value)
            return self
        else:
            self.nxt = ListElement(value, None)
            return self

    def length(self):
        if self.nxt is None:
            return 1
        else:
            return self.nxt.length() + 1

    def get(self, index:int):
        if index == 0:
            return self.value
        else:
            if self.nxt is None:
                raise IndexError("Index out of bounds.")
            else:
                return self.nxt.get(index-1)

class List :
    start : ListElement

    def __init__(self, value:int):
        self.start = ListElement(value, None)

    def insert_sorted(self, value):
        if self.start is not None:
            self.start = self.start.insert_sorted(value)
        else:
            self.start = ListElement(value, None)

    def length(self):
        if self.start is None:
            return -1
        return self.start.length()

    def get(self, index:int):
        if index < 0:
            raise IndexError("Negative index")
        elif self.start is None:
            raise IndexError("List is empty")
        return self.start.get(index)

def diff_list(list0, list1):
    i = 0
    result = 0
    max = list0.length()
    while i < max:
        result += abs(list0.get(i)-list1.get(i))
        i=i+1
    return result

def main():
    sys.setrecursionlimit(1500)
    listleft = None
    listright = None
    input_file = open('input.txt', 'r')
    for line in input_file.readlines():
        x = line.split()
        left = int(x[0])
        right = int(x[1])
        if listleft is None:
            listleft = List(left)
        else:
            listleft.insert_sorted(left)
        if listright is None:
            listright = List(right)
        else:
            listright.insert_sorted(right)
    print(diff_list(listleft, listright))
    input_file.close()

if __name__ == "__main__":
    main()