# This will be a text-based game that the player 
# will be able to navigate several maps and find cool items! 
import colorama
from colorama import Fore, init 


colorama.init()


def navTerrain()-> int: 

    # Different LOCATIONS
    maps = ["Start", "Forest", "Cave", "River", "Treasure"]
    position: int = 0
    inventory = ["","",""]
    game_running = True
    
    menuActions = ["1. Move Forward",
        "2. Move Backward",
        "3. Pick Item",
        "4. Drop Item",
        "5. Show Inventory",
        "6. Exit"]
    
    while game_running: 
        # Iterate over maps list
        for i in range(0, len(maps)):
            print('\033[32m' + f"Location: {maps[i]}\n" + '\033[39m')
            print(f"Here are your current items: {inventory}\n")
            print(f"current position value: {position}\n") #DEBUG
            
    # Forest
        if maps[i] == maps[1]:
            # Learn to use .INSERT (appending value to specific index)
            # Learn to use .APPEND(appending value end of list)
            autoItem1 = inventory.insert(1,"torch")
            break
    # Cave
        if maps[i] == maps[2]:
            autoItem2 = inventory.insert(2,"key")
            break
        
        if maps[i] == maps[3]:
            break
        
        # Interacting menu options 
        for j in range(0, len(menuActions)):
            print(f"\033[36m{menuActions[j]}\033[39m\n")
            if menuActions[j] == menuActions[0]:
                position += 1
                continue
        
            elif menuActions[j] == menuActions[1]:
                print("\033[36m 2. Move Backward\033[39m\n")
                # position -= 1
                continue
        
            elif menuActions[j] == menuActions[2]:
                # print("\033[36m 3. Pick Item\033[39m\n")
                continue
                
            elif menuActions[j] == menuActions[3]:
                # print("\033[36m 4. Drop Item \033[39m\n")
                continue
                        
            elif menuActions[j] == menuActions[4]:
                # print("\033[36m 5. Show Inventory \033[39m\n")
                continue
                
            elif menuActions[j] == menuActions[5]: 
                continue
                    
        # Fail-safe conditionals for Positioning:
        if position < 0:
            navTerrain()
    
            
        start_inputChoices = input("Choose your action: ")
        store_player_choice = start_inputChoices
                        
        try:
            # convert integer
            conv_choice = int(store_player_choice)
            if conv_choice >= 1 and conv_choice < 6: 
                continue
                
                print(f"Current maps value: {maps[i]}\n")
                print(f"Position: {position} <--- DEBUG MAIN ")
                
                if conv_choice == 1: 
                    print("conv_choice 1\n")
                    print(f"Position: {position} <--- DEBUG 1 ")
                
                if conv_choice == 2: 
                    print("conv_choice 2\n")
                    print(f"Position: {position} <--- DEBUG 2 ")
                        
                if conv_choice == 3:
                    print("conv_choice 3\n")
                    print(f"Position: {position} <--- DEBUG 3 ")
                    
                if conv_choice == 4:
                    print("conv_choice 4\n")
                    print(f"Position: {position} <--- DEBUG 4 ")
                    
                if conv_choice == 5: 
                    print("conv_choice 5\n")
                
                    print(f"Position: {position} <--- DEBUG 4 ")
                  

                        
        except ValueError: 
            print("Please choose a whole number option!\n")
            
                          
                                
                                    
            # elif maps[i] == "Forest": 
            #     for j in range(0, len(menuActions)):
            #         if menuActions[j] == 1:
            #             print("\033[36m 1. Move Forward\033[39m\n")
            #             position += 1
            #             continue
            
            #         elif menuActions[j] == 2:
            #             print("\033[36m 2. Move Backward\033[39m\n")
            #             continue
            
            #         elif menuActions[j] == 3:
            #             print("\033[36m 3. Pick Item\033[39m\n")
            #             continue
                        
            #         elif menuActions[j] == 4:
            #             print("\033[36m 4. Drop Item \033[39m\n")
            #             continue
                        
            #         elif menuActions[j] == 5:
            #             print("\033[36m 5. Show Inventory \033[39m\n")
            #             continue
                        
            #         elif menuActions[j] == 6: 
            #             print("\033[36m 6. Exit \033[39m\n")
                        
        print(f"converted_input type = {type(conv_choice)}")                   

        
navTerrain()        
        
        
        
        








        
    

    
    
    

