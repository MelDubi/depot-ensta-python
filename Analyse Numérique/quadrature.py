import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x**3-x

def f2(x):
    return np.sin(x)

def f3(x):
    return 2*x*np.exp(-x**2)

def f4(x):
    return 4*x + 2

def F1(x):
    return x**4/4 - x**2/2

def F2(x):
    return -np.cos(x)

def F3(x):
    return -np.exp(-x**2)

def F4(x):
    return 2*x**2 + 2*x

def Ferr1(x, n):
    return F1(x) + x/n

def Ferr2(x, n):
    return F1(x) + x/n**2

def Ferr3(x, n):
    return F1(x) + (x*np.cos(np.log(n)))/n**2

def erreurs():
    """ Réalise les tracés des questions 5 à 7 """
    n = np.logspace(0,10,300)
    plt.figure()
    plt.plot(n, Ferr1(3, n), label="Ferr1")
    plt.plot(n, Ferr2(3, n), label="Ferr2")
    plt.plot(n, Ferr3(3, n), label="Ferr3")
    plt.plot(n, np.ones(n.size)*F1(3), label="exact")
    plt.legend()
    
    plt.figure()
    plt.semilogx(n, Ferr1(3, n), label="Ferr1")
    plt.semilogx(n, Ferr2(3, n), label="Ferr2")
    plt.semilogx(n, Ferr3(3, n), label="Ferr3")
    plt.semilogx(n, np.ones(n.size)*F1(3), label="exact")
    plt.legend()
    
    plt.figure()
    plt.loglog(n, np.abs(Ferr1(3, n)-F1(3)), label="Ferr1")
    plt.loglog(n, np.abs(Ferr2(3, n)-F1(3)), label="Ferr2")
    plt.loglog(n, np.abs(Ferr3(3, n)-F1(3)), label="Ferr3")
    plt.legend()
    
    plt.show()
    

def rectangleGauche(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des rectangles centrés """
    pas = (b-a)/n
    I = 0
    for i in range(n):
        ai = a + i*pas
        I += f(ai)
    return I*pas

def rectangleCentre(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des rectangles centrés """
    pas = (b-a)/n
    I = 0
    for i in range(n):
        ai = a + (i+0.5)*pas
        I += f(ai)
    return I*pas

def trapezeOpt(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des trapèzes """
    pas = (b-a)/n
    I=0.5*(f(a)+f(b))
    for i in range(1,n):
        ai = a+i*pas
        I = I+f(ai)
    return I*pas

def rectangleDroite(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des rectangles à droite """
    pas = (b-a)/n
    I = 0
    for i in range(n):
        ai = a + (i+1)*pas
        I += f(ai)
    return I*pas

def rectangles(a, b, f, F):
    exact = F(b)-F(a)
    nb_points = np.array([10,20,50,100,200,1000,2000,5000,10000,20000])
    intG = np.zeros(nb_points.shape)
    intD = np.zeros(nb_points.shape)
    intC = np.zeros(nb_points.shape)
    for n in range(len(nb_points)):
        intG[n] = rectangleGauche(a,b,nb_points[n],f)
        intD[n] = rectangleDroite(a,b,nb_points[n],f)
        intC[n] = rectangleCentre(a,b,nb_points[n],f)
    
    plt.figure()
    plt.loglog(nb_points, abs(intG-exact), label='R. Gauche')
    plt.loglog(nb_points, abs(intD-exact), label='R. Droite')
    plt.loglog(nb_points, abs(intC-exact), label='R. Centre')
    plt.legend()
    plt.show()

def rectangleGaucheVect(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des rectangles centrés """
    pas = (b-a)/n
    return pas*np.sum(f(np.arange(a, b-pas/2, pas)))

def rectangleCentreVect(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des rectangles centrés """
    pas = (b-a)/n
    return pas*np.sum(f(np.arange(a+pas/2, b, pas)))

def rectangleDroiteVect(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des rectangles à droite """
    pas = (b-a)/n
    return pas*np.sum(f(np.arange(a+pas, b+pas/2, pas)))

def rectanglesVect(a, b, f, F):
    exact = F(b)-F(a)
    nb_points = np.array([10,20,50,100,200,1000,2000,5000,10000,20000])
    intG = np.zeros(nb_points.shape)
    intD = np.zeros(nb_points.shape)
    intC = np.zeros(nb_points.shape)
    for n in range(len(nb_points)):
        intG[n] = rectangleGaucheVect(a,b,nb_points[n],f)
        intD[n] = rectangleDroiteVect(a,b,nb_points[n],f)
        intC[n] = rectangleCentreVect(a,b,nb_points[n],f)
    
    plt.figure()
    plt.loglog(nb_points, abs(intG-exact), label='R. Gauche')
    plt.loglog(nb_points, abs(intD-exact), label='R. Droite')
    plt.loglog(nb_points, abs(intC-exact), label='R. Centre')
    plt.legend()
    plt.show()



def trapezeNaif(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode des trapèzes """
    pas = (b-a)/n
    I = 0
    for i in range(0,n):
        ai = a + i*pas
        I = I + 0.5*f(ai) + 0.5*f(ai+pas)
    return I*pas

def simpson(a,b,n,f):
    """ Calcule l'intégrale de f entre a et b avec n subdivisions
        en utilisant la méthode de Simpson """
    pas = (b-a)/n
    I = 0
    for i in range(0,n):
        ai = a + i*pas
        I = I + f(ai)/6 + 2*f(ai+pas/2)/3 + f(ai+pas)/6
    return I*pas

def methodes(a, b, f, F):
    exact = F(b)-F(a)
    nb_points = np.array([10,20,50,100,200,1000,2000,5000,10000,20000])
    intG = np.zeros(nb_points.shape)
    intD = np.zeros(nb_points.shape)
    intC = np.zeros(nb_points.shape)
    intT = np.zeros(nb_points.shape)
    intS = np.zeros(nb_points.shape)
    for n in range(len(nb_points)):
        intG[n] = rectangleGauche(a,b,nb_points[n],f)
        intD[n] = rectangleDroite(a,b,nb_points[n],f)
        intC[n] = rectangleCentre(a,b,nb_points[n],f)
        intT[n] = trapezeOpt(a,b,nb_points[n],f)
        intS[n] = simpson(a,b,nb_points[n],f)
   
    plt.figure()
    plt.loglog(nb_points, abs(intG-exact), label='R. Gauche')
    plt.loglog(nb_points, abs(intD-exact), label='R. Droite')
    plt.loglog(nb_points, abs(intC-exact), label='R. Centre')
    plt.loglog(nb_points, abs(intT-exact), label='Trapezes')
    plt.loglog(nb_points, abs(intS-exact), label='Simpson')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # erreurs()
    # rectangles(0, 3, f1, F1)   # Question 10
    rectanglesVect(0, 3, f1, F1)   # Question 10, optimisée
    # methodes(0, 3, f2, F2)      # Question 15
