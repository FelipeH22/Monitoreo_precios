import persona
import names
import random

def gen_per():
    generos={0:"Male",1:"Female"}
    dominio={0:"gmail.com",1:"hotmail.com",2:"outlook.com",3:"yahoo.com"}
    signos={0:"$",1:"_",2:"-",3:".",4:"%",5:"#"}
    genero=generos[random.randint(0,1)]
    nombre=names.get_full_name(genero).lower().split()
    correo=nombre[0]+nombre[1]+"@"+dominio[random.randint(0,3)]
    password=nombre[0]+nombre[1]+signos[random.randint(0,5)]+str(random.randint(0,9999))
    return correo,password

def insert():
    sujeto=gen_per()
    try:
        persona.insert_persona(sujeto[0],sujeto[1])
        print("Usuario agregado exitosamente")
    except:
        print("No se pudo insertar el usuario, este ya existe")
        insert()

insert()