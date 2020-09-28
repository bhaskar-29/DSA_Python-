def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements):
    pivot_index = 0
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while elements[start] <= pivot:
        start += 1

    while elements[end] > pivot:
        end -= 1
    if start < end:
        swap(start, end, elements)
    swap()

def quick_sort(elements):
    pass


if __name__ == '__main__':
    pass

