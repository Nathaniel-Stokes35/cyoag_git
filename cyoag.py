# Obviously I have a lot of extra stuff beyond the initial Terminal Choose your own Adventure Game. As of 11-16-2024 The GUI based adventure only has the first selection screen for the Space Leader Archtype Campaign (Commander, Squad Leader, Shock Trooper Classes)
# As far as the extra stuff for JUST the terminal Game I have an implemented "Save" system that allows a user to go back at anytime during the story by writing "back" as an option. In fact, the story is very mobile in general, you can go anywhere you want within the trees pretty much at anytime, with the exception of jumping ahead. 
# The text is also wrapped (With OS formatted linebreaks as well as utilizing the textwrap class) and if you use the executable run_cyoag.exe file matching your specific OS you'll find it opens a curated Console window for the adventure. 
# As of 11-20 the first section of the Space setting is nearly finished. The "Tech" archetype needs some finishing touches but everything is coming together quite nicely. I also tweaked the "Leader" section to better connect with the other paths. The stories now fit rather well together and the system is looking quite established.

###---------------- PLEASE READ THE README.txt FILE! it will explain how to run the code properly! Running in VS Code is fine and Dandy but the executable is the preferred way (Font's and images look much sharper and cleaner). -------------------------------------------###

import sys
sys.setrecursionlimit(5000)
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
import re
import sys
import textwrap
import os

text_w = 100
current_directory = Path(__file__).parent

def terminal_game():
    history = [] # Used to store players choices

    while True:
        print(textwrap.fill('\nWelcome to the tutorial and starting guide preparing you for how this is played. Have you played a Choose Your Own Adventure game before? (YES / NO)', width=text_w, replace_whitespace=False)) # Allowing a quick solution to get directly to the GUI program
        answer = str(input('Type one of the all caps options for each choice or "BACK" to revert to a previous choice: \n')) ## Explaining the basic rules of this particular program

        if answer.lower() == 'no': # A quick guide on how choices affect actions and a basic layout for a story.
            history.append('no')
            print(textwrap.fill('That\'s fine, this is going to be a short three option adventure that has multiple endings which encapsulates how your choices affect the world and your decsions moving forward. Each option after the first will be restricted to two choices for the rest of the adventure. This is a three layer tree so the final layer will ask you if you would like to continue '
            'and you can always type "back" as an option to travel to the previous decsion tree. Do not worry about whether it\'s uppercase or lowercase ("HoMe" will work as well as "HOME" and "home") I just have the choices in all CAPS for this side adventure for easy readability to understand the choices.\nNow that we have that taken care of, feel free to go through the encounters as many times as you would like. after the game you will have the '
            'choice to play a deeper more complex version which includes a fully functional GUI. Most of all though, regardless of your choices; Have fun. :)'.replace('\n', os.linesep),width=text_w, replace_whitespace=False))
            while True:
                current_choice = input(textwrap.fill('\n\nAs you walk along the beaten road, heading back to your cottage with your rifle and some fresh produce you got at the market, '
                'you come across a pecuilar sight. It seems a wolf has made a fresh kill of a goose but must have heard your approach and made a dash into the wood. Your home is only '
                'a few miles from here, and you know the lazy city watch won\'t hunt a wolf unless they have too, but maybe you could convince one or two to investigate. \n\nWhere would you like to go? (WOODS, CITY, HOME): '.replace('\n', os.linesep).replace('\n', os.linesep), width=text_w, replace_whitespace=False) + '\n'.replace('\n', os.linesep)) # I'm putting breaks after every input to help divide the code, making it easier to read.

                if current_choice.lower() == 'home':
                    history.append('home')
                    print(textwrap.fill('\nYeah it\'s probably best you take the produce home, wouldn\'t want the trip to the market be a waste after all.\n'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                    while True:
                        current_choice = input(textwrap.fill('As you start walking home past the goose lying dead on the side of the withered roadway you begin to hear growling from behind you. '
                        '"Looks like he didn\'t get very far after all." You think to yourself as you start sprinting down the trail.\nAfter making it home safely you place your produce and rifle on the table '
                        'but your mind starts wondering why a wolf would be hunting so close to the road. A goose is a fine catch, sure, but the road has many patorls and would-be-adventures just itching for a fight '
                        'why would a wolf risk it? Come to think of it, why didn\'t he run away after confirming I was there? Do you want to (RELAX) at home or investigate the (WOODS):'.replace('\n', os.linesep), width=text_w, replace_whitespace=False) + '\n'.replace('\n', os.linesep))

                        if current_choice.lower() == 'relax':
                            history.append('relax')
                            print(textwrap.fill('Ah, it\'s probably nothing, if a animal was hungry enough he\'d probably risk anything at the thought of getting food.\n'.replace('\n', os.linesep),width=text_w, replace_whitespace=False))
                            while True:
                                current_choice = input(textwrap.fill('Laying down on your wool bed, getting ready to get some well deserved shut-eye, you hear a rustling outside. Do you want to grab the rifle and head outside to (FIGHT) or (STAY) inside and wait:'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+ '\n'.replace('\n', os.linesep))

                                if current_choice.lower() == 'fight':
                                    print(textwrap.fill('You relent, "Whatever it is, they don\'t seem to be leaving anytime soon. I bet it\'s just some kids out later than their supposed to be.\nHeading out the door you\'re confronted by a large direwolf. '
                                    'Raising your rifle to bring it down the wolf from earlier pounces on you from your right. As you hit the ground you wonder if this was always how it was supposed to go. The night feels cool as you close your eyes.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                                    current_choice = input('Would you like to try again? ').lower().replace('\n', os.linesep) # Death save basically, asking if they would like to try a different route from where they were, otherwise the program terminates.
                                    if current_choice == 'yes':
                                        history.pop()
                                        break
                                    else:
                                        sys.exit()
                                        
                                elif current_choice.lower() == 'stay':
                                    print(textwrap.fill('You know it\'s probably just someone playing tricks on you but with the wolf on the road it\'s probably just better you wait it out. After a while the rustling around the house, that sounded like a horse circling around the building, seems to quiet. '
                                    'What was once a frantic heavy sound now just seems to be a distant echo, the fire in the fireplace crackling louder than anything outside you stand up ready to go to sleep. As you stand however you hear the wood floor creak and, bursting through the closed '
                                    'window, stands a large direwolf. The crash made you drop your gun and as you scrammble to try and pick it up the pack of the wolf you ran away from earlier joins their direwolf comrade. Bringing the gun up to fire you let off a few rounds as you\'re attacked '
                                    'from each side. Your last sight, staring into the maw of a fercious 5 foot tall behemoth. You close your eyes finally ready to sleep.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep))
                                    current_choice = input('Would you like to try again? ').lower().replace('\n', os.linesep)
                                    if current_choice == 'yes':
                                        history.pop()
                                        break
                                    else:
                                        sys.exit()

                                elif current_choice.lower() == 'back' and history: # Allowing the user to go back and make a different choice
                                    history.pop()
                                    break

                                else:
                                    print(textwrap.fill('Please input one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                        elif current_choice.lower() == 'woods':
                            history.append('woods')
                            print(textwrap.fill('"Someone needs to get to the bottom of it." Grabbing your rifle you head outside. Looking up, it seems like it\'s just a little past 5 and the sun will be setting in a couple of hours. "I need to act fast" you think headed to the place you found the dead goose.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                            while True:
                                current_choice = input(textwrap.fill('Arriving at the corpse you notice the goose had suffered grevious wounds that look far too deep for the size of the wolf you saw earlier. "If the wolf didn\'t do this than was the wolf following something larger?" Looking into the woods, '
                                'then back at the city gate you wonder if you should handle this alone or get a guard. If you show them the wound they\'ll probably come to the same conclusion that you did, and that might convince them to help. (GUARD / ALONE):\n'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep))

                                if current_choice.lower() == 'guard':
                                    history.append('guard')
                                    print(textwrap.fill('Looking at the damage on the goose you surmise it had to have been an large creature that did this. The guards should be involved. Walking towards the gate you meet a patrol. After explaining the situation they shrug and decide to see what you are going on about.'
                                    'After seeing the wounds they conclude it was just a wolf and demand you go with them as they hunt it down; "Safety in numbers" they tell you as they follow the trail of blood. Looking up towards the sky you see the sun setting, in the woods, at twlight, you won\'t be able '
                                    'to see anything.\n\nComing across a break in the trees, standing the middle of the grove with the sun missing completely from the night sky you and the guards hear a deep menacing growl circling around you. The guards ready their swords but before you know it they\'re ambushed '
                                    'and on the ground; a massive 5 foot tall direwolf standing above them. Bringing your rifle up to aim you fire two shots which look like they dig deep into the beasts theigh, unphased by the wounds the direwolf jumps upon you, as your head slams against the ground you feel a warm '
                                    'ooze run down the back of your head and before long you really can\'t feel anything anymore. You wonder, "Was this always how it was going to end?"'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                                    current_choice = input('Would you like to try again? '+'\n')
                                    if current_choice == 'yes':
                                        history.pop()
                                        break
                                    elif current_choice.lower() == 'back' and history:
                                        history.pop()
                                        break
                                    else:
                                        sys.exit()

                                elif current_choice.lower() == 'alone':
                                    history.append('alone')
                                    print(textwrap.fill('It\'s getting late and I doubt the guards are going to help, they\'ll probably see the wounds and think it didn\'t matter. Rifle in hand you decide to follow the trail of blood into the woods. Traveling about half a mile into the thicket you notice the sun starting to set. '
                                    '"I may have better luck tomorrow" you think but then, out of the corener of your eye you catch a glimpse of a tuff of fur menuvering through the trees. Staying still you drop to the ground peering through the thicket with a keener observation. Then you see it. A bahemoth of a creature '
                                    'looking at you through the trees. "Here I thought I was doing the stalking" you calmly think as you slowly lift your rifle to aim at the dire wolves head. In a moment everything springs forth, with the help of aiming you were able to put a bullet through one of the direwolves eyes but '
                                    'because of the limited visability you weren\'t able to defend against the pack of the wolf you ran into earlier pouncing upon you from the bushes surrounding the glade. Lying in the grass, unable to feel your gun in your hands the now one-eyed dire wolf stands over you. In an instant it\'s over. You last thought '
                                    'wondering "Did it always have to end this way?"'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep))
                                    current_choice = input('Would you like to try again? ').lower()
                                    if current_choice == 'yes':
                                        history.pop()
                                        break
                                    elif current_choice.lower() == 'back' and history:
                                        history.pop()
                                        break
                                    else:
                                        sys.exit()

                                elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break
                                else:
                                    print(textwrap.fill('Please input one of the choices that are in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                        elif current_choice.lower() == 'back' and history:
                                history.pop()
                                break

                        else:
                            print(textwrap.fill('Please input one of the choices that are in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                elif current_choice.lower() == 'city':
                    history.append('city')
                    print(textwrap.fill('\nThe city guards may be lazy but someones goose has obviously been hurt and the path to the city needs to safe.\n'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                    while True:
                        current_choice = input(textwrap.fill('\nWalking to the city gate you stop in front of the patrol stationed there. Saying to the guard standing in front of the right toll house "I thought I saw a wolf on the road after it killed a goose." The guard stared at me looking irritated I was still in front of him. '
                        '"Did you hear me? I think a wolf is on the road." "Yeah? Then why are you here talking with us? Why didn\'t you go after em? You have that rifle, is it just for show?" It\'s useless these guards clearly don\'t care about anything outside the city walls. You might be able to tell their commander '
                        'and get him involved, he could get these two to do thier jobs as well. You could also try the local game shop, maybe the hunters have ran into some information? Where do you want to go? (COMMANDER / HUNTERS)'.replace('\n', os.linesep), width=text_w, replace_whitespace=False) + '\n'.replace('\n', os.linesep))

                        if current_choice.lower() == 'commander':
                            history.append('commander')
                            print(textwrap.fill('\nThis is the city watch\'s job and getting the commander involved may help these guards remember their duty.\n\n'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                            while True:
                                current_choice = input(textwrap.fill('"Where can I find your commander, he may be more interested in this than you seem to be?" "Yeah, best of luck with that, he\'s up that stairway at the top of the watchtower." Heading past the guards standing post you hear them snickering behind you. "We\'ll see whose '
                                'laughing by the end of this." \nClimbing the staircase you come accross a large ornate room at the top. The door looks rough, like it has been slammed one-to-many times, and inside the room is a large rectangular desk with a stout man sitting behind it, looking especially frustrated at the pile '
                                'of papers on his desk. "Yes, what is it? Can you not see the work I have to do just to keep this city safe? Talk of direwolf attacks out on some of the farm land, can you believe that? A direwolf. I swear these people get so bored they\'ll make up anything to give them some entertainment. Are you '
                                'also here to tell me about a 7 foot tall wolf that can paralyze a man just by looking at them, can travel anywhere instantly, and is some secret wolf gang leader?" Setting the Sarcasm aside you explain the wounds on the goose and confidently exclaim "They definitly weren\'t made by any wolf I\'ve ever seen.\n\nThe commander '
                                'rolls his eyes then explains "Look, anything big would have been seen and accounted for by a patrol. Not just some workhands passing along tall tales. The goose probably was dragged a fair bit and got snagged on a rock, which probably accounts for the damage you saw. It\'s starting to get late so if you\'re '
                                'planning on heading home you should probably head out now, unless you want to get mugged on the pass." You tell the commander "I\'m sorry you have such little faith in the people you are asked to protect." Then you head out the door and down the stairs, The sun is setting. \nWhat do you want to do? '
                                'stay at the (INN) or start heading (HOME)?\n'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep))

                                if current_choice.lower() == 'inn':
                                    history.append('inn')
                                    while True:
                                        print(textwrap.fill('You look around for the nearest inn, produce still in hand. You see some lights on down the road as the fading sunlight sets past the city walls. You hurry to the inn which seems to be hosting people a little too excited the sun is going down. Each of the inn patrons seem to be marry and very drunk, '
                                        'holding a flask of ale in one hand, and who knows what with the other. You go up to the innkeeper and ask how much a room would be for the night. He looks you over, glances out the window looking at the setting sun, then replies "20 copper peices". It\'s an outrageous price but you figure it would '
                                        'cost you more to get mugged on the road. You hand over the peices, grab your things and head to your room. Laying on the bed your exhausted and fall asleep with barely any warning. \n\nThe next morning you get up and decide to see the hunters, but as you head out to leave you notice your produce and gun are missing. '
                                        'Stepping up to the innkeeper you ask if anyone else entered your room while you were asleep. The innkeeper shrugs. Annoyed, you head out of the inn looking for someone to help you track down your missing stuff. The city is empty and the guards you met with yesterday seem to be gone from their post at the gate. "Well, '
                                        'isn\'t this great." you say sarcastically. Fed up with the city you decide to head home.\nAs you are walking down the road past where the goose had been yesterdsay, striped clean by wildlife, you were thinking about where you stuff may have ran off to then suddenly a pair of bandits appear, having nothing to give them they '
                                        'attack you assuming you were lying. As you lay on the ground, stab wound in your side, you wonder. "Was this always how it ended?"'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep))
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()

                                elif current_choice.lower() == 'home':
                                    history.append('home')
                                    while True:
                                        print(textwrap.fill('Annoyed with the city and just not wanting to deal with anymore surprises you decide to start heading home. Walking past the city guards at the gate they sarcastically reply "Oh no, he\'s come back without our commander, it must mean we\'re in for a real sore beating when we get off duty and start partying at the inn." Then they both '
                                        'chuckle to themselves. On your way back to your cottage you notice the goose looks like it was striped clean in the few hours you\'ve been going to and from the market. \n\nComing up to the cottage you heart is lifted and you\'re just ready to get home and lay on that nice comfy wool bed to finally get some sleep. The shrub next to the left wall starts to shuffle '
                                        'and your heart drops again. "Please tell me that\'s just a rabbit." The wolf jumps out from the bush and you ready your rifle. "I should have taken care of you this afternoon on the road." You load a chamber in the barrel and fire, the wolf goes down and you think about all the trouble this has been. As you step up towards the '
                                        'door a massive beast lunges out against you. Knocking you to the ground, standing over you a massive 5 foot tall direwolf with razor sharp claws and a penetrating stare that chills you to the bone. The rifle thrown from your hand, you quickly try to find it without breaking eye contact but before you can make '
                                        'even the first movement towards the gun a razon sharp claw cuts through you. As the light leaves your vision on this cool autumn evening, you wonder if it could have been avoided: "I wonder if it always had to end this way?"', width=text_w, replace_whitespace=False)+ '\n').replace('\n', os.linesep)
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()

                                elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break

                                else:
                                    print(textwrap.fill('Please input one of the choices in all caps.', width=text_w, replace_whitespace=False)+ '\n')

                        elif current_choice.lower() == 'hunters':
                            history.append('hunters')
                            print(textwrap.fill('I\'d imagine the corruption goes all the way to the top, considering how consistently reliable their effort is to help the farmers.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                            current_choice = input(textwrap.fill('As you walk past them shaking your head the guard you were just talking with makes a sound that resembles a sneer, you don\'t look back to check. Heading into the main square '
                                    'you see a row of cobblestone buildings with a sign of the different tradesmen. You spot the one with a bow behind a quiver of arrows. As you step in the man at the front desk recognizes you and asks you to step in. "We were just sharing stories about some nasty rumors going about with the dark woods. You haven\'t heard anything '
                                    'about a direwolf round \'ere have you?" A direwolf, the wounds were big but you\'ve heard direwolves were 7 or 8 feet tall. "I actually saw a mangled goose this afternoon on the road heading out of the market with odd wounds. They weren\'t no direwolf though. Much too small, and the kill was fresh, I think I would have '
                                    'spotted an 8 foot monster strolling away. The wounds were strange though, too big for a regular wolf in a lot ways, the carcass didn\'t look to beaten up either so I don\'t reckon it was dragged around too far." "You said heading out of the market?" Before I could nod Hamish the huntsman stood up and shouted "Let\'s go '
                                    'take a look at this beast then!" Just like that the whole building was packing their supplies and ready for hunt.\n\nIt took a few minutes for everybody wanting to go to get ready and fully armed so it was a little before nightfall when I showed Hamish and his hunting friends the carcass, by then wildlife had '
                                    'already striped it clean and there wasn\'t much of a trail left. "I\'m sorry it isn\'t as clean as it was but you have to believe me, this wasn\'t a normal wolf attack." Most of the hunter\'s shrugged, scattered around deciding to look for something else to kill in the night. Hamish on the other hand looked over the goose and '
                                    'gave a look towards the dark woods. "I belive you, but you may be wrong. I don\'t think a direwolf made the mess we see now but it may have been the one that brought her down." "Hamish I already told you though, I didn\'t see anything that big." "Some of the stories I\'ve heard have been about a pup trying to find a pack '
                                    'and I\'m thinking that\'s what happened here." You never thought of a pup but It makes sense, maybe it made the kill and was out of sight by the time you had gotten there, a pup would still be large but could have hidden easier in the woods for sure. "Why would a direwolf pack travel so far south?" "I don\'t know but there is '
                                    'a good way to find out. Are you coming in there with me, could use an extra pair of eyes, especially chasing down a direwolf?" (IN / OUT)\n', width=text_w, replace_whitespace=False)+ '\n').replace('\n', os.linesep)
                            while True:
                                if current_choice == 'in':
                                    history.append('in')
                                    print(textwrap.fill('"Fine, you say reluctantly, I guess someone has to bring this monster down, if you\'re right about this, but this better not be a wild goose chase though." You look at Hamish with a grin on your face from the pun. Hamish doesn\'t seem amused. "So how do we start?" You ask patiently, Hamish looks back at you curiously and points '
                                    'to the woods "We stay low and hidden. After nightfall hits we need to always have a good idea of where each other are. Neither of us go out alone under any circumstances, if you need to pee best get it done now." "Don\'t worry about me." You both head into the woods, crouching, trying to make as little noise as possible. Hamish is '
                                    'taking point but you\'re right there behind him, keeping a hand on his back as you both look for any sign or evidence of a 6 or 7 foot wolf roaming around. after about an hour you come across a glade but before you enter Hamish stops you dead in your tracks. Looking toward Hamish you notice he holds a finger to his mouth signaling to '
                                    'be quiet and he points towards the left-hand side of the glade. You don\'t notice anything at first but then the large oak trees begin to shake like they were being blown in the wind. Upon closer inspection you see it, a huge wolf with a thick black coat the color of midnight. Hamish lifts his rifle to take a shot but the moment he '
                                    'does you see a wolf with dried goose blood on its lips behind him getting ready to attack Hamish. BAM! A load shock explodes out of the barrel of Hamish\'s rifle, without a seconds hesitation the rifle I had cocked is lifted towards the wolf I spotted and a second explosion rings through the trees as that wolf falls to the ground '
                                    'lifeless. I turn to face the direction of Hamish when the smoldering beast sprints toward us through the clearing. Pulling the slide back and rounding another bullet, I point it towards the direwolf. I watch as the wolf slashes Hamish with razor sharp claws and a surgeons percsion, I don\'t have time to think. With the beast right on '
                                    'top of me, my rifle finds it\'s way into it\'s mouth and with a third BANG! the wolf collapses on top of me. \n\nI must have stayed lying there, an arms length away from my disembowled friend, for what felt like days, if I was being crushed by the wolf I never knew it. I don\'t exactly know how long I stayed in the woods but when I '
                                    'left, the world seemed quiet, the night had an errie peace about it that I\'ll never forget. My heart aches at the loss of a friend but I\'m still alive. That has to account for something, right? As I lay on my wool bed, unable to sleep while feeling the most tired I\'ve ever been, I wonder... "Did it always have to end this way?"'.replace('\n', os.linesep), width=text_w, replace_whitespace=False) + '\n'.replace('\n', os.linesep))
                                    current_choice = input('Would you like to try again? ').lower()
                                    if current_choice == 'yes':
                                        history.pop()
                                        break
                                    elif current_choice.lower() == 'back' and history:
                                        history.pop()
                                        break
                                    else:
                                        sys.exit()

                                elif current_choice == 'out':
                                    history.append('out')
                                    current_choice = input(textwrap.fill('"If you think there is a direwolf out there, you\'d be crazy to actually try and pick a fight with it. "You\'re saying there is a pup, that mean\'s the pack isn\'t far behind. Worse yet Hammish, what if you kill the thing? Mom and Dad won\'t be able to let that slide. You should let the city watch handle this '
                                    'I\'m going home." "Wait!" Hammish says franctically, "You said you scared off the wolf that was eating on this this morning?" "Yeah I-" You start to explain what happened when Hammish inturepts you saying "You Can\'t Go Home!" "Wait, What? Why not?" "If this thing was trying to get a pack together and it sees you as a threat to that '
                                    'dominance, because you threatened a member of it\'s adopted family, it will want to take you out." You roll your eyes at the notion. "Hammish, dire wolves would never come this far south and even if they did they wouldn\'t care about some schmuck walking down the road and even more impossible is the fact they have no idea where I '
                                    'live. I\'m going to head home, I\'m going to lay on my bed, and I\'m going to get a good nights rest." Hammish grabs your shoulder as you head toward the road. "Please, let\'s kill this thing together... can I count you in? (IN / HOME)', width=text_w, replace_whitespace=False) + '\n').lower().replace('\n', os.linesep)
                                    
                                    if current_choice == 'in':
                                        continue

                                    elif current_choice == 'home':
                                        history.append('home')
                                        print(textwrap.fill('"Hammish, I\'m sorry but I\'m simply too tired to be going on soem wild adventure into the dark woods over someone elses dead goose. I\'ve had a long day. Please, I need to sleep." Hammish\'s dissappointed face was pretty telling of how he felt about the whole thing. "Hammish, You don\'t need to be hunting this thing on '
                                        'your own either. Just leave it for the City Watch and let them do their jobs." Hammish chuckled at the thought but he started walking back into town. YOu look up at the night sky, A bright waxxing gibous, the moonlight guiding the path. Being cautious you round a chamber in the rifle as you dtart walking home.\nWhen your cottage '
                                        'comes into view you feel like your heart lifted. "Finally this day is almost over." As you start approaching the door you hear a soft rustling from behind you, scared you whip around only to be met with the gaze of a 5 foot tall large black wolf growling at you. You back into the door raising your rifle but before you could pull '
                                        'the trigger the beast rips into your belly. Collapsing in front of your home you chuckle... "I guess Hammish was right? Suppose they never lost track of me? maybe it was my scent all over the house." As you bleed out losing conciousness your last thought is: "I wonder if it always had to have ended this way?"'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+ '\n')
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()
                                    
                                    else:
                                        print(textwrap.fill('Please input one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                                elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break

                                else:
                                    print(textwrap.fill('Please input one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                                
                        elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break
                        
                        else:
                            print(textwrap.fill('Please input one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                elif current_choice.lower() == 'woods':
                    print(textwrap.fill('You think to yourself, "someone needs to protect the people, if the guards won\'t do it." You ready your rifle, place your produce on the side of the road and head into the woods following the trail of blood.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                    history.append('woods')
                    while True:
                        current_choice = input(textwrap.fill('As you croach moving from thicket to thicket looking for any signs of disruption the trail of blood becomes more and more scarce but you think you recgonize a pattern to the movements. It feels like the blood is spread out around the road and not necessarily the farms, which is what you '
                        'orginally assumed. Following the footprints you notice there are two trails that make up the majority of the paws. The larger, adult, wolf sized prints and the smaller more immature prints. Noticing the larger prints seem to follow the path of the road more while the smaller prints seem to head deeper into the woods. '
                        'There is an ominous presence from the wood but, looking up to the sky past the trees, it looks about mid-afternoon. "There is a dark pressence here, I can\'t quite put my finger on it though.\n\nWhich path would you like to follow? The (LARGE) marks along the road, or the (SMALL) marks deeper into the forest.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep)).lower()
                        if current_choice == 'large':
                            history.append('large')
                            print(textwrap.fill('The larger prints are what you were after from the beginning. If they\'re following the roads they\'re hunting livestock and people.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                            while True:
                                current_choice = input(textwrap.fill('You think to yourself "They\'re headed towards my house, I wonder if that\'s a coincidence or if they\'ve been meaning to hunt me down for scaring them off?" and as you approach your cottage, staying low and in the thicket, you notice an adult wolf circling your empty home, '
                                'appearing to be both scavenging and finding suitable ambush locations, evidenced by the constant look towards the road. "Why do I have the drop on this wolf? It was looking for me why didn\'t it wait at the goose attack? Was there something it needed first?" These thoughts race into your mind as you see the wolf. '
                                'Tired of the game you decide to make your next move. Feeling your gun you decide to pull the slide back loading a live round into the chamber. Are you going to (SHOOT) at the wolf or decide to wait and (INVESTIGATE) longer?'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n').lower()
                                if current_choice == 'shoot':
                                    history.append('shoot')
                                    print(textwrap.fill('"I don\'t know why I\'ve decided to take so long to make my decsion already; it is almost nightfall and I have a wolf right here in front of me."'))
                                    while True:
                                        print(textwrap.fill('You ready your rifle by resting the stock against your shoulder. You align the sights and aim at the jaw of the beast, hoping to either hit his head or his neck, putting him out of his misery quick. Holding your breath the world melts around you, a strong tunnel vision and focus on the wolf '
                                        'begins to grow in your mind until... BAM! a loud bullet explodes from your rifle, the wolf hits the ground motionless, and you get up from the thicket. "That was a lot easier than I expected, I must have been getting worked up over nothing." As you enter the grove of your front yard you rememeber the supplies '
                                        'you left on the side of the road. Not wanting a wasted trip you turn around and start heading down the path back to the market, it\'s getting dark so you want to be quick when, out of the corner of your eye, you catch the glimpse of something huge in the trees. Spooked, you retreat some back to the steps '
                                        'of your cottage. Readying your rifle again you shout "If anyone is out there I\'m warning you. Best come out right now or I might-" Interrupted, by a massive black direwolf exploding from the trees, in full sprint he runs at you, letting off a shot you see it embed into it\'s cheek but without so much as a flinch the 5 '
                                        'foot tall direwolf lunges toward you and with one quick jerk with its head you feel the teeth and jaw crush your ribcage. Instantly letting go of the rifle, unable to feel your legs, in unspeakable pain, you start to lose consciousness. You can feel the bullet rubbing somewhere in your flesh and you can\'t help '
                                        'thinking: "Was this always how it had to end?'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+ '\n'.replace('\n', os.linesep))
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()
                                elif current_choice == 'investigate':
                                    history.append('investigate')
                                    print(textwrap.fill('"It would be irresponsible to shoot without understanding the full situation... right? I mean, what if it isn\'t just a wolf on your property?"'))
                                    while True:
                                        print(textwrap.fill('You think to yourself, but for whatever reason you keep being brought back to the feeling you had outside of the deep woods. "They say the dark woods are haunted by evil spirits, that demons and foul creatures can be heard at night. Could someone be playing a game with these wolves?" '
                                        'You don\'t know the answers but you feel like there is more to this goose than just a simple hungry wolf pack. "Why is he hunting me? Why didn\'t he wait for me at the corpse? What\'s going on here?" As if to answer your question you begin to feel that darkness approach. Hand on the rifle you muster the '
                                        'courage to turn around and see what you may find. Following the feeling of dread you turn and you see the source. Deep into the wood, fixated on the wolf scavenging a dark looming shadow of what appears to be a very large bear, or wolf rests ready to pounce. Holding your breath you raise your rifle. Stock '
                                        'held against your shoulder you let off a shot hoping to bring the beast down, the moment the bullet escapes and you\'ve recovered from the recoil, you load another round and fire. Recovering and loading another round after the second shot you turn to face the wolf on this side. BAM! For the third time another '
                                        'explosion rings through the trees and the wolf outside your home goes down. Feeling relieved you load your second to last round into the rifle and turn back around trying to remember if you saw the shadow fall. As you stand up to see what the beast was you realize it\'s shadow is missing. There is no lump or '
                                        'mound of the beast. "Surely a bear couldn\'t have survived two shots from my rifle." In an instant, before you could even process exactly what happened your vision went blurred and you felt yourself sliding down something until finally hitting the floor of the leaf covered forest floor. Lying on the ground, maybe as if '
                                        'to taunt you, a large 5 foot tall direwolf steps out from behind you and into view. It didn\'t hurt, it was so quick and clean that at the end you realized how beautiful the night had been, only to wonder: "Was that always how it was supposed to end?"'.replace('\n', os.linesep)) + '\n'.replace('\n', os.linesep))
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()
                                elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break

                                else:
                                    print(textwrap.fill('You can only write one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                        elif current_choice == 'small':
                            history.append('small')
                            print(textwrap.fill('"I need to get to the bottom of this, maybe their den could hold the secret to why the pack has gotten so brave."'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                            while True:
                                current_choice = input(textwrap.fill('Being careful not to damage the footprints as you follow their trail, you creep deeper into the woods. The darker area and that feeling of dread you\'ve felt since you entered has only grown stronger. You truly feel as though you do not belong here and that you\'re constantly being '
                                'watched from some distant hunter. Focusing on your mission, keeping your rifle close and ready, you tread through the thick brush, your sight becomes very limited, the space you\'re in feels huge and yet it feels like you\'re locked in a closet, the trees feel more oppresive than inviting now and the sun is nowhere to '
                                'be seen. The forest is dark, darker than anything you\'ve ever experienced before. There are sounds all around you, you feel alert but know you need to keep following the footprints to find an answer. You look behind you, thinking how you could leave and try again with more light, or with more people, or with anything '
                                'besides your gun and your own mortality. You question if you should turn away, you wonder if you should have just left this up to the guards or maybe should have just gone home ignoring the goose, "Why am I out here? What am I doing this for?" Should you (LEAVE) or (KEEP GOING)?'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n').lower()
                                if current_choice == 'leave':
                                    history.append('leave')
                                    print(textwrap.fill('"Yeah, why should I risk my life to help a bunch of lazy, entitled, nobodies who wouldn\'t have helped me even if I was dying right in front of em. I bet, if I was outside their walls, they wouldn\'t even notice; or at least would pretend not to have. Yeah, I don\'t need this."'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                                    while True:
                                        print(textwrap.fill('As you pickup your rifle to leave, looking around you, you feel a sense of calm with deciding to head home. "I\'ll grab my vegetables from the road, head home, and have myself a cabbage stew, with scallons, some basel, maybe a pinch of ginger root to give it a kick-" as you start rattling '
                                        'off more ingrediants you suddenly hear some rustling in a shrub behind you. Turning around you think you can see glade off in the distance and a large shadow moving toward you. Having made up your mind on how much time you would like to spend among these trees you start sprinting out of the woods with you rifle '
                                        'in hand. Ignoring the scratches from the trees and shrubs, you see the road through a clearing of the trees, but as you draw closer you stumble on a loose disturbed rock close to the road. Hitting your arm on some jagged terrain you find your rifle and try to lift it up to meet the threat chasing you. '
                                        'To your surprise you can\'t see a danger. The night sounds quiet apart from the ocasional sacadia. Straining yourself to keep rifle perched on your bum shoulder you relax. Laying down, feeling the endorphanes of adrenaline and safety you look towards the sky, seeing the moon hanging over the landscape. "Wow, I '
                                        'probably would have never realized how beautiful this evening would have been if I had just gone home making stew. That stew does sound good th-" before finishing the thought a large, 5 foot tall, solid black, direwolf hovers over you and places a heavy paw against your chest. In an instant the beast has your '
                                        'throat and in the next darkness. Maybe you had a chance to wonder, "Did it always have to end this way?"'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n'.replace('\n', os.linesep))
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()
                                elif current_choice == 'keep going':
                                    history.append('keep_going')
                                    print(textwrap.fill('"I\'m doing this the people I love in the village. I\'m doing this so we can have a place where we can be lazy, where we can laugh, where we can live healthy, happy lives. There is no turning back, I\'m doing this for me, and everyone behind me."'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                                    while True:
                                        print(textwrap.fill('Reinvigerated you buckle down, grit your teeth and keep moving forward. Through the dark wood the trail leads you to clearing with two seperate dens, among one has some playful wolf pups and in the much larger den, utilizing an open cliff face as shelter, rests the shadow of a large black '
                                        'direwolf. It\'s starting to make sense. "It looks like the direwolf has come south either running from some unknown danger north or-" The beast detects a gaze, opens its eyes and stands in front of the pups den alerting them to stop rough-housing. As it stands, providing a better view, you realize it isn\'t '
                                        'fully mature. "This must be a youth trying to secure their own alpha sinority. Must not have liked dear old ma and pa telling him what to do." Resting the rifle against your shoulder, aiming at the whites in his eyes, holding your breath you whisper "You can\'t live here." then BANG! the shot echoes through '
                                        'the trees, racking back and loading another round in the chamber, keeping your eyes fixed on the wounded wolf which sprints toward you ferociously, you set your sights again, aiming for the torso and with a second BANG the bullet finds its way to the beast heart. The wolf tumbles forward and slams into an old '
                                        'oak tree. The normal wolf pups scurry away, howling and yelping as you wonder over to the direwolfs corpse. Leaning down to meet its gaze, noticing the light hasn\'t fully left his eyes you give a soft frown. "You belong with your own kind, away from us. We\'re scared, you understand." Petting it\'s beautiful '
                                        'mane. You rest beside him for 10 or 20 minutes looking up at the night sky and moon through the trees. Afterwards, you see a haze washed over his eyes and know he has passed so you stand up, and make your way through the forst back to the goose and your produce. You start walking home only to be met by what must '
                                        'have been the original wolf you heard on the road howl to the moon, then run off into the woods. Inside your cottage you make yourself a nice bowl of cabbage stew and lay on your wool bed. Before falling aslepp you wonder: "Did it always have to end like this?" '.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                                        current_choice = input('Would you like to try again? ').lower()
                                        if current_choice == 'yes':
                                            history.pop()
                                            break
                                        elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                        else:
                                            sys.exit()
                                elif current_choice.lower() == 'back' and history:
                                            history.pop()
                                            break
                                else:
                                    print(textwrap.fill('You can only write one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))

                        elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break      
                        else:
                            print(textwrap.fill('You can only write one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)) 


                elif current_choice.lower() == 'back' and history:
                                    history.pop()
                                    break

                else:
                    print(textwrap.fill('You can only write one of the choices in all caps.'.replace('\n', os.linesep), width=text_w, replace_whitespace=False))
                    
        elif answer.lower() == 'back' and history:
                                    history.pop()
                                    break

        else:
            print('\n\n***--- STILL IN DEVELOPMENT ---***')
            gui_choice = input(textwrap.fill('Then would you like to try my GUI Choose your own Adventure Game instead? (YES / NO)'.replace('\n', os.linesep), width=text_w, replace_whitespace=False)+'\n').lower()
            if gui_choice == 'yes':
                launch_gui()
            else:
                sys.exit()

def get_personality_name(MBTI): # Assigning names given by the 16 personalities website for the various personality types
    if MBTI == 'INTJ': 
        return ['The Architect', ('Approach: Logical, strategic, prefers long-term solutions.\nGameplay Impact: Might approach negotiations with a meticulous, calculated strategy, opting for planned, methodical discussions.' + os.linesep +
                'These players would excel in situations requiring a clear, logical argument but might struggle in emotionally charged situations.' + os.linesep +
                'Possible Scenarios: "Negotiate the terms using hard data," "Create a strategic alliance for future gain," "Advocate for a systemized solution."')]
    if MBTI == 'INTP':  
        return ['The Thinker', ('Approach: Inventive, curious, loves abstract ideas and theories.' + os.linesep +
                'Gameplay Impact: Likely to take a more unconventional approach in dialogue, proposing creative but perhaps impractical solutions. They may question authority and challenge the status quo, which could result in conflict or new opportunities.' + os.linesep +
                'Possible Choices: "Explore a theoretical solution to the issue," "Challenge assumptions and propose something radical," "Consider an alternative perspective."')]
    if MBTI == 'ENTJ': 
        return ['The Commander', ('Approach: Assertive, determined, focused on results.' + os.linesep +
                'Gameplay Impact: Characters with this personality would have strong, forceful dialogue options, demanding respect and pushing for quick, decisive action. They may try to impose their will on situations and could face resistance or admiration depending on the outcome.' + os.linesep +
                'Possible Choices: "Take charge of the situation and dictate terms," "Leverage authority to bend the rules," "Take immediate action to secure a victory."')]
    if MBTI == 'ENTP': 
        return ['The Debater', ('Approach: Outspoken, enjoys arguing and testing ideas.' + os.linesep +
                'Gameplay Impact: Known for being persuasive, they might engage in witty or sarcastic repartee during diplomatic situations. The Debator\'s could turn confrontations into debates, potentially winning allies through charm or sharp arguments.' + os.linesep +
                'Possible Choices: "Debate the other party into submission," "Challenge the opposing argument with logic," "Play devil\'s advocate to get more information."')]
    if MBTI == 'INFJ':
        return ['The Advocate', ('Approach: Insightful, empathetic, values deep connections.' + os.linesep +
                'Gameplay Impact: Empathetic dialogue options, often trying to mediate between conflicting sides. Advocates will be drawn to moral causes and seeking pragmatic, cooperative solutions that benefit everyone. However, they may avoid direct confrontation, opting for indirect solutions.' + os.linesep +
                'Possible Choices: "Appeal to the other party\'s sense of morality," "Find common ground through shared values," "Create a peaceful compromise."')]
    if MBTI == 'INFP': 
        return ['The Mediator', ('Approach: Idealistic, values harmony and understanding.' + os.linesep +
                'Gameplay Impact: Soft-spoken and diplomatic, likely to offer creative, peaceful solutions. INFPs might avoid conflict or work towards emotional resolution rather than practical outcomes. This could be both an advantage and a disadvantage, depending on the scenario.' + os.linesep +
                'Possible Choices: "Find a win-win scenario for both sides," "Encourage mutual understanding through storytelling," "Diffuse tension with compassion."')]
    if MBTI == 'ENFJ':
        return ['The Protagonist', ('Approach: Charismatic, socially aware, strong leadership skills.' + os.linesep +
                'Gameplay Impact: Protagonists will naturally engage in people-focused diplomacy, working to rally support for their cause and using their charisma to bring others into their vision. They would excel in motivating others but could be too idealistic at times.' + os.linesep +
                'Possible Choices: "Inspire the group to take action together," "Lead with compassion and warmth," "Offer solutions that cater to everyone\'s needs."')]
    if MBTI == 'ENFP':
        return ['The Campaigner', ('Approach: Campaugner\'s are creative, spontaneous, and value freedom.' + os.linesep +
                'Gameplay Impact: Known for their enthusiastic, optimistic approach to challenges. They might try to find a fun, unconventional solution to a diplomatic issue, preferring creative, flexible thinking over rigid rules.' + os.linesep +
                'Possible Choices: "Use charm and enthusiasm to sway opinions," "Think outside the box to win over the crowd," "Offer a lighthearted, flexible solution."')]
    if MBTI == 'ISTJ':
        return ['The Logistician', ('Approach: Practical, dependable, values tradition.' + os.linesep +
                'Gameplay Impact: Logisticians will likely approach diplomatic situations with a strong sense of duty and an adherence to rules. They prefer clear, organized solutions and will avoid ambiguity.' + os.linesep +
                'Possible Choices: "Propose a tried-and-true solution," "Stick to tradition and established norms," "Offer a detailed, step-by-step plan."')]
    if MBTI == 'ISFJ':
        return ['The Defender', ('Approach: Loyal, supportive, focuses on security.' + os.linesep +
                'Gameplay Impact: Defenders are service-oriented, often putting others\' needs first. In a diplomatic context, they will likely mediate and support the needs of others rather than assert their own will.' + os.linesep +
                'Possible Choices: "Advocate for the protection of those who need help," "Ensure everyone\'s safety before proceeding," "Create a solution that preserves stability and order."')]
    if MBTI == 'ESTJ':
        return ['The Executive', ('Approach: Efficient, organized, prefers structure and authority.' + os.linesep +
                'Gameplay Impact: Executives are likely to be straightforward and practical, preferring decisive actions that are well-planned. They would excel in roles where they can take charge and lead with authority.' + os.linesep +
                'Possible Choices: "Make a decision and implement it immediately," "Organize the team to complete the task effectively," "Stick to a well-structured plan."')]
    if MBTI == 'ESFJ':
        return ['The Consul', ('Approach: Social, caring, values cooperation.' + os.linesep +
                'Gameplay Impact: Consuls are likely to seek cooperative, peaceful solutions, relying on their strong interpersonal skills. They may work to ensure everyone is happy and included, sometimes at the cost of more practical or idealistic goals.' + os.linesep +
                'Possible Choices: "Appeal to the group\'s sense of community," "Find a consensus that everyone can agree on," "Ensure that no one is left behind in the discussion."')]
    if MBTI == 'ISTP':
        return ['The Virtuoso', ('Approach: Analytical, flexible, enjoys hands-on problem solving.' + os.linesep +
                'Gameplay Impact: Virtuoso\'s are likely to approach diplomatic situations with pragmatism and flexibility, often looking for solutions based on action rather than words. They might favor direct solutions that require little negotiation.' + os.linesep +
                'Possible Choices: "Find a practical solution that requires action," "Use logic to simplify the situation," "Make quick decisions and adapt as things change."')]
    if MBTI == 'ISFP': 
        return ['The Adventurer', ('Approach: Artistic, gentle, values personal freedom.' + os.linesep +
                'Gameplay Impact: Adventurers would focus on harmonious, creative solutions to diplomacy, offering peaceful ways to resolve conflict. They may have a more emotional, heartfelt approach to negotiations.' + os.linesep +
                'Possible Choices: "Appeal to the emotions of others," "Use creativity to inspire a peaceful resolution," "Suggest a flexible, open-ended compromise."')]
    if MBTI == 'ESTP':
        return ['The Entrepreneur', ('Approach: Energetic, bold, enjoys excitement.' + os.linesep +
                'Gameplay Impact: Entrepreneurs are likely to engage with a bold, spontaneous approach. They thrive in action-oriented environments and may push for immediate solutions, sometimes foregoing diplomacy in favor of action.' + os.linesep +
                'Possible Choices: "Take action without waiting for consensus," "Challenge others to make a quick decision," "Push forward with a bold plan."')]
    if MBTI == 'ESFP':
        return ['The Entertainer', ('Approach: Fun-loving, spontaneous, enjoys the moment.' + os.linesep +
                'Gameplay Impact: Entertainers would likely use charismatic charm to win over others and create a fun, easygoing atmosphere. They may use humor and lightheartedness to diffuse tension, although they can command more serious confrontations.' + os.linesep +
                'Possible Choices: "Lighten the mood with humor," "Charm the group into agreeing with your idea," "Suggest a spontaneous, fun solution to the problem."')]


def class_check(att, set):
    first_att, second_att = [attr.strip().lower() for attr in att]
    
    class_mapping = {
        # Theme: Space, Fantasy, Pirate, then followed by the class archetype
        'spa': {
            ('str', 'int'): {'class': 'shock-trooper', 'description': 'A powerful leader who excels in close combat and strategic planning.'},  # Leader
            ('str', 'agi'): {'class': 'tactician', 'description': 'A survivor who relies on agility and quick thinking to outmaneuver enemies.'},  # Survivor
            ('str', 'wis'): {'class': 'war-hero', 'description': 'A resourceful survivor with knowledge of tactics and survival skills.'},  # Diplomat
            ('str', 'cha'): {'class': 'smuggler', 'description': 'A charismatic diplomat who can talk their way out of almost any situation.'},  # Diplomat
            ('str', 'end'): {'class': 'survivalist', 'description': 'A hardy survivor focused on enduring the harshest environments.'},  # Survivor
            ('int', 'agi'): {'class': 'hacker', 'description': 'A tech-savvy individual who can manipulate systems and hack into networks.'},  # Tech
            ('int', 'wis'): {'class': 'doctor', 'description': 'A skilled medic who can heal wounds and treat ailments with precision.'},  # Tech
            ('int', 'cha'): {'class': 'embassy-diplomat', 'description': 'A charming negotiator who excels in diplomatic relations.'},  # Diplomat
            ('int', 'end'): {'class': 'researcher', 'description': 'A methodical and curious individual dedicated to discovering new technologies.'},  # Tech
            ('agi', 'wis'): {'class': 'stowaway', 'description': 'A stealthy individual who can blend into the background and avoid detection.'},  # Stealth
            ('agi', 'cha'): {'class': 'scoundrel', 'description': 'A charming and agile rogue who uses wit and cunning to outsmart their foes.'},  # Stealth
            ('agi', 'end'): {'class': 'scout', 'description': 'A quick and observant individual who excels at reconnaissance and exploration.'},  # Stealth
            ('wis', 'cha'): {'class': 'squad-leader', 'description': 'A seasoned leader who can command troops with wisdom and authority.'},  # Leader
            ('wis', 'end'): {'class': 'worker', 'description': 'A battle-hardened warrior who leads with courage and strength.'},  # Survivor
            ('cha', 'end'): {'class': 'commander', 'description': 'A charismatic and strategic leader, known for their decisive nature and tactical mind.'}  # Leader
        },
        'fan': {
            ('str', 'int'): {'class': 'battle mage', 'description': 'A mage who combines martial prowess with magical abilities for devastating results.'},  # Mage
            ('str', 'agi'): {'class': 'monk', 'description': 'A skilled fighter focused on hand-to-hand combat and quick strikes.'},  # Fighter
            ('str', 'wis'): {'class': 'fighter', 'description': 'A strong and resilient warrior, well-versed in a variety of combat styles.'},  # Fighter
            ('str', 'cha'): {'class': 'warlord', 'description': 'A powerful and charismatic guardian who leads their people with might and wisdom.'},  # Guardian
            ('str', 'end'): {'class': 'barbarian', 'description': 'A fierce and untamed warrior who relies on strength and endurance.'},  # Fighter
            ('int', 'agi'): {'class': 'rogue', 'description': 'A stealthy character who specializes in subterfuge, stealth, and surprise attacks.'},  # Stealth
            ('int', 'wis'): {'class': 'shaman', 'description': 'A spiritual and wise nature-based caster who can commune with the elements.'},  # Nature
            ('int', 'cha'): {'class': 'spy', 'description': 'A covert agent skilled in espionage and gathering vital information.'},  # Stealth
            ('int', 'end'): {'class': 'healer', 'description': 'A dedicated mage focused on healing and supporting allies in battle.'},  # Mage
            ('agi', 'wis'): {'class': 'thief', 'description': 'A nimble and quick character who specializes in stealth and stealing valuable items.'},  # Stealth
            ('agi', 'cha'): {'class': 'beastmaster', 'description': 'A master of animals, using their bond with creatures to gain an advantage in combat.'},  # Nature
            ('agi', 'end'): {'class': 'ranger', 'description': 'A guardian skilled in ranged combat and survival in the wild.'},  # Guardian
            ('wis', 'cha'): {'class': 'cleric', 'description': 'A holy mage focused on healing and supporting allies through divine magic.'},  # Mage
            ('wis', 'end'): {'class': 'druid', 'description': 'A nature-based caster who can shapeshift and command the forces of nature.'},  # Nature
            ('cha', 'end'): {'class': 'paladin', 'description': 'A noble and righteous warrior who fights for justice and the protection of others.'}  # Guardian
        },
        'pir': {
            ('str', 'int'): {'class': 'corsair', 'description': 'An imperial pirate with a mastery of naval combat and swashbuckling.'},  # Imperial
            ('str', 'agi'): {'class': 'specialist', 'description': 'A versatile pirate skilled in various forms of combat and tactics.'},  # Trader
            ('str', 'wis'): {'class': 'captain', 'description': 'A seasoned leader who commands a pirate crew with experience and wisdom.'},  # Captain
            ('str', 'cha'): {'class': 'first-mate', 'description': 'A charismatic and reliable second-in-command aboard a pirate ship.'},  # Captain
            ('str', 'end'): {'class': 'bouncer', 'description': 'A strong and tough pirate who handles physical confrontations with ease.'},  # Swashbuckler
            ('int', 'agi'): {'class': 'swindler', 'description': 'A cunning and agile pirate who uses deception and trickery to outwit opponents.'},  # Trader
            ('int', 'wis'): {'class': 'alchemist', 'description': 'A pirate with knowledge of arcane potions and chemicals, useful in combat and healing.'},  # Arcana
            ('int', 'cha'): {'class': 'privateer', 'description': 'A pirate who operates with a sense of honor, often working for the crown.'},  # Imperial
            ('int', 'end'): {'class': 'quartermaster', 'description': 'A pirate in charge of supplies and inventory, ensuring the crew is well-equipped.'},  # Trader
            ('agi', 'wis'): {'class': 'navigator', 'description': 'A skilled sailor and mapmaker, essential for navigating the high seas.'},  # Imperial
            ('agi', 'cha'): {'class': 'swashbuckler', 'description': 'A daring and charming pirate who excels in close combat with a rapier.'},  # Swashbuckler
            ('agi', 'end'): {'class': 'deckhand', 'description': 'A hardworking pirate who performs essential tasks aboard a ship.'},  # Swashbuckler
            ('wis', 'cha'): {'class': 'witchdoctor', 'description': 'A mystical pirate who uses dark magic and potions to heal and curse others.'},  # Arcana
            ('wis', 'end'): {'class': 'medic', 'description': 'A pirate healer who uses knowledge of anatomy and medicine to tend to injuries.'},  # Arcana
            ('cha', 'end'): {'class': 'pirate lord', 'description': 'A powerful and influential pirate captain, ruling over the high seas.'}  # Captain
        }
    }
        # Determine the correct class based on the selected theme and attribute combination
    if (first_att[:3], second_att[:3]) in class_mapping[set]:
        return class_mapping[set][(first_att[:3], second_att[:3])]
    elif (second_att[:3], first_att[:3]) in class_mapping[set]:  # Handle reverse order of attributes
        return class_mapping[set][(second_att[:3], first_att[:3])]
    else:
        return "\nClass not found for the given attributes and theme.\n"

def initialize_scores(person_scores=None):
    order = ['e', 'i', 'n', 's', 'f', 't', 'p', 'j']
    if not person_scores:
        return [0, 0, 0, 0, 0, 0, 0, 0]
    else:
        ordered_scores = [person_scores[key] for key in order]
        return ordered_scores

def apply_attribute_modifiers(att, person_scores, att_modifiers):
    """Apply the modifiers based on selected attributes."""
    for attribute in att:
        if attribute in att_modifiers:
            modifiers = att_modifiers[attribute]
            # Dampening the modification
            person_scores[0] += modifiers[0] * 0.25  # Extraversion vs Introversion
            person_scores[1] -= modifiers[0] * 0.25
            person_scores[2] += modifiers[1] * 0.25  # Intuition vs Sensing
            person_scores[3] -= modifiers[1] * 0.25
            person_scores[4] += modifiers[2] * 0.25  # Feeling vs Thinking
            person_scores[5] -= modifiers[2] * 0.25
            person_scores[6] += modifiers[3] * 0.25  # Perceiving vs Judging
            person_scores[7] -= modifiers[3] * 0.25
    return person_scores

def process_description(desc, person_scores, word_lists):
    """Process the character description and update the scores based on keywords."""
    clean_desc = re.sub(r'[^\w\s]', '', desc)  # Clean the description
    desc_words = clean_desc.split()  # Split into individual words
    
    # Check each word against predefined word lists
    for word in desc_words:
        for idx, word_list in enumerate(word_lists):
            if word in word_list:
                person_scores[idx] += 1
    return person_scores

def normalize_scores(person_scores, desc_weight, att_weight):
    """Normalize the scores based on description and attribute weights."""
    for i in range(8):
        person_scores[i] = person_scores[i] * desc_weight + person_scores[i] * att_weight
    return person_scores

def determine_mbti(person_scores):
    """Determine the MBTI personality type based on the scores."""
    # Determine dominant traits for each pair (E/I, N/S, F/T, P/J)
    e_i = "E" if person_scores[0] > person_scores[1] else "I"
    s_n = "S" if person_scores[3] > person_scores[2] else "N"
    f_t = "F" if person_scores[4] > person_scores[5] else "T"
    j_p = "J" if person_scores[7] > person_scores[6] else "P"
    
    # Construct MBTI type
    MBTI = (e_i + s_n + f_t + j_p).upper()
    type = get_personality_name(MBTI)  # Assuming you have a function like this
    
    return [type[0], type[1], MBTI]

def discover(desc, att, person_scores=None):
    """Main function to discover personality traits and MBTI type based on description and attributes."""
    # Initialize scores if not provided
    person_scores = initialize_scores(person_scores)
    
    # Attribute Modifiers Dictionary (kept as is for now)
    att_modifiers = {
        'intelligence': [-2, -2, -3, 1],   # ISTP
        'strength': [1, -2, -1, -1],       # ESTJ
        'endurance': [-1, -3, -2, 1],      # ISTP
        'charisma': [3, 2, 3, 1],          # ENFP
        'wisdom': [1, 2, 2, -1],           # ENFJ
        'agility': [-1, 2, 2, -1]          # INFJ
    }

    # Word lists for each personality trait
    E = ['outgoing', 'charismatic', 'bold', 'social', 'adventurous', 'energetic', 'talkative', 'expressive', 'leader', 'optimistic', 'enthusiastic', 'engaging', 'funloving', 'gregarious', 'assertive']
    I = ['quiet', 'reflective', 'thoughtful', 'reserved', 'independent', 'observant', 'contemplative', 'private', 'mysterious', 'shy', 'introspective', 'calm', 'focused', 'selfsufficient', 'self', 'serene']
    N = ['imaginative', 'visionary', 'creative', 'abstract', 'theoretical', 'insightful', 'curious', 'innovative', 'future', 'idealistic', 'conceptual', 'dreamer', 'pattern', 'reflective', 'imagination', 'vision']
    S = ['practical', 'realistic', 'detail', 'observant', 'grounded', 'logical', 'concrete', 'present', 'action', 'reliable', 'precise', 'sensible', 'cautious', 'hands', 'focused', 'dirty', 'mess', 'clean', 'touch']
    F = ['compassionate', 'empathetic', 'caring', 'sensitive', 'altruistic', 'harmonious', 'supportive', 'kind', 'heart', 'idealistic', 'genuine', 'considerate', 'patient', 'warm', 'understanding', 'cooperative']
    T = ['Analytical', 'logical', 'objective', 'strategic', 'decisive', 'detached', 'independent', 'rational', 'problemsolver', 'solver', 'skeptical', 'critical', 'realistic', 'efficient', 'pragmatic', 'direct', 'smart']
    P = ['spontaneous', 'flexible', 'openminded', 'open', 'adaptable', 'curious', 'freespirited', 'free', 'playful', 'resourceful', 'creative', 'unconventional', 'disorganized', 'exploratory', 'risktaking', 'risk', 'innovative', 'carefree', 'careless']
    J = ['organized', 'structured', 'responsible', 'decisive', 'planner', 'disciplined', 'systematic', 'goaloriented', 'goal', 'reliable', 'focused', 'efficient', 'methodical', 'conscientious', 'punctual', 'predictable']
    
    # Call all helper functions
    person_scores = apply_attribute_modifiers(att, person_scores, att_modifiers)
    person_scores = process_description(desc, person_scores, [E, I, N, S, F, T, P, J])
    person_scores = normalize_scores(person_scores, 0.7, 0.3)
    
    # Determine MBTI
    return determine_mbti(person_scores)

def check_name(name): # Function to handle names appropriatly and streamlined
    first_name = ''
    middle_name = ''
    last_name = ''

    names = name.split()
    if len(names) == 1:
        first_name = names[0].title()
    elif len(names) == 2:
        first_name = names[0].title()
        last_name = names[1].title()
    elif len(names) == 3:
        first_name = names[0].title()
        middle_name = names[1].title()
        last_name = names[2].title()
    else:
        return None
    return [first_name, middle_name, last_name]

def launch_gui():
    root = tk.Tk()
    app = character_creation(root)
    app.root.mainloop()

class character_creation:
    def __init__(self, root):
        self.root = root
        self.root.title('Character Creation')

        # Window Size
        self.root.geometry('950x1055+{}+{}'.format(int(self.root.winfo_screenwidth()/4), int(self.root.winfo_screenheight()/4)))

        # Global variables
        self.attributes = {'strength':0, 'intelligence':0, 'agility':0, 'wisdom':0, 'charisma':0, 'endurance':0}
        self.archetypes = {"outgoing": 0, "introvert": 0, "imaginative": 0, "practical": 0, "compassionate": 0, "analytical": 0, "spontaneous": 0, "organized": 0}
        cc_bg_image = Image.open(current_directory/ 'images' / 'solar_eclipse.jpg')
        self.bg_photo = ImageTk.PhotoImage(cc_bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.on_exit)
        self.exit_button.pack(side="right", anchor="ne", padx=10, pady=10)

        # Create Restart Button
        self.restart_button = tk.Button(self.root, text="Restart", command=self.on_restart)
        self.restart_button.pack(side="left", anchor="nw", padx=10, pady=10)

        # Character variables
        self.character_data = {}
        self.selected_attributes = []
        self.app_choice = tk.StringVar()
        self.app_radio = []
        self.selected = []
        self.selected_class = ""
        self.personality = []
        self.person_scores = {'e':0, 'i':0, 's':0, 'n':0, 'f':0, 't':0, 'j':0, 'p':0}
        self.app_selection = []
        self.app_selections = []

        # Font
        self.input_font = ("Times New Roman", 12)
        self.label_font = ("Times New Roman", 14)
        self.title_font = ("Times New Roman", 18)

        self.title_label = tk.Label(root, text="Character Creation", font=self.title_font)
        self.title_label.pack(pady=0)

        self.create_name_frame()
    
    def on_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            sys.exit()  # Close the application

    def on_restart(self):
        if messagebox.askyesno("Restart", f"Are you sure you want to completly restart fresh? \n(all Saved Data will be lost)?"):
            self.root.destroy()
            launch_gui()  # Going back to character Creation

    def create_input_entry(self, label, frame, action_func):
        f_label = tk.Label(frame, text=label, font=self.label_font)
        f_label.pack(pady=10)
    
        if label.startswith('Description'):
            text_widget = tk.Text(frame, height=20, width=100, wrap=tk.WORD, font=self.input_font)
            text_widget.pack(pady=10)
            if label in self.character_data:
                saved_description = self.character_data.get(label)
                text_widget.insert(tk.END, saved_description)
            self.character_data.update({label: text_widget})
            user_input = text_widget
        else:
            entry = tk.Entry(frame, font=self.input_font)
            entry.pack(pady=10)
            self.character_data.update({label:entry})

            button = tk.Button(frame, text="Next", command=lambda: action_func(frame))
            button.pack(pady=10)
            entry.bind("<Return>",lambda event, frame=frame: action_func(frame))
            user_input = entry

        return user_input

    def create_name_frame(self):
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(padx=20, pady=20)

        name_label=tk.Label(self.name_frame, text='Please Enter a Character Name (i.e. John Jacob Jingleheimer-Schmidt) \n| note the hyphen instead of a space on the last name |:'.replace('\n', os.linesep))
        name_label.pack(pady=10)

        def on_next(event=None):
            name = name_entry.get()
            while not name:
                messagebox.showerror("Input Error", "Name cannot be empty.")
                return
            names = check_name(name)
            if names:
                self.character_data['Name'] = names
                self.next_step(self.name_frame)
            else:
                messagebox.showerror("Input Error", "Only First, Middle, and Last names are acceptable\nPlease enter a valid name.".replace('\n', os.linesep))
        
        # Check if a name already exists to pre-fill the entry
        if 'Name' in self.character_data:
            name = " ".join(self.character_data['Name'])
        else:
            name = ""
        
        name_entry = self.create_input_entry('Name', self.name_frame, on_next)
        name_entry.insert(0, name)
        name_entry.focus_set()

    def next_step(self, current_frame): #----------- Handles the flow from one section to the next -------------# 
        current_frame.pack_forget()

        if current_frame == self.name_frame:
            self.create_sex_frame()
        elif current_frame == self.sex_frame:
            self.create_setting_frame()
        elif current_frame == self.setting_frame:
            self.create_class_frame()
        elif current_frame == self.class_frame:
            self.create_app_frame()
        elif current_frame == self.app_frame:
            self.create_desc_frame()
        elif current_frame == self.desc_frame:
            self.create_final_frame()

    def create_sex_frame(self):
        self.sex_frame = tk.Frame(self.root)
        self.sex_frame.pack(padx=20, pady=20)

        sex_label = tk.Label(self.sex_frame, text="What is your character's sex (Male, Female):", font=self.label_font)
        sex_label.pack(pady=10)

        self.sex_var = tk.StringVar()

        saved_sex = self.character_data.get('Sex', None)
        if saved_sex:
            self.sex_var.set(saved_sex)

        male_button = tk.Radiobutton(self.sex_frame, text="Male", variable=self.sex_var, value='male', font=self.label_font)
        female_button = tk.Radiobutton(self.sex_frame, text="Female", variable=self.sex_var, value='female', font=self.label_font)

        male_button.pack(pady=5)
        female_button.pack(pady=5)

        def on_next(event=None):
            sex = self.sex_var.get()
            if not sex:  # If sex isn't selected, show an error
                messagebox.showerror("Input Error", "Please select a sex.")
                return
            self.character_data.update({'Sex': sex})
            self.next_step(self.sex_frame)

        # Next button to move to the next step
        next_button = tk.Button(self.sex_frame, text="Next", command=on_next, font=self.label_font)
        next_button.pack(pady=10)
    
    def create_setting_frame(self):
        self.setting_frame = tk.Frame(self.root)
        self.setting_frame.pack(padx=20, pady=20)

        setting_label = tk.Label(self.setting_frame, text="Select a Setting for your Adventure:" )
        setting_label.pack(pady=10)

        self.set_var = tk.StringVar()

        space_button = tk.Radiobutton(self.setting_frame, text="Space", variable=self.set_var, value="space", font=self.label_font)
        fantasy_button = tk.Radiobutton(self.setting_frame, text="Fantasy (Arthurian)", variable=self.set_var, value="fantasy", font=self.label_font)
        pirate_button = tk.Radiobutton(self.setting_frame, text="Pirate", variable=self.set_var, value="pirate", font=self.label_font)

        space_button.pack(pady=5)
        fantasy_button.pack(pady=5)
        pirate_button.pack(pady=5)

        def on_next(event=None):
            set = self.set_var.get()
            if not set:
                messagebox.showerror("Input Error", "We need to know where the story is.")
                return
            self.character_data.update({'Setting':set})
            self.next_step(self.setting_frame)

        saved_set = self.character_data.get('Setting', None)
        if saved_set:
            self.set_var.set(saved_set)

        next_button = tk.Button(self.setting_frame, text="Next", command=on_next, font=self.label_font)
        next_button.pack(pady=10)
    
    def create_class_frame(self):
        self.class_frame = tk.Frame(self.root)
        self.class_frame.pack(padx=20, pady=20)

        class_label = tk.Label(self.class_frame, text="Select the TWO(2) attributes your character is proficient in:")
        class_label.pack(pady=10)

        def select_attributes(event=None):
            self.selected = [attr for attr, var in self.attribute_vars.items() if var.get()]
            if len(self.selected) != 2 and len(self.selected) != 1:
                self.class_display_label.config(text="Two attributes can be selected")
                return
            if len(self.selected) > 1:
                self.selected_class = class_check(self.selected, self.character_data['Setting'][:3])
                self.class_display_label.config(text=f"Class: {self.selected_class['class'].title()}")

        self.attribute_vars = {attr: tk.BooleanVar() for attr in self.attributes}
        for attr in self.attributes:
            checkbox = tk.Checkbutton(self.class_frame, text=attr.title(), var=self.attribute_vars[attr], command=select_attributes)
            checkbox.pack(pady=5)
            checkbox.bind("<ButtonRelease-1>", lambda event: select_attributes())

        # Add a label to show the selected class
        self.class_display_label = tk.Label(self.class_frame, text="Your character class will appear here", font=self.label_font)
        self.class_display_label.pack(pady=10)
        
        def on_next(event=None):
            if len(self.selected) != 2:
                messagebox.showerror("Input Error", "Please select TWO attributes.")
                return
            else:
                self.character_data.update({'Class':self.selected_class['class'].lower()})
                self.character_data.update({'Attributes':self.selected})
                self.next_step(self.class_frame)

        saved_attributes = self.character_data.get('Attributes', None)
        if saved_attributes:
            for attr in saved_attributes:
                self.attribute_vars[attr].set(True) 
            select_attributes()

        next_button = tk.Button(self.class_frame, text="Next", command=on_next, font=self.label_font)
        next_button.pack(pady=10)

    def start_questionaire(self):
        self.curr_question = 0
        self.app_questions = [
            ("Your friend presents you with a complicated puzzle on the bus, that you've never seen before. The puzzle is interesting and your friend seems excited to have you try.", 
            [
                ("Study the puzzle attempting new ways to approach the problems it presents, not putting it down until it's solved.", "intelligence,1,endurance,1"),
                ("Chuckle at the notion he'd assume you would care. Snap the puzzle in two and hand it back to him still chuckling as you walk away.", "intelligence,-1,strength,1"),
                ("Study the puzzle briefly, weighing whether you can solve it. Looking around you see a kid sitting behind you, you turn and dare him to solve it.", "intelligence,1,charisma,1"),
                ("Watch your friend's reaction to the different ways you handle the puzzle, trying to find a clue as to how it's solved.", "intelligence,1,wisdom,1"),
                ("Analyzing the puzzle, you notice how the pieces move together, knowing if you're quick enough with your movements you can bypass a major segement of the puzzle alltogether.", "intelligence,1,agility,1")
            ]),
            ("You're participating in an athletic competition when you see someone you like watching you, wanting to impress them you...", 
            [
                ("Find the heaviest peice of equipment hoping to hoist it over your shoulder and showing them how much you can handle.", "strength,1,endurance,1"),
                ("You quickly analyze and preform what would provide the most \"awe\" that you can safely do without too much effort.", "strength,-1,intelligence,1"),
                ("Give them a wink as you flex, then a soft smile as you complete your menuvear in the flashiest of ways.", "strength,1,charisma,1"),
                ("Remember what they said to you about what they enjoyed in your practice, Begin to show them the results of your training.", "strength,1,wisdom,1"),
                ("Hoping to show off, you quickly assess the best way to move through the competition, relying on your strength and quick movements to impress them with your speed.", "strength,1,agility,1")
            ]),
            ("You've found yourself stranded and lost in some dark woods, whether you came here intentionally or by accident doesn't matter, what do you do?", 
            [
                ("Keep moving forward, pushing through exhaustion and fear, determined to find a way out no matter how long it takes.", "endurance,1,strength,1"), 
                ("Start by finding shelter and food, preparing to endure the night with what little resources you have.", "endurance,1,wisdom,1"), 
                ("Sit down and try to focus, conserving your energy while thinking of the best way to escape or survive.", "endurance,1,intelligence,1"), 
                ("Shout for help, hoping that someone can hear you, continuing to look for an exit but beginning to get worried about how much longer you can make it alone.", "endurance,-1,charisma,1"), 
                ("Start walking in a specific direction, hoping to find a way out, focusing on staying calm and pushing through.", "endurance,1,agility,1")
            ]),
            ("You are at a friends party and the games are about to start but you notice your friend doesn't seem all that interested, so you ...", 
            [
                ("Walk over to your friend, put your arm around them, and pull them towards the group with a playful but firm challenge and invitation.", "charisma,1,strength,1"), 
                ("You come up with an exciting and interesting new way to play the game hoping it will arouse their curiosity.", "charisma,1,intelligence,1"), 
                ("Calmly walk over and engage in a heart to heart, trying to understand what might be throwing them off and listening to what they have to say.", "charisma,1,wisdom,1"), 
                ("Comically waddle over to them trying your best to make them laugh. Acting Loud you demand the game move to the pair of you; hoping to get them involved with your lively energy.", "charisma,1,agility,1"), 
                ("Ignoring them you continue to have fun at the party, you won't let their bad mood spoil your fun.", "charisma,-1,endurance,1")
            ]),
            ("You come across a difficult scene after a hard day of work, it looks like some children have encountered the neighborhood cat dead in the allyway next to your home. You decide to... ", 
            [
                ("Take a deep breath, crouch down, and calmly explain to the children what has happened, offering them reassurance and suggesting they leave the area to play and get their minds off of it.", "wisdom,1,charisma,1"), 
                ("Pause for a moment, reflecting on how to best help the children process their feelings, then you gently lead them away from the scene, offering a quiet, comforting presence.", "wisdom,1,endurance,1"), 
                ("Call animal control, keeping the children safe and out of harm's way, while ensuring proper steps are taken to not attract more wildlife.", "wisdom,-1,intelligence,1"), 
                ("say nothing to the children, not wanting to disturb their innocence. With a heavy heart you simply gather the cat and move it away, not making eye-contact or acknowledging any of the children.", "wisdom,1,strength,1"), 
                ("Assess the situation thoughtfully, then offer to guide the children through a ritual of saying goodbye to the cat, helping them understand the natural cycle of life and death.", "wisdom,1,agility,1")
            ]),
            ("You don't know how you ended up here but, looking at the barrel of a loaded .357 magnum, you hold your hands over your head offering vulnerability to the angry table player and... ", 
            [
                ("Slowly and carefully, you reach for the chair behind you, using it to carefully maneuver the chair until you can quickly and decisively throw it at the assaliant.", "agility,1,strength,1"),
                ("You drop to the floor, quickly rolling behind the counter saying \"Now I thought this was going to be a friendly game!\".", "agility,1,charisma,1"),
                ("With a deep breath, you sit back down at the table, moving your hands slowly and deliberately on the table, resting against the scattered chips, hoping to avoid further provocation.", "agility,-1,wisdom,1"),
                ("You steady yourself, then with a surge of perserverance, you push the table aside, fighting to close the gap and grab his gun.", "agility,1,endurance,1"),
                ("You calculate the best way to dodge or disarm the opponent, your mind racing through potential outcomes as you plan your next move.", "agility,1,intelligence,1")
            ]),
            ("You find yourself in a large group of strangers, no one seems to know what's going on or why they're here. What do you do?",
            [
                ("I need to find out what's going on. You look around for anything out of the ordinary that stands out, people, things, doesn't matter... What doesn't belong?", "i,1,s,1"),
                ("Engage with the people around you, was there something you missed?", "e,1,n,1"),
                ("Punch the person next to you, might as well make this exciting.", "e,0,j,2"),
                ("Start telling people you'll let them leave if they pay you $10.", "e,1,j,1"),
                ("Check your pockets for any clues, do a quick survey of yourself to understand what kind of condition you are in.", "i,1,f,1")
            ]),
            ("You've made a wrong turn heading to your mothers house. Looking around you see a few paths laid before you. You choose to...",
            [
                ("try and recall the time you went to your mom's house, closing your eyes to mentally recreate the directions you took", "n,1,t,1"),
                ("Look around trying to find a possible landmark or something familiar that can help you get back on track.", "s,1,j,1"),
                ("Look around and knock on a door, seeing if you can be given directions. It's Practical but could be dangerous, if you knock on the wrong door.", "s,0,e,1"),
                ("Follow the path you were walking down earlier. After all, you *must* have been going in the right direction at the start.", "n,1,j,1"),
                ("Pull out your map and try to figure out where you are and where you need to be.", "s,1,t,1")
            ]),
            ("Oh no! You've been exposed to radiation, and a mutated hand has grown out of your stomach. What is the best course of treatment?",
            [
                ("A bullet to the brain.", "f,2,j,2"),
                ("A large dose of anti-mutagen agent.", "f,1,s,1"),
                ("Prayer. Maybe God will spare you in exchange for a life of pious devotion.", "f,0,p,1"),
                ("Removal of the mutated tissue with a precision laser.", "t,1,s,1"),
                ("Observe, with a third hand you'll be able to complete tasks much faster.", "t,1,p,2")
            ]),
            ("There is work that needs to be done and everyone else is laying around. What do you do?",
            [
                ("Lounge with them, if it's a group effort we can't all get in trouble.", "p,1,e,1"),
                ("Watch and wait for everyone else to get motivated, they know the work needs to be completed as much as you do.", "p,1,s,1"),
                ("Talk with a friend, maybe you can motivate him and together you can get the group working.", "j,0,t,1"),
                ("Grab a nearby pan and wooden spoon, walk around everyone banging the pan with the spoon and telling everyone to get up.", "j,1,e,1"),
                ("Explode a firecracker in a barrel next to one of your coworkers right before they doze off.", "j,1,t,1")
            ])
        ]


    def update_question(self):
        """Update the UI with the next question and options."""
        self.skip_button.pack_forget()
        self.app_button.config(text="Next")
        self.app_button.pack(side="top")

        for button in self.app_radio:
            button.pack_forget()
        if self.app_selection:
            self.update_attributes(*self.app_selection[0])
            self.app_selections.append(self.app_selection)
        if self.curr_question < len(self.app_questions):
            question, options = self.app_questions[self.curr_question]
            self.quest_label.config(text=question)
            self.create_app_radio(options)
            self.curr_question += 1
        else:
            for attr in self.selected:
                self.attributes[attr] += 1 
            sorted_att = sorted(self.attributes.items(), key=lambda x: x[1], reverse=True)
            self.character_data.update({'Attributes':[attr for attr, _ in sorted_att[:2]]})
            self.selected_class = class_check(self.character_data['Attributes'], self.character_data['Setting'][:3])
            self.character_data.update({'Class':self.selected_class['class'].lower()})
            self.next_step(self.app_frame)

    def update_frame(self, question_text, options):
        """Updates the label and creates new radio buttons for the current question."""
        if not self.quest_label:
            self.quest_label = tk.Label(self.app_frame, text=question_text, font=("Helvetica", 15), fg="Black", wraplength=500)
            self.quest_label.pack(pady=20)
        else:
            self.quest_label.config(text=question_text)  # Update text of the label
        
        # Create new radio buttons for the current options
        self.create_app_radio(options)

    def update_attributes(self, pri_att, pri_val, sec_att, sec_val):
        personality_var = ['e','i','s','n','f','t','j','p']
        if pri_att in personality_var:
            self.person_scores[pri_att] += pri_val
            self.person_scores[sec_att] += sec_val
        else:            
            self.attributes[pri_att] += pri_val
            self.attributes[sec_att] += sec_val


    def create_app_radio(self, options):
        """Create a set of radio buttons based on the options list"""

        # Create new radio buttons
        for text, val in options:
            radio_button = tk.Radiobutton(
                self.app_frame, 
                text=text, 
                variable=self.app_choice, 
                value=val, 
                wraplength=600, 
                bg='#203030', 
                fg='#BBC8C8', 
                font=("Arial", 12),
                relief='ridge',
                width=300,
                indicatoron=0,
                command=lambda: self.app_select()
            )

            # Pack the radio button and add it to the list of current buttons
            radio_button.pack(anchor="center", pady=2, padx=10)
            self.app_radio.append(radio_button)

    def app_select(self):
        """Store the selected value temporarily"""
        self.app_selection.clear()
        selected_value = self.app_choice.get()  # Get the selected value (comma-separated string)
        
        # Split the string into individual parts
        pri_att, pri_val, sec_att, sec_val = selected_value.split(',')

        # Convert values to integers
        pri_val = int(pri_val)
        sec_val = int(sec_val)

        # Store the selected values in a temporary list (or dictionary, or other structure)
        self.app_selection.append((pri_att, pri_val, sec_att, sec_val))

    def create_app_frame(self):
        self.start_questionaire()
        self.app_frame = tk.Frame(self.root)
        self.app_frame.pack(padx=20, pady=20)
        self.curr_question = 0

        app_label = tk.Label(
            self.app_frame,
            text="Apptitude Test",
            font=("Helvetica", 15),
            fg="Black", 
            wraplength=500
        )
        app_label.pack(pady=10)

        self.quest_label = tk.Label(self.app_frame, text="Would you like to take a personality and apptitude quiz for your character?", font=("Helvetica", 15), fg="Black", wraplength=500)
        self.quest_label.pack(padx=20, pady=20)

        self.app_button = tk.Button(self.app_frame, text="Quiz", command=self.update_question,  font=self.label_font)
        self.app_button.pack(side="left", pady=10)

        self.skip_button = tk.Button(self.app_frame, text="Skip", command=self.skip_app,  font=self.label_font)
        self.skip_button.pack(side="right", pady=10)

    def skip_app(self):
        self.next_step(self.app_frame)

    def create_desc_frame(self):
        self.desc_frame = tk.Frame(self.root)
        self.desc_frame.pack(padx=20, pady=20)

        desc_label = tk.Label(
            self.desc_frame, 
            text="Describe your character: Who are they? How do people describe them? What are they like?", 
            font=("Helvetica", 18, "bold"), 
            fg="Black",                    
            wraplength=500                  
        )
        desc_label.pack(pady=10)

        def on_next(event=None):
            description_text = description.get("1.0", tk.END).strip()
            self.character_data.update({'Description':description_text})
            self.next_step(self.desc_frame)
        
        description = self.create_input_entry('Description', self.desc_frame, on_next)
        next_button = tk.Button(self.desc_frame, text="Next", command=on_next, font=self.label_font)
        next_button.pack(pady=10)
    
    def create_final_frame(self):
        self.final_frame = tk.Frame(self.root)
        self.final_frame.pack(padx=20, pady=20)

        frame_label = tk.Label(self.final_frame, text="Here are the results of your input")
        frame_label.pack(pady=10)
        self.personality = discover(self.character_data.get('Description'), self.character_data.get('Attributes'), self.person_scores)
        self.character_data.update({'Personality': self.personality}) # discover will return three variables (the Name of the MBTI, as defined by the 16 personalities group, and a description of that name | the letter combination of that code [i.e. "ENFP", "ISTJ" etc.])

        results_label = tk.Label(self.final_frame, 
            text=(f"Congratulations!!! {os.linesep}The {self.character_data.get('Class')}: "
                f"{' '.join(self.character_data.get('Name')).replace('  ', ' ')}, "
                f"has a personality matching {self.character_data['Personality'][0]}; "
                f"and is ready to face their challenges.")) # Pulling the title of the MBTI, not the letters.
        results_label.pack(pady=10)
        class_label = tk.Label(self.final_frame,
            text=f"A {self.character_data.get('Class').title()} is {self.selected_class.get('description').lower()}",
            wraplength=600)
        class_label.pack(pady=10)
        character_role_label = tk.Label(self.final_frame,
                                text=self.personality[1],
                                wraplength=600)
        character_role_label.pack(pady=10)

        self.proceed_var = tk.StringVar()
        proceed_button = tk.Radiobutton(self.final_frame, text="Proceed?", variable=self.proceed_var, value="proceed", font=self.label_font)
        edit_button = tk.Radiobutton(self.final_frame, text="Edit Character?", variable=self.proceed_var, value="edit", font=self.label_font) # Allowing the player to make changes.
        proceed_button.pack(pady=5)
        edit_button.pack(pady=5)

        def on_next():
            if self.proceed_var.get() == 'proceed':
                self.final_frame.pack_forget()
                storyboard(self.root, self.character_data, self.title_label, self.bg_label)
            elif self.proceed_var.get() == 'edit':
                self.final_frame.pack_forget()
                self.name_frame.pack(padx=20, pady=20)

        next_button = tk.Button(self.final_frame, text="Next", command=on_next, font=self.label_font)
        next_button.pack(pady=10)

class storyboard:
    def __init__ (self, root, character, title_label, bg_label):
        self.root = root
        self.root.geometry('2000x2000+{}+{}'.format(int(self.root.winfo_screenwidth()/4), int(self.root.winfo_screenheight()/4)))
        self.root.title(f"Adventure in {character.get('Setting').title()}")

        title_label.config(text=f"{character.get('Setting').title()} {character.get('Class').title()} Adventure", bg='#200000', fg='#DFDFDF')

        self.label_font = ('Times New Roman', 14, 'bold')

        self.bg_label = bg_label
        self.character_data = character
        self.stage = 'intro'
        self.character_choice = tk.StringVar()
        self.radio_buttons = []

        self.A_person = 0
        self.T_person = 0

        self.space_frame = tk.Frame(self.root, bg='#000000', width=10, height=10)

        self.space_label_font = ('Exo', 12, 'bold')
        self.space_input_font = ('Helvetica', 11)
        
        self.space_label_fg = '#BBC8C8'

        self.space_intro_label = tk.Label(self.space_frame)
        self.space_first_label = tk.Label(self.space_frame)
        self.space_second_label = tk.Label(self.space_frame)

        self.space_event = ""
        self.class_event = ""

        self.character_class = self.character_data.get('Class')

        self.personality = str(character.get('Personality')[2])
        self.role = self.personality[1:3].upper() # Takes the second and third letters from the MBTI analysis to determine the character "role" (NF, NT | SF, ST)
        if self.personality[1] == 'S':
            self.role = self.personality[1] + self.personality[3] 
            # If the Character is a sensory minded character the Role switches from the Nature trait, to the Tactics Trait

        self.start_story()
    
    def start_story(self):
        if self.character_data.get('Setting') == 'space':
            self.create_space_story()
        elif self.character_data.get('Setting') == 'pirate':
            self.create_pirate_story()
        else:
            self.create_fantasy_story()

    def remove_radio_buttons(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()
    
    def create_space_radio(self, options):
        """Create a set of radio buttons based on the options list"""

        # Create new radio buttons
        for text, value in options:
            radio_button = tk.Radiobutton(
                self.space_frame, 
                text=text, 
                variable=self.character_choice, 
                value=value, 
                wraplength=600, 
                bg='#203030', 
                fg='#BBC8C8', 
                font=("Arial", 12),
                relief='ridge',
                indicatoron=0
            )

            # Pack the radio button and add it to the list of current buttons
            radio_button.pack(anchor="center", pady=5)
            self.radio_buttons.append(radio_button)
    
    def on_intro(self):
        if self.character_data.get('Class') == 'researcher':
            if self.character_choice.get() == 'log':
                self.class_event = ('You painstakingly input each of your findings into the entry log. Your mind feels like it is going a million miles a second but the sound of the input pads recoginition keeps you grounded in your observations. You start forming hypothesis and placing those theories within the log '
                                    'under headings of each reason you believe it to be a possible source of the reaction. You focus on understanding what this compound is, how it it alive? What is it\'s purpose, was it manufactured by an unknown culture or a deceased one? The log goes on, branching antropology, biology, '
                                    'physics, just the mental gauntlet you could run through trying to elaborate on any of the findings.')
                
            elif self.character_choice.get() == 'experiment':
                self.class_event = ('Yeah, no. There is no way you\'re stopping now. Preparing the speculative experiments you and your team had constructed over the last 8 months you prepare an isolated enviroment to test and study the desease and how it reacts to different forms of life. After several hours, '
                                    'evidenced by the general increase of sentient activity occuring outside the lab, you begin to wonder if your team will barge in and let you know they feel robbed you ran their experiments without them and that all of the theories expose this desease as being potentially '
                                    'cataclysmic on a planetary level. Best part of the experiments though? They are totally correct. With the work you put in you have introduced enough stimuli to the contained, and dormant, disease that, if unchecked, could easily wipe out a system. Leaving the planet rich '
                                    'with hydrogen, carbon, and oxygen atoms galoire. With this and a simple atmosphere dome any planet, regardless how hostile or barren, can be colonized. Even astroids with enough mass can become veritable oasis.')
                
            elif self.character_choice.get() == 'sleep':
                self.class_event = ('As you pack up the telescope, writing yourself a scrawled note on a peice of paper just with the words "Donuts", you head to the pristine, clean, and ever so cozy (and familiar) guest bed in the lab to finally pass out and get some sleep. The next morning you arise.')

        elif self.character_data.get('Class') == 'doctor':
            if self.character_choice.get() == 'log':
                self.class_event = ('You log the discovery in a journal entry then proceed to work backwards to understand the "why" as well as the "how". Spending hours you lose track of time in your work.')
            elif self.character_choice.get() == 'experiment':
                self.class_event = ('No time to record, this opens the possibility to too many wonderful theories. You experiment with the specimen in every extreme enviroment you can safely recreate in the med bay. Each experiment you synthesize a compund to expand the capabilities. After hours and finishing '
                                    'one of the more complex puzzles that were presented during these trials you proudly recognize the compund which, if used properly, could vastly improve planetary modeling and habitation efforts. Think... with your work it wouldn\'t be unreasonable for everyone to have their '
                                    'own planet sized world. Think about it... Hunger, Overcrowding, Finite Resources... A thing of the past. You marvel at the possibilities.')
            elif self.character_choice.get() == 'sleep':
                self.class_event = ('Yeah, it\'s been a long day and with some sleep you can work with the team and fully understand this discovery. You write a note for yourself to properly remind you to discuss this with everyone when you wake up. Exhausted, you collapse on the patient table and fall asleep.')

        elif self.character_data.get('Class') == 'hacker':
            if self.character_choice.get() == 'log':
                self.class_event = ('Agreeing it would be a smart idea to backup the system and upload it to a breached folder on the research vessel\'s network, you start setting up a local backup and system redirect. The entire process takes about 20 minutes for the systems to upload successfully. '
                                    'After the system is backed up, you excitedly open the file. The details are methodical and chaotic. Every entry has a different structure and syntax, and it looks like, especially in the beginning, there were many contributors to the work. '
                                    'It\'s hard to decipher exactly what the meaning is of many of the entries, but after navigating through the windows until you found the most recent logs, they start making more sense. The cooling system pipes hum with the eerie sound of rushing water as you read. '
                                    'As the words sink in, you uncover just how deadly "Clean-Slate" is. "Apparently, it is a molecular disease which breaks down atoms to the most basic elements. The energy of which is devastating enough, but the disease will attach to any permeable matter while in a basic atmosphere and leave behind just hydrogen, carbon, or oxygen elements. '
                                    'It is hypothesized that the disease is able to spread across a planet\'s surface, remove all life, and leave behind just these elements where gravitational weight doesn\'t exceed a threshold. The only specimens found were from a distant planet named "Praimer", '
                                    'all of which were put in some kind of advanced stasis which the researchers are trying to understand as they speak. With this knowledge, you make your way back to your hideout.')
                
            elif self.character_choice.get() == 'open':
                self.class_event = ('The details are methodical and chaotic. Every entry has a different structure and syntax and it looks like, especially in the beginning, there were many contributors to the work. It\'s hard to decipher exactly what the meaning is of many of the entries but after '
                                    'navigating through the windows until you found the most recent logs they start making more sense. The cooling systems pipes provide the errie sound of rushing water all around you, as you read you uncover just how deadly "Clean-Slate" is. Apparently it is a molecular disease which breaks down '
                                    'atoms to the most basic elements. The energy of which is devestating enough but the desease will attach to any permeriable matter while in a basic atmosphere and leave behind just hydrogen, carbon, or oxygen elements. It is hypothesized that the desease is able to spread across a planets surface, '
                                    'remove all life and leave behind just these elements where gravitational weight doesn\'t exceed a threshold. The only specimen\'s found were from a distant planet named "Praimer", all of which were put in some kind of advanced stasis which the researchers are trying to understand as they speak. You '
                                    'question your motives. "This is a compound that destroys planets... If this fell into the wrong hands. If this fell into my hands... what would I do with it?" You get engulfed in the thought, the moral complexity of what it means and the people it could save. "This could provide planets to anyone, '
                                    'anywhere we could establish an atmosphere could be a private residence and home. Limited resources a thing of the past, poverty... gone... but... how many people want poverty to exist? want there to be those with power and those without." The thought takes an hour of your time but eventually you, '
                                    'make your way back to the hideout, changed.')
                
            elif self.character_choice.get() == 'home':
                self.class_event = ("Heading back to the hideout excitedly you meet up with each member of the crew as they return as well. \"Guys... I found a \'Project Clean-Slate\', What do you think it is? Some juicy secrets of a superiour officer who had too much trouble with the law and needed a new identy? Maybe it\'s a device "
                                    f"that can wipe the memory of a user and make them docile and obediant? Oo! Maybe its--\" one of your companions cuts you off saying \"A new ration meal recipe. Seriously {self.character_data.get('Name')[0]} You could have at least looked it over before running all the way back here. If it\'s nothing "
                                    "you\'re going to look pretty foolish.\" scoffing you think to yourself, \"No... It\'s something big, I know it.\" Opening up the file the beginning is cryptic and hard to make out because each entry is written in a different format following different syntax. \"It looks like there are a lot of different "
                                    "contributors on this one project, must be a pretty good recipe.\" You give a smirk at the dig. \"Here let me see that.\" Your companion pushes over you and takes the pad from your hand. You see them navigating several screens until finally \"Oh wow. Yeah, this is big. It looks like the research team has "
                                    "been working on a molecular disease that breaks down matter atomically. It infects a planet and within hours everything on the planet is dead leaving behind rich oxygen, hydrogen, and carbon deposits. The desease disipates when it is unable to reproduce.\" You think about the implications of such a thing. "
                                    "\"Do you know what this is?\" Looking up at their face still lost in thought about how devestatingly powerful this is you see the smirk shine through their eyes. \"This is our ticket to limitless fortune. With one of these specimen we could threaten anyone and everyone. We could make astroids mansions, we "
                                    "have anyone we want have the resources and power needed to do whatever we asked them to do...\" You look around gauging the reactions around you.")

        self.remove_radio_buttons(self.space_frame)
        self.space_event = f"{self.class_event}\n\n" + ("A commontion comes from the door as the rest of your team arrives in the lab. As they begin to prepare for the day you anxiously wait to inform them of your recent discovery but as you are about to confide the monumental evidence and realization the intercom system blares "
                                                    'the voice of an obviously terrified military personal. "Listen, I—I don\'t have much time. They\'re on the ship—do you hear me? They\'re boarding. You need to move—now!" Suddenly in Shock your mind races to the research and what your discovery may mean in the wrong hands. '
                                                    f"\"Where is our security personel?\" Shouts Maria, a fellow {self.character_data.get('Class')}. You look around and notice she\'s right. Aside from your team you are all alone in the lab. Maria frantically looks to you, the defacto leader, \"What do we do?\"")
        if self.character_data.get('Class') == 'hacker':
            self.space_event = f"{self.class_event}\n\n" + ("As you discuss the implications with the rest of your team you\'re interupted by a loud microphone. Blaring through the hallways of the dark undercroft in the bellies of the ship you hear \"Listen, I—I don\'t have much time. They\'re on the ship—do you "
                                                            'hear me? They\'re boarding. You need to move—now!" Realizing there isn\'t much time to move, you\'re not a soldier. You don\'t want to get wrapped up in the chaos of open battles and warfare. How do you want to handle this situation?')
        self.space_intro_label.config(text=self.space_event)
        self.space_intro_label.pack(pady=0, anchor="center")

        self.create_space_radio([
            ('We need to get with security personal, we can just blend in with everyone else and no one needs to know about this discovery until we''re all safe', 'retreat'),
            ('We have to secure the disease, this discovery makes it even more important to ensure it is in the right hands.', 'secure'),
            ('We\'ll be safe here, we can setup fortifications and secure the entry points.', 'defend')
        ])

        if self.character_data.get('Class') == 'doctor':
            self.create_space_radio([
                ('', 'smooth-talk'),
                ('"The clock\'s ticking. I\'ll stall them with a little misdirection and use the distraction to slip away with the goods."', 'misdirection')
            ])
        elif self.character_data.get('Class') == 'researcher':
            self.create_space_radio([
                ('"I\'m not used to sitting at a table, but I\'ve fought for peace before. I\'ll try to use my reputation to sway them to my side."', 'use-reputation'),
                ('"Words aren\'t enough now. We\'re at a breaking point—time to act." If they won\'t listen, I\'ll take control of the situation."', 'take-charge'),
                ('"There\'s only one way forward. I\'ll have to appeal to their sense of honor and reason, and hold my ground until we come to a solution."', 'honor')
            ])
        elif self.character_data.get('Class') == 'hacker':
            self.create_space_radio([
                ('"I\'ve been trained for moments like this. I\'ll find common ground, keep the peace, and maintain control of this negotiation."', 'find-common-ground'),
                ('"I need to hold my position and remain calm, despite the growing pressure. This is the moment I\'ve been preparing for."', 'stay-calm'),
                ('"If diplomacy fails, I\'ll offer them an alternative: a gesture of goodwill that might buy us the time we need to escape."', 'gesture-of-goodwill')
            ])
        if self.role == 'NF':
            self.create_space_radio([
                ('"I know we can avoid conflict if we just talk through our differences. I\'ll appeal to their higher ideals, to their better nature."', 'appeal-to-ideals'),
                ('"I\'m going to try to calm them, using compassion and empathy. There\'s always a way to talk this through."', 'empathize')
            ])
        elif self.role == 'NT':
            self.create_space_radio([
                ('"This is a game of logic and strategy. I\'ll look for their weaknesses and turn them to our advantage."', 'strategize'),
                ('"I need to understand the bigger picture. I\'ll observe carefully and calculate my next move with precision."', 'analyze')
            ])
        elif self.role == 'SP':    
            self.create_space_radio([
                ('"I\'ll improvise. The situation\'s fluid, and I\'m good at adapting. Let\'s turn this around, whatever it takes."', 'improvise'),
                ('"The door\'s almost open, but I need to get out fast. I\'ll make a quick decision and get ahead of them."', 'decisive-action')
            ])
        elif self.role == 'SJ':
            self.create_space_radio([
                ('"I need to keep everything under control. If I can organize my thoughts and make a well-planned move, we\'ll be okay."', 'plan'),
                ('"There\'s no room for mistakes here. I\'ll stick to the rules and maintain order, even under pressure."', 'stay-orderly')
                ])
            self.next_button(command=self.on_next)

    def create_space_story(self):
        self.space_frame.pack(fill=tk.NONE, expand=True, padx=10, pady=10, anchor="center")

        next_button = tk.Button(self.space_frame, text="Next", command=self.on_next,  font=self.label_font)
        next_button.pack(pady=10)

        if self.character_data.get('Class') in ('commander', 'squad-leader', 'shock-trooper'):

            space_bg_image = Image.open(current_directory / 'images' / 'spiral_galaxy.jpg')
            space_bg_image = space_bg_image.resize((2000, 2000), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(space_bg_image)
            self.bg_label.config(image=self.bg_photo, bg='#000000', width=2000, height=2000)
            self.space_label_bg = '#382020'

            self.character_data.update({'Archtype':'Leader'})
            if self.character_data.get('Class') == 'commander':    
                self.class_event = ('The Research Vessel\'s constant, almost rhythmic, activity usually lends itself to helping you relax. You find yourself unable to sleep, weighed down by the upcoming meeting with the outer-region dignitaries. The political tension hanging in the air as the fate of entire systems '
                                    'may rest on their words. Some poor diplomatic handlings by rogue traders, but there is also this trip, despite being your third on this route in the last year, '
                                    'feels like it\'s leading us into unknown and dangerous territory. The empty void of space has never felt less familiar, and the uncertainty about what lies ahead has you on edge—')
                
            elif self.character_data.get('Class') == 'squad-leader':
                self.class_event = ('The Research Vessel hums with quiet energy as you try to rest. The hum of the vessel is a constant drone, like the pulse of a beating heart—steady, but strangely unsettling in its consistency. '
                                    'You can\'t shake the nagging feeling that something is wrong. You\'ve seen enough to know when things don\'t sit right. '
                                    'Everything about this mission feels off. They\'ve got you and your squad on "extra security" for a diplomatic mission, but it\'s hard to ignore the truth—this isn\'t what you and your '
                                    'crew are made for. You\'re here to babysit the colony delegates and embassy-diplomats, but that\'s all it is: a babysitting job. You don\'t even think the outer-region delegates had their '
                                    'own security brought on board. In all your years on the front lines, during missions with real danger, you\'ve never been asked to just watch over people who have no clue about space, '
                                    'or how many ways you can die out here. "I don\'t know, there\'s something off..." You sit on your bed, staring into the quiet emptiness of your quarters. The thought lingers—"Something doesn\'t '
                                    'feel right about this." You can\'t shake the feeling of being sidelined. As you lie there, trying to refocus, you don\'t even hear the door to your quarters open.')

            elif self.character_data.get('Class') == 'shock-trooper':
                self.class_event = ('The hum of the Research Vessel and the rhythmic vibrations beneath your feet usually help you zone out, but tonight it\'s different. Something feels wrong. '
                                    'You\'ve been through enough to know that feeling, the one that creeps up your spine and won\'t let go. In all your years in the field, it\'s always when things go quiet you need to worry, '
                                    'and this mission, while routine on the surface, has been anything but. The higher-ups brought in an additional team for security detail, and you don\'t know them. '
                                    'That alone is enough to make you uneasy. This ship was supposed to be straightforward, just ferrying diplomats through space and letting the researchers work on their "projects"—but the cargo traffic, '
                                    'the unusual comms silence from your usual contacts with the cartels, and the subtle changes in the air just make you feel like there\'s something more going on. You\'ve been told to stay on standby, '
                                    'to wait for orders as the negotiations take place, and it doesn\'t sit well with you. You\'ve seen this before— everything\'s going to go smooth, or it\'s going to go sideways fast. And with the silence in the air... you\'re betting on the latter.')

            space_event = f"{self.class_event}\n\n" + ('"Sir!" \nThe sudden shock of hearing a fresh cadets plea alerts your attention. '
                                        '"There appears to be a ship off our bow and it looks like it is gearing its weapons for a possible '
                                        'assualt on our vessel." \nStill half-paying attention you move to look at the fresh cadet, smothered '
                                        'in sweat. You wonder if he has gotten any sleep since we have left the port on Ralgerius 3 days ago. ' 
                                        '\n\n"What are our orders, sir?"')

            space_event= space_event.replace('\n', os.linesep)
            self.space_intro_label.config(text=space_event, font=(self.label_font), wraplength=600, bg=self.space_label_bg, fg=self.space_label_fg)
            self.space_intro_label.pack(pady=0, anchor="center")

            # General answers for everyone who is in the "Leader" Archetype
            self.create_space_radio([
                ('"I know you are scared cadet but at times like these we need to stay calm, you know more about what\'s going on. What do you think we should do?"', 'inspire'),
                ('With all the people on board they are trying to catch us off guard and assume we will try to avoid a direct confrontation so they won\'t be prepared for a real '
                 'battle. "Cadet, Man your post, They are not going to bring us down without a fight."', 'combat'),
                ('"We need to know everything we can about them, fast. Why do they think we\'re a threat? Have you been able to secure any other intel on the ship, what makes you say '
                 'they are preparing to assualt us?" This is a Routine mission, What is going on?', 'research')
            ])

            # Class-Specific Decisions (for each class)
            if self.character_data.get('Class') == 'commander':
                self.create_space_radio([
                    ('"We need to understand their intentions first. Let\'s open up communication and see if we can de-escalate before things go south."', 'diplomat'),
                    ('I need to take command of this. "Let\'s deploy a drone and gather intel. We\'ll act decisively once we know more, no more guessing."', 'investigate')
                ])
                
            elif self.character_data.get('Class') == 'squad-leader':
                self.create_space_radio([
                    ('I need to calm the squad. They need to be prepared for whatever comes next. "Cadet, you\'ve been trained, you\'ve been seasoned. No matter '
                     'what some random nobody is going to throw at us, we\'ll be able to brush it off like we\'re just in a game of dodgeball."', 'calm'),
                    ('We need to know what we\'re up against. "Jenkins, you know the drill—send a scout to gather intel, but make sure they don\'t get spotted. No surprises this time."', 'investigate')
                ])
                
            elif self.character_data.get('Class') == 'shock-trooper':
                self.create_space_radio([
                    ('We\'ll get a readout of their systems from the command deck before getting in my two-man fighter in the cargo bay, to jump ship. We\'ll hit thier weak points and overwhelm them with decisive force leaving them no time to react. '
                     '"We\'re not waiting around for them to make the first move. Let\'s hit them hard, hit them fast, and show them who they decided to mess with."', 'charge'),
                    ('This could turn into a drawn-out fight, so we need to dig in and prepare. Strong positions, clear exit strategies. If they want a fight, let\'s make sure we control the ground. '
                     '"Let\'s fortify the positions and hold the line until we have the full intel. Let them come, but make them regret it."', 'tactical')
                ])

            # Role based Decsions (For Character Personalities)
            if self.role == 'NF':
                self.create_space_radio([
                    ('"I know you\'re feeling the pressure, Cadet, but we can get through this together. We need to stay focused, for all of us. What do you say, can we get through this together?"', 'encourage'),
                    ('It doesn\'t matter if I just woke up; my team needs me. I need to lead by example and keep our spirits high. Grabbing my laser rifle, I give the cadet a reassuring pat on the shoulder. "Looks like we\'re going to take care of it."', 'rally')
                ])
            elif self.role == 'NT':
                self.create_space_radio([
                    ('"We need to understand what we\'re up against. Do you have any useful intel, Cadet, or are you still processing the basics?" Walking past the cadet, rifle in hand, you prepare yourself for '
                     'whatever comes next. "Let\'s get to the facts. We need to figure out what\'s going on."', 'research'),
                    ('Intel is likely our best source for info on their ship. A quick sweep of their systems will tell us who they are and what their intentions might be. "Cadet, focus on the sensors and data '
                     'feeds. We need precise information, and we need it fast. Are you prepared to move quickly?"', 'tactical')
                ])
            elif self.role == 'SP':
                self.create_space_radio([
                    ('If they\'re preparing for an assualt, now may be the best time to avoid catastrophe, we could bum rush them with the full force of our security personel then if we make it '
                    'quick and decisive they won\'t have the chance to react. "We need to prepare for an assualt on the ship, We need a small team to head out, hit em hard and hit em fast."', 'charge'),
                    ('After grabbing the laser rifle off the bed mantle, you turn to Cadet Jenkins and say, "We don\'t have time for a deep dive, but we need some quick answers. Let\'s get a scan on that ship, '
                    'check for any weaknesses or hidden capabilities. After that, we hit them fast, we hit them hard."', 'research')
                ])
            elif self.role == 'SJ':
                self.create_space_radio([
                    ('"We have a protocol for unknown vessels, Jenkins. First, we need to know what we\'re dealing with. I need a detailed readout on their movements, ship status, and any communications activity." '
                    'You quickly activate your comm unit. "Get me all available intel on our neighbor vessel, let\'s ensure we have all the facts before making any moves."', 'command'),
                    ('"We need to ensure the ship is secure, Jenkins. I want you to double-check the ship\'s external sensors and shields. Prepare all security teams for a possible boarding, but we won\'t act until '
                     'we know what we\'re dealing with." You pull up the ship\'s security dashboard, watching for any signs of vulnerability. "We may need to reinforce key areas, but let\'s not act rashly until we '
                     'have a full read on their intentions."', 'security')
                ]) 

        if self.character_data.get('Class') in ('stowaway', 'scout', 'scoundrel'):
            
            self.root.geometry('1024x1024+{}+{}'.format(int(self.root.winfo_screenwidth()/4), int(self.root.winfo_screenheight()/4)))

            space_bg_image = Image.open(current_directory / 'images' / 'cramp_space.jpg')
            space_bg_image = space_bg_image.resize((1024, 1024), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(space_bg_image)
            self.bg_label.config(image=self.bg_photo, bg='#000000', width=1024, height=1024)
            self.space_label_bg = '#202020'
            
            self.character_data.update({'Archetype':'Stealth'})
            if self.character_data.get('Class') == 'scoundrel':    
                self.class_event = ('As you awake from another sleepless night, aboard another vessel one of the cartels have a problem with you; you wonder how you ended up working for some of the sleaziest people in the galaxy. '
                                    'Get in, grab the research, get paid. A simple job to put food on the table. "Being a good talker doesn\'t make you lucky I guess." Thinking back to the kingpins on Ralgarius that asked for this '
                                    '"favor" to pay off your debt. A clap of boots against the hallway chambers echo through the cargo bay, tightening up, you listen. ')
            elif self.character_data.get('Class') == 'stowaway':
                self.class_event = ('You\'re familiar with the dark underbelly of a research cruiser, they make lots of stops on their travels with ample opportunities to take what you need to survive and the crew are either too '
                                    'preoccupied with their research, or too apathetic, to care about a few missing ration tokens and some general supplies missing here and there. The crew seems nice enough though, they may not know who ' 
                                    'I am, they may not care, but they could be my last chance. "Maybe I can become more than just a cargo rat?" Resting on the makeshift bed you fashioned from some '
                                    'discarded goods you "found" at the Ralgarius system 3 weeks ago, your thought is interrupted by an echo of footsteps in the hallway, perking up your ears you listen. ')
            elif self.character_data.get('Class') == 'scout':
                self.class_event = ('Another mission to understand the enemy. This time a research cruiser working on regional data of systems and people. The only reason I\'m here is because the higher-ups thought they may unearth '
                                    'deep military tech from the far reaches of space. This must be the third or fourth time we\'ve been out this far though. Overhearing some discussions from the doctors and researchers it seems they '
                                    'may have come across an interesting bacteria that might change this war effort, for one side or the other "Does it matter to me?" Only a handful of the crew even know anything has been found so maybe '
                                    'it doesn\'t matter. In the hallway you hear an echoing of footsteps that forces you to pay attention. ')
            
            space_event = f"{self.class_event}\n\n" + (f"You can hear the faint hum of machinery above you as you notice shadows entering from the hallway. The patter of boots echoing off the walls has you freeze in your tracks as "
                                                            'you realize they are getting closer to your hideout. You glance around, trying to pinpoint what they may be after. You come behind a group of crew members checking the bay. They '
                                                            'haven\'t seen you. This is your chance to make a move. Whatever you do, make it count.')
            
            space_event= space_event.replace('\n', os.linesep)
            self.space_intro_label.config(text=space_event, font=(self.label_font), wraplength=600, bg=self.space_label_bg, fg =self.space_label_fg)
            self.space_intro_label.pack(pady=0, anchor="center")

            # General answers for everyone in the "Stealth" Archetype
            self.create_space_radio([
                ('I need to stay quiet and out of sight. I\'d rather sneak by them unnoticed and get to a safer spot, doing nothing may cost me.', 'sneak'),
                ('I can create a distraction, draw them away and keep the coast clear for now. It\'s a risky move, but I\'ll take the gamble.', 'distraction'),
                ('I need to understand why they\'ll coming into cargo. We haven\'t taken port yet, I\'ll stay out of sight and try and understand more.', 'spy')
            ])

            # Class-Specific Decisions (for each class)
            if self.character_data.get('Class') == 'stowaway':
                self.create_space_radio([
                    ('I\'ve hidden in worse places before. They won\'t find me. But I need to make sure they don\'t hear or spot me, I\'ll drop the cover, then just wait and listen, as always.', 'con'),
                    ('As you watch the crew from behind, you can\'t help but think: "Maybe this ship is getting too hot, if I can force them to land I\'ll get off, find another ship, leave this behind... It\'s risky and if I\'m found it\'s all '
                     'over but what else can I do? I\'ll have to be quick. The engine room isn\'t too far and that port off the side panel could get me there without having to deal with our guests. I\'ll just keep moving on..."', 'sabotage')
                ])
                
            elif self.character_data.get('Class') == 'scout':
                self.create_space_radio([
                    ('I\'ll stay in the shadows, watch their movements, learn their search pattern. It\'s odd they\'re down here, what are they looking for? I should find out.', 'con'),
                    ('They won\'t expect to find me. If I\'m fast and silent, I could take out this search party and make a move for the research. I think the engine room is close by, I could stall their engines and leave before they ever '
                     'knew anything was taken.', 'sabotage')
                ])
                
            elif self.character_data.get('Class') == 'scoundrel':
                self.create_space_radio([
                    ('"I could try playing it off that I\'m supposed to be here, maybe a lost researcher? If I can find someone vulnerable, maybe I can get better quarters and provisions.', 'con'),
                    ('The engine bay is just around the corner, I bet I can get there while they\'re looking in here. If I ran into anyone, "I could say I was a maintance worker picked up to help lighten the load. I could do some damage, '
                     'grab the research, and hea out, lickity split."', 'sabotage')
                ])

            # Role-based Decisions can be tailored similarly based on personality types (NF, NT, SF, ST)
            if self.role == 'NF':
                self.create_space_radio([
                    ('I have to wait this out, Whatever they\'re after they will be in and out, I\'m just going to stay low and stay quiet, I don\'t need to get involved yet.', 'quiet'),
                    ('I hate to even think it, but it\'s starting to feel like it\'s coming down to them or me. "Please don\'t come over here... I don\'t want to hurt you." readying the knife you\'ve kept hidden for emergencies', 'defend')
                ])
            elif self.role == 'NT':
                self.create_space_radio([
                    ('"I need to be smart about this. I\'ll hang back and just watch what they\'re doing, If I can figure that out maybe I can make it easier for them next time they feel like snooping."', 'quiet'),
                    ('"I can make it quick and decisive; I can take them down, figure out why they\'re here, and maybe cause some chaos I can exploit, if nothing else, I could always use a fresh replecator."', 'defend')
                ])
            elif self.role == 'SP':
                self.create_space_radio([
                    ('"I need to understand the problem. I can watch where they are going, what they\'re here to do, then I\'ll know how best to use them.', 'quiet'),
                    ('"If I get their attention I could draw them in and ambush them in the storage chamber, that place is a maze, so I would just have to get them seperated, then it would be nothing to swipe a higher clearance key. '
                     '"That would make travel a lot easier around the ship."', 'defend')
                ])
            elif self.role == 'SJ': # Organized and Conscientious
                self.create_space_radio([
                    ('"This isn\'t anything new. Just blend in, disappear, no one knows I\'m here. They won\'t catch me." I whisper to myself as the hallway door slides close behind the crew members.', 'quiet'),
                    ('"This won\'t be difficult, they don\'t even look like officers. I\'ll take them down one at a time, I haven\'t had to be a ghost in some-time, I\'ll swipe their keycards and move on to a better posisiton."', 'defend')
                ])   

        if self.character_data.get('Class') in ('survivalist', 'worker', 'tactician'):

            space_bg_image = Image.open(current_directory / 'images' / 'tight_space.png')
            space_bg_image = space_bg_image.resize((2000, 2000), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(space_bg_image)
            self.bg_label.config(image=self.bg_photo, bg='#000000', width=2000, height=2000)
            self.space_label_bg = '#202020'
            
            self.character_data.update({'Archetype':'Survivor'})
            if self.character_data.get('Class') == 'survivalist':    
                self.class_event = ('Pushing the heavy weights off your chest and resting the bar on the hooks, you feel the strain in your chest, the afterburn of the workout. The endorphins rush in as your body rejoices in the raw power you\'ve '
                                    'built for any eventuality. Rising from the bench, you reach for your towel and head for the sink to wash the sweat from your face. Just as you finish, you hear a commotion outside the gym. Looking around, you '
                                    'notice the room is eerily empty—there were no other trainers or gym-goers around you. Were you too caught up in your workout to notice? Or had everyone else left already? ')
                
            elif self.character_data.get('Class') == 'worker':
                self.class_event = ('You\'re coming up on your second hour and you\'re stuck cleaning the gym with the junior enlisted crew—these young recruits are fresh, eager, and have no idea what space travel really entails. '
                                    'You finish wiping down the last of the equipment with them, explaining your years of \"wisdom\". But as they hyper-focus on some peice you usually just brush off, you notice some uneasy glances between them. The buzz from their comm units is unnerving. '
                                    '"What... This can\'t be real." One of the juniors mutters. '
                                    'Then the unmistakable sounds of blaster fire and plasma discharges erupt from outside. The gym quickly is engulfed in chaos, everyone scrambling for the exit, but you lock eyes with the juniors, their first off world mission and it\'s going to start like this? You can\'t afford to let them panic. '
                                    'You quickly signal the older patrons in the gym to lead the juniors to a safe spot, the patrons don\'t seem to notice or care about what you\'re doing or whatever crazy symbols you may be making. looking towards the newbies you mouth the words "Stay hidden, stay quiet, stay alive." You hear another '
                                    'blast echo through the hallway outside of the gym, \"it\'s closer this time. Time is running out."')
                
            elif self.character_data.get('Class') == 'tactician':
                self.class_event = ('Your days off are a rare moment of peace, a break from the endless war-games and worst-case scenario simulations that you\'re usually locked into. The gym is a quiet place where you can unwind and focus on improving '
                                    'yourself physically. Lifting the dumbbell, you feel your muscles stretch, each movement an exercise in endurance. But as you lower the weight on the final rep, a sudden commotion outside snaps you out of your rhythm. '
                                    'Blaster fire and plasma discharge echo in the distance. You pause for a second, listening to the positions of the parties at play. The sense of peace gone. Back to the war-games, understanding threats, responses, contingency—they\'re all running at full speed. '
                                    'You can\'t relax. Whatever this is, it won\'t give you that luxery, and let\'s be honest, you can never afford it. ')
            
            space_event = f"{self.class_event}\n\n" + (f"Suddenly over the intercom, a clearly rattled cadet hastily speaks into the mic: \"Listen, I—I don\'t have much time. They\'re on the ship—do you hear me? They\'re boarding. You need to move—now!\" The transmission cuts out abruptly, followed by "
                                                        'plasma shots and the sound of blaster fire, which is closer and just outside the gym doors. Your body\'s prepared... but are you? What do you do now? The danger is real, and it\'s here. ')

            if self.character_data.get('Class') == 'tactician':
                space_event = space_event + f"\n\nAs you listen to the blaster fire that echoes and fills the training center you are aware that a group of presummed security within the research vessel is just outside the left-hand entry way. They\'re setting up for a defense but it doesn\'t sound like they are moving forward."
            
            space_event= space_event.replace('\n', os.linesep)
            self.space_intro_label.config(text=space_event, font=(self.label_font), wraplength=1000, bg=self.space_label_bg, fg=self.space_label_fg)
            self.space_intro_label.pack(pady=0, anchor="center")

            # General answers for everyone in the "Survivor" Archetype
            self.create_space_radio([
                ('Hold your ground, The best thing to do is fortify and set up a strong defense. "We\'ll need a place to setup shop, regardless of who\'s out there."', 'defense'),
                ('I need to coordinate with the rest of the crew, if we\'re planning an offensive it has to be together.', 'communication'),
                ('"Only one way out of this mess, and that\'s through that door. I\'ll need to find a weapon then setup a parimeter." ', 'offense')
            ])

            # Class-Specific Decisions (for each class)
            if self.character_data.get('Class') == 'survivalist':
                self.create_space_radio([
                    ('Lowering your head you feel the adrelinaline rush through your body. Hearing the shots being fired you sumise that someone is pushing back, for now, and you should go join them, they might be able to provide a weapon and support to meet objectives.', 'group-up'),
                    ('You scan the room for anything you can turn into a weapon. Seeing the replecator that is used to provide appropriate sports wear you wonder if you could rig the machine to explode. You have little time; there may not be much before the '
                    'enemy is in front of you, eyes constantly on the door, you quickly rework the wring and position the machine near the entry way, hoping the improvision will be enough. "I could attract them in the gym, then, with some good planning and luck, I\'ll have it go off. '
                    'Leaving me with their weapons for the next wave." Holding the remote you fashioned from the module, you prepare to face the enemy', 'trap')
                ])
                
            elif self.character_data.get('Class') == 'worker':
                self.create_space_radio([
                    ('I need to keep the juniors safe, If I can meet up with the team outside we could organize an offensive and get these fresh bodies to safety. I probably can\'t wait for a break in combat, I\'m going to have to stay low, who knows how much time I have left before they get overrun.', 'group-up'),
                    ('Thinking to yourself you question "Do I even care? They knew what they were getting into when they signed on to this job. We\'re here because we need the money, nobody said it was going to be easy." Looking around you find some resistance bands, you position yourself with a good view of the entry '
                     'points and locker room. "This may be every man for themselves, I can defend this position until there is a break and then I can run for it."', 'abandon')
                ])
                
            elif self.character_data.get('Class') == 'tactician':
                self.create_space_radio([
                    ('"I need to get out there and help them advance." I\'ll meet with the commander and help prepare an offensive. Readying your laser sidearm you fallback into the routine you\'ve been preapring since you were a cadet, to head out and meet the enemy.', 'group-up'),
                    ('"We need a central postion to mount our strategies if we\'re going to survive long. I can try and meet with the group outside to help them pull back so we can set an ambush. If they\'re not going to move forward lets at least turn that to our advantage." You ready your laser sidearm to give cover-fire while your '
                    'moving security to this central location, fighting to a stalemate helps no one. They\'re inability to advance will be just what we need to force them into a trap.', 'trap')
                ])

            # Role-based Decisions can be tailored similarly based on personality types (NF, NT, SF, ST)
            if self.role == 'NF':
                self.create_space_radio([
                    ('"I can\'t let anyone else get hurt, I need to get out there and meet the enemy head on. I\'ll be smart, staying low and any advantage that presents itself will be all I need."', 'confront'),
                    ('They\'ll need my support out there, I\'ll have to try and setup a central base here to help us enter a position to deesculate the situation. We can get on comms and everyone will know this is a refuge.', 'defend')
                ])
            elif self.role == 'NT':
                self.create_space_radio([
                    ('"I need to be smart about this. If I can help tip the numbers in our favor we could push back and never let them get a chance to recover."', 'confront'),
                    ('"It would make more sense to construct a fortification here. I can establish an ambush at the entryway letting in only our allies, with the drink dispensers and calorie stations we could pull off a game of attrition, if it ever came to that."', 'defend')
                ])
            elif self.role == 'SP':
                self.create_space_radio([
                    ('"I need to meet them head-on. With the blaster fire they won\'t be expecting someone to confront them here. I just need to wait for the right moment" putting your ear to the wall to hear the commotion on the otherside attempting to postion the players.', 'confront'),
                    ('"With the resources and gym equipment I could improvise a diversion and obstacle that would allow me to gain the upperhand in a one on one. A quick one-two punch with a dumbbell, than I can learn a lot about who our guests are and what they may be after."', 'defend')
                ])
            elif self.role == 'SJ': # Organized and Conscientious
                self.create_space_radio([
                    ('"There\'s no rest for the wicked it seems. I\'ll join the team outside, hopefully gaining a tactical edge by an unexpected appearance, we\'ll push them back to the cargo corridor and I\'ll meet with whoever\'s stationed here to see how we\'ll get ahead of this."', 'confront'),
                    ('"We need a place to call home. The right thing to do would be fallback and establish a central space for our forces to rally, we may lose this battle but I can get as many in this defensible position as I can and we can get a working plan organized."', 'defend')
                ]) 
                
        if self.character_data.get('Class') in ('embassy-diplomat', 'war-hero', 'smuggler'):
            self.character_data.update({'Archetype':'Diplomat'})
            space_bg_image = Image.open(current_directory / 'images' / 'training_in_space.png')
            space_bg_image = space_bg_image.resize((2000, 2000), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(space_bg_image)
            self.bg_label.config(image=self.bg_photo, bg='#000000', width=2000, height=2000)
            self.space_label_bg = '#202020'
            self.space_frame.config(width=1200, height=500)

            if self.character_data.get('Class') == 'smuggler':
                self.class_event = ('A research vessel is a safe enough space, all the researchers and scientists are so far up their own butt you can pretty much get away with murder as long as you don\'t interfere with whatever "fantastic" work they\'re dealing with. It\'s not like it\'s made '
                                    'life any easier for the little guy. The ones at the bottom scrounging to collect enough for the chance to sit at the "big boy" table. That\'s where you\'re at right now; The big boy table. Sitting across from you, shimmying his laser pistol, is one of the kingpin lackey\'s from Ralgerius. '
                                    '"Look, I didn\'t want to waste anyone\'s time. We\'re litterally coming to pick up the cargo as we speak. You think it\'s easy getting the credientials to head on a class E Research Vessel?" The large man sitting across the cargo boxes you\'ve fashioned for a meeting house stands up, '
                                    f"his face no longer hidden in the shadows you see a long knife scar run down the side. \"This could change the war-effort {self.character_data.get('Name')[0].title()}, we need results and we had hoped you had something, a specimen from the lab or anything that proved you were on the right "
                                    'side... Oh well, I\'ve heard this ship may not be able to make it\'s intended destination, let\'s hope you didn\'t count on this being your only way out." Won\'t make it to it\'s intended destination? "What does that mean? Are you thinking sabatoge?" You '
                                    'feel your pulse quicken, the weight of the situation sinking in. "This is the only vessel that can get us to Parimer. If you\'re planning something, it won\'t just be the specimens they have on the ship you\'ll be throwing away, it\'ll mean no one will want to head-" then it dawns on you. '
                                    'They want the only ship that can make the journey. They have research stations but ... even one other ship is too crowded and risky for the underbelly of society. Smaller traffic will help to "change the war-effort"; but If they want noterity so no one will rebuild, it won\'t '
                                    'be pretty. I\'m not a soldier. I\'ve been in tight spots but what this lab is working on... "Change the war-effort", sure. More like take control of the only ship that can get us to Parimer. They\'re not after a specimen, they\'re after power. \nThe lackey stands up, sneering as he turns to leave. '
                                    '"I knew this was a waste of time," he mutters. "Oh well, my ride\'s almost here. Good luck with... whatever you decide." You think... Which side should I be on when the power shifts? As the lackey leaves and you ponder, you feel a subtle change in the atmosphere, as though something is about to snap. '
                                    'The Cargo bay falls still and quiet.')

            elif self.character_data.get('Class') == 'war-hero':
                self.class_event = ('You\'ve earned your reputation as a hero of countless battles, but now you\'re caught in a different kind of battle—one of words. A diplomatic mission to broker peace has led you to a tense meeting room, where the fate of entire systems, and the possibility of open war, is at stake. '
                                    'As you sit across the table of the dignitaries and respected ambassadors for the outer region systems—the colonies have only recently been able to meet—you feel the clash of cultures weighing on your mind. Am I so self important I believe any of these people '
                                    'care about the battles I\'ve seen or the friends I lost? The proud diplomat for the imperial colonies stands at his spot, addressing the colorful delegation sitting opposite your group. "We need to exercise fruitfulness and compassion. We should open our spaces to each other, fostering unity and..." '
                                    'He is abruptly interrupted by the ambassador sitting directly opposite yourself. "What you want is control! It\'s written in your history, clear in your actions and regard. You think we care to adopt your cruel society? Understand, it is your wanton disregard for our '
                                    'people and their laws that has brought us to this table—not because we envy your way of life." The diplomat sits down, deflated, leaving his words hanging in the air. You rise, unshaken, acknowledging the floor. "That\'s unfair, wouldn\'t you say? Many of the grievances you\'ve outlined stem from '
                                    'miscommunication, not malice." Stepping forward, you lean in, your presence commanding the room. "This isn\'t envy or some misplaced sense of recompense. Surely we can not dismiss the strength of friendship and camaraderie because of the careless actions of a few misguided individuals. Are your '
                                    'people so well off and perfect you believe you can impose such judgment—that our infrastructure, our security, our commerce and trade, the diverse cultures we represent offer your people nothing?" Your voice cuts through the tension in the room. The ambassador lowers his gaze and you speak before '
                                    'taking your seat. There\'s a subtle change in the atmosphere, as though something is about to snap. "We are offering you strength in unity and you come to us, whimpering, saying your people need nothing. I wonder if they would be so quick to think us the cruel ones?" The room falls still.')

            elif self.character_data.get('Class') == 'embassy-diplomat':
                self.class_event = ('You stand tall, confident in your role as the voice of reason, the one who can bring order to this tense room. The fate of entire systems rests on these negotiations, and you\'ve prepared for this moment—your entire career has led to this. As you speak, you feel the eyes of the outer-region ambassadors on you, '
                                    'waiting for the chance to form an opinion, a judgment, of the colonies. "We need to exercise fruitfulness and compassion. We should open our spaces to each other, fostering unity and..." you begin, setting the tone for what you believe will be a productive conversation. But then, the interruption. A harsh '
                                    'voice from the other side of the table cuts you off. "What you want is control! It\'s written in your history, clear in your actions and regard. You think we care to adopt your cruel society? Understand, it is your wanton disregard for our people and their laws that has brought us to this table—not because '
                                    'we envy your way of life." The words hit you like a slap. You\'re not used to being interrupted, It\'s not just the interruption—it\'s the accusation. They can\'t understand the situation. The colonies are compassionate, how could they not be? How can they appreciate that if they keep dragging up the past? '
                                    'Your stomach churns, but you hold your ground. You try to give a measured response but the tension is intense. You need to sit to not offend them more. It may be impossible to reason with these delegates if they can\'t see what the colonies have to offer, or would be so petty as to burn that bridge over some '
                                    'simple trading misscommunications. To your horror, the war-hero stationed in the room as nothing more than a symbol of strength rises from their seat. The stance hardening as they speak in a voice that fills the room. You watch in disbelief as they step forward, their gaze sharp, and their voice cutting through '
                                    'the air. They acknowledge the group and assume the floor. "This isn\'t envy or some misplaced sense of recompense," they declare, leaning in, their tone unwavering. "Surely we can\'t dismiss the strength of friendship and camaraderie because of the careless actions of a few misguided individuals." Your heart '
                                    'sinks. This is going to insult them even more, they will never want to be brought to the table again. As you listen though you realize they\'re making the case you were building, but it\'s with such force and such passion, it\'s impossible to deny the weight of their words. You\'ve been careful. You\'ve been '
                                    'strategic, taken great lengths to traverse the delicate rules and customs to even have the ambassadors here. However, Now, with the War-Hero\'s boldness filling the room, you feel small. They continue, their voice sharp, "Are your people so well off and perfect you believe you can impose such judgment—that our '
                                    'infrastructure, our security, our commerce and trade, the diverse cultures we represent offer your people nothing?" The room falls silent, the tension palpable. You feel the eyes of the ambassadors now not on you, but on the War-Hero. The room, usually full of calm calculation, has shifted. There\'s no going back. '
                                    'You bow your head, humbled, letting the War-Hero finish their speech. "We are offering you strength in unity and you come to us, whimpering, saying your people need nothing. I wonder if they would be so quick to think us the cruel ones?" You remain silent, unsure of how to respond. The War-Hero\'s words hang '
                                    'in the air, and in that moment, you realize that perhaps there\'s more than one way to win these battles. As the last words of the War-Hero still linger in the air, you feel a subtle change in the atmosphere. The War-Hero has made their case, but will they succeed where '
                                    'your careful diplomacy has failed? Will they get the final applause? Or will it be you—when you find a way to redeem this situation? The atmosphere feels as though something is about to snap. The room falls still.' )

            space_event = f"{self.class_event}\n\n" + ('Suddenly, the air feels heavier, and the distant hum of the ship seems to grow louder. The door begins to rattle, and you realize the situation has shifted. A message flashes across your communicator: "We\'re under attack." which is followed by a fresh cadet, probably on his first '
                                                        'off-world mission, on the intercom, barely able to speak coherently. Exhasperated he shouts in the microphone "Listen, I—I don\'t have much time. They\'re on the ship—do you hear me? They\'re boarding. You need to move—now!"')

            self.space_intro_label.config(text=space_event, font=(self.label_font), wraplength=1200, bg=self.space_label_bg, fg =self.space_label_fg)
            self.space_intro_label.pack(pady=0, anchor="center")
            self.create_space_radio([
                ('We need to come to a conclusion. Security should handle the boarding party but if relations between us don\'t improve, a lot more people could die than just those on this ship.', 'negotiate'),
                ('There is a system to these crisis\', I\'m sure the relevant parties are being contacted. What\'s important now is taking control of the situation in this room.', 'calm'),
                ('I can\'t stay here, for no other reason than I\'m good to no one if I\'m dead. We need to get off and resume this somewhere more appropriate.', 'retreat')
            ])

            if self.character_data.get('Class') == 'smuggler':
                self.create_space_radio([
                    ('"Stop! Look, I have details about the ship that could make this whole process cleaner and save your people their lives. How about we actually talk about my assistance in helping you take the ship." At least that way not as many people will have to die.', 'talk'),
                    ('"You think you can push me around? I have details on every inch of this ship. You won\'t be able to navigate security without my help. This attack you staged, is going to end with thousands of your people dead and you facing litigation and undue attention unless we find a way to work together." I can keep them distracted while the commander leads an offensive.', 'intimidate')
                ])
            elif self.character_data.get('Class') == 'war-hero':
                self.create_space_radio([
                    ('"It seems our conversation will be being cut short. I hope this doesn\'t distract from what is important here. We can\'t be fighting with ourselves while fighting the world."', 'talk'),
                    ('Tired of the politics when there is real danger you swallow your pride and fear. "Whatever is on the other side of that doo, whatever blaster-fire or plasma assaults come our way, we need to take care of our people. Are you going to open your borders and let us help you or will you just sit back and watch as your people die?"', 'intimidate')
                ])
            elif self.character_data.get('Class') == 'embassy-diplomat':
                self.create_space_radio([
                    ('"There isn\'t anytime to iron this out completely but we need to work together, all of us, for the people who have trusted us to take care of things. I-I don\'t know what\'s going on with the ship but we need to not let this get between us."', 'talk'),
                    ('"We need to move out and get to a safe location. Look, I don\'t think it\'s important you like me right now or not, we have a duty to take care of this with as little friction as we can. If we aren\'t working together than you might as well just ask our security to let the enemies in."', 'intimidate')
                ])
            if self.role == 'NF':
                self.create_space_radio([
                    ('"I know we can avoid conflict if we just talk through our differences. You say we need to respect your custom\'s more? then lets start by working together and learning to understand each other."', 'appeal'),
                    ('"There is only one way to ensure the most people get through this alive. We need to come together and create a plan together. I understand the fear, the terror of trusting someone you don\'t understand. We owe it to ourselves and those around us at being friends and getting through this... together."', 'connection')
                ])
            elif self.role == 'NT':
                self.create_space_radio([
                    ('An appeal to logic will probably be what works best here, "If we can join our forces, both here on the ship and pursueing our assaliants, we\'ll have the best chance of getting out safely."', 'appeal'),
                    ('If I can empathesize with them, help them see we have more in common than different, we may be able to get over these disagreements. "I know it\'s difficult to come together with someone you believed was your enemy. The colonies weren\'t formed because we all had good feelings towards one another. It was the necessity of having '
                    'a central alliance, a universal culture and custom, that brought us together. Times in trial and danger were the catalyst to friendship. We could finally began to see how we fit together, rather than the edges that tore us apart." Extending your hand you offer to help the outer region dignatary up. "You heard him, we need to move.', 'connection')
                ])
            elif self.role == 'SP':    
                self.create_space_radio([
                    ('"We can\'t predict everything move, but we can definetly figure things out along the way. Together, let\'s adjust as we go and use our combined strengths to keep things moving forward, not looking back towards the past."', 'appeal'),
                    ('"This situation won\'t be easy, but I\'ll keep us connected. We can make a quick deciseve action and we\'ll stay ahead of the threat. We can all play a part, and that is how we will all survive this, together."', 'connection')
                ])
            elif self.role == 'SJ':
                self.create_space_radio([
                    ('I need to keep everything under control. If I can organize my thoughts and take the right steps, we\'ll make it through. Stability and leadership will keep us safe. "Listen, we need to work together to get through this. Everyone, follow me.', 'appeal'),
                    ('"We don\'t have time for mistakes, but we do have time to stick a plan. I\'ll make sure we stay coordinated and unified, we\'ll follow the plan, maintain order and we WILL get through this."', 'connection')
                ])

        if self.character_data.get('Class') in ('doctor', 'researcher', 'hacker'):
            next_button.pack_forget()

            intro_button = tk.Button(self.space_frame, text="Next", command=self.on_intro,  font=self.label_font)
            intro_button.pack(pady=10)

            space_bg_image = Image.open(current_directory / 'images' / 'sterile_lab.jpg')
            space_bg_image = space_bg_image.resize((2000, 2000), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(space_bg_image)
            self.bg_label.config(image=self.bg_photo, bg='#000000', width=2000, height=2000)
            self.space_label_bg = '#808080'
            self.space_label_fg = '#202020'
            self.space_frame.config(width=1200, height=500)

            self.character_data.update({'Archetype':'Tech'})
            if self.character_data.get('Class') == 'researcher':  
                self.class_event = ('The research lab is almost lifeless this late at what you presume must be night, morning, it\'s so hard to keep your circadian rhythem to the galactic standard time. You usually get so engrossed in your work that what felt like hours turns out to be days. Breifly looking towards the '
                                    'discarded ramen ration boxes thrown about the bay you make the educated guess you have been at this research for 3 or so days now. You know you can get this to work though, the data supports the hypothesis and you and the doctor teams on board have been so close to a breakthrough it feels '
                                    'like a cruel joke by this point. Staring into the microscope you see two seperate blue stained mounds pressed against the glass being shine through by the backlight. Others told you that these old devices were useless, and you would hate to prove them right, but there is just '
                                    'nothing like the feeling of looking at something through your own eyeball instead of having it being projected to you. You don\'t need to examine each organelle and fiber that works its way into the specimen, you just. need. it. to. reproduce! "Ugh" you say in disgust. "Is it '
                                    'the radiation? Is it the light? I\'ve seen you reproduce in -70°C. I\'ve seen you multiply on magma over 800°C! Wait" you say excidedly "No, please it really can\'t be so simple" as you get up and browse your collection of assorted specimen\'s. "Please let it still be here, come '
                                    'on, tell me we didn\'t get rid of it all." Your rummaging through the bins above the food station until "YES! Here she is" you sing, holding a half eaten box of powdered donuts. \n\nYou step in front of the telescope letting out a slow heavy breath. "Was sugar all you needed little fellow? '
                                    'get some pep in your step as it were?" as you place a small amount of powdered sugar on the telescope slide you wait as the disease explodes in reaction, in almost an instant 2 became 4 became 16 became 256. The "old device" recognizing the expanse of material purged the slides with '
                                    'quantum void immedately emptying the space between the slides into a random portion of space across infinity, where, without the ability to reproduce, they died. Of course, all you saw was a green light *ping* as soon as you laid the powder sugar. Reading the "neutralized lifeforms count" '
                                    'on the monitor adjacent from you, you explain: "That\'s an interesting find. If you get the disease started after being dorment with simple sugar it will expand exponentially." With this discovery, what should you do?'.replace('\n', os.linesep))
                
                self.space_intro_label.config(text=self.class_event, font=(self.label_font), wraplength=1000, bg=self.space_label_bg, fg=self.space_label_fg)
                self.space_intro_label.pack(pady=0, anchor="center")
                # Providing options on how to handle the new data
                self.create_space_radio([
                    ('Log your findings in a log entry and begin to try and work backwards with why the reaction is so strong with sugar. Hoping to understand this aspect instead of branching forward with the disease itself', 'log'),
                    ('No, this is too important to just through away. We\'ve been picking up how many dormant specimens from Parimer unable to bring it out of hibernation, now we know how to restart them and you want to give up? You\'re a researcher, prove it.', 'experiment'),
                    ('That was a good find and I\'ll be excited to dive deeper tomorrow with the full team but right now, I need to sleep.', 'sleep')
                ])

            elif self.character_data.get('Class') == 'doctor':  
                self.class_event = ('The med-bay has a quiet errieness this late at night. You look at the clock hanging over the trash bin in the corner of the room: "11:00PM GST" it reads in the digital, robotic, font assigned to it. "Global standard Time is always so hard to get accustomed to. '
                                    'As you sit in front of this "live" specimen of a disease encounted on Praimer you start to wonder if it\'s really any benefit to you. The cells are, in theory, able to break down matter into it\'s simple atotomical components of hydrogen, carbon, and oxygen. '
                                    'This theory if it\'s true could change the way planets are handled '.replace('\n', os.linesep))
                
                self.space_intro_label.config(text=self.class_event, font=(self.label_font), wraplength=1000, bg=self.space_label_bg, fg=self.space_label_fg)
                self.space_intro_label.pack(pady=0, anchor="center")
                # Providing options on how to handle the new data
                self.create_space_radio([
                    ('Log your findings in a log entry and begin to try and work backwards with why the reaction is so strong with sugar. Hoping to understand this aspect instead of branching forward with the disease itself', 'log'),
                    ('No, this is too important to just through away. We\'ve been picking up how many dormant specimens from Parimer unable to bring it out of hibernation, now we know how to restart them and you want to give up? You\'re a researcher, prove it.', 'experiment'),
                    ('That was a good find and I\'ll be excited to dive deeper tomorrow with the full team but right now, I need to sleep.', 'sleep')
                ])
            elif self.character_data.get('Class') == 'hacker':  
                self.class_event = ('The dark communication array is cold and lifeless. The quiet hum of systems running as you type on your portable device gaining access to the network drives for the entire facility. As you breach each security firewall, bypass each network probe, you '
                                    'dig deeper and deeper into the research vessel\'s logs. You make silent judgments about the trivial information that populates 90% of the data you\'ve accessed, things like "The Commander had his egg whites before hitting the gym" have you mocking "because '
                                    'he believes all eggs should be white." Nevertheless you always come accross something interesting if you dig deep enough, maybe you\'ll find something immoral that you can plaster on all the display units before the important diplomatic meetings today. Maybe you\'ll '
                                    'find some secret cache of biological weapons that could finally shift the scales of this "war" back to the people of the colonies. *ping* The notification jars you from your focus. Your pulse quickens as you open the file, and the words on the screen make your stomach drop. '
                                    '"Looks like I finally drummed up something..." The words on the screen are clear: "All known information about the highly sensitive and classsified project, codenamed: \'Clean-Slate.\'" This is it. This was what you\'ve been searching for. Your heart skips a beat. This is bigger '
                                    'than anything you imagined. What do you do?'.replace('\n', os.linesep))
                
                self.space_intro_label.config(text=self.class_event, font=(self.label_font), wraplength=1000, bg=self.space_label_bg, fg=self.space_label_fg)
                self.space_intro_label.pack(pady=0, anchor="center")
                # Providing options on how to handle the new data
                self.create_space_radio([
                    ('Take the extra time to save a system backup, incase something happens and you lose this information', 'log'),
                    ('Open the file and read the contents', 'open'),
                    ('Having what you came for head back to your hide out and review the file in the abandoned side-cabin off the medical wing you\'ve setup as you base of operations.', 'home')
                ])

    def first_label(self):
            # Leader Archtype Options
            if self.character_choice.get() == 'inspire':
                self.space_first_label.config(text='"Yeah, you\'re right. I just need to relax. I think we should focus on getting some intelligence." Moving forward '
                'with your laser rifle, you give a smile to the Cadet. "I know you could do it." You head out the door passing down the hallway with Cadet Jenkins behind you. The '
                'hallway is realitively quiet and the conversations seems to be just gossip so you suspect the information that had Jenkins so worried hasn\'t been made public. '
                'Entering an elevator you select the option to head to the...', font=(self.label_font), wraplength=600, bg=self.space_label_bg, fg =self.space_label_fg)
                self.A_person += 1
                self.space_first_label.pack(pady=0)
            
                # ----------------------- General Leader Decisions ------------------------------------
                self.create_space_radio([
                    ('Comm Station, everyone needs to know what may lay ahead for them and having more eyes and ears open might provide hidden answers.', 'rally'),
                    ('Command Deck, We\'ll have the most information from the command deck, this is the central hub for the research stations, which would provide real-time information about the capabilities of the stranger', 'tactical'),
                    ('Telecommunication Array, This will have the most information to try and cross reference anything noticable on the ship and compare it with known archives.', 'research')
                ])

                #--------------------------- Class Decisions ------------------------------------------
                if self.character_data.get('Class') == 'commander':
                    # Commander-specific options
                    self.create_space_radio([
                        ('Battle-Bridge, "We\'re going to speak softly but let\'s make sure they can see we have a big stick."', 'diplomat'),
                        ('Command Deck, "We\'re going to send a squad out to investigate and get some of that intelligence you\'re looking for."', 'investigate')
                    ])
                    
                elif self.character_data.get('Class') == 'squad-leader':
                    # Squad-Leader-specific options
                    self.create_space_radio([
                        ('Command Deck, "You\'re right, lucky for us I know some people who are probably itching to get some. Jenkins, you can lead the big picture from the command deck My squad and I will get you some working information", stepping off the elevator to find the rest of the squad.', 'board'),
                        ('Battle-Bridge, "I\'m betting the captain is on the battle bridge, we\'ll meet up with him and see what his plan is. He may have that information you\'re after."', 'captain')
                    ])
                    
                elif self.character_data.get('Class') == 'shock-trooper':
                    # Shock-Trooper-specific options
                    self.create_space_radio([
                        ('Cargo Bay, "You and me Jenkins, we\'re going to get that intelligence and figure out what\'s going on. Are you ready to find the best seats in the house? Oh, and have you ever flown in a modified Spector-9 Stealth Cat? You\'ll see your life flash before your eyes on startup."', 'board'),
                        ('Engineering, "I\'m not about to let them see us with our pants down, we can check the ship logs but first we need to be prepared for the worst."', 'preperation')
                    ])

                # ------------------------ Role based Decsions -------------------------------------------
                if self.role == 'NF':
                    self.create_space_radio([
                        ('Command Deck, "You\'re right, Jenkins. The Command Deck is where we can get the most up-to-date information. It\'s also the place where we can come together as a team. Everyone needs to feel like we\'re in this together. Let\'s unite the crew and focus on what\'s next."', 'unity'),
                        ('Comm Station, "I agree, Jenkins. We need everyone on the same page. If we\'re going to face whatever comes next, we need to keep the lines open and get a plan together. It\'s not just about information, it\'s about **communicating** and **connecting** with everyone involved."', 'communication')
                    ])
                elif self.role == 'NT':
                    self.create_space_radio([
                        ('Command Deck, "We need to consolidate our resources and take a strategic position. If the other ship is a threat, we need to stay one step ahead. Jenkins, I know it\'s difficult, but we need precise focus from everyone—this could be our best chance to get ahead."', 'analysis'),
                        ('Comm Station, "Exactly. Understanding the bigger picture is crucial. Comms will give us the most direct access to enemy intentions and external communications. We can use this to figure out their next move and prepare to meet them, wherever that may be."', 'communication')
                    ])
                elif self.role == 'SP':
                    self.create_space_radio([
                        ('Comm Station, "We need to get to the Comm Station. Let\'s get everyone on the same page and see if we can make a quick assessment of the situation."', 'communication'),
                        ('Command Deck, "Forget the comms, we need to head straight to the Command Deck. We can\'t waste time—we need all hands on deck for whatever comes next."', 'unity')
                    ])
                elif self.role == 'SJ':
                    self.create_space_radio([
                        ('Command Deck, "We need to go to the Command Deck immediately. I want a full report on the situation from everyone. We need to take control of this."', 'leadership'),
                        ('Telecommunications Array, "We should hit the Telecommunications Array first. We might be able to cross-reference the ship\'s data and figure out what they want from us."', 'research')
                    ])


    def on_next(self):
        choice = self.stage  # Get the current selected choice value
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()

        # Clear the list of current radio buttons
        self.radio_buttons.clear()

        if self.character_data.get('Setting') == 'space':
            if choice == 'intro':
                self.stage = 'first'
                self.space_intro_label.pack_forget()  # Hide intro label
                self.first_label()  # Update to 'first' step

            elif choice == 'first':
                self.stage = 'second'
                self.space_first_label.pack_forget()
                self.second_label()
            
    


# Main program execution
if __name__ == "__main__":
    terminal_game()