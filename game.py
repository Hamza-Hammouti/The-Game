print("Level 1: Eigenschappen")

print("We beginnen met je eigenschappen.")
print("")
naamChar = input ("Wat is je voornaam en je achternaam?: ")

print("Dan hebben we ook je gewenste lengte nodig.")
print("")
print("Je lengte in cm:")
lengteChar = int(input(""))

print("")

print("En als laatste nog je leeftijd.")
print("")
print("Je leeftijd:")
leeftijdChar = int(input(""))

print("Je naam is " + naamChar)
print("Je bent " + str(lengteChar) + " in cm")
print("Je bent " + str(leeftijdChar) + " jaar oud")

print("")

if lengteChar < 170:
    print("Je bent best kort, misschien komt dit wel van pas..")
elif lengteChar > 169:
    print("Je bent best lang, misschien komt dit wel van pas..")

print("")

print("Level 2: De eerste dag")

print("")

print("Het is maandag, je loopt naar de bakker voor een broodje en je komt binnen.")
print("Je ziet dat dat bakker leeg is en je komt al snel aan de beurt.")
print("")
print("Bakker: Hallo! Wat mag het zijn?")
print("1) Een broodje kip")
print("2) Een frikandelbroodje")

broodjeOptie = input("Keuze: ")

print("")

if broodjeOptie == "1":
    print("Een broodje kip zal dan €3,50 zijn.")
elif broodjeOptie != "1":
    print("Een frikandelbroodje zal je dan €2,50 kosten.")

print("Wil je pinnen of contant betalen?")
print("1) Pinnen")
print("2) Contant betalen")

betaalOptie = input("Keuze: ")

print("")

if betaalOptie == "1":
    print("Je steekt je pinpas in het pinautomaat en je voert jouw pincode in. Je hoort een foutmelding op het apparaat.")
    print("Bakker: Je saldo is te laag..")
    print("Je verontschuldigt je en loopt de bakkerij uit vol met schaamte.")
elif betaalOptie == "2":
    print("Je graait in je zak en je voelt niets. Je checkt je andere zakken maar het blijkt dat je geen geld meer hebt.")
    print("Je verontschuldigt je en loopt de bakkerij uit vol met schaamte.")

print("")

print("Je beseft je dat je geen geld meer over hebt.")
print("Je realiseert je dat als je niet snel iets regelt dat je op straat komt te komen.")
print("Je denkt stevig na en er schiet je opeens wat te binnen, een overval..")

print ("")

confirmOptie = input("Wil je dit zeker weten doen? (ja of nee): ").lower()

print("")

print("Level 3: Setup")

print("")

if not confirmOptie == "nee":
    print("Je komt thuis en je gaat nadenken over jouw doelwit.")
    print("Je hebt 2 keuzes:")
    print("1) Een winkel")
    print("2) Een bank")
    targetOptie = input("Keuze: ")
    print("")
    
    if targetOptie == "1":
        print("Je kiest voor een winkel omdat dit simpeler lijkt dan een bank.")
    elif targetOptie == "2":
        print("Je kiest voor een bank omdat de beloning groter lijkt.")

    print("")
    print("Je hebt keuzes tussen een paar wapens")
    print("1) Een pistool")
    print("2) Een AK-47 rifle")
    print("3) Een AR-15 rifle")
    wapenOptie = int(input("Keuze: "))

    print("")

    if wapenOptie < 2:
        print("Je kiest voor een pistool")
        
    elif wapenOptie == 2 or wapenOptie == 3:
        print("Je kiest voor een rifle")

    print()

    print("Level 4: De grote dag") 

    print()

    if targetOptie == "1":
        print("Je loopt naar de Gucci winkel met een gespannen gevoel..")
        print("Je komt steeds dichterbij en je staat op veilige kijkafstand van de winkel.")
        print("")
        print("Zet je een masker op of niet? (ja of nee)")
        print("")
        maskerOptie = input("Keuze: ").lower()
    
    elif targetOptie == "2":
        print("Je loopt richting de dichtsbijzijnde bank met een gespannen gevoel..")
        print("Je komt steeds dichterbij en je staat op veilige kijkafstand van de bank.")
        print("")
        print("Zet je een masker op of niet? (ja of nee)")
        print("")
        maskerOptie = input("Keuze: ").lower()

    if wapenOptie <= 1 and maskerOptie == "ja":
        print("Je zet je masker op en je haalt je pistool tevoorschijn.")
    
    elif wapenOptie >= 2 and maskerOptie == "ja":
        print("Je zet je masker op en je haalt je rifle tevoorschijn.")

    elif wapenOptie == 1 and maskerOptie == "nee":
        print("Je zet je masker niet op want je denkt dat dit niet nodig is.")
        print("Je haalt je pistool tevoosrschijn.")

    elif wapenOptie >= 2 and maskerOptie == "nee":
        print("Je zet je masker niet op want je denkt dat dit niet nodig is.")
        print("Je haalt je rifle tevoorschijn.")
    
    elif targetOptie == "1" and wapenOptie == 1 and maskerOptie == "ja":
        print("Je rent de winkel in en je richt je pistool.")   
        print("Je zet de camera's niet uit aangezien je een masker op hebt.")

    elif targetOptie == "1" and wapenOptie >= 2 and maskerOptie == "ja":
        print("Je rent de winkel in en je richt je rifle.")
        print("Je vertelt de medewerker om niets geks te proberen.")
        print("Je zet de camera's niet uit aangezien je een masker op hebt.")

    elif targetOptie == "2" and wapenOptie == 1 and maskerOptie == "ja":
        print("Je rent de bank in en je richt je pistool op de bankmedewerker")
        print("Hij zit achter kogelvrij glas")
        print("Je vertelt de bankmedewerker om de deur open te doen")
        print("Hij toont geen gehoor en je schiet op het glas")
        print("Doordat je maar een pistool hebt richt het bijna geen schade aan")
        print("De bankmedewerker drukt op de noodknop en je beslist om te gaan vluchten")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Je wordt uiteindelijk niet gepakt maar je faalt en je komt de komen op straat.")
        print("Je komt te onderkoelen op straat doordat je je huis bent uitgestuurd. Je overlijdt.")
        print("")
        print("GAME OVER")
    
    elif targetOptie == "2" and wapenOptie == 1 and maskerOptie == "nee":
        print("Je rent de bank in en je richt je pistool op de bankmedewerker")
        print("Hij zit achter kogelvrij glas")
        print("Je vertelt de bankmedewerker om de deur open te doen")
        print("Hij toont geen gehoor en je schiet op het glas")
        print("Doordat je maar een pistool hebt richt het bijna geen schade aan")
        print("De bankmedewerker drukt op de noodknop en je beslist om te gaan vluchten")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("De politie doet een inval op je huis en je wordt opgepakt")
        print("Je krijgt levenslang door de ernst van de zaak")
        print("")
        print("GAME OVER")

    elif targetOptie == "2" and wapenOptie >= 2 and maskerOptie == "ja":
        print("Je rent de bank in en je richt je rifle op de bankmedewerker")
        print("Hij zit achter kogelvrij glas")
        print("Je vertelt de bankmedewerker om de deur open te doen")
        print("Hij toont geen gehoor en je schiet op het glas")
        print("Door de rifle die je hebt komt er een barst in het glas en schrikt de bankmedewerker")
        print("Hij opent de deur zonder op de noodknop te drukken")
        print("Je loopt naar de kluis en je vertelt de medewerker om de deur open te doen")
        print("De bankmedewerker doet wat je zegt omdat hij je rifle ziet.")
        print("De kluis gaat open en je ziet een kluis vol met biljetten.")
        print("Je pakt wat je kan pakken en je vlucht, voordat de politie aankomt ben je al thuis.")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Je hebt gewonnen, je hebt in totaal 100 miljoen euro gestolen en je bent verhuist naar je droomland.")
        print("Hier leef je nog een lang en gelukkig leven.")

    elif targetOptie == "2" and wapenOptie >= 2 and maskerOptie == "nee":
        print("Je rent de bank in en je richt je rifle op de bankmedewerker")
        print("Hij zit achter kogelvrij glas")
        print("Je vertelt de bankmedewerker om de deur open te doen")
        print("Hij toont geen gehoor en je schiet op het glas")
        print("Door de rifle die je hebt komt er een barst in het glas en schrikt de bankmedewerker")
        print("Hij opent de deur zonder op de noodknop te drukken")
        print("Je loopt naar de kluis en je vertelt de medewerker om de deur open te doen")
        print("De bankmedewerker doet wat je zegt omdat hij je rifle ziet.")
        print("De kluis gaat open en je ziet een kluis vol met biljetten.")
        print("Je pakt wat je kan pakken en je vlucht, voordat de politie aankomt ben je al thuis.")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Doordat je je masker niet hebt op gedaan wordt er binnen 20 minuten een inval gedaan op je huis.")
        print("Je wordt meegenomen en je krijgt uiteindelijk levenslang door de ernst van de zaak.")
        print("")
        print("GAME OVER")

    elif targetOptie == "1" and wapenOptie == 1 and maskerOptie == "nee":
        print("Je rent de winkel in en je richt je pistool.")
        print("Je vertelt de medewerker om niets geks te proberen.")
        print("Je ziet dat er camera's zijn in de winkel dus je probeert die kapot te maken.")
        print("Je gaat op de toonbank staan maar terwijl je dit doet wordt je van achter aangevallen")
        print("Je verliest je bewustzijn..")
        print("")
        print("GAME OVER")
    
    elif targetOptie == "1" and wapenOptie >= 2 and maskerOptie == "nee":
        print("Je rent de winkel in en je richt je pistool.")
        print("Je vertelt de medewerker om niets geks te proberen.")
        print("Je ziet dat er camera's zijn in de winkel dus je probeert die kapot te maken.")
        print("Je gaat op de toonbank staan maar terwijl je dit doet wordt je van achter aangevallen")
        print("Je verliest je bewustzijn..")
        print("")
        print("GAME OVER")
    
    else:
        print("Je hebt iets verkeerds ingevoerd.")
    
elif confirmOptie == "nee":
    print("Je doet verder niets en je wordt je huis uit gestuurd.")
    print("Je komt op straat en je zinkt steeds dieper door.")
    print("Je komt te overlijden op straat tussen de armoede..")
    print("")
    print("GAME OVER")

else:
    print("Je hebt iets verkeerds ingevoerd.")