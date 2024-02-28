class LinearSearchAlgo:

    def __init__(self, arr):
        self.arr = arr
    
    def linearSearch(self, value):
        indexes = []
        for i in range(len(self.arr)):
            if self.arr[i]==value:
                indexes.append(i)
        return indexes

