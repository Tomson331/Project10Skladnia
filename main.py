# Day 19 -Składnia
a = 2

if a != 1:
    print(">> a jest różne od jeden")
elif a == 1:
    print(">> a jest równe jeden")
else:
    print(">> żaden warunek nie spełniony")

print(">> wyszlismy z if'a ten komunikat zawsze się wyświetli")

a = 2

if a == 1:
    print(">> a jest różne od jeden")

print("To się zawsze wyświetli")

a = 2

if a != 1:
    print(">> a jest różne od jeden")
    print("To się zawsze wyświetli")

# wariant 1
if a != 1:
    print(">> a jest różne od jeden")
elif a == 1:
    print(">> a jest równe jeden")
else:
    print(">> żaden warunek nie spełniony")

# wariant 2
if a != 1:
    print(">> a jest różne od jeden")
elif a == 1:
    print(">> a jest równe jeden")

#wariant 3
if a != 1:
    print(">> a jest różne od jeden")
else:
    print(">> żaden warunek nie spełniony")

if a != 1:
    print(">> a jest różne od jeden")
elif a > 0:
    print(">> a jest większe od zera")

nazwaBloga = "Zero To Junior"

print(nazwaBloga.upper())
print(nazwaBloga.lower())
print(nazwaBloga.startswith("Junior"))
print(nazwaBloga.endswith("Junior"))
print(nazwaBloga.count("o"))
