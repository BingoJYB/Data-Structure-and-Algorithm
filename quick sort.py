def quick_sort(arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:
        quick_sort(arr, left, index-1)
    if index < right:
        quick_sort(arr, index, right)


def partition(arr, left, right):
    pivot = arr[(left+right)//2]

    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1

    return left


def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp


if __name__ == '__main__':
    arr = [5, 2, 8, 9, 0, 1, 4, 6, 3, 7]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
