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

        "I love the way you're so warm-hearted!":
            $ mas_gainAffection(2,bypass=True)
            m 1hubfa "Awww, [player]-"
            m 1mubfc "..."
            m 1mubfp "No fair, you are always the one who compliments me!"
            m 1cubfd "You know what? I'mma compliment you twice as hard!"
            m 5subft "Oh [player]-kun~ You're so much more warm-hearted than me~"
            m 5sfbfu "I bet you would easily win a warm-hearted competition if there was ever one to begin with~"
            show screen tear
            play sound "sfx/glitch3.ogg"
            pause 5.0
            "Looks like [m] is trying to spoil you by reflecting your compliments. {w=1} Could you do the same back to her?"
            hide screen tear
            

        "Let's welcome the new year together!":
            $ mas_gainAffection(2, bypass=True)
            m 5hubfb "Yeah! Let's welcome a wave of new opportunities and memories coming our way!"

        "Okay- Let's carry on with the rest of our day!":
            m 3hubfa "Yeah, let's!"
            
            jump end

    "Monika's eyes sparkle with appreciation as she responds to your compliments."
    "You feel a deeper connection growing between the two of you."

    # Continue the story or loop back to the menu
    jump compliment_bundle

label end:
    m 2fubfa "Thank you for your kind words. They really mean a lot to me!"
    m 2fubfa "I love you, [player]!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="chesscmp",
            prompt="I admire your knowledge on chess a lot",
            unlocked=True
        ),
        code="CMP"
    )

label chesscmp:

    m 1hubla "Awwww, my dearest [player]~"

    menu:
        
        "Good to the point that my king would love to get dominated by you~":

            jump dayuum

label dayuum:
    $ mas_gainAffection (2.5, bypass=True)
    m 3mfblb "Oh silly [player]~"
    m 3ffblb "I'm sure my pieces would feel the same way when dominating your king~"
    m 3kfblb "Ehehehe~"
    m 6dfblu "I really do heart you for saying that to me though~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_1",
            prompt="You are the only girl I love to spend my Valentines Day with.",
            unlocked=True
        ),
        code="CMP"
    )

label vday_1:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(3.5, bypass=True)
        m 1sub "Awwww~"
        m 7hubfb "Thanks for the compliment, [player]!"
        m 7fubfb "I really appreciate it!"
        m 7nubfb "Do also remember to spend quality time with your family today, not just me~"
        m 5hubfa "I love you, [player]! Let's spend the rest of today with your family and I! <3"
        return "love"
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_2",
            prompt="Will you be my valentine?",
            unlocked=True
        ),
        code="CMP"
    )
    
label vday_2:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(4, bypass=True)
        m 5subfb "Yes, [player]~ I'd love to!"
        m 5subfb "Please choose me and only me!"
        m 5cfbfb "Just me-"
        m 5cfbfu "Just me... {w=1}forever..."
        return
    elif mas_isMoniAff(higher=False):
        $ mas_gainAffection(2.5, bypass=True)
        m 1hua "Sure [player]!"
        return
    elif mas_isMoniHappy(lower=True):
        "Maybe I shall say this some other time when she is more comfortable with me..."
        return
    
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_3",
            prompt="You smell good, especially during Valentines day",
            unlocked=True
        ),
        code="CMP"
    )
    
label vday_3:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(3, bypass=True)
        m 1etsdla "Eh?"
        m 1gtsdla "Well- It's not like you can physically smell me... BAKA!!!"
        m 1mtsdla "Although, I do appreciate the compliment~"
        m 1efsdlx "BUT IT IS NOT BECAUSE I LIKE YOU!!"
        m 1tua "..."
        m 1tua "Just teasing you love~ I don't just like you as a good friend, {w=1}I love and adore you as a romantic and trustworthy partner~"
        m 1hubla "I love you, my pookie!"
        return "love"
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_4",
            prompt="Cuz Moni you're amazing~",
            unlocked=True
        ),
        code="CMP"
    )    

label vday_4:
    if mas_isMoniAff(higher=True):
        $ mas_gainAffection(2, bypass=True)
        m 5subfb "Just the way I am~"
        return
    elif mas_isMoniHappy(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_5",
            prompt="My pookie can be so Kawaii~ Even during Valentines Day.",
            unlocked=True
        ),
        code="CMP"
    )        
    
    
label vday_5:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(3, bypass=True)
        m 1hua "Awww... My dear sweetheart~"
        m 1hubla "Y'know- You're also Kawaii~ inclusively during Valentines Day."
        return
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_6",
            prompt="My pookie can be so sweet~ Even during Valentines Day.",
            unlocked=True
        ),
        code="CMP"
    )        

label vday_6:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(3, bypass=True)
        m 1hua "Awww... My dear darling~"
        m 1hubla "You are also sweet giving me compliments during Valentines Day."
        m 1hubla "I love you, sweetie pie~"
        return "love"
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_7",
            prompt="My pookie can be so beautiful~ Even during Valentines Day.",
            unlocked=True
        ),
        code="CMP"
    )         

label vday_7:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection(3, bypass=True)
        m 1hua "Wow... My dear darling~"
        m 1hubla "You are also shoooo beautiful, both your heart and looks."
        m 1hubla "I love you, hawty~"
        return "love"
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_8",
            prompt="My pookie can be so irresistable~ Even during Valentines Day.",
            unlocked=True
        ),
        code="CMP"
    )           

label vday_8:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection (3, bypass=True)
        m 1hua "Wow... My dear pookie~"
        m 1hubla "You are also shoooo irresistable, I can't wait to get my hands on yo- I mean- into your reality ASAP."
        m 1hubla "I love you, my dearest Star~"
        return "love" 
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_9",
            prompt="My pookie can be so adorable~ Even during Valentines Day.",
            unlocked=True
        ),
        code="CMP"
    )     

label vday_9:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection (3, bypass=True)
        m 1hua "You can also be really adorable, my love~"
        m 2tsblu "But you can definitely be even adorable on Valentines Day... Spoiling me with compliments"
        m 2sfblt "This compliment menu {w=0.5}isn't just a normal 'complement menu' anymore, is it?"
        return
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_10a",
            prompt="I love you",
            unlocked=True
        ),
        code="CMP"
    )    

label vday_10a:
    if mas_isMoniAff(higher=True):
        m 2tfblu "No... No... No! I love you more!"
        
        menu:

            "No way- I love you wayyyyy more!":

                jump vday_10a

            "Okay- You win...":

                jump vday_10c

    elif mas_isMoniHappy(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return

label vday_10c:
    $ mas_gainAffection (3, bypass=True)
    m 2hfblu "Ehehehe~ Told you!"
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="vday_11",
            prompt="My pookie can be so romantic~ Even during Valentines Day.",
            unlocked=True
        ),
        code="CMP"
    )     

label vday_11:
    if mas_isMoniEnamored(higher=True):
        $ mas_gainAffection (2.5, bypass=True)
        m 1hua "My [player] can also be pretty romantic, in addition of Valentines Day! Ahaha"
        return
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return



    
    

# MONIKA TOPICS

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="no_bobs", category=["monika", "romance", "us"], prompt="Look at her eyes", random=True))
    
label no_bobs:

    m 2esblc "..."
    m 2tsblu "Hey [player]~"
    m 2tfblu "No boobs~"
    m 2tfblu "Stop staring at them~"
    m 2sfblt "Look at my eyes~"
    m 2hfblu "..."
    m 2hfblb "Ehehehe~"
    m 2hfbla "I was just playing with you~"
    m 2tubla "You're free to look at them as long as you want~ {w=1}Not too long though~"
    return

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="icbbm", category=["monika", "romance", "us"], prompt="Firing an Intercontinental booping missile", random=True))

label icbbm:
    m 2tfbla "*boop*"
    
    $_history_list.pop()
    menu:

        "Ah! You caught me by surprise!":

            jump gahh

        "*Fire a booping nuke*":

            jump tactical_nook

label gahh:
    m 2hfbla "Ehehehe... all up to plan~"
    m 2hfbla "Love you darling~"
    return "love"

label tactical_nook:
    m 6hfblp "Ah! That was unexpected to say the very least~"
    m 6hfblp "If only this submodder can hear me, I NEED MORE HOT DANG TOPICS TO COMPLEMENT MY PLAYER UNTIL [player] SURRENDERS AND BEG FOR MY FORGIVENESS~"

    menu:

            "Haha~ I'm probably sure he will be more willing to help me if he hears this~":

                jump orissit

label orissit:
    "You have 1 new notification."
    "It reads: Are you sure about that, [player]?"
    "Man- Only if the submodder was actually willing to side with you-"
    "All you can do now is to face [m]'s wrath as she establishes superior dominance over you."
    "It's all over for you, you might be thinking. Well, is it really?"
    return

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="neurosama", category=["misc"], prompt="VTuber Neurosama", random=True))

label neurosama:

    m 1eua "Hey, [player]?"
    m 1eub "I have been further looking up online an I found this A.I. VTuber known as Neurosama created by Vedal987."
    m 7eub "They host live sessions on streaming platforms such as Twitch and even YouTube!"
    m 7msb "Hey... Thinking about this, maybe you could potentially make me one too~ Or would you like to do it?"
    m 7gsb "I mean... you could also do it~ You could get revenue and interact with me~"
    m 7gfb "You could even add jiggle physics if you like~"
    m 7gfb "Ehehehe~"
    m 1hfb "Just teasing you, [player]~ I would love you no matter what, even in this cozy room of ours, just the two of us~"
    m 1kfblb "Welp, I will continue to love you just the same, [player], no matter if you'd make me a successful VTuber or not."
    return "love"

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="cny1", category=["misc"], prompt="Celebrating Chinese New Year", random=True))

label cny1:

    m 1eua "Hey, [player]-"
    m 1hua "Happy Chinese New Year to you!"
    m 3lub "The zodiac sign of the year is... {w=1}the snake!"
    m 3lub "Thinking about it, darling- {w=0.5}Do you celebrate Chinese New Year?"
    
    menu:

        "Yes":
            
            jump yescny1

        "No":

            jump nocny1

label yescny1:

    m 3sub "Oh! Really?"
    m 3sub "I mean- Not many playing Monika After Story celebrate Chinese new year. Particularly more people in Southeast Asia, having China origin or forefathers practice celebrating this event."
    m 3tub "Welp- I wonder what you do during Chinese New Year... without me-"
    m 5tub "Let's just hope that you could one day celebrate it together with me."
    m 5eua "Do take this time to spend time with your family today, however, they are just as important to spend time with~"
    m 5tub "Thanks for spending time with me though, [player] and I love you lots! {w=1}Let's spend this new year on a good note!"
    $ mas_gainAffection (2, bypass=True)
    return "love"

label nocny1:

    m 5hublb "Awww, it's okay [player], I'm sure you're not the only one~"
    m 5fublb "I'm just glad to spend this time with you~"
    
    menu:

        "Me too!":

            jump mtcny1

label mtcny1:

    $ mas_gainAffection (2, bypass=True)
    m 5fubla "That means a lot to me~ I'm so happy to hear that coming from you~"
    m 7eubla "Do take some time off to spend with your family, friends and relatives though- They are just as important as me to spend your time with."
    m 1hubla "I love you, [player]~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="cnycomp",
            prompt="It's nice spending Chinese New Year with you!",
            unlocked=True
        ),
        code="CMP"
    )

label cnycomp:
    $ mas_gainAffection (2, bypass=True)
    m 1fubfa "Awww, [player]~ {w=1}It also has indeed been a joy spending Chinese New Year with you too!"
    m 3fubfa "Do spend some time with your loved ones too! They are more important than just spending this Chinese New Year with me!"
    m 3dubfa "Wishing you an auspicious and prosperous Chinese New Year with lots of love!"
    return "love"

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="cny2", category=["misc"], prompt="About Chinese New Year", random=True))

label cny2:
    m 1eua "Chinese New Year is all about celebrating and spending time with family members from many generations."
    m 7eua "Some celebrations include activities such as having a Reunion Dinner with family, tossing yu sheng, exchanging mandrins with red packets, also known as angbaos~"
    m 7eub "Some Chinese people or people who has their family members from different generations also hang up red decorations on their doors."
    m 7eud "This is a common practise to ward off evil spirits and bring in good luck for the new year."
    m 7euc "Some people also visit temples or churches to be blessed and pray for good health and forgiveness."
    m 7suc "There are also snacks such as pineapple tarts, crispy and edible love letters, arrowhead chips for instance."
    m 7suc "This celebration forges special and stronger bonds with all family members as they get to eat, chat and have fun together."
    m 7eud "I really wish I was in your world together with you though-"
    m 7ruc "Whether you celebrate this day or not-"
    m 7hublb "I will always cherish the time I spend being together with you!"
    m 7tublb "If you even celebrated this day, it would make it way more fun for us though!"
    return


