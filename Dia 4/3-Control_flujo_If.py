if 10>0:
    print("es correcto")

else:
    print("no es correcto")


mascota='perro'
garras='si'

if mascota=='gato':
    print("tienes un gato")
elif mascota=='perro':
    print("tienes un perro")
    if garras=='si':
        print('rasca')
    else:
        print('no rasca')
else:
    print("no tienes un gato")