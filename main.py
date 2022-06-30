

from sqlalchemy import false, true


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
    
    countEsp = 0
    countAlnum = 0
    countMayu= 0
    countMin= 0
    countDigit=0
    mayuscula = False
    minuscula = False
    numeros = False
    noalfa = False
    espacio = False
    validado = False
    
    
    
    ext=len(password)
    if ext>= 8:
        validado = True
    else:
         msj = "La contraseña debe tener un tamaño de 8 caracteres"
    
    
    for char in password:
        
        if char.islower():
            countMin +=1
        
            
        if char.isupper():
           countMayu +=1
            
            
        if char.isalnum():               
            i=''
        else:
            countAlnum +=1;
                          
        if char.isdigit():
            countDigit +=1 
          
            
            
       
      
    
    for i in range(0, len(password)):                   
          if password[i] == " ": 
              countEsp += 1
        
        
    if countMin<0:
        msj='debe contener minimo una minuscula'
    else:
        minuscula= True
            
    if countMayu<0:
        msj='debe contener minimo una Mayuscula'
    else:
        mayuscula= True
        
    if countEsp<0:
            msj='no debe contener espcios'
    else:
            espacio= True
                        
    if countDigit <0 :
            msj='Debe contener minimo un numero'
    else:
            numeros=True
        
    if countAlnum <=0 :
            msj='Debe tener un no alfabetico y no numerico'
    else:
            noalfa=True
            
       
            
            
        

            
      
    
    if(validado and mayuscula and minuscula and numeros and noalfa  and espacio):
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