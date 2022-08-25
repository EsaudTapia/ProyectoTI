
#l,dclcc,. cls,cla,scls,dc lsc lsdc,lsdc sldc sldcls,dclsd,clsd,cl sdlc sldc lsdclsd,c

def main():
    k = input("Ingresa el valor K: ")
    k = int(k)
    mayor = []
    menor = []
    igual = 0
    multiplo = []
    if(k > 0): 
        tam = input("Ingresa tamaño de la lista: ")
        tam = int(tam)
        lista = []
        i = 0
        while i < tam:
            v = input("Ingresa el número {}: ".format(i+1))
            val = int(v)
            if(val > 0):  
                if val > k:
                    mayor.append(val)
                elif val < k:
                    menor.append(val)
                elif val == k:
                    igual += 1
                    
                
                if val % k == 0:
                    multiplo.append(val)
                i += 1 
            else:
                print("Ingresa un número valido en la posición {}".format(i+1))
        
        print("N° mayores a {}".format(k))
        print(mayor)
        print("N° menores a {}".format(k))
        print(menor)
        print("N° iguales a {}".format(k))
        print(igual)
        print("N° multiplos a {}".format(k))
        print(multiplo)
        

if __name__=='__main__':
    main()
