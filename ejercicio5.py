


def main():
    k = input("Ingresa el valor K: ")
    mayor = []
    menor = []
    igual = []
    multiplo = []
    if(k.isnumeric): 
        tam = input("Ingresa tamaño de la lista: ")
        
        lista = []
        i = 0
        while i < tam:
            val = input("Ingresa el número {}: ".format(i+1))
            if(val.isnumeric):  
                lista.append(val)
                i += 1 
            else:
                print("Ingresa un número valido en la posición {}".format(i+1))
        
    
        
    
    
    

if __name__=='__main__':
    main()