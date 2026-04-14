# This will be a text-based game that the player 
# will be able to navigate several maps and find cool items! 
 
 
 
 
 
 
 
 # CHANGING IT TO FOR LOOP ITERATION BY 

 
 
 
import colorama
from colorama import Fore, init 


colorama.init()


def navTerrain()-> int: 

    # Different LOCATIONS
    maps = ["Start", "Forest", "Cave", "River", "Treasure"]
    position: int = 0
    inventory = ["","",""]
    cave_Items = {"useful": "rope", "stupid": "chocolate"}
    game_running = True
    
    
    while game_running: 
        if game_running == False: 
            print("Okay Goodbye!\n")
            return 
        # Fail-safe conditionals for Positioning:
        if position < 0:
            print("\033[31mCan't go back to start!\033[39m")
            
            reset_Inventory = len(inventory[0])
            print(f"reset_Inventory value: {reset_Inventory}")
            navTerrain()
            break
        
        if position > 6: 
            print("You've finished your journey!\n...")
            return 
        # Iterate over maps list
        for i in range(0, len(maps)):
            print('\033[32m' + f"Location: {maps[i]}\n" + '\033[39m')
            print(f"Here are your current items: {inventory}\n")
            print(f"current position value: {position}\n") #DEBUG
            print("\033[36m1. Move Forward\n2. Move Backward\n3. Pick Item\n4. Drop Item\n5. Show Inventory\n6. Exit\n\033[39m")
            
     
     
            # Menu interactions INPUT
            start_inputChoices = input("Choose your action: ")
            store_player_choice = int(start_inputChoices)
            
            # LOOP over all Locations
            if i == 0: 
                print("\033[0;35mGood luck on your journey, brave soul!..\033[39m\n")
            # Forest maps[1]
            if i == 1:
                # Learn to use .INSERT (appending value to specific index)
                # Learn to use .APPEND(appending value end of list)
                print("\033[1;93mYou see a torch in your midst...\033[39m\n")
                
            # Cave maps[2]
            if i == 2:
                # autoItem2 = inventory.insert(1,"key")
                print("Welcome to the cave...\n")
                
            # River maps[3]   
            if i == 3:
                print("Welcome to the River!\n")
                
            if i == 4:
                print("You've finally reached the treasure\n!")
            
            
            
            if position < 0:
                print("\033[31mCan't go back to start!\033[39m")
                 
                reset_Inventory = len(inventory[0])
                print(f"reset_Inventory value: {reset_Inventory}")
                navTerrain()
                break
             
            if position > 6: 
                print("You've finished your journey!\n...")
                return 
                
            # Move Forward 
            if store_player_choice == 1: 
                print("store_player_choice 1--> Move Forward\n")
                position += 1
                print(f"Position: {position} <--- DEBUG 1 ")
                continue
        
            # Move Backward 
            elif store_player_choice == 2: 
                print("store_player_choice 2 --> Move Backward\n")
                position -= 1
                print(f"Position: {position} <--- DEBUG 2 ")
        # Interacting menu options 
            # Pick Item 
            elif store_player_choice == 3:
                print("store_player_choice 3 --> Pick Item\n")
                print(f"Position: {position} <--- DEBUG 3 ")
        # for j in range(0, len(menuActions)):
            # Drop Item       
            elif store_player_choice == 4:
                print("store_player_choice 4 --> Drop Item\n")
                print(f"Position: {position} <--- DEBUG 4 ")
        #     print(f"\033[36m{menuActions[j]}\033[39m\n")
            # Show Inventory 
            elif store_player_choice == 5: 
                print("store_player_choice 5\n")
                print(f"Position: {position} <--- DEBUG 5 ")
        #     if menuActions[j] == menuActions[0]:
            # Exit   
            elif store_player_choice == 6: 
                print("store_player_choice 6\n")
                print(f"Position: {position} <--- DEBUG 6 ")
                game_running = False
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
                    

        # ERROR HANDLING                        
            try:
                store_player_choice = int(start_inputChoices)
            
                
            except store_player_choice == None or store_player_choice < 1 or store_player_choice > 6:
                raise ValueError("Please make a choice with whole numbers of 1 through 6!")
                print("\033[31mPlease choose a whole number option!\033[0m\n")
                print(f"FAIL-SAFE converted _input type = {type(store_player_choice)}")
            
            print(f"Current maps value: {maps[i]}\n")
            print(f"Position: {position} <--- DEBUG MAIN ")
            print(f"successful converted_input type = {store_player_choice}")

                
        
                
            
            
                           

        
navTerrain()        
        
        
        
        








        
    

    
    
    

