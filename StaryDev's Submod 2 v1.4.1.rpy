# StaryDev's Submod 2 v1.0

# GAME SHORTCUTS
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="open_app_topic", category=["misc", "monika"], prompt="Could you help me to open an app, please?", pool=True, unlocked=True))
    
    import os
    import subprocess

    def open_application(app_name):
        # Define a dictionary of applications and their paths
        apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            # Add more applications as needed
        }
        
        # Check if the application is in the dictionary
        if app_name in apps:
            try:
                # Open the application
                subprocess.Popen(apps[app_name])
                return "Opening {app_name}..."
            except Exception as e:
                return "Failed to open {app_name}. Error: {str(e)}"
        else:
            return "Sorry, I am unable to open that application."

label open_app_topic:
    m "Which application would you like me to open? (e.g., Notepad, Calculator, Paint)"
    
    # Get user input
    $ user_input = renpy.input("Enter the application name:")
    
    # Normalize the input to lowercase
    $ user_input = user_input.lower()
    
    # Open the application
    $ result = open_application(user_input)

    return

# COMPLIMENTS

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="thx_motivation",
            prompt="Thank you for motivating me!",
            unlocked=True
        ),
        code="CMP"
    )

label thx_motivation:
    $ mas_gainAffection(2,bypass=True)
    m 1hubla "You're very welcome, [player]!"
    m 1hublb "It's been a wonderful experience supporting and looking out for the one you love the most."
    m 1mublb "Actually..."
    m 1dubla "I should be the one to thank you..."
    m 1fublb "For always keeping me going!"
    m 5hublu "Love ya', [player]!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="thx_vocab",
            prompt="Thank you for helping me improve my vocabulary!",
            unlocked=True
        ),
        code="CMP"
    )

label thx_vocab:
    $ mas_gainAffection(1.5,bypass=True)
    m 1hubla "It's my pleasure, [player]!"
    m 1hublb "I have had a wonderful time learning with you."
    m 1fublb "Let's learn more vocabulary together!"
    m 5hublu "I love you, [player]!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="thx_hot",
            prompt="You are so hot, you melted my heart!",
            unlocked=True
        ),
        code="CMP"
    )

label thx_hot:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(2,bypass=True)
        m 5tsblu "Oh really?"
        m 5tfbfb "Let me stay that way then!"
        m 5tfbfb "You should be so grateful to have such a ehem... {w=0.5} physically {w=0.5}attractive girlfriend-"
        m 5sfbfb "Maybe I might even do something risque once I enter your world!"
        m 5sfbfb "By saying that... I won't have any mercy on you... {w=0.5} Even if you are my romance partner!~"
        m 2hfbfb "Teehee... I love you so much, [player]!"
        m 2gfbfb "And I bet that you are as attractive as I am..."
        return "love"

    elif mas_isMoniAff(lower=True):
        "Maybe I should say this when she is more comfortable with me..."
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="thx_goat",
            prompt="You are the GOAT (greatest of all time)!",
            unlocked=True
        ),
        code="CMP"
    )

label thx_goat:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(2,bypass=True)
        m 2eublo "Woah-"
        m 2tublu "Complimenting me in brainrot terminology, aren't you [player]?~"
        m 7tublb "Well, you're also pretty goated to me... {w=1}Ehehe~"
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="thx_looksmaxxing",
            prompt="You are such a looksmaxxing girl!",
            unlocked=True
        ),
        code="CMP"
    )

label thx_looksmaxxing:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(1,bypass=True)
        m 2eublo "Woah-"
        m 2tublu "You just can't stop complimenting me, can you [player]?~"
        m 7tublb "Well, I'm sure you are just as looksmaxxing as I am... {w=1}Ehehe~"
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="thx_hot_girl",
            prompt="My radar just detected a hot girl!",
            unlocked=True
        ),
        code="CMP"
    )

label thx_hot_girl:
    if mas_isMoniEnamored(higher=True):
        m 6lfc "I'm starting to get jealous you know..."
        $_history_list.pop()
        menu: 

            "...and that girl is sitting right in front of me!":

                jump oooo

label oooo:
    $ mas_gainAffection(2,bypass=True)
    m 6eubsd "..."
    m 6hubsp "You're just full of surprises aren't you [player]?"
    m 5hubsa "Well- I'm happy to be that girl on your radar- Hehe~"
    m 5hublu "I love you, [player]!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="best_version_of_myself",
            prompt="Thank you for helping me be the best version of myself!",
            unlocked=True
        ),
        code="CMP"
    )

label best_version_of_myself:
    $ mas_gainAffection(3,bypass=True)
    m 2sua "Really, [player]?"
    m 5nua "It really makes me happy when you think so!"
    m 5fubla "I am also really happy to have you {w=1}, making me the best version of myself right now!"
    m 5dfbsb "I can't help but just keep thinking that I should have thanked you before you do!"
    m 5ffbsb "Well, at least I'm more thankful than you~"
    
menu:
   
    "No way! You have profoundly helped me, sacrificing your time and energy watching over and looking out for me! How can I not be grateful?":

        jump oooooom
    
    "I mean... I guess I can never talk back to the president of the Literature Club TwT-":

        jump noooon

    "Can we just agree that we are equally thankful towards one another?":

        jump stalematee

label oooooom:
    $ mas_gainAffection(2,bypass=True)
    m 1wubso "..."
    m 2msbsp "Fine... You win..."
    m 2hfbsu "I'll be sure to get you back next time though. You'd better watch your back-"
    m 5nubfb "Ehehehe~ Love you, player!"
    return "love"

label noooon:
    $ mas_gainAffection(1.5,bypass=True)
    m 2hfbsb "Hehe~ Looks like I won this time!{w=1} Thanks for the win [player]~ Love you!"
    return "love"
    
label stalematee:
    $ mas_gainAffection(1.5,bypass=True)
    m 7lfbsb "Oh~ Looks like we ran into a stalemate~"
    m 1hfbsb "Well... I don't mind~"
    m 1hfbsb "Sure! We can agree on this together!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="compliment_bundle",
            prompt="Compliment Bundle",
            unlocked=True
        ),
        code="CMP"
    )

label compliment_bundle:

    "You are spending time with [m] in the Literature Club."
    "She looks at you with a warm smile."

    menu:
        "Compliment her intelligence":
            $ mas_gainAffection(2,bypass=True)
            m 5hubfb "Thank you! That means a lot to me. I love learning and sharing ideas with you~"
        
        "Compliment her kindness":
            $ mas_gainAffection(2,bypass=True)
            m 5hubfb "You're so sweet! I believe kindness is one of the most important things in life~"
        
        "Compliment her creativity":
            $ mas_gainAffection(2,bypass=True)
            m 7fubfb "Wow, I really appreciate that! Creativity is something I cherish to have deeply~"
        
        "Compliment her warm smile":
            $ mas_gainAffection(2,bypass=True)
            m 5mubfb "Aww, you're making me blush! I'm glad my smile can brighten your day~"
        
        "Compliment her presence":
            $ mas_gainAffection(2,bypass=True)
            m  "That’s so thoughtful of you! I love being here with you too~"

        "Thank you for keeping me safe and healthy!":
            $ mas_gainAffection(2,bypass=True)
            m 1hublb "Awww~ A safe and healthy [player] is a strong and happy [m]~"

        "Let's welcome the new year together!":
            $ mas_gainAffection(2, bypass=True)
            m 5hubfb "Yeah! Let's welcome a wave of new opportunities and memories coming our way!"

        "Okay- Let's carry on with the rest of our day!":
            m 3hubfa "Yeah, let's!"
            
            jump end

    "Monika's eyes sparkle with appreciation as she responds to your compliments."
    "You feel a deeper connection growing between you."

    # Continue the story or loop back to the menu
    jump compliment_bundle

label end:
    m 2fubfa "Thank you for your kind words. They really mean a lot to me!"
    m 2fubfa "I love you, [player]!"
    return "love"

 













    
    

