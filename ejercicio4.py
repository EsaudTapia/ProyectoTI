


def main():
    tam = input("Cuantos nombres ingrsaras: ")
    tam = int(tam)
    i = 0
    nombres = []
    generos= []
    while i < tam:
        nom = input("Ingresa el nombre {}: ".format(i+1))
        gen = input("Ingresa el genero de {}: H es hombre y M es mujer: ".format(nom))
        generos.append(gen)
        nombres.append(nom)
        i+=1
    p = input("Ingresa la poscicion de origen: ")
    p = int(p)
    n = input("Ingresa la cantidad de registros a mostrar: ")
    n = int(n)
    contador = 0
    while contador < n:
        if(generos[p]=="H"):
            print("Estimado {},  vote por mi".format(nombres[p-1]))
        else:
            print("Estimada {},  vote por mi".format(nombres[p-1]))
        contador+=1
        p+=1
        
        

if __name__=='__main__':
    main()