from game_LCM import brain_lcm
from game_Progression import brain_progression

while True:
    game_option = input("1 - LCM\n2 - Progressions\n9 - quit\n")
    if game_option == '1':
        brain_lcm()
    elif game_option == '2':
        brain_progression()
    elif game_option == '9':
        print("Bye!")
        break
    else:
        print("Invalid option. Choose again")