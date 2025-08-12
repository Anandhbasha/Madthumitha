# import numpy as np

# arr = np.array([10,20,30])

# print(arr)

# arr1 = np.array([[1,2],[2,3]])
# print(arr1)

# arr2 = np.array([[1,2,3],[2,3,5],[4,5,7]])
# print(arr2)

# arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr3d)

# zeros = np.zeros((3, 4))  
# print(zeros)

# eye = np.eye(3) 
# print(eye)

# range_arr = np.arange(0, 10, 2)
# print(range_arr)

# linspace_arr = np.linspace(0, 1, 5) 
# print(linspace_arr)


# Pandas
import pandas as pd

# From a list
s1 = pd.Series([1, 3, 5, 7, 9])
print(s1)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df)

df.to_csv('output.csv', index=False)