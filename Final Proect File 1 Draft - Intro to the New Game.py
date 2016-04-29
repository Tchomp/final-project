# Timothy Swain
# Final Project File 1

print('Hello Traveler!\nWelcome to the country of Astora!\nWe are in a bit of a pickle, which is why I must ask your assistance.\nThere are currently monsters all over the empire, preventing trade, and even putting lives in danger! I could not ask you to murder them, but that is up to you. \nSo please! On behalf of my family, I beseech you to begin your quest! Traveler, what is your name!')
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
                GiantQuizOne = input("Human! *You look up to see the giant cackling down at you, the Giant who had sent you down here!* Me guard exit to cave, me have quiz to give dumb human, no living person answer quiz right. What start day 4 legs, go 3 legs mid day, and 2 legs at the end. *A human?* ")
                        
                if GiantQuizOne == "Giant":
                    print("The giant looks stunned, he seems to rise up to both legs, looking at the human with a fuming attitude as its hands shake with rage! The giant appears ready to fight!")
                    GiantFightThree = input("Finally! You get to pay back the giant! Do you choose to run towards the sword in the ground, run away, or attack the giant! ")

                    if GiantFightOne == "Run Away":
                        print("You pick up speed, and attempt to run between the giants legs towards the door at the end of the room! The giant roars, and makes an effort turning around in the tiny dungeon room. It swings a fist, but with already picked up speed, you easily dodge. You escape!\n You open the door and find freedom, you no longer have to go through that hellish dungeon again.")
                        quit()

                    if GiantFightOne == "Fight Giant":
                        print("You rear your arm back, you feel all of the moments in your life have led up to this moment. Both beings clash fists, you die. Game Over.")
                        quit()

                    if GiantFightOne == "Run for Sword":
                        print("You roll with astonishing accuracy and flexibility towards the sword, pulling it out in an almost elegant fashion, you whip forward to lunge at the giant, your arm leaning back. Unfortunately, it's the giants turn. Splat. Game Over.")
                        quit()

                if GiantQuizOne == "Human":
                    print("'Gah! Silly human! Tis a giant!' You splat. Game Over.")
                    quit()
                            
                else:
                    print("'Stupid human! No one pass quiz anyway!' Why do you feel terrible....You go splat anyways before you can think further on the mental bug! Game Over!")
                    quit()

                
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
    SearchOne = input("Do you wish to touch the Red Orb, touch the Blue Orb, touch the Yellow Orb, Look around, or Move Forward? ")
    
    if SearchOne == "Look Around":
        print("There appear to be three tiles on the floor, the first being a Red Tile, the second being a Blue Tile, and the third being a Yellow Tile.")
        LookAround = input("Do you wish to touch the Red Orb, the Blue Orb, the Yellow Orb, or to Move Forward despite the different colored tiles? ")
        
        if LookAround == "Touch Red Orb":
            print("You hear a clicking noise, even when looking at the red tile, nothing appears to have changed.")
            TouchRedOrb = input("It appears there's not many other things to do. Do you wish to touch the Blue Orb, the Yellow Orb, or Move Forward? ")
            
            if TouchRedOrb == "Touch Blue Orb":
                print("You hear a clicking noise, even when looking at the blue tile, nothing appears to have changed.")
                TouchBlueOrb = input("It appears there's only two things left to do. Do you wish to touch the Yellow Orb, or Move Forward? ")

                if TouchBlueOrb == "Touch Yellow Orb":
                    print("You hear a clicking noise, even when looking at the yellow tile, nothing appears to have changed.")
                    TouchYellowOrb = input("It appears there's only one thing left to do! That being said, you could just stay here. ")

                    if TouchYellowOrb == "Move Forward":
                        print("Nothing happens. You move to the end of the hallway and open the door. Geez, what an easy room.")
                        GiantQuizTwo = input("Human! *You look up to see the giant cackling down at you, the Giant who had sent you down here!* Me guard exit to cave, me have quiz to give dumb human, no living person answer quiz right. What start day 4 legs, go 3 legs mid day, and 2 legs at the end. *A human?* ")
                        
                        if GiantQuizTwo == "Giant":
                            print("The giant looks stunned, he seems to rise up to both legs, looking at the human with a fuming attitude as its hands shake with rage! The giant appears ready to fight!")
                            GiantFightThree = input("Finally! You get to pay back the giant! Do you choose to run towards the sword in the ground, run away, or attack the giant! ")

                            if GiantFightTwo == "Run Away":
                                print("You pick up speed, and attempt to run between the giants legs towards the door at the end of the room! The giant roars, and makes an effort turning around in the tiny dungeon room. It swings a fist, but with already picked up speed, you easily dodge. You escape!\n You open the door and find freedom, you no longer have to go through that hellish dungeon again.")
                                quit()

                            if GiantFightTwo == "Fight Giant":
                                print("You rear your arm back, you feel all of the moments in your life have led up to this moment. Both beings clash fists, you die. Game Over.")
                                quit()

                            if GiantFightTwo == "Run for Sword":
                                print("You roll with astonishing accuracy and flexibility towards the sword, pulling it out in an almost elegant fashion, you whip forward to lunge at the giant, your arm leaning back. Unfortunately, it's the giants turn. Splat. Game Over.")
                                quit()

                        if GiantQuizTwo == "Human":
                            print("'Gah! Silly human! Tis a giant!' You splat. Game Over.")
                            quit()
                            
                        else:
                            print("'Stupid human! No one pass quiz anyway!' Why do you feel terrible....You go splat anyways before you can think further on the mental bug! Game Over!")
                            quit()

    if SearchOne == "Touch Red Orb":
        print("You hear a clicking noise, but nothing appears to happen!")
        BlindRed = input("You don't know what happened, but you didn't die at least. You can still touch the Blue Orb, Yellow Orb, Move forward, or Look around. ")

        if BlindRed == "Touch Blue Orb":
            print("You hear a clicking noise, but nothing appears to happen!")
            BlindBlue = input("Do you touch the Yellow Orb, Look around, or Move forward? ")

            if BlindBlue == "Touch Yellow Orb":
                print("You hear a clicking noise, but nothing appears to happen!")
                BlindYellow = input("You have touched all the orbs and nothing has happened! You can still Look around, or Move forward, maybe even stay here. ")

                if BlindYellow == "Look Around":
                    print("What do you know! There are three tiles ahead of you. The first tile being red, the second being blue, and the third being yellow.")
                    FoundTilesOne = input("What do you do now? Move forward or stay here? ")

                    if FoundTilesOne == "Move forward":
                        print("Nothing happens. You move to the end of the hallway and open the door. Geez, what an easy room.")
                        DidntWatchOne = input("What, you move through the door, just move forward like you did before. Easy. Right? ")

                        if DidntWatchOne == "Move Forward":
                            print("Someone wasn't paying attention to what was moving. You suddenly feel a stab wound from behind. You don't get a look at the creature behind, but hear devious cackling. Game Over.")
                            quit()

                        else:
                            print("Or not, just stay here forever. Game Over.")
                            quit()
                        
        if BlindRed == "Look Around":
            print("There appear to be three tiles on the floor, the first being a Red Tile, the second being a Blue Tile, and the third being a Yellow Tile.")
            VisiRed = input("You have plenty of options left! Do you choose to touch the Blue Orb, the Yellow Orb, or do you wish to Move Forward? ")

            if VisiRed == "Touch Blue Orb":
                print("You hear a clicking noise, you look at the blue tile but nothing appears to have changed!")
                VisiBlue = input("Only some things are left to be done! Do you wish to touch the Yellow Orb or Move Forward? ")

                if VisiBlue == "Touch Yellow Orb":
                    print("You hear a clicking noise, you look at the yellow tile but nothing appears to have changed!")
                    VisiYellow = input("There is only one thing left to do, to Move Forward, but the traveler can also choose to stay here. ")

                    if VisiYellow == "Move Forward":
                        print("Nothing happens. You move to the end of the hallway and open the door. Geez, what an easy room.")
                        DidntWatchTwo = input("What, you move through the door, just move forward like you did before. Easy. Right? ")

                        if DidntWatchTwo == "Move Forward":
                            print("Someone wasn't paying attention to what was moving. You suddenly feel a stab wound from behind. You don't get a look at the creature behind, but hear devious cackling. Game Over.")
                            quit()

                        else:
                            print("Or not, just stay here forever. Game Over.")
                            quit()

            if BlindBlue == "Look Around":
                print("What do you know! There are three tiles ahead of you. The first tile being red, the second being blue, and the third being yellow.")
                VisiBlueTwo = input("There are more things to do! Do you wish to touch the Yellow Orb, or move forward? ")

                if VisiBlueTwo == "Touch Yellow Orb":
                    print("You hear a clicking sound, you look at the yellow tile and nothing seems to have happened.")
                    VisiYellowTwo = input("There are two things left to do. You could move forward, or stay here. ")

                    if VisiYellowTwo == "Move Forward":
                        print("Nothing happens. You move to the end of the hallway and open the door. Geez, what an easy room.")
                        DidntWatchThree = input("What, you mvoe through the door, just move forward like you did before. Easy. Right? ")

                        if DidntWatchThree == "Move Forward":
                            print("Someone wasn't paying attention to what was moving. You suddenly feel a stab wound from behind. You don't get a look at the creature behind, but hear devious cackling. Game Over.")
                            quit()

                        else:
                            print("Or not, just stay here forever. Game Over.")
                            quit()

            
            if BlindBlue == "Move Forward":
                print("You move forward and hear a 'Shing' from underneath you, spikes have impaled your body! Game Over.")

                if TouchYellowOrb == "Stay":
                        print("Nothing happens. You stay there forever, achieve perfect mentality, and realized what a waste this was. Game Over.")
                        quit()

                if TouchBlueOrb == "Move Forward":
                    print("You move forward and hear a 'Shing' from underneath you, spikes have impaled your body! Game Over.")
                    quit()
                    
            if TouchRedOrb == "Touch Yellow Orb":
                print("You hear a violent whirring in the walls, you hear a 'Crack' as your bones splinter in on themselves. The walls have crushed you. Game Over.")
                quit()

            if TouchRedOrb == "Move Forward":
                print("You move forward and hear a 'Shing' from underneath you, spikes have impaled your body! Game Over.")
                quit()

        if LookAround == "Touch Blue Orb":
            print("You hear a violent whirring in the walls, you hear a 'Crack' as your bones splinter in on themselves. The walls have crushed you. Game Over.")
            quit()
            
        if LookAround == "Touch Yellow Orb":
            print("You hear a violent whirring in the walls, you hear a 'Crack' as your bones splinter in on themselves. The walls have crushed you. Game Over.")
            quit()

        if LookAround == "Move Forward":
            print("You move forward and hear a 'Shing' from underneath you, spikes have impaled your body! Game Over.")
            quit()

        if BlindRed == "Touch Yellow Orb":
            print("You hear a violent whirring in the walls, you hear a 'Crack' as your bones splinter in on themselves. The walls have crushed you. Game Over.")
            quit()
            
        if BlindRed == "Move Forward":
            print("You move forward and hear a 'Shing' from underneath you, spikes have impaled your body! Perhaps you should have looked around first! Game Over.")
            quit()
        

    if SearchOne == "Touch Blue Orb":
        print("You hear a violent whirring in the walls, you hear a 'Crack' as your bones splinter in on themselves. The walls have crushed you. Game Over.")
        quit()
        
    if SearchOne == "Touch Yellow Orb":
        print("You hear a violent whirring in the walls, you hear a 'Crack' as your bones splinter in on themselves. The walls have crushed you. Game Over.")
        quit()

    if SearchOne == "Move Forward":
        print("You move forward and hear a 'Shing' from underneath you, spikes have impaled your body! Perhaps you should have looked around first! Game Over.")
        quit()
    
elif DoorOne == "Right":
    print("You turn towards the right door and move over. Upon the door opening, you head inside and find what looks like a large wolf resting in the middle of a hallway. Do you pet the beast or try to sneak past it?")
    LargeWolf = input("Zzzzzzzzzzzzzzzzzzzz................ ")
    
    if LargeWolf == "Pet":
        print("Playful growling, the wolf continues to sleep, and the adventurer moves past the wolf to the end of the hallway")
        NewDogRoom = input("You see so many little white dogs running around! It appears the wolf outside was guarding a room full of adorable white furred puppies! They're all short with stubby legs, long snouts, brown eyes and have corkscrew tails!\n That being said, what are you going to do? Do you choose to pet dogs, run past them, yell at the dogs, or engage a fight? ")

        if NewDogRoom == "Pet Dogs":
            print("You grace the fluffy dogs with your nimble fingers in their fur. The happy yelping of the dogs wakes the wolf! The wolf bounds in, but carries you across its back, the wolf carries you out of the room, and through several dangerous puzzles! You are left in the final room.")
            GiantQuizThree = input("Human! *You look up to see the giant cackling down at you, the Giant who had sent you down here!* Me guard exit to cave, me have quiz to give dumb human, no living person answer quiz right. What start day 4 legs, go 3 legs mid day, and 2 legs at the end. *A human?* ")

            if GiantQuizThree == "Giant":
                print("The giant looks stunned, he seems to rise up to both legs, looking at the human with a fuming attitude as its hands shake with rage! The giant appears ready to fight!")
                GiantFightThree = input("Finally! You get to pay back the giant! Do you choose to run towards the sword in the ground, run away, or attack the giant! ")

                if GiantFightThree == "Run Away":
                    print("You pick up speed, and attempt to run between the giants legs towards the door at the end of the room! The giant roars, and makes an effort turning around in the tiny dungeon room. It swings a fist, but with already picked up speed, you easily dodge. You escape!\n You open the door and find freedom, you no longer have to go through that hellish dungeon again.")
                    quit()

                if GiantFightThree == "Fight Giant":
                    print("You rear your arm back, you feel all of the moments in your life have led up to this moment. Both beings clash fists, you die. Game Over.")
                    quit()

                if GiantFightThree == "Run for Sword":
                    print("You roll with astonishing accuracy and flexibility towards the sword, pulling it out in an almost elegant fashion, you whip forward to lunge at the giant, your arm leaning back. Unfortunately, it's the giants turn. Splat. Game Over.")
                    quit()

            if GiantQuizThree == "Human":
                print("'Gah! Silly human! Tis a giant!' You splat. Game Over.")
                quit()

            else:
                print("'Stupid human! No one pass quiz anyway!' Why do you feel terrible....You go splat anyways before you can think further on the mental bug! Game Over!")
                quit()

        if NewDogRoom == "Run Past Dogs":
            print("You attempt to run past the small cute little dogs! You trip over one and land face-first in concrete! You lose the capacity to think! Game Over!")
            quit()

        if NewDogRoom == "Yell at Dogs":
            print("You yell at the dogs with a fierce roar. The dogs all yelp and scurry away from you! Cowards! You then hear a growling behind you, the wolf was woken up. A viscious ending appears. Dogs are fed. Game Over.")
            quit()

        if NewDogRoom == "Engage Dog Fight":
            print("You attempt to fight the dogs! They all turn torwards you and growl menacingly! They surge forward and before you can even think, it becomes a little doggy hell. Game Over.")
            quit()

    if LargeWolf == "Sneak":
        print("BARK, a viscious, horrifying ending appears. Game Over")
        quit() 
