def new_file_and_exercise()
    a = input("What do you want to call your fitness tracker? ")
    new_file = open(a+".txt", 'w') #creates a new file
    print("Created new file. ")
    store = input("Input your exercise in the format: Muscle Group | Exercise Name | Sets| Weight | Reps | ")
    print("Input stored.")
    again = input("Do you want to enter another exercise. Yes or No.")
    if again == 'No':
        print("Thanks for using the exercise input app.")
    else:
        print("We will reset the app now so you can input another one.")
        new_file_and_exercise()
        
new_file_and_exercise()