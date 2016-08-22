# -*- coding: utf-8 -*-


def quick_sort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    middle = array.pop()
    for item in array:
        if item <= middle:
            less.append(item)
        else:
            greater.append(item)

    return quick_sort(less) + [middle, ] + quick_sort(greater)


if __name__ == '__main__':
    array = [2, 1, 5, 6, 9, 10, 3, 8, 16, 7]
    result = quick_sort(array)
    print result