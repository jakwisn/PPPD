
import random 
import copy 


#counting sort 

def bucket_sort(t) : 
    """
    t - lista liczb naturalnych
    """ 

    n = len(t) 

    # liczba kubełków taka jak najwieksza liczba w t
    buckets = [[] for i in range (max(t)+1)] 

    for i in range(n): 
        
        #dla kubełków stojących na indeksie o wartości t[i] apenduję tą wartość 
        buckets[t[i]].append(t[i])  
    
    output = [0] * n   # output 
    a = 0 

    for i in range (len(buckets)) : 
        for j in range (len(buckets[i])) :
            
            # chcę zwrócić kubełki w ludzki sposób
            output[a] = buckets[i][j]   
            a+= 1 

    return output



# quick sort 


def partition(t, start, stop):
    """
    Podzial zbioru wzgledem k-tego elementu dla k = (stop + start)//2
    Modyfikacja zadania 4.6
    """
    k = (stop + start) // 2
    p = t[k]
    i = start # indeks z przodu
    j = stop - 1 # indeks z tylu


    while True:

        while t[i] <= p and i < k:
            # idziemy do gory z dolnym licznikiem, az
            # dotrzemy do elementu ktory trzeba zamieniec
            i += 1
        while t[j] > p and j > k:
            # j.w tylko idziemy w dol z gornym licznikiem
            j -= 1

        if i == j:
            return i

        if i == k:
            # gdy na lewo od k były same liczby mniejsze 
            # to zamień t[k] z liczbą większą ( t[j]) i zmień k na j 
            t[j], t[k] = t[k], t[j]
            k = j
        elif j == k: 
            # gdy na prawo od k były same liczby od niego większe 
            # to zamień miejscami liczbę wiekszą oraz t[k] i zamień k na i 
            t[i], t[k] = t[k], t[i]
            k = i
        else:
            # znalezlismy elementy do zamiany
            # t[i] - pierwszy od lewej wiekszy od t[k]
            # t[j] - pierwszy od prawej mniejszy od t[k]
            t[i], t[j] = t[j], t[i]
            i += 1
            j -= 1
    return k        # zwróć pivota 



def quicksort(t):
    """ Wersja podstawowa """

    def _quicksort(t, start, stop):
        """ funkcja pomocnicza -- quicksort na podliscie """

        if start < stop:

            # dzielimy liste wzgledem elemntu t[(stop + start) // 2]
            p = partition(t, start, stop)

            # teraz t[p] jest na swoim miejscu i rekurencyjnie sortujemy
            # podlisty
            _quicksort(t, start, p)
            _quicksort(t, p+1, stop)

    _quicksort(t, 0, len(t))
    return t



def k_quicksort(t, k):
    """ k ostatnich jest posortowanych, reszta niekoniecznie """

    def _k_quicksort(t, k, start, stop):
        """ funkcja pomocnicza -- k_quicksort na podliscie """
        if start < stop:

            # dzielimy liste wzgledem elemntu t[(stop + start) // 2]
            p = partition(t, start, stop)

            if p > k : 
            # lewa podliste trzeba posortowac
                _k_quicksort(t, k, start, p)

            # a prawa tylko jesli p < k
            
            _k_quicksort(t, k, p+1, stop)

    _k_quicksort(t, k, 0, len(t))
    return t


#counting sort simplified 
def counting_sort(array, maxval):
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array

def our_digit(numer, miejsce)  : 
        
        bazowy = numer // 10**miejsce
        do_odjecia = (numer //10**(miejsce +1))*10 

        return bazowy - do_odjecia

#radix sort 


    


    
 
def counting_sort(alist, miejsce) : 

    lista  = copy.copy(alist) 
    for l in range(len(lista)) : 
        lista[l] = our_digit(lista[l], miejsce) 
    


    c = [0] * (max(lista)+1) 
     
    b = [0] * (len(lista)) 

    for i in range(len(c)) : 
        c[lista[i]] += 1 
    
    for j in range(0,len(c)) : 
        c[j] += c[j-1] 
    

    for j in range(len(lista)):
        b[c[lista[j]]] = alist[j] 
        c[lista[j]] -= 1  
        

    return b 


def mergeSort(alist):

    print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return alist

            
x = [random.randint(0,999) for i in range (10)] 
print(x) 
x = counting_sort(x, 2)       
print(x)  














    