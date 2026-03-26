

def main():
    
    print("Welcome to your first program regarding for-loops\n")

    # USED for a direct list[]
    # Arbitrary lists

    food_list = ["Tomato", "Onion ", "Potato", "Chili"]
    num_list = [10, 20, 50, 90]


    # DIRECT ITERATION
    for i in food_list:
        print(f"Here is the list of food items: {i}\n")
        for j in num_list: 
            print(f"Here are the corresponding items to each one: {j}\n")

    # 
    for j in range(0,len(num_list)):
        element = food_list[j]
        print(f"Here are the price values: {element}\n")


if __name__ == "__main__":
    main()
