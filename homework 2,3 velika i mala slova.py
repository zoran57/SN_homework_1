# promjena velikih slova u mala i obrnuto

tekst = input("unesite tekst:")

print(" tekst napisan malim slovima: " + str.lower(tekst))
print("")

print(" tekst napisana VELIKIM slovima: " + str.upper(tekst))
print("")

print(" riječ napisan VELIKIM početnim slovom: " + str.capitalize(tekst))
print("")

print(" tekst napisan VELIKIM prvim slovom riječi: " + str.title(tekst))

