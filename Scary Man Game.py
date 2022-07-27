print("WELCOME! LET'S START THE ADVENTURE!")
print("")
print("You are standing outside of your house and you see a man running towards you and asking for urgent shelter.")
print("")

print("Will you provide shelter to him. (Yes / No)")

ans1 = input(">>")

if ans1 == "Yes" or ans1 == "yes" or ans1 == "y" or ans1 == "Y":
    print(" After 2 minutes, the Police came to your house and ask you that whether the thief is in your house or not. Will you say (Yes / No) ")
    
    ans2= input(">>")    
    
    if ans2 == "Yes" or ans1 == "yes" or ans1 == "y" or ans1 == "Y":
        print(" You are an honest person. He was a thief and you won the Game.")
        
    elif ans2 == "No" or ans1 == "no" or ans1 == "n" or ans1 == "N":
              print(" You helped a thief. Now, go to Jail. GAME OVER")
            
    else:
              print(" You typed the wrong input. GOODBYE!")
            
elif ans1 == "No" or ans1 == "no" or ans1 == "n" or ans1 == "N":
    print(" Now, he is trying to kill you. Will you knock him down? (Yes / No)")
    ans3 = input(">>")
              
    if ans3 == "Yes" or ans1 == "yes" or ans1 == "y" or ans1 == "Y":
        print(" Congrats! He was a thief and you helped the police catch him with your bravery!")
        
    elif ans3 == "No" or ans1 == "no" or ans1 == "n" or ans1 == "N":
        print("Sorry you are dead. He was a thief and he killed you. GAME OVER")
        
    else:
        print(" You typed the wrong input. GOODBYE!")
else:
    print(" You typed the wrong input. GOODBYE!")
