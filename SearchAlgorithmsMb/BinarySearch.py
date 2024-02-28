class BinarySearchAlgo:

    def __init__(self, arr):
        self.arr = arr
    
    def binarySearch(self, value):
        start = 0
        end = len(self.arr)-1
        while start<=end:
            mid = start+(end-start)//2
            if self.arr[mid]==value:
                return mid
            elif self.arr[mid]>value:
                end = mid-1
            else:
                start = mid+1
        print(self.indices)
    
    def displayResult(self):
        print(self.indices)




