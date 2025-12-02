serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

print('-------------------------------------')

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")
        
print('-------------------------------------')

cliente = {'nombre': 'Edeher', 'edad': 43, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix', 
            'ficha_tecnica': {'protagonista': 'keanu reeves',
                              'director': 'Lana y Lilly Wachowsky'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
                'edad': edad,
                'ocupacion': ocupacion}:
            print("Es u cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print("esto es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("nose que es esto")