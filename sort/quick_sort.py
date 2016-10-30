# -*- coding: utf-8 -*-

'''
快速排序法
1. 从数列中挑出一个元素，称为 “基准”（middle），
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序
平均时间复杂度为: O(NlogN)
最坏时间复杂度为：O(n2) n平方
'''

def quick_sort_pythonic(array):
    '''
    Pythonic recursive quick sort.
    '''
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

    return quick_sort_pythonic(less) + [middle, ] + quick_sort_pythonic(greater)


def partition(array, start, end):
    import random
    # 获取比较基准，并将基准值放最后
    middle = random.randint(start, end)
    array[middle], array[end] = array[end], array[middle]
    # small 保存基准值按照排序应该存放的位置
    small = start - 1
    for i in range(start, end):
        if array[i] < array[end]:
            small += 1
            if i != small:
                print i, small
                # 将small指向的大的值和i指向的小的值交换
                array[i], array[small] = array[small], array[i]
    # 最后再将基准值交换到排序应该在的位置
    small += 1
    array[small], array[end] = array[end], array[small]
    return small


def quick_sort_recursive(array, start, end):
    if start == end:
        return
    index = partition(array, start, end)
    if (index > start):
        quick_sort_recursive(array, start, index - 1)
    if (index < end):
        quick_sort_recursive(array, index + 1, end)
    return array


def quick_sort_no_recursive(array):
    pass



if __name__ == '__main__':
    array = [2, 1, 5, 6, 9, 10, 3, 8, 16, 7]
    result = quick_sort_pythonic(array)
    print 'Pythonic recursive quick sort result:'
    print result

    result = quick_sort_recursive(array, 0, len(array) - 1)
    print 'Recursive quick sort result:'
    print result

    result = quick_sort_no_recursive(array)
    print 'No recursive quick sort result:'
    print result
