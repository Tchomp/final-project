# Timothy Swain
# Final Project File 1

print('Hello Traveler!\nWelcome to the country of Astora!\nWe are in a bit of a pickle, which is why I must ask your assistance.\nThere are currently monsters all over the empire, preventing trade, and even putting lives in danger! I could not ask you to murder them, but that is up to you. So please! On behalf of my family, I beseech you to begin your quest! Traveler, what is your name!')
playerName = input("What would you like your name to be? ")
print("So your name is " + playerName)
print('A shining light comes down to you, in a voice lighter than the clearest water, it speaks to you,' + playerName + 'There are many trials that lie ahead of you. It will be \ntedious, but it will test your wit. Use your skills to surpass these challenges, and become the new hero.' "The voice fades.")
print('Suddenly, a giant appears in front of you! What do you do?')
regardless = input("Fight it or Run away! ")
print('The giant does not give you a choice anyways! It smashes the ground underneath you and you fall deep into a cavern!')
print('You view many doors around you that lead to different places, it appears that you have fallen deep inside of a dungeon. What will you do?')
print('You find a Front Door, Left Door, and Right Door. Which path will you take?') 
DoorOne = input("Which door do you choose? ")

if DoorOne == "Left":
    print("You turn towards the left door and move over. Upon the door opening, you head inside and find a hallway. Inside of that hallway is a chuckling goblin.")
    Goblin = input("Human! What are you doing down in my caverns? You wish to pass? Then answer my question!\nWhat is the name of a small red fruit? ")
    
    if Goblin == "Apple":
        GoblinAnswer = input("Human! You have answered my question, would you like an apple? ")
        
        if GoblinAnswer == "Yes":
            print("Human! Have an apple.")
            Apple  = input("The human recieved an apple, do they choose to eat it in front of the gleaming goblin, or make a show of eating it, and pretend to eat it? ")

            if Apple == "Pretend":
                print("You make a show of eating the apple, the goblin seems mystified but allows the player entry through the hallway, you move to the end of the hallway and open the door.")

            if Apple == "Eat":
                print("You make a show of eating the apple, and the goblin laughs heartily. The apple was poisonous! You collapse. Game Over")
                quit()

        else:
            print ("Terrible human! Accept my knife in the apples stead!" "Game Over.")
            quit()
    else:
        print("Game Over")
        quit()

elif DoorOne == "Front":
    print("You move directly ini front of you to the Front Door. You open the door and head inside to find a towering trap! On the wall are three different colored devices.")
    print("The devices on the wall appear to be orbs of three different colors, red, blue, and yellow")
    print("Do you wish to touch the Red Orb, touch the Blue Orb, touch the Yellow Orb, or Look around?")
    if SearchOne == "Look around":
            print("There appear to be three tiles on the floor, the first being a Red Tile, the second being a Blue Tile, and the third being a Yellow Tile.")
            

elif DoorOne == "Right":
    print("You turn towards the right door and move over. Upon the door opening, you head inside and find what looks like a large wolf resting in the middle of a hallway. Do you pet the beast or try to sneak past it?")
    LargeWolf = input("Zzzzzzzzzzzzzzzzzzzz................")
    if LargeWolf == "Pet":
        print("Playful growling, the wolf continues to sleep, and the adventurer moves past the wolf to the end of the hallway")

    if LargeWolf == "Sneak":
        print("BARK, a viscious, horrifying ending appears. Game Over")
        quit() 
