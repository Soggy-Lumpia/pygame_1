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
    
    
    while game_running: 
        # Iterate over maps list
        for i in range(0, len(maps)):
            print('\033[32m' + f"Location: {maps[i]}\n" + '\033[39m')
            print(f"Here are your current items: {inventory}\n")
            print(f"current position value: {position}\n") #DEBUG
            
            
            print("\033[36m1. Move Forward\n2. Move Backward\n3. Pick Item\n4. Drop Item\n5. Show Inventory\n6. Exit\n\033[39m")
        
            break
    # LOOP over all Locations
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
        # for j in range(0, len(menuActions)):
        #     print(f"\033[36m{menuActions[j]}\033[39m\n")
        #     if menuActions[j] == menuActions[0]:
        #         position += 1
        #         continue
        
        #     elif menuActions[j] == menuActions[1]:
        #         Move Backwards
        #         position -= 1
        #         continue
        
        #     elif menuActions[j] == menuActions[2]:
        #         print("\033[36m 3. Pick Item\033[39m\n")
        #         continue
                
        #     elif menuActions[j] == menuActions[3]:
        #         print("\033[36m 4. Drop Item \033[39m\n")
        #         continue
                        
        #     elif menuActions[j] == menuActions[4]:
        #         print("\033[36m 5. Show Inventory \033[39m\n")
        #         continue
                
        #     elif menuActions[j] == menuActions[5]: 
        #         game_running = False
                
        #         continue
                    
        # Fail-safe conditionals for Positioning:
        if position < 0:
            navTerrain()
        
        if game_running == False: 
            print("Okay Goodbye!\n")
            return 
        
        
        # Menu interactions 
        start_inputChoices = input("Choose your action: ")
        store_player_choice = start_inputChoices
        conv_choice = int(store_player_choice)
        store_conv_choice = conv_choice
        

                        
        try:
            
            store_conv_choice == type(int)
            print(f"Current maps value: {maps[i]}\n")
            print(f"Position: {position} <--- DEBUG MAIN ")
            print(f"successful converted_input type = {type(store_conv_choice)}")
            
          
                
        except store_conv_choice != type(int) or store_conv_choice < 1 or store_conv_choice > 6:
            raise ValueError("Please make a choice with whole numbers of 1 through 6!")
            print("\033[31mPlease choose a whole number option!\033[0m\n")
            print(f"FAIL-SAFE converted_input type = {type(start_inputChoices)}")
            
                          
        if store_conv_choice == 1: 
            print("store_conv_choice 1\n")
            position += 1
            print(f"Position: {position} <--- DEBUG 1 ")
            break
           
        elif store_conv_choice == 2: 
            print("store_conv_choice 2\n")
            print(f"Position: {position} <--- DEBUG 2 ")
                   
        elif store_conv_choice == 3:
            print("store_conv_choice 3\n")
            print(f"Position: {position} <--- DEBUG 3 ")
               
        elif store_conv_choice == 4:
            print("store_conv_choice 4\n")
            print(f"Position: {position} <--- DEBUG 4 ")
               
        elif store_conv_choice == 5: 
            print("store_conv_choice 5\n")
            print(f"Position: {position} <--- DEBUG 5 ")
           
        elif store_conv_choice == 6: 
            print("store_conv_choice 6\n")
            print(f"Position: {position} <--- DEBUG 6 ")             
                           

        
navTerrain()        
        
        
        
        








        
    

    
    
    

