#!/usr/bin/python

def main():
    left = []
    right = []
    result = 0
    inputf = open('input.txt', 'r')
    for line in inputf.readlines():
        x = line.split()
        left.append(int(x[0]))
        right.append(int(x[1]))
    for i in left:
        result += i * right.count(i)
    print(result)

if __name__ == '__main__':
    main()