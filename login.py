

def login(clientes):
    
    activador=True
    while activador==True:
     try:
        id=int(input("ingrese su ID de inicio "))
        
        if id==0:
            
            return "admin"
            activador=False
            
        while id not in clientes:
            print("ese id no esta registrado seleccione otro")
            id=int(input("ingrese su ID de inicio"))
            
     
        
        nombre=input("ingrese su nombre o (salir) para salir").lower().strip()
        
        if nombre =="salir":
            activador=False
        
        while not nombre.isalpha():
            print("ingrese un nombre valido")
            nombre=input("ingrese su nombre").lower().strip()
            
        contraseña=int(input("ingrese su id registrado"))
        
        if nombre==clientes[id]["nombre"] and contraseña==id:
            
            return "cliente"
            activador=False
            
        else: 
            print("ese id no coincide con su nombre o contraseña")
            
    
     except ValueError:
         print("ingrese un valor valido")


    