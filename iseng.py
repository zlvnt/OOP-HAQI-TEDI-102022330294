
#P
def P():
    for baris in range(7):
        for kolom in range(7):
            if kolom == 0 or (baris == 0 or baris == 7 // 2) and kolom < 7 // 2 + 1 or (kolom == 7 // 2 + 1 and (baris == 1 or baris == 7 // 2 - 1)):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()

#7
def N() : 
    counter = 0
    for i in range(0,7) : 
        print("*",end="") 
        for j in range(0,7+1) : 
            if ( j == 7 ): 
                print("*",end="") 
            elif ( j == counter) : 
                print("*",end="") 
            else : 
                print(end=" ") 
        counter = counter + 1
        print() 
    print()

#B
def B():
    for baris in range(7):
        for kolom in range(7):
            if (kolom == 0 or (baris == 0 or baris == 7 // 2 or baris == 7 - 1) and kolom < 5 - 1) or (kolom == 5 - 1 and (baris != 0 and baris != 7 // 2 and baris != 7 - 1)):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()
    
#Z
def Z():
    for baris in range(6):
        for kolom in range(6):
            if baris == 0 or baris == 6 - 1 or baris + kolom == 6 - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()

def Y() : 
    counter = 0
    for i in range(0,7) : 
        for j in range(0,7+1) : 
            if ( j == counter or j == 7 - counter and i <= 7 // 2 ): 
                print("*",end="") 
            else : 
                print(end=" ") 
        print() 
        if (i < 7 // 2) : 
            counter = counter + 1
    print()

def A(): 
    width = 10
    n = width // 2
    for i in range(0, 7): 
        for j in range(0, width+1): 
            if (j == n or j == (width - n) or (i == (7 // 2) and j > n and j < (width - n))): 
                print("*", end="") 
            else: 
                print(end=" ") 
        print() 
        n = n-1

def C() : 
    for i in range(0, 7) : 
        print("*",end="") 
        for j in range(0, 6 - 1) : 
            if (i == 0 or i == 7 - 1 ) : 
                print("*", end=" ") 
            else : 
                continue
        print() 

def D() : 
    for i in range(0,7) : 
        print("*", end="") 
        for j in range(0,9) : 
            if ( (i == 0 or i == 7 - 1) and j < 5 - 1 ): 
                print("*", end=" ") 
            elif (j == 9 - 1 and i != 0 and i != 7 - 1) : 
                print("*", end="") 
            else : 
                print(end=" ") 
        print() 

def E() :  
    for i in range(0,7) : 
        print("*",end="") 
        for j in range(0,5) : 
            if ( (i == 0 or i == 7 - 1) or (i == 7 // 2 and j <= 5 // 2) ): 
                print("*",end=" ") 
            else : 
                continue
        print() 

def F() : 
      
    for i in range(0,7) : 
        print("*",end="") 
        for j in range(0,6) : 
            if ( (i == 0) or (i == 7 // 2 and j <= 6 // 2) ): 
                print("*",end=" ") 
            else : 
                continue
        print()  



P()
N()
B()
Z()
Y()
A()
C()
D()
E()
F()