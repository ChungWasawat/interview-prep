import numpy as np

"""how to find more information without internet"""
#print(np.info(np.ndarray.dtype)) 
"""save/ load file"""
#np.loadtxt("mytxt.txt")
#np.genfromtxt("mytxt.csv", delimeter=", ")
#np.savetxt('mytxt.txt', array1, delimeter=" ")
"""how to create array"""
# basic one
zeros_array = np.zeros(10)              # result -> [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
ones_array = np.ones(10)                # result -> [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
constant_array = np.full(10, 3)         # result -> [3 3 3 3 3 3 3 3 3 3]
# from list
my_list = [2, 3, 4]
array_from_list = np.array(my_list, dtype=float)     # result -> [2 3 4]
# from function
range_array = np.arange(10)             # result -> [0 1 2 3 4 5 6 7 8 9]
linspace_array = np.linspace(0, 1, 11)  # result -> [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
"""copy arrays"""
range_array_view = range_array.view()
range_array_copy = range_array.copy()
"""how to create matix array"""
# basic one
zeros_matrix = np.zeros((5, 2))         # 5 rows, 2 columns -> [[0. 0.] [0. 0.] [0. 0.] [0. 0.] [0. 0.]]
ones_matrix = np.ones((5, 2))
constant_matrix = np.full((5, 2), (3, 5))       # it can be 3 or (3, 5) but not (3, 5, 7) as it exceeds array size ->[[3 5] [3 5] [3 5] [3 5] [3 5]]
# more customizable
arr = np.array([[2, 3, 4], [4, 5, 6]])          # [[2 3 4] [4 5 6]]
first_row = arr[0]                              # Gets the first row -> [2 3 4]
first_col = arr[:, 0]                           # Gets the first column -> [2 4]
# random function
np.random.seed(2)  
random_array = np.random.rand(3, 2)     # Generates random numbers between 0 and 1 -> [[0.43  0.02] [0.54 0.43] [0.42 0.33]]
normal_distribution = np.random.randn(3, 2)     # the result should be randomed according to normal distribution
random_integers = np.random.randint(low=0, high=100, size=(3, 2))   # [[67  4] [42 51] [38 33]]
"""array operation"""
# Element-wise Operations **Similar operations for division and exponentiation
arr = arr + 1                           # Adds 1 to each element
arr = arr * 2                           # Multiplies each element by 2
# matrix matrix
arr1 = np.ones(4)
arr2 = np.full(4, 2)
result = arr1 + arr2                    # Element-wise addition   [3. 3. 3. 3.]
result = arr1 / arr2                    # Element-wise division   [0.5 0.5 0.5 0.5]
# math function
arr3 = np.exp(arr)
arr3 = np.sqrt(arr)
arr3 = np.sin(arr)
arr3 = np.cos(arr)
arr3 = np.log(arr)
arr3 = np.dot(arr1, arr2)
arr3 = np.array([[1,2,1], [3,4,3]]).T
# condition
arr = np.array([1, 2, 3, 4])
greater_than_2 = arr > 2                # Produces [False, False, True, True]
selected_elements = arr[arr > 1]        # Gets elements greater than 1 **[2 3 4]
equal = np.array_equal(arr1, arr2)
# basic agg function
min_value = arr.min()                   # Minimum value
max_value = arr.max()                   # Maximum value
sum_value = arr.sum()                   # Sum of all elements
csum_value = arr.cumsum(axis=0)
mean_value = arr.mean()                 # Mean (average) value
med_value = np.median(arr)
coef = np.corrcoef(arr)
std_deviation = arr.std()               # Standard deviation
"""inspect an array"""
#print(arr.shape)
#print(len(arr))
#print(arr.ndim)
#print(arr.size)
#print(arr.dtype)
#print(arr.dtype.name)
#print(arr.astype(float))               # all types: np.int64/ float32/ complex(complex number)/ np.bool/ np.object/ np.string_/ unicode_
"""sort arrays"""
#print( np.sort(arr3, axis=None) )
"""array manipulation"""
# array shape
#print(arr3.ravel())
#print(arr3.reshape(2,3))
arr3.resize((3,2))
# add/ remove
#print(np.append(arr3, np.array([7,9])))
arr4 = np.insert(arr3, 1, 5)            # (array, pos, input)
arr4 = np.delete(arr4, [1])             # (array, pos)
print(np.concatenate((arr1, arr2), axis=0))
print(np.vstack((arr1, arr2)))
print(np.r_[arr1, arr2])
print(np.hstack((arr1, arr2)))
print(np.column_stack((arr1, arr2,)))
print(np.c_[arr1, arr2])
print(np.hsplit(arr3, 2))               # according to row?
print(np.vsplit(arr3, 3))               # according to col?



