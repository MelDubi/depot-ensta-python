import numpy as np

def divide(img,taille):
# Syntaxe:
#        classe1=divide(Image,Taille);
    res=[]
    nox=np.floor(img.shape[0]/taille)
    noy=np.floor(img.shape[1]/taille)
    for x in range(1,np.uint8(nox)+1):
       for y in range(1,np.uint8(noy)+1):
          res.append(img[(x-1)*taille+1:x*taille+1,(y-1)*taille+1:y*taille+1])
    return res

def formate_resultat(img,taille,vect_param_seg):
    res=np.zeros(img.shape)
    nox=np.floor(img.shape[0]/taille)
    noy=np.floor(img.shape[1]/taille)
    cpt = 0
    for x in range(1,np.uint8(nox)+1):
       for y in range(1,np.uint8(noy)+1):
          res[(x-1)*taille+1:x*taille,(y-1)*taille+1:y*taille]=vect_param_seg[cpt]
          cpt=cpt+1
    return res