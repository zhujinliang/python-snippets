# -*- coding: utf-8 -*-


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


if __name__ == '__main__':
    array = [2, 1, 5, 6, 9, 10, 3, 8, 16, 7]
    result = bubble_sort(array)
    print result