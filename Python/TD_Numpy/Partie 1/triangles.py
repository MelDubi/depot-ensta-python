# -*- coding: utf-8 -*-
import numpy as np
short_sides = np.random.randint(1, 10, (200,2))

# hypothenuse = np.atleast_2d(np.sqrt(short_sides[:,1]**2+short_sides[:,0]**2)).T
# triangles = np.concatenate([short_sides, hypothenuse], axis=1)

# much easier
hypothenuse = np.sqrt(short_sides[:,1]**2 + short_sides[:,0]**2)
triangles = np.column_stack((short_sides, hypothenuse))

acos_tr = np.arccos(triangles[:,0] / triangles[:,2])
asin_tr = np.arcsin(triangles[:,1] / triangles[:,2])
atan_tr = np.arctan2(triangles[:,1], triangles[:,0])
# not really useful
compare_cos_sin_useless = acos_tr == asin_tr
compare_cos_tan_useless = acos_tr == atan_tr

# are all values equal ?
compare_cos_sin_all = np.all(acos_tr == asin_tr)
compare_cos_tan_all = np.all(acos_tr == atan_tr)

# are some of them equal
compare_cos_sin_any = np.any(acos_tr == asin_tr)
compare_cos_tan_any = np.any(acos_tr == atan_tr)


# direct comparisons through == have to be avoided for float values, use allclose instead
compare_cos_sin_close_enough = np.allclose(acos_tr, asin_tr)
compare_cos_tan_close_enough = np.allclose(acos_tr, atan_tr)
