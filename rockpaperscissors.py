#SCHERE STEIN PAPIER MIT HAL 9000

print("Hallo, ich bin HAL 9000.")
print("Es ist 2001 und du fliegst mit dem Raumschiff 'Discovery' zum Jupiter.") 
print("Die Mission ist die Erforschung eines mysteriösen Monolithen,") 
print("der auf dem Mond gefunden wurde und ein Signal an Jupiter sendet.")
print("Lass uns Schere-Stein-Papier spielen. Wenn du gewinnst, lasse ich dich leben.")

from random import randint

hal_pkt = 0
hum_pkt = 0
hal9000 = 0

while True:

    human = input("Wähle Schere, Stein oder Papier. Wenn du das Spiel beenden möchtest, schreibe 'exit'.").lower()
    if human == "stein":
        human = 1
    elif human == "schere":
        human = 2
    elif human == "papier":
        human = 3
    else:
        if human == "exit":
            if hal_pkt > hum_pkt:
                print("Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte. Damit habe ich gewonnen!")
                break
            elif hum_pkt > hal9000:
                print("Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte. Damit hast du gewonnen und bleibst am Leben.")
                break
            else:
                print("Unentschieden!")
                break
        
    hal9000 = randint(1, 3)       
    
    if hal9000 == human:
       print("Unentschieden - Weiter geht's!")
    elif hal9000 == 1 and human == 2:                       # hal: Stein - hu: Schere
       hal_pkt += 1
       print("Ich Stein und du Schere. Ein Punkt für mich! Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte.")
    elif hal9000 == 3 and human == 2:                          # hal: Papier - hu: Schere
        hum_pkt += 1
        print("Ich Schere und du Stein. Ein Punkt für dich. Nicht schlecht. Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte.")        
    elif hal9000 == 2 and human == 1:                       # hal: Schere - hu: Stein
        hum_pkt += 1
        print("Ich Schere und du Stein. Ein Punkt für dich. Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte.")
    elif hal9000 == 3 and human == 1:                       # hal: Papier - hu: Stein
        hal_pkt += 1
        print("Ich Papier und du Stein. Ein Punkt für mich. Es sieht schlecht für dich aus. Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte.")
    elif hal9000 == 2 and human == 3:                       # hal: Schere - hu: Papier
        hum_pkt += 1
        print("Ich Schere und du Papier. Ein Punkt für dich. Das bedeutet nichts. Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte.")
    elif hal9000 == 1 and human == 3:                       # hal: Stein - hu: Papier
        hum_pkt += 1
        print("Ich Stein und du Papier. Der geht an dich. Du hast jetzt", hum_pkt, "und ich", hal_pkt, "Punkte.")
    else:
        print("Deine Eingabe ist nicht eindeutig. Versuche es nochmal!")
