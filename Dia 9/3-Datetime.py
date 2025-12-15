import datetime

mi_hora = datetime.time(17, 35, 50, 1500)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.minute)
print(mi_hora.second)
print(mi_hora.microsecond)
print('----------------------------------------------')
mi_dia = datetime.date(2025, 10, 17)
print(mi_dia)
print(mi_dia.year)
print(mi_dia.month)
print(mi_dia.day)
print(mi_dia.ctime())
print(mi_dia.today())
print(datetime.datetime.now().date())
minutos = datetime.datetime.now().time().minute
print(minutos)

# from datetime import datetime, date, time

# mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
# print(mi_fecha)

# mi_fecha = mi_fecha.replace(month=11)
# print(mi_fecha)
# print('----------------------------------------------')
# nacimiento = date(1995, 3, 5)
# defuncion = date(2095, 6, 19)
# vida = defuncion - nacimiento
# print(vida.days)
# print('----------------------------------------------')
# despierta = datetime(2022, 10, 5, 7, 30)
# duerme = datetime(2022, 10, 5, 23, 45)

# vigilia = duerme - despierta
# print(vigilia)
# print(vigilia.seconds)
# minutos = time(14, 15, 14).minute
# print(minutos)



