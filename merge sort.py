def merge_sort(arr):
    buffer = [0] * len(arr)
    merge_helper(arr, buffer, 0, len(arr)-1)
    

def merge_helper(arr, buffer, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_helper(arr, buffer, low, middle)
        merge_helper(arr, buffer, middle+1, high)
        merge(arr, buffer, low, middle, high)
        
        
def merge(arr, buffer, low, middle, high):
    for i in range(low, high+1):
        buffer[i] = arr[i]
        
    curr = low
    left = low
    right = middle + 1
    
    while left <= middle and right <= high:
        if buffer[left] <= buffer[right]:
            arr[curr] = buffer[left]
            left = left + 1
        else:
            arr[curr] = buffer[right]
            right = right + 1
            
        curr = curr + 1
        
    for i in range(middle-left+1):
        arr[curr+i] = buffer[left+i]
        
        
if __name__ == '__main__':
    arr = [5, 2, 8, 9, 0, 1, 4, 6, 3, 7]
    merge_sort(arr)
    print(arr)
    