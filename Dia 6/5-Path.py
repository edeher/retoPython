from pathlib import Path

base = Path.home()
guia = Path("Barcelona", "Sagrada _familia")
guia1 = Path(base, "Europa", "España",
             Path("Barcelona", "sagrada_Familia.txt"))
guia2 = guia1.with_name("La_pedrera.txt")

print("base  : ", base)
print("guia  : ", guia)
print("guia1 : ", guia1)
print("guia2 : ", guia2)
print("Parent : ", guia1.parent)
print("Parent_Parent : ", guia1.parent.parent)
print("Parent_Parent_Parent : ", guia1.parent.parent.parent)
print('---------------------------------------------------------------------')

guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("*.txt"):
    print(txt)
print('---------------------------------------------------------------------')

for txt in Path(guia).glob("**/*.txt"):
    print(txt)
    print(txt)
print('---------------------------------------------------------------------')

guia3 = Path("Europa", "España", "Barcelona", "SagradaFamilia.txt")
print(guia3)
en_europa = guia3.relative_to(Path("Europa"))
en_espania = guia3.relative_to(Path("Europa", "España"))
print("Europa : ", en_europa)
print("espana : ", en_espania)