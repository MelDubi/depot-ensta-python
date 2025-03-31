import numpy as np
foo = np.random.randint(0, 10, (np.random.randint(50, 60), np.random.randint(42, 69)))
l=foo.shape[0]
c=foo.shape[1]
print(l,"-",c)

#another=np.argwhere((foo<5)==True)
mask=1+(foo<5)
foo=foo*mask

#print(foo)
bar = foo[:, 0:13:2]
bar_copy = foo[:, 0:13:2].copy()
bar_float = bar.astype(float)
baz = foo[4:14,(1,6,11,26)]
print("\n",bar)
print("\n",baz)
foo[5,6] = 42
print(foo[5,6], bar[5,3], baz[1,1], bar_float[5,3])