def bubble_sort(array):
    size = len(array)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            temp = array[j]
            if array[j] > array[j+1]:
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if not swapped:
            break
    return array


def bubble_sort_dict(array, key):
    size = len(array)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            temp = array[j]
            if array[j][key] > array[j+1][key]:
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if not swapped:
            break
    return array


if __name__ == '__main__':
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    print(bubble_sort_dict(elements, 'name'))