

def usuario():
    validado = True
    nombre = input("Ingresa tu nombre de usuario: ")
    
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
        
    if(validado):
        passw()
    else:
        usuario()

def passw():
    validado = True
    password = input("Ingresa tu password: ")
    msj = "La contraseña elegida no es segura."
    
    if len(password) < 8:
        validado = False
    
    mayuscula = False
    minuscula = False
    numeros = False
    noalfa = False
    
    for char in password:
        
        if char.islower():
            minuscula = True
        if char.isupper():
            mayuscula = True
            
        if char.isalnum():
            noalfa = True
        if char.isdigit():
            numeros = True
        
    
    if(validado and mayuscula and minuscula and numeros and noalfa):
        return True
    else:
        print(msj)
        passw()
    

if __name__=='__main__':
    usuario()