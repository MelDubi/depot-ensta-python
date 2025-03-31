def conv1(s):
    liste = [ord(x) for x in s]
    liste.sort()
    return liste


def exo2():
    s = 'Quarante-deux, dit Compute-Un, avec infiniment de calme et de majesté.'
    print(conv1(s))





exo2()
