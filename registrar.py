
datos_user=()





def registrar(clientes):

 
    activador=True
    while activador==True:
        try:
            id=int(input("ingrese su ID de inicio "))
            activador=True

        except ValueError:
            print("ingrese un valor valido")
            id=int(input("ingrese su ID de inicio "))

        while id in clientes:
            print("ese id ya fue tomado seleccione otro")
            id=int(input("ingrese su ID de inicio"))




        nombre=input("porvafor ingrese su nombre ").lower().strip()

        while not nombre.isalpha():
            print("ingrese un nombre valido")
            nombre=input("porvafor ingrese su nombre ").lower().strip()

        email=input("ingrese su email ")

        while "@" not in email:
            print("ingrese un correro valido")
            email=input("ingrese su email ")



        clientes[id]={"nombre":nombre,
                    "email":email}

        data= list(clientes.items())
        data+=datos_user

        desea_registrar=input("desea registrar otro usuario si/no ").lower().strip()

        while desea_registrar!="si" and desea_registrar!="no":
            print("ingrese un valor valido")
            desea_registrar=input("desea registrar otro usuario si/no").lower().strip()

        if desea_registrar=="no":
            activador=False

        
    return clientes

