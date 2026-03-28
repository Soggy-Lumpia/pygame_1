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
    
    menuActions = [1,2,3,4,5,6]

    while True: 
        print("Here are your current items: \n")
        # Iterate over maps list
        for i in range(0, len(maps)):
            if maps[i] == maps[0]:
                # print("Start -->  DEBUG")
                print('\033[32m' + f"Location: {maps[i]}\n" + '\033[39m')
                
                if maps[i] == "Start": 
                    for j in range(0, len(menuActions)):
                        if menuActions[j] == 0:
                            print("\033[36m 1. Move Forward\033[39m\n")
                            return 0
                            continue
                
                        elif menuActions[j] == 1:
                            print("\033[36m 2. Move Backward\033[39m\n")
                            return 1
                            continue
                
                        elif menuActions[j] == 2:
                            print("\033[36m 3. Pick Item\033[39m\n")
                            return 2
                            continue
                            
                        elif menuActions[j] == 3:
                            print("\033[36m 4. Drop Item \033[39m\n")
                            return 3
                            continue
                            
                        elif menuActions[j] == 4:
                            print("\033[36m 5. Show Inventory \033[39m\n")
                            return 4
                            continue
                            
                        elif menuActions[j] == 5: 
                            print("\033[36m 6. Exit \033[39m\n")
                            return 5
                            

                        start_inputChoices = input("Choose your action: ")
                        
                    try:
                        conv_input_int = int(start_inputChoices)
                        return conv_input_int
                            
                    except ValueError: 
                        print("Please choose a numerical option!\n")
                            
                
                                    
                elif maps[i] == "Forest": 
                    for j in range(0, len(menuActions)):
                        if menuActions[j] == 1:
                            print("\033[36m 1. Move Forward\033[39m\n")
                            position += 1
                            continue
                
                        elif menuActions[j] == 2:
                            print("\033[36m 2. Move Backward\033[39m\n")
                            continue
                
                        elif menuActions[j] == 3:
                            print("\033[36m 3. Pick Item\033[39m\n")
                            continue
                            
                        elif menuActions[j] == 4:
                            print("\033[36m 4. Drop Item \033[39m\n")
                            continue
                            
                        elif menuActions[j] == 5:
                            print("\033[36m 5. Show Inventory \033[39m\n")
                            continue
                            
                        elif menuActions[j] == 6: 
                            print("\033[36m 6. Exit \033[39m\n")
                            
                            
                            
                        start_inputChoices = input("Choose your action: ")
                        conv_input_int = int(start_inputChoices)
                        print(f"start_inputChoices type = {type(conv_input_int)}\n")
                        
                    if conv_input_int == 1 and position == 2: 
                        print("conv_input_int 1\n")
                        print(f"Current maps value: {maps[i]}\n")
                        position += 1
                  
                    
                    elif conv_input_int == 2: 
                        print("conv_input_int 2\n")
                        
                    elif conv_input_int == 3:
                        print("conv_input_int 3\n")
                    
                    elif conv_input_int == 4:
                        print("conv_input_int 4\n")
                    
                    elif conv_input_int == 5: 
                        print("conv_input_int 5\n")
                           
                          
        print(f"Position: {position} <--- DEBUG ")
    
                
            

                
    

navTerrain()        
        
        
        
        








        
    

    
    
    


