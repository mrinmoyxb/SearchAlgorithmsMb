
# searchAlgorithmsMb
This Python library provides efficient implementations of two common search algorithms: **Linear search** and **Binary search**. These algorithms are essential tools for finding specific values within a collection of data

## Installation:
You can install this library using pip:

```pip install searchAlgorithmsMb```


## Usage
**Linear Search:**

The linear search algorithm scans through each element in an array until it finds the target value. Time complexity for linear search is denoted by **O(n)** as every element in the array is compared only once. In linear search, best-case complexity is **O(1)** where the element is found at the first index.

Here’s how you can use it:

```
from searchAlgorithmsMb import LinearSearchAlgo

l1 = [12, 30, 45, 89, 90]
target = 30

ls = LinearSearchAlgo(l1)
index = ls.linearSearch(target)
if index!=[]:
    print(f"{target}, Found at index: {index}")
else:
    print("Not found!")

```

**Binary Search:**

Binary search requires a sorted array. It repeatedly divides the array into halves until the value is found. The time complexity of the binary search algorithm is **O(log n)**. The best-case time complexity would be **O(1)** when the central index would directly match the desired value.

Here’s how you can use it:

```
from searchAlgorithmsMb import BinarySearchAlgo

l1 = [12, 30, 45, 89, 90]
target = 45

bs = BinarySearchAlgo(l1)
index = bs.binarySearch(target)
if index!=-1:
    print(f"{target}, Found at index: {index}")
else:
    print("Not found!")
```
## Contributing
Contributions are welcome! If you’d like to add more search algorithms or improve existing ones, feel free to submit a pull request. Drop a like and followe me on the [github.](https://github.com/mrinmoyxb)

Happy coding! 🚀
