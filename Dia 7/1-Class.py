class Pajaro:
    pass


mi_pajaro = Pajaro()
print(mi_pajaro)
print(type(mi_pajaro))  # <class '__main__.Pajaro'>
print(isinstance(mi_pajaro, Pajaro))  # True
print(isinstance(mi_pajaro, object))  # True
print(dir(mi_pajaro))  # Muestra los atributos y métodos del objeto mi_pajaro
print(mi_pajaro.__class__)  # <class '__main__.Pajaro'>
print(mi_pajaro.__dict__)  # {}  # {}
print(Pajaro.__name__)  # 'Pajaro'
print(Pajaro.__module__)  # '__main__'
print(Pajaro.__bases__)  # (<class 'object'>,)
print(Pajaro.__doc__)  # None
print(Pajaro.__dict__)  # Muestra los atributos y métodos de la clase Pajaro

