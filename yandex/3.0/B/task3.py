
def search(arr, x):
    low = 0
    high = len(arr) - 1

    if x <= arr[0]:
        return -1
    if x > arr[-1]:
        return high
    if x == arr[-1]:
        return high - 1

    mid = (low + high + 1) // 2
    while low < high:

        mid = (low + high + 1) // 2

        if arr[mid] < x:
            low = mid
        else:
            mid -= 1
            high = mid


    return mid

def search1(array, start_idx, end_idx, search_val):

   if start_idx == end_idx:
       if array[start_idx] < search_val:
           return start_idx
       else:
           return -1

   mid_idx = start_idx + (end_idx - start_idx) // 2

   if search_val < array[mid_idx]:
       return search1(array, start_idx, mid_idx, search_val )
   ret = search1(array, mid_idx+1, end_idx, search_val)
   if ret == -1:
       return mid_idx
   else:
       return ret



if __name__ == "__main__":

    n_Diego = int(input())
    marks = list(set(map(int, input().split())))
    marks.sort()
    n_collectors = int(input())
    marks_collectors = list(map(int, input().split()))

    for mark in marks_collectors:
        print(search(marks, mark) + 1)
