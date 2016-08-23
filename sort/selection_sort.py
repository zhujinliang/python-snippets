# -*- coding: utf-8 -*-


def selection_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(i+1, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


if __name__ == '__main__':
    array = [2, 1, 5, 6, 9, 10, 3, 8, 16, 7]
    result = selection_sort(array)
    print result