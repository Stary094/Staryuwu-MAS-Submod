init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="stary_brb_toilet",
            category=["be right back"],
            prompt="I'm going to the toilet",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label stary_brb_toilet:
    m 1wuo "Oh!"
    m 3hua "Okay [player]! Hurry then!"
    m 1hsu "I'll see you in a bit." 

    $ mas_idle_mailbox.send_idle_cb("stary_brb_toilet_callback")
    return "idle"

label stary_brb_toilet_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "stary_brb_toilet"):
        m 1wuo "Oh! You were gone for a long time, [player]." 
        m 1hublb "But since you are back, let's enjou the rest of our day together!"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "stary_brb_toilet"):
        m 1hsb "Yay! You're back!"
        m 1gsbsa "I missed you..."
        m 1ksbsa "Let's spend more time together~"

    else:
        m 1hsbsb "Yay! Back already?"
        m 1ksbsa "Let's spend more time together then~"

    return        
