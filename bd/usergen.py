"""import persona
import names
import random

def gen_per():
    generos={0:"Male",1:"Female"}
    dominio={0:"gmail.com",1:"hotmail.com",2:"outlook.com",3:"yahoo.com"}
    signos={0:"$",1:"_",2:"-",3:".",4:"%",5:"#"}
    genero=generos[random.randint(0,1)]
    nombre=names.get_first_name(generos[random.randint(0,1)])+names.get_first_name(generos[random.randint(0,1)])+names.get_last_name()+names.get_last_name()
    nombre=nombre.lower()
    correo=nombre+"@"+dominio[random.randint(0,3)]
    password=nombre[0]+nombre[1]+signos[random.randint(0,5)]+str(random.randint(0,9999))
    return correo,password

def insert():
    cantidad=100
    for _ in range(0,cantidad):
        sujeto=gen_per()
        try:
            persona.insert_persona(sujeto[0],sujeto[1])
            print(f"Usuario {_} agregado exitosamente")
        except Exception as e:
            print("No se pudo insertar el usuario, este ya existe",e)
            cantidad+=1

insert()


"""
import names
import random
import base64

def genera_correos():
    correo=str(names.get_first_name()+names.get_first_name()+names.get_last_name()+names.get_last_name())
    return correo

def genera_claves(correo):
    signos={0:"$",1:"_",2:"-",3:".",4:"%",5:"#"}
    password=correo+signos[random.randint(0,5)]+str(random.randint(0,9999))
    password=base64.b64encode(bytes(password, 'utf-8'))
    return password

def genera_usuario():
    archivo=open("datos0.txt","a")
    for v in range(0,50000000):
        correo=genera_correos()
        clave=genera_claves(correo)
        correo=correo+str(v)+"@monitoreo_precios.co"
        archivo.write("\""+correo+"\";\""+str(clave)[2:].rsplit("\'")[0]+"\""+"\n")
genera_usuario()