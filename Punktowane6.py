
import math 
import matplotlib.pyplot as plt

class Wielomian : 

    def __init__(self, wspolczynniki ) :
        if not isinstance(wspolczynniki,list) : 
            raise Exception(" wspolczynniki nie sa lista")

        # dla kazdego sprawdz czy jest intem 
        for i in range(len(wspolczynniki)) : 
            assert isinstance(wspolczynniki[i], int) 
                # jesli nie zwroc blad  
        

        #zaczynajac od konca wywal wszystkie zera po ostatniej niezerowej cyferze
        suma = -1 
        for i in range(len(wspolczynniki)-1 ,-1, -1) :
            suma += 1  
            if wspolczynniki[i] != 0 :
                break
        
        do_ktorego = len(wspolczynniki) -suma 
        
        wlasciwe_wspolczynniki = [] 
        for i in range(do_ktorego) : 
            wlasciwe_wspolczynniki.append(wspolczynniki[i]) 

        self.__wspolczynniki = wlasciwe_wspolczynniki 
     
    def __repr__(self) : 
        """ printuje sama siebie w estetyczny sposob""" 
        napis =''
        for i in range(len(self.__wspolczynniki)) : 
            a = self.__wspolczynniki[i]
            str_i = str(i)  
            str_a = str(a)+'x'+'^'+str_i+' '
             
            napis += str_a 
        return napis

    def get_stopien(self) : 
        """zwraca stopien wielomianu""" 

        m = len(self.__wspolczynniki) -1 
        return m
    

    def get_wspolczynniki(self) : 
        """ zwraca wspolczynniki wielomianu""" 
        return self.__wspolczynniki


    def __call__(self, x) : 

        w = self.__wspolczynniki
        output = 1 
        for i in range(len(w)-1,0,-1) : 
            if i == (len(w) -1) : 
                output *= w[i]*x  
            else: 
                output *=x 
            
            output += w[i-1]
        return output
    
    def plot(self, a=0,b=1,hline = 0 ) : 

        x = [i/100 for i in range (a*100,b*100)]
        y = [self(i/100) for i in range(len(x)) ]
        plt.plot(x, y) # rysuje lamana laczaca punkty

        z = [hline for i in range(len(x))] 
        plt.plot(x,z)
        plt.show()

    def pochodna(self) :
        wsp = self.__wspolczynniki 
        w = [0]*(len(wsp)-1) 

        for i in range(len(w)) : 
            w[i] = wsp[i+1]*(i+1) 

        W = Wielomian(w) 
        return W
    
    def miejsce_zerowe(self, start, eps= 10**(-12), M=100):
        """ Metoda Newtona """ 
        x0 = start 
        
        p = self.pochodna() 

        for i in range(1,M) : 
            prev = x0
            if p(x0) != 0 :
                x0 = x0 - self(x0)/p(x0)  
               

            if math.fabs(self(x0)) < eps or math.fabs(x0 - prev) < eps : 
                return x0 

        return math.nan 
        





##### TESTOWANIE ###

w1 = Wielomian([1,2,3])
print("""--- test 1 ---\nw1: {0},
         stopien: {1:d},
         w1(0) = {2:6.3f},
         w1(1) = {3:6.3f},
         miejsce zerowe: {4:6.3f}\n""".format(w1, w1.get_stopien(), 
                                              w1(0), w1(1), w1.miejsce_zerowe(start=0)))

d1 = w1.pochodna()
print("""d1: {0},
         stopien: {1:d},
         d1(0) = {2:6.3f},
         d1(1) = {3:6.3f},
         miejsce zerowe: {4:6.3f}""".format(d1, d1.get_stopien(), 
                                            d1(0), d1(1), d1.miejsce_zerowe(start=0)))



w2 = Wielomian([3])
print("""--- test 2 ---\nw2: {0},
         stopien: {1:d},
         w2(0) = {2:6.3f},
         w2(1) = {3:6.3f},
         miejsce zerowe: {4:6.3f}\n""".format(w2, w2.get_stopien(), 
                                              w2(0), w2(1), w2.miejsce_zerowe(start=0)))


d2 = w2.pochodna()
print("""d2: {0},
         stopien: {1:d},
         d2(0) = {2:6.3f},
         d2(1) = {3:6.3f},
         miejsce zerowe: {4:6.3f}""".format(d2, d2.get_stopien(), 
                                            d2(0), d2(1), d2.miejsce_zerowe(start=0)))


w3 = Wielomian([8, -7, 6, -5, 4, -3,  2, -1, 0])
print("""--- test 3 ---\nw3: {0},
         stopien: {1:d},
         w3(0) = {2:6.3f},
         w3(1) = {3:6.3f},
         miejsce zerowe: {4:6.3f}\n""".format(w3, w3.get_stopien(), 
                                              w3(0), w3(1), w3.miejsce_zerowe(start=0)))


d3 = w3.pochodna()
print("""d3: {0},
         stopien: {1:d},
         d3(0) = {2:6.3f},
         d3(1) = {3:6.3f},
         miejsce zerowe: {4:6.3f}""".format(d3, d3.get_stopien(), 
                                            d3(0), d3(1), d3.miejsce_zerowe(start=-5)))

w3.plot() # zob. Rys. 1
d3.plot() # zob. Rys. 2

