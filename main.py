"""
print ("hello world")
IMIE = "Piotr"

print ("mam na imię " + IMIE)

a=5

for i in range (5):
    print(i)

Value =2

value_2 = 3

a = 'hello world'

for i in a:
    print(i, end = ' ')

for i in a:
    print(i)

lista = ['Maciek', 'Jola', 'Karol', 'Artur', 'Rozalia', 'Grzesiek', 'Magda', 'Kasia', 'Marcin', 'Jacek'
, 'Karol_2', 'Patryk', 'Piotr']
nowa_lista = sorted(lista)
for i in nowa_lista:
    print(i)

"""
"""
strat_value= 2
n= 7
krok = 2

for i in range (strat_value, n+1, krok):
    print(i)


owoce = ("jablko", 'gruszka', 'winogorono', 'wsinia', 'kiwi', 'banan', 'borowka','malina', 'mango', 'pomarańcza','grejfrut')

for i, owoce, in enumerate (owoce, 1):
    print(i, owoce)


a=3
b=25
for i in range(25,3,-1):
    print(i)

start_value=1
end=5
zmienna_pomocnicza=1

for i in range(start_value,end+1,1):
    wynik=zmienna_pomocnicza*i
    zmienna_pomocnicza=wynik
print(wynik)
"""
"""
a = 1
b = 5
zmienna = 1
wynik_suma = 0

for i in range(a,b+1,1):
    wynik_silnia = zmienna*i
    zmienna = wynik_silnia
    wynik_suma = wynik_suma + wynik_silnia
print(wynik_suma)
"""
1
12
123
"""

a=1
b=5

for i in range(a,b+1):
    for j in range(a,i+1):
        print(j,sep=' ',end=' ')
    print()

imie = input("jak masz na imie")
nazwisko = input("jak masz na nazwisko")

k="*"

nazwa=len(imie)+len(nazwisko)+3
gorny_dolny_wiersz= (10+10+nazwa)*k
srodek=10*k+" "+imie +" "+ nazwisko+" "+10*k
print(gorny_dolny_wiersz)
print(srodek)
print(gorny_dolny_wiersz)
"""

a = [1,2,3,4,5]
b = [6,7,8,9]
print(a+b)
print(a[2:]+b[:3])
c=a[2:3]
print(c)




#Marian Kowalski


