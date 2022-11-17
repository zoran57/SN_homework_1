# pretvori km u milje
import random

ime = input("Kako se zoveš:")
print("Pozdrav" + " " + str.title(ime))

udaljenost = int(input("Upiši koliku si udaljenost danas prevalio u km:"))

print("Prevalili ste udaljenost u miljama:  ""(udaljenost * 0.621371)")

novi_unos = input("Dali želite ponovo unijeti udaljenost? (da ili ne): ")
if novi_unos == "da":
    udaljenost = int(input("Upiši koliku si udaljenost danas prevalio u km:"))
    print("Prevalili ste udaljenost u miljama:  ""(udaljenost * 0.621371)")
else:
    print("Žao nam je, želimo vam ugodan dan." )


"""
novi_unos = input("dali želite ponovo unijeti udaljenost? (da ili ne): ")
if novi_unos == "da":
    udaljenost = int(input("upiši koliku si udaljenost danas prevalio u km:"))
    print("Prevalili ste udaljenost u miljama:  ""(udaljenost * 0.621371)")

else:
    print("žao nam je, želimo vam ugodan dan." )
"""
print("Hvala na druženju s nama, pokušajte ponovo")
