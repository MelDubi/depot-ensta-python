import numpy as np
foo = np.random.randint(
        0, 10, 
        (np.random.randint(50, 60), np.random.randint(42, 69))
        ) 

# number of lines
print(foo.shape[0])
# number of columns
print(foo.shape[1])
# array size
print(foo.size)

# data type
print(foo.dtype)

#  find the coordinates of the matrix where its values are < 5 
less_than_5 = np.where(foo < 5)

# OR if we don't care about the coordinates (we'll get an array of booleans instead)
# less_than_5_bool = foo < 5

# multiply by 2 these points
foo[less_than_5] *= 2

# OR if we don't care about the coordinates
# foo[foo < 5] *= 2
# OR
# foo[less_than_5_bool] *= 2

# type conversion
foo_float = foo.astype(float)

# OR
# foofloat = np.float(foo)

# slice view, no copy
bar = foo[:, 0:13:2]

# slice view, force copy
bar_copy = foo[:, 0:13:2].copy()

# change type
bar_float = bar.astype(float)

# fancy indexing view: copy
baz = foo[4:14,(1,6,11,26)]

print(foo[5,6])
foo[5,6] = 42
print(foo[5,6])
print(bar[5,3])
print(baz[1,1])
print(bar_float[5,3])

# foo and bar are not copies of each other, they point to the same data in memory, beware !