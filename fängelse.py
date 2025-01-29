def main_menu():
    print("välkommen till helvetet denna spel är för åldergrupp 18+ ")
    print("1. Starta spelet")
    print("2. Exit")
    choice = input("ange 1 eller 2: ")
    if choice == "1":
        steg_ett()
    elif choice == "2":
        print(" tack föratt du spelade spelet1.")
        main_menu()
    else:
        print("game over ")
        main_menu()
def steg_ett():
    print("de heter bashar epstien diddy du är gripen för att du hailade på hitler på en synagoga du har rätt att ringa advokat  ")
    print("1. ring till advokat")
    print("2. vänta ")
    choice= input("välja 1 eller 2: ")
    if choice == "1":
        steg_två()
    elif choice == "2":  
        print(" du har blivit avrättad  ") 
    else:
        print("game over ")
        main_menu()
        
def steg_två():
    print("advokat tar dig ut från cellen det finns en vakt i hela fängelset vad ska du göra du har sovmedicin med dig ")
    print("1 spötta på vakten")
    print("2 fylla vakten kaffe med sov medicin ")
    choice = input("välja 1 eller 2")
    if choice == "1":
        print("vakten blir arg och dödar dig ")
    elif choice == "2": 
        print (" vakten sover nu du kan gå till fängelse gården ")
        steg_tre()
    else:
        print("forsökt igen ")


def steg_tre():
    print("du är på gården och sista steg")
    print("1 öppna dörren och rymma från fängelse")
    print("2 gå till polisstationen och be om en donut ")
    choice = input("välja 1 eller 2")
    if choice == "1":
        print("du rymmde du vann ")
    elif choice == "2": 
        print ("du har blivit gripen av polisen och blivit avrättat direkt på polisstationen ")
    else:
        print("game over  ")
        steg_tre()   
main_menu() 





