

def usuario(nom):
    validado = True
    nombre = nom
    
    if len(nombre) < 6:
        validado = False
        print("El nombre de usuario debe contener al menos 6 caracteres.")
        
    if len(nombre) > 12:
        validado = False
        print("El nombre de usuario no puede contener más de 12 caracteres.")
    
    if nombre.isalnum():
        valido = True
    else:
        print("El nombre de usuario puede contener solo letras y números.")
        validado = False
        
    return validado

def passw():
    validado = True
    password = input("Ingresa tu password: ")
    msj = "La contraseña elegida no es segura."
    
 
    mayuscula = False
    minuscula = False
    numeros = False
    noalfa = False
    espacio = False
    
    
    ext=len(password)
    if ext<= 8:
        validado = True
    else:
         msj = "La contraseña debe tener un tamaño de 8 caracteres"
    
    
    for char in password:
        
        if char.islower():
            minuscula = True
        else:
            msj='Debe tener letras'
            
        if char.isupper():
            mayuscula = True
        else:
            msj='Debe tener minimo uan letra mayuscuala'
            
            
        if char.isalnum(): 
            noalfa = True
        else:
            msj='Debe tener minimo un alfanumerico'    
        
        
        if char.isdigit():
            numeros = True
        else:
            msj='Debe tener minimo un numero'    
            
            
        if char.isspace():
           espacio  = True
        else:
            msj='No debe tener espacio'  
            
      
    
    if(validado and mayuscula and minuscula and numeros and noalfa ):
         print("Todo esta validado")
    else:
        print(msj)
        passw()
    
def main():
    nom = input("Ingresa tu nombre de usuario: ")
    res = usuario(nom)
    
    if res:
        passw()
           
    else:
        main()
    

if __name__=='__main__':
    main()