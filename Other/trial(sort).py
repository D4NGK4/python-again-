lst = [1, 3, 5, 2, 4]


def sorting(array):
    for i in range(len(array)):
        for j in range(len(array)+1):
            if array[j] < array[i]:
                array[j] = array[i]


print(sorting(lst))
