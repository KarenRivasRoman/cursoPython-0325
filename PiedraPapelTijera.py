print("Bienvenido!!!")
player_1 = input("Ingresa el nombre del primer jugador:")
print("-----")
player_2 = input("Ingresa el nombre del segundo jugador:")

print(f"{player_1} VS {player_2}")

acction_1 = input(f"Jugador {player_1} ingresa tu tiro: ")
print("-----")
acction_2 = input(f"Jugador {player_2} ingresa tu tiro: ")

actions = ["piedra","papel","tijeras"]
acction_1 = acction_1.lower()
acction_2 = acction_2.lower()

if acction_1 in actions:
    if acction_2 in actions:
        if acction_1 ==  acction_2 :
            print("Empate")
        elif (acction_1 == actions[0] and acction_2 == actions[2]) or (acction_1 == actions[1] and acction_2 == actions[0]) or (acction_1 == actions[2] and acction_2 == actions[1]):
            print(f"Gana {player_1}")
        else:
            print(f"Gana {player_2}")
    else:
        print(f"{player_2} Revise su acción, las acciones permitidas son: piedra,papel,tijeras ")
else:
    print(f"{player_1} Revise su acción, las acciones permitidas son: piedra,papel,tijeras ")

