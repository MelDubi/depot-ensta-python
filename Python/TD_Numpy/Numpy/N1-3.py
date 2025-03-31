import numpy as np

short_sides = np.random.randint(1, 10, (3,2))
hypotenuses = np.sqrt(short_sides[:,0]**2+short_sides[:,1]**2)

triangles = np.column_stack((short_sides[:,0],short_sides[:,1],hypotenuses))
print(triangles)

anglecos = np.arccos(triangles[:,1]/triangles[:,2])
anglesin = np.arcsin(triangles[:,0]/triangles[:,2])
angletan = np.arctan(triangles[:,0]/triangles[:,1])
print("cos:",anglecos)
print("sin:",anglesin)
print("tan:",angletan)