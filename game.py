print("Het is maandag, je loopt naar de bakker voor een broodje en je komt binnen.")
print("Je ziet dat dat bakker leeg is en je komt al snel aan de beurt.")
print("")
print("Bakker: Hallo! Wat mag het zijn?")
print("1) Een broodje kip")
print("2) Een frikandelbroodje")

optie1 = input("Keuze: ")

print("")

if optie1 == "1":
    print("Een broodje kip zal dan €3,50 zijn.")
elif optie1 == "2":
    print("Een frikandelbroodje zal je dan €2,50 kosten.")

print("Wil je pinnen of contant betalen?")
print("1) Pinnen")
print("2) Contant betalen")

optie2 = input("Keuze: ")

print("")

if optie2 == "1":
    print("Je steekt je pinpas in het pinautomaat en je voert jouw pincode in. Je hoort een foutmelding op het apparaat.")
    print("Bakker: Je saldo is te laag..")
    print("Je verontschuldigt je en loopt de bakkerij uit vol met schaamte.")
elif optie2 == "2":
    print("Je graait in je zak en je voelt niets. Je checkt je andere zakken maar het blijkt dat je geen geld meer hebt.")
    print("Je verontschuldigt je en loopt de bakkerij uit vol met schaamte.")

print("")

print("Je beseft je dat je geen geld meer over hebt.")
print("Je realiseert je dat als je niet snel iets regelt dat je op straat komt te komen.")
print("Je denkt stevig na en er schiet je opeens wat te binnen, een overval..")

print ("")

optie3 = input("Wil je dit zeker weten doen? (ja of nee): ").lower()

print("")

if optie3 == "ja":
    print("Je komt thuis en je gaat nadenken over jouw doelwit.")
    print("Je hebt 2 keuzes:")
    print("1) Een winkel")
    print("2) Een bank")
    optie4 = input("Keuze: ")
    print("")
    
    if optie4 == "1":
        print("Je kiest voor een winkel omdat dit simpeler lijkt dan een bank.")
    elif optie4 == "2":
        print("Je kiest voor een bank omdat de beloning groter lijkt.")

    print("")
    print("Je hebt keuzes tussen een paar wapens")
    print("1) Een pistool")
    print("2) Een AK-47 rifle")
    print("3) Een AR-15 rifle")
    optie5 = input("Keuze: ")

    print("")

    if optie5 == "1":
        print("Je kiest voor een pistool")
        
    elif optie5 == "2" or optie5 == "3":
        print("Je kiest voor een rifle")


elif optie3 == "nee":
    print("Je doet verder niets en je wordt je huis uit gestuurd.")
    print("Je komt op straat en je zinkt steeds dieper door.")
    print("Je komt te overlijden op straat tussen de armoede..")
    print("")
    print("GAME OVER")