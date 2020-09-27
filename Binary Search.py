#works on concept of sorted list
import timeit

def linear_search(arr, val):
    pass


def binary_search(arr, val):

    arr.sort()

    if len(arr) % 2 == 0:
        mid_val, index = arr[len(arr) // 2], int(len(arr)/2)
    else:
        mid_val, index = arr[len(arr) // 2], int((len(arr) / 2))

    if len(arr) != 1:
        if val == mid_val:
            return index

        if val > mid_val:
            new_arr = arr[index:]
            b = binary_search(new_arr, val)
        if val < mid_val:
            new_arr = arr[:index]
            b = binary_search(new_arr, val)
    elif len(arr) == 1:
        if val == mid_val:
            return index

        else:
            return -1
    else:
        return -1

    return b


if __name__ == '__main__':
    array = [1,4,6,9,11,15,15,15,17,21,34,34,56]

    bs = binary_search(array, 15)
    print(bs)
    print(timeit.timeit())
