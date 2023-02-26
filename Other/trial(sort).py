# TODO
lst = [1, 3, 5, 2, 4, 6, 9, 7, 8, 10]


def sorting(array):
    for i in range(0, (len(array)-1)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


print(sorting(lst))
