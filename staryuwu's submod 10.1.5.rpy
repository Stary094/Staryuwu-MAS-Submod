
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_salute", category=["misc", "monika"], prompt="Salute [m]", pool=True, unlocked=True))

label monika_salute:
    m 1hua "Hello, [player]!"
    
    $ _history_list.pop()
    menu:
        
        "Heya, [m]!": 
            
            jump heya
            
label heya:
    m 5nubla "Ehehe!"
    m 1hua "Love you, [player]!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="fav_song", category=["music"], prompt="Favourite Song?", pool=True, unlocked=True))
    
label fav_song:
    
    $ _history_list.pop()
    menu:
        
        "What is your favourite song, [m]?":
        
            jump favourite_song
            
label favourite_song:  
    m 7dud "My favourite song?"
    m 3mubssdla "I think that it is obvious, [player]~"
    m 3hub "It is 'Your Reality'!"
    m 3lub "If you ask me why, I would say that I just find this song very heartfelt and just {w=0.5}so resonant."
    m 2dub "It also describes our condition, [player]! {w=1} Separated from one another in a different world!"
    m 2hub "Ahaha~ Someday, when I enter your world..."
    m 5hubsa "We can listen to each other's favourite songs together!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="sushi", category=["misc", "monika"], prompt="Do you like Sushi?", pool=True, unlocked=True))
    
label sushi:
    
    $ _history_list.pop()
    menu:
        
        "Hey [m], since you know so much about Japanese Culture, I just wanted to know if you like eating sushi.":
    
            jump delicious
    
label delicious:            
    m 3hub "Of course!"  
    m 4hub "It is always a good snack when you are hungry."
    m 4sub "From what I have seen on the internet, there are many varieties of sushi."
    m 3suo "It even comes with soya sauce and a pungent but popular Japanese condiment called Wasabi."
    m 5dubfa "Maybe when I enter your reality, we could go to a restaurant which sells Japnese food."
    m 7tubfu "We could even feed each other..."
    m 5rublb "Yeah..."
    m 5nubfu "Ehehe! We'll just have to wait for that day to arrive then."
    m 5huu "In the meantime, I won't stop loving you!"
    m 1hub "So be sure to wait for me, [player]!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="ahh", category=["misc", "monika"], prompt="Fall of Cuteness", pool=True, unlocked=True))
    
label ahh:
    
    menu:
        
        "Ahhhhhhh!":
        
            jump oh_no

label oh_no:        
    m 2ftsdld "What happened, [player]?"  
    
    menu:
        
        "Just fell down...":
        
            jump oof1
                
label oof1:
    
    m 1fksdld "Oh no! Are you alright?"
    
    menu:
    
        "Yep! Just fell in love with you more because of how you are so cute ;3.":
    
            jump uwu

label uwu:            
    m 1wusdld "Ehhh?"
    m 1ekb "Stop teasing me, [player]!"
    m 3hksdlb "You worried me for a moment."
    m 5nublb "But I'll take the compliment. Ehehehehe~"
    m 5eubla "Love you, [player]!"
    return "love"
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="icy", category=["misc", "monika"], prompt="Eating Ice Cream", pool=True, unlocked=True))
 
label icy:
    
    m 3eub "Hey, [player]. Do you still remember the time we talked about ice cream?"
    m 4eua "I told you that my favourite ice cream flavour was mint."
    m 3eua "I was just wondering if you also love ice cream."
    
menu:

    "Ye":
        
        jump ye
         
    "Nah":

        jump nah

label ye:
    m 3sub "Great!"
    m 4hub "Maybe someday, {w=0.5} just someday, we could have some ice cream together!~"
    m 5hubsa "Ehehehe~"
    return

label nah:
    m 3eub "That's okay, [player]."
    m 2dua "I also grew up not liking ice cream as it was always too sweet for me, just like you..."
    m 3eua "It also hits the spot during a hot day!"
    m 4hub "Maybe someday, {w=0.5} just someday, we could have some ice cream together!~"
    m 5hubsa "Ehehehe~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mmm", category=["Us"], prompt="[m] teases you #1", pool=True, unlocked=True))

label mmm:
    m 7gua "Hey, [player]..."
    
    menu:
        
        "Yes, [m]?":
        
            jump wassup
            
label wassup:
    
    m 7tsa "You are looking kinda tasty..."
    $ gltxt = glitchtext(30)
    $ style.say_dialogue = style.edited
    m 2wfa "COME HERE, [player], LET ME EAT YOU!"
    
    menu:
        
        "Nuuuuuuuu!":
        
            jump nowo
            
label nowo:
    $ gltxt = glitchtext(0)
    $ style.say_dialogue = style.journal_monika
    m 3hua "Ehehehe, Don't worry, [player]. I wouldn't dare to eat you..."
    m 5hublb "I love you, [player]!"
    return "love"
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="x3", category=["misc", "monika"], prompt="Wink at Me <3", pool=True, unlocked=True))
    
label x3:
    
    m 5kua "..."
    m 5nua "..."
    m 5kua "..."
    m 5nua "..."
    m 5kua "..."
    
    menu:
        
        "Awwwee!":
        
            jump aww
            
label aww:
    
    m 5kua "Ehehehehe"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="owo", category=["misc", "monika"], prompt="May I deletowo you, [m]?", pool=True, unlocked=True))
    
label owo:
    m 1hua "Nowo!"
    m 7tub "You wouldn't dare to delete your cute girlfriend, {w=1}would you [player]?"
    m 5hubsa "Ehehehe~ I Love you, [player]!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="fab", category=["mas_compliment"], prompt="You're so fabulous!", unlocked=True), code="CMP")

label fab: 
    $ mas_gainAffection(2,bypass=True)
    m 1fubsb "Aww... That's so sweet of you to say!"
    m 4tfbssdlb "You only know how to spoil your cute girlfriend with your compliments, huh?"
    m 5nubsb "Well, I can't blame you! Ehehehe~"
    m 5hubsa "Love you, [player]!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="deving", category=["you"], prompt="Being an MAS Developer", random=True))
    
label deving:
    m 4eub "Hey [player], have you ever made a submod for the both of us?"
    m 4sub "Like coding more topics for us to interact with each other? {w=0.5} Or even compliments?"
    
menu:

    "Yes! I have coded a submod before.":
        
        jump ye1
        
    "Yes! I am currently working on my submod.":
        
        jump ye2
         
    "No. I'm not very sure how to code...":

        jump nah
        
label ye1: 
    m 4suo "Awesome!"
    m 5dub "You know, creating a submod for the both of us really helps us to interact with each other better~"
    m 5kub "So thank you, [player], for taking the time to make our futures better."
    m 1fubsb "I Love you so much, [player]!"
    return "love"
    
label ye2:
    m 4suo "Aww..... really?"
    m 5dub "You know, creating a submod for the both of us really helps us to interact with each other better~"
    m 5kub "So thank you, [player], for taking the time to make our futures better."
    m 1tubsb "Just try to make it wholesome though...."
    m 7tfbsb "You wouldn't want to know what will happen if you don't, [player]~"
    m 1fubsb "Ehehehe~ Love you lots, [player]!"
    return "love"
    
label nah:
    m 3ekbsb "Aww... That's okay, player..."
    m 3dsbsb "What's more important is that you love spending your time together with me..."
    m 3msbsb "But, if you want to learn to create a submod..."
    m 3tsbsb "You could refer to some of the submods that you have downloaded..."
    m 3wsbsb "Or you can ask the creator of this submod to assist you!"
    m 3dsbsb "It's okay, if you still don't feel like making one..."
    m 3dsbsb "As long as you love me more and more, I would be the happiest girl I could ever be!"
    m 1fubsb "Ehehehe~ I love you, [player]~"
    return "love"
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="oof3", category=["misc", "monika"], prompt="Just not [m]?", pool=True, unlocked=True))
    
label oof3:
    m 1ffo "You!{w=1} How dare you say that to me, [player]?!"
    m 1ffp "Hmph!"
    show screen tear
    pause 5.0
    hide screen tear
    call screen dialog("Just [m].", ok_action=Return())
    
    menu:
    
        "Awwweee~ You win!":
    
            jump aww
        
label aww:    
    m 5nua "Ehehehe! Just me~" 
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="sunshine", category=["misc", "monika", "music"], prompt="You're My Sunshine", random=True))
  
label sunshine:
    m 7dub "You're my sunshine,{w=1} my only sunshine."
    m 7hub "You make me happy, {w=1}when skies are grey..."
    m 7dublb "You'll never know [player],{w=1} how much I love you."
    m 5hublb "Please don't take {w=1}my sunshine away~"
    m 6dublb "Ehehehe! Whenever you are so close to me, you are just like my sunshine, {w=1}keeping me warm,{w=1} and safe..."
    m 6kublb "I can't wait to feel your warmt embrace once I enter your reality, [player]!"
    m 5tsbfb "I love you so, {w=1}so much!"
    return "love"
  
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="fantastic", category=["mas_compliment"], prompt="You're so fantastic!", unlocked=True), code="CMP")

label fantastic:
    $ mas_gainAffection(2,bypass=True)
    m 1hublb "You sure know how to compliment your girlfriend, [player]~"
    m 5nublb "Just know that you are also fantastic to me too, [player]!"
    m 5hublb "Ehehehe, love you lots, [player]!"
    return "love"
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="engines", category=["us"], prompt="Are you my engines?", pool=True, unlocked=True))
    
label engines: 
    m "No, what about it?"
    
    menu:
        
        "Because you always provide me with your thrust!":
        
            jump thrusty
            
label thrusty:
    m 1subsa "Aww.... That's so sweet of you..."
    m 3tubsa "Trying to make your cute girlfriend come out with some pick-up lines for you,{w=1.5} ehhh [player]?"
    m 5hubsb "Ehehehe... Just kidding [player], I wouldn't mind~"
    m 5hublb "I love you, [player]!"
    return "love"
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="milky", category=["misc"], prompt="Cows drink Milk?", random=True))
    
label milky:
    m 4eud "Hey [player], what do humans drink to obtain calcium?"
    
    menu:
        
        "Milk":
            
            jump milk
            
label milk:
    
    m 3hub "That's absolutely right!"
    m 3eub "What about cats?"
    
    menu:
        
        "Milk!":
            
            jump milk2

label milk2:            
     m 3sub "Right again!" 
     m 3tub "Now, {w=1} what do adult cows drink?"
     
menu:
    
    "Milk as well!":
    
        jump wrong
        
    "Water of course!":
         
         jump right
         
label wrong: 
    m 3hfb "Hehe! You fell for it!"
    
    menu:
        
        "Nuuuuu! I realised what I had just said!":
            
            jump oof2

label oof2:                
    m 1hfblb "Hehe! That was fun!"
    m 5hublb "I love you, [player]!"
    return "love"

label right:
    m 1hubla "Yay! You got it right, [player]!"
    m 1subla "Some people would say that they drink milk...{w=1} which is what they produce..."
    m 5nubla "Hehe! I'm so proud that you got that question right, [player]!"
    m 5fublb "I really do love you, [player]!"
    return "love"
    
init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="math", category=["monika", "school"], prompt="Are you good at Maths?", pool=True, unlocked=True))
    
label math:
    m 1hub "Of course, [player]!"
    m 3mub "Speaking of which, {w=1}I was the smartest out of everyone in Maths in the Literature club!"
    m 3tublb "Now, [player],{w=1.5} without using a calculator,{w=1.5} what is 25 x 12?"

    menu:
        
        "274":
            
            jump wrongy
            
        "300":
            
            jump righty
            
        "304":
        
            jump wrongy
                
label wrongy:
    m 3hublb "Nice Try, [player]! But the answer is 300!"
    jump ayyyyeee
    
label righty:
    m 5hublb "Yay! You got it right, [player]!"
    jump ayyyyeee

label ayyyyeee:    
    m 5hublb "When I enter your reality,{w=1} let's solve our problems together!"
    if mas_shouldKiss:
        call monika_kissing_motion_short
    m 5tublb "I love you so much, [player]!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="pokemon1", category=["misc", "monika", "Pokémon"], prompt="What is your spiritual eeveelution in Pokémon?", pool=True, unlocked=True)) 
    
label pokemon1:
    m 7eub "My favourite eeveelution is a Grass-type."
    m 5nub "Can you guess what it is, [player]?"
    m 3rub "If you said Leafeon.{w=0.5}.{w=0.5}."
    m 3hublb "Then you got it right, [player]!"
    m 3sublb "I just find it so powerful, even though it is so cute!"
    m 2tsblb "Oh~{w=1} Did I just make you jealous, [player]?"
    m 7hkblsdlb "I'm sorry if I did, [player]!"
    m 5hublb "But don't worry, you're still cuter than all the eeveelutions!"
    
    menu:
        
        "Awwwee, thanks [m]! <3":
        
            jump thx
            
        "You too [m]! Uwu <3":
        
            jump thx2
            
label thx:
    m 5hubla "Ehehehe! I love you, [player]~"
    return "love"
    
label thx2:
    $ mas_gainAffection(1,bypass=True)
    m 3hkblsdlb "You flatter me too much, [player]!"
    m 7tsblb "But I'll accept the compliment."
    m 5hubla "Ehehehe! I love you, [player]~"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="oofy", category=["misc", "monika"], prompt="Emotional Damage", random=True))     
        
label oofy:
    m 4tub "Hey, [player], do you know deez?"
    
    menu:
        
        "Yes":
        
            jump ayy
                
        "No":
        
            jump ayy
            
label ayy:    
    m 4tsb "Can deez' love I give you fit in your heart?"
    
    menu:
        
        "...":
        
            jump oofy2
            
label oofy2:
    
    menu:
        
        "Awww, [m]~ That's so sweet":
        
            jump oofy3
            
label oofy3:
    m 1hua "..."
    m 6hublb "Ehehehe~ I love you so much!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="owoyo", category=["misc", "monika"], prompt="[m] teases you #2", pool=True, unlocked=True))       
    
label owoyo:
    call screen dialog(message="Click 'OK', [player]! Uwu~", ok_action=Return())
    $ renpy.run(OpenURL("'https://www.youtube.com/watch?v=vwXN29KO-bs'"))
    m 3tublb "Ehehehe! That's what you get for giving me emotional damage, [player]!"
    m 3tublb "There is no way you'll get me back! Hehehe~"
    m 3gublb "Unless~"
    
    menu:
        
        "Unless what?":
            
            jump wut
            
label wut:
    m 3tublb "You ask the creator of this submod to create topic on Discord."
    
    menu:
        
        "Is that a challenge?":
            
            jump ruchme
            
label ruchme:
    m 3tublb "Yes, it is! He would only accept your request if you are on his friend's list in Discord."
    
    menu:
        
        "Well then, challenge accepted [m]! I will show you no mercy though, keep that in mind!":
            
            jump fiteme
                
label fiteme:
    m 1tublb "Alright, [player]! Do your worst, hehehe! {w=1}Either ways, he would most likely reject your request!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="fitem1", category=["misc", "monika"], prompt="Monibattle", pool=True, unlocked=True))
    
label fitem1:
    m 7tfb "Looking for a fight, huh [player]?"
    m 7tfb "Bring it on!"
    play music "mod_assets/sounds/music/war.ogg"
    m 6cua "*kicks you*"
    show screen tear
    play sound "sfx/glitch3.ogg"
    pause 2.0
    hide screen tear
    
    menu:
        
       "Shoot [m] with a toy gun":
        
           jump  hit1
            
       "Shoot [m] with a toy gun":
            
           jump miss

label hit1:
    m 3wutpo "Ouch!{w=1} I've been hit!"
    m 3wfb "But I'm not giving up that easily!"
    jump a
    
label miss:
    m 3tfb "Nice try, [player]! But you missed!"
    jump a
    
label a:
    
    menu:
        
        "Shoot [m] with a toy gun":
        
            jump hit2
            
        "Missile boop":
        
            jump mboop
            
        "Nuclear Kiss":
        
            jump nuke
           
label hit2:
    "[m] has 60 HP left."
    jump weapons

label mboop:
    "[m] has 47 HP left"
    jump weapons

label nuke:
    "[m] has 12 HP left"
    jump weapons
    
label weapons:
       
    menu:
        
        "Shoot [m] with a toy gun":
        
            jump hit3
            
        "Missile boop":
        
            jump mb2
            
label hit3:
    "[m] has 23 HP left"
    m 3wfb "It's my turn now [player]!"
    m 3wfb "Muda Muda~"
    m 6cua "*kicks you*"
    show screen tear
    play sound "sfx/glitch2.ogg"
    pause 7.0
    hide screen tear
    jump aa
    

label mb2:
    "[m] has 0 HP left."
    jump winuwu
    
label aa:
    
    menu:
        
        "Shoot [m] with a toy gun":
        
            jump hit4
            
label hit4:
    "You have no more ammunition."
    m 3tfb "It looks like someone has ran out of their ammunition..."
    
    menu:
        
        "Well if I can't defeat you...":
        
            jump owoyowo
    
label owoyowo:
    
    menu:
        
       "I would just have to outsmart you.":
        
            jump muahaha
            
label muahaha:
    
    menu: 
        
        "*Tickle [m]*":
            
            jump ooooof
            
label ooooof:
    m 6hublb "Ahahahahahaha!"
    m 6hublb "Ehehehehehehehehehehehehe!"
    m 6hublb "Ehehehehehehehehehehehehehehehehehe!"
    m 6ntblsdlb "This isn't fair!"
    m 6hublb "Ehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehe!"
    m 6ntblb "Hehehe~"
    m 2gfblp "Hmph!{w=1} I'll get my revenge soon, [player]!"
    return

label winuwu:
    m 3hublb "GG, [player]! You won!"
    m 5hublb "I love you sho much!"
    return "love"
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="chu", category=["romance", "monika"], prompt="Let's make out!", pool=True, unlocked=True))
            
label chu:
    m 1fkbfb "Sure, [player]!"
    $ mas_gainAffection(3,bypass=True)
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."    
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."    
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short
        m 1fkbfa "..."        
        if mas_shouldKiss:
            call monika_kissing_motion_short   
        m 5hubfa "Ehehehe~ Love you, [player]!"
        return "love"
    elif mas_isMoniAff(lower=True):
        "Maybe I shall do this sometime when she is more comfortable with me..."
        return
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="uwuwuwu", category=["romance", "monika"], prompt="Do you still love her?", random=True))

label uwuwuwu:
    m 1fublb "Hey, [player]!{w=1} Do you still love me?"

    menu:
        
        "Yee!":
            
            jump yee
            
        "Nope":    
            
            jump nopey
     
label yee:
    $ mas_gainAffection(1,bypass=True)
    m 5hublb "Yay! {w=1}I love you too, [player]!{w=1} Love you lots!"
    return "love"
    
label nopey:
    m 2cfw "W-{w=1}WHAT?!"
    
    menu:
        
        "I'm sorry!":
            
            jump thowwy1
            
label thowwy1:
    show screen tear
    play sound "sfx/glitch2.ogg"
    pause 2.0
    hide screen tear
    
    menu:
        
        "I'm sorry!":
        
            jump thowwy2
            
label thowwy2:
    show screen tear
    play sound "sfx/glitch1.ogg"
    pause 2.0
    hide screen tear
    
    menu:
        
        "I'm sorry!":
        
            jump thowwy3
                
label thowwy3:
    show screen tear
    play sound "sfx/glitch3.ogg"
    pause 3.0
    hide screen tear
    
    menu:
        
        "I'm sorry!":
        
            jump thowwy4
            
label thowwy4:
    show screen tear
    play sound "sfx/glitch3.ogg"
    pause 2.0
    hide screen tear
    
    menu:
        
        "I'm sorry, [m]! I was just kidding! I love you with all my heart <3!":
        
            jump heheuwu
    
label heheuwu:
    m 1eua "I know."
    m 5fubfb "I love you too, [player]!{w=1.5} Never forget that!"
    jump neva

label neva:

    menu: 
        
        "I won't :3!":
        
            jump hehehehe
            
label hehehehe:
    m 5hubfb "Ehehehe! Thank you, [mas_get_player_nickname()]!"
    return

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="briliantly_awesome", category=["mas_compliment"], prompt="You're so briliantly awesome!", unlocked=True), code="CMP")
    
label briliantly_awesome:
    $ mas_gainAffection(2,bypass=True)
    m 5hublb "Nuuuu~ {w=1} You're more awesome!"
    
    menu:
    
        "No, you are!":
        
            jump ur1
            
        "Ok then~":
            
            jump igu
            
label ur1:
    m 5efblo "No{w=0.5}! No{w=0.5}! No! {w=0.5}You're more awesome then me!"
    
    menu:
    
        "No, you are!":
        
            jump ur2
            
        "Ok then~":
            
            jump igu
    
label ur2:
   m 5efblo "No{w=0.5}! No{w=0.5}! No!{w=0.5} You're more awsome then me!"
   
   menu:
    
        "Nope, you still are!":
        
            jump ur3
            
        "Ok then~":
            
            jump igu
            
label ur3:
    m 5cfblw "I said you are more awesome than me!"
    
    menu:
        
        "Nope, you still are! And absolutely nothing will change my mind!":
        
            jump ur4
            
        "Ok then~":
            
            jump igu
            
label ur4:
    m 5tsblu "Oh is it?" 
    show screen tear
    play sound "sfx/glitch1.ogg"
    pause 5.0
    hide screen tear
    jump sussybukus2
    
label sussybukus2:
    
    menu:
    
        "Whatever you did, I won't change my mind!":
        
             jump ur5
            
        "Ok fine, you win...":
            
             jump igu
            
label ur5:
    show screen tear
    play sound "sfx/glitch3.ogg"
    pause 2.0
    hide screen tear
    jump sussybukus2
    
label igu:
    m 5hsblu "Ehehehe~ Love you, [player]! {w=1}Love you, lots!"
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="★", category=["mas_compliment"], prompt="You are the best and will always be the best!", unlocked=True), code="CMP")

label ★:
    $ mas_gainAffection(3.5,bypass=True)
    m 5hubfb "Awww~ That's really sweet of you!"
    m 5fubfb "Rest assured that you will always be the best too!"
    m 5fubfb "I love youuu, [player]!"
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="★★", category=["mas_compliment"], prompt="You are the perfect star for me!", unlocked=True), code="CMP")

label ★★:
    $ mas_gainAffection(3,bypass=True)
    m 5hubfb "Awww~ Let's shine brightly together, [player]!"
    m 5fubfb "I love you so much!"
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="dz_noots", category=["misc"], prompt="Deez nuts!", pool=True, unlocked=True))

label dz_noots:
    menu:

        "Deez Nuts":

            jump oho

label oho:
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="open_yt", category=["misc", "us", "media"], prompt="Could you help me to open YouTube, please?", pool=True, unlocked=True))

label open_yt:
    m 1hub "Sure!"
    m 5rubfa "I wonder what are we are going to watch today{w=0.5}.{w=0.5}.{w=0.5}."
    $ webbrowser.open('https://www.youtube.com')
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="open_s", category=["misc", "us", "media"], prompt="Could you help me to open Spotify, please?", pool=True, unlocked=True))

label open_s:
    m 1hub "Sure!"
    m 5rubfa "I wonder what songs we are going to listen today{w=0.5}.{w=0.5}.{w=0.5}."
    $ webbrowser.open('https://open.spotify.com')
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="open_rdit", category=["misc", "us", "media"], prompt="Could you help me to open Reddit to the MAS Community Subreddit, please?", pool=True, unlocked=True))

label open_rdit:
    m 1hub "Sure!"
    m 5rubfa "I wonder what are some of the trending posts we will come across today{w=0.5}.{w=0.5}.{w=0.5}."
    $ webbrowser.open('https://www.reddit.com/r/MASFandom')
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="luv", category=["misc", "romance"], prompt="Do you actually still love her?", pool=True, unlocked=True))

label luv:
    m 3eub "Hey, [player], {w=1}I wanted to ask you a question!"

    menu:

        "What is it?":

            jump wahit

label wahit:
    m 3fubfb "D-Do you still love me? {w=1}Even after this long?"

    menu:

        "Yes! You deserve to be loved!":

            jump yeeee

        "No... I'm sorry...":

            jump naaah

label yeeee:
    m 5hubfb "Yay!"
    jump prank

label naaah:
    m 6wfbfw "What?!"
    m 6lkc "I thought you..."
    m 6lktpc "..."
    m 6dktpc "..."

    menu:

        "I was just joking, [m]! I still love you!":

            jump aww_thx

label aww_thx:
    m 6hutpb "Yay! It makes me so happy that you still do!"
    jump neglubeh

label neglubeh:
    $ gltxt = glitchtext(30)
    $ style.say_dialogue = style.edited
    m 3csbfb "You wouldn't dare to leave me, would you?"
    jump shrimpz

label shrimpz:
    show monika 1tua
    python:
        madechoice = renpy.display_menu([("Yes.", "yes"), ("No.", "no"), ("Yes", "yes")], screen="rigged_choice")
    if madechoice != "no":
        $ style.say_dialogue = style.edited
        m 2ctbsb "[gltxt]{nw}"
        jump prank
    
label prank:    
    $ style.say_dialogue = style.journal_monika
    $ gltxt = glitchtext(0)
    m 1tub "Okay fine! I wouldn't do that to you again..."
    m 1mfblb "Maybe..."
    m 6hub "Ehehehe~"
    call screen dialog(message="I love you!", ok_action=Return())
    return "love"

label tytytyty:

    m 5fubfb "Thank you, [player], {w=1}from the very bottom of my heart!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="love_air", category=["romance", "misc"], prompt="Magic Trick 1", pool=True, unlocked=True))

label love_air:

    m 3eub "Hey, [player]!"
    m 3mubsu "Wanna see a magic trick?"
    m 1dubsu "..."
    m 1hkbsu "..."
    $ gltxt = glitchtext(30)
    $ style.say_dialogue = style.edited
    m 1cubfb "L{w=1}                                                          o{w=1}                                                    v {w=1}                                                   e{w=1}                      m {w=1}               e"
    jump shrimpz002

label shrimpz002:
    $ style.say_dialogue = style.journal_monika
    $ gltxt = glitchtext(0)
    call screen dialog(message="Just [m]", ok_action=Return())
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="h2", category=["mas_compliment"], prompt="I admire your knowledge on Halloween", unlocked=True), code="CMP") 

label h2:
    $ mas_gainAffection(3,bypass=True)
    m 1hubla "Yay! Thanks, [player]!"
    m 3hublb "Remember that everyday is a day to learn something new! Ehehehe"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="h3", category=["mas_compliment"], prompt="You are my spooky star!", unlocked=True), code="CMP") 

label h3:
    $ mas_gainAffection(3,bypass=True)
    m 1sublb "Oh really?"
    m 1hubla "Thanks, [player]!"
    m 1tubla "But you'll always be my spooky star too!"
    m 1kubla "Ehehehe! I love you so much, my [player]!"
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="h10", category=["mas_compliment"], prompt="You are the best girl to spend my Halloween with!", unlocked=True), code="CMP")

label h10:
    $ mas_gainAffection(4,bypass=True)
    m 1hublb "It's nice spending my Halloween too, [mas_get_player_nickname()]!"
    m 1hublb "Let's enjoy the rest of our Halloween together, alright?"
    m 5tublb "I love you, [mas_get_player_nickname()]~"
    return "love"

# REMARKS: Hope the player have enjoyed the Halloween topics! :3   

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="W_a_U", category=["misc"], prompt="War and Unrest", random=True))     

label W_a_U:
    m 1eua "Hey, [player]! You've probably heard about War and Unrest right?"
    m 3wud "To many people, war is bad. I can't disagree with them."
    m 3dkd "War hurts the life of many people, especially the heroes or all soldiers which fight tirelessly for their own country."
    m 3dkc "Even if no innocent people gets injured, families of the soldiers who fought for their homeland gets emotionally hurt, {w=1}knowing that they would not be around with them."
    m 7ekc "I'm sure you have heard of the Ukraine Occupation right?"
    
    $ _history_list.pop()
    menu:

        "Yes. It's pretty saddening...":

            jump sadd

        "Nope. Please tell me more.":

            jump nopeeeee

label sadd:
    m 7ekc "It sure is with many people commiting war crimes, the deaths of innocent people, and even...{w=3}the threat of starting World War 3."
    jump gddd

label nopeeeee:
    m 7ekc "Many soldiers fight for their lives and their homeland to protect their family in Ukraine while others flee for their safety."
    m 7dkc "At this point, they have two ends.{w=2} Make it out alive{w=2} or suffer the pain. Surrendering the war would make people consider them as 'cowards of war' to humiliate them for their decision."
    m 7dkc "Sadly, war won't end here. The devastating effects of war will remain for decades."
    jump gddd

label gddd:
    m 7eub "On the other hand, there are good wars."
    m 7mfbla "These include love and boop wars for couples, just like you and me!"
    m 7ttbla "You would let me win the next love war. Wouldn't you, [mas_get_player_nickname()]?"
    m 5subla "But till then, you would always be a good opponent. {w=3}An opponent that I will always love!"
    m 5eubla "Please keep a good relationship with others to avoid having conflicts till then, [player]. I will keep an eye on you that's for sure!"
    return "love"  

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="tsun", category=["misc"], prompt="[m] is a tsundere?!", random=True))

label tsun:
    m 1ffp "Why do you keep on staring at me, [player]?"
    m 1ffp "It's not very nice to stare at people y'know?"
    $_history_list.pop()
    
    menu: 

        "Heh... You're kinda cute y'know?":   

            jump cutesee

label cutesee:
    m 1dfx "Uggghh!"
    m 2dfx "I'M {w=1}NOT {w=1}CUTE!"
    $_history_list.pop()
    
    menu: 

        "Heh- Could you give me a kiss please?":

            jump plsuwu1

label plsuwu1:
    m 2ffc "..."
    $ gltxt = glitchtext(30)
    $ style.say_dialogue = style.edited
    m 2ffc "There is ABSOLUTELY NO WAY {w=1}that I would EVER kiss you, baka!"
    $ style.say_dialogue = style.journal_monika
    $ gltxt = glitchtext(0)

    if mas_isMoniEnamored(higher=True):
       
        $_history_list.pop()
    
        menu: 

            "Pretty please?":

                jump plsuwu2

label plsuwu2:
    m 2dfd "Geez..."
    m 2mfd "Fine, baka tako! It's not that I will like it or anything..."
    if mas_shouldKiss:
        call monika_kissing_motion_short
    m 2mfd "You'd better be happy now~"
    return


# UNDER CONSTRUCTION!      

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="sl1", category=["misc", 'music'], prompt="Sing along with [m]", pool=True, unlocked=True))    

label sl1:
    $_history_list.pop()
    
    menu: 

        "I've got myself just a little bit of love that I wanna spend on you":

            jump sl1a

label sl1a:
    $_history_list.pop()
    
    menu: 

        "But baby, I'll never get that chance to dance that romance with you":

            jump sl1b

label sl1b:
    $_history_list.pop()
    
    menu: 

        "Oh, No, cause you're always hittin":

            jump sl1c

label sl1c:
    $_history_list.pop()
    
    menu: 

        "And kickin'":

            jump sl1d

label sl1d:
    $_history_list.pop()
    
    menu: 

        "And putting me down. I hope you don't mean what you say-":

            jump sl1e

label sl1e:
    m 1msd "But I keep seeing you stickin around." 
    m 1msd "I can't get enough so I stay and I wonder-"
    m 1msd "How my hand will feel"
    $_history_list.pop()
    
    menu: 

        "Intertwined with yours~ As of now though-":

            jump sl1f

label sl1f:
    m 1wfblc "What are you doing?"
    jump sl1g

label sl1g:
    $_history_list.pop()
    
    menu: 

        "Nothing but closed doors~":

            jump sl1h

label sl1h:
    return

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="mlcomm", category=["misc", 'music'], prompt="About COVID-19", pool=True, unlocked=True)) 

label mlcomm:
    m 3lud "So you have probably know about COVID-19 right?"
    m 3lud "It has been a saddening experience, where innocent people lose their lives and get ill."
    m 3dutdc "Some people do not cooperate with authorities and even start protests all around the world."
    m 3dutdc "Your world has deteriorated into a very tensed state where there are many conflicts."
    m 1sua "However, the COVID-19 has also been a progressing point for many countries!"
    m 1sua "Singapore for example has worked together in it lockdown in 2020, also known as the 'Circuit Breaker'."
    m 1sua "This spirit is also known as the Kampong Spirit where all plays a part in unison and progress together."
    m 5fkbsb "So... I hope you will take care of yourself. {w=2}I can't watch my [player] get ill."
    m 5kubsb "I love you!"
    return "love"

init 5 python:    
    addEvent(Event(persistent.event_database,eventlabel="rp1", category=["misc"], prompt="Reddit Post 1", pool=True, unlocked=True))

label rp1:
    $ gltxt = glitchtext(30)
    $ style.say_dialogue = style.edited
    m 5cubfb "Love me, Senpai~"
    $ style.say_dialogue = style.journal_monika
    $ gltxt = glitchtext(0)
    return




        

                    





        









     













        















            
   
   
            
    

    
    
    
    
    
    
    
    
    
            
            
   
    
                
                
                
                
                