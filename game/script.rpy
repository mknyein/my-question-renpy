define e = Character("Eileen")
label start:
    scene bg cave
    with fade
    show eileen happy
    with dissolve
    e "We are in the cave. Lets get out of here."
    e "Choose the place you want to go."
    default choice_washington = False
    default choice_whitehouse = False 
    default is_click_all_choices = False
    menu choose_something:
        "Washington.":
            scene bg washington
            show eileen vhappy
            with dissolve
            e "Washington! It is a good idea."
            $ choice_washington = True # change to 'True'
            jump checking_all_choices
        "Let's go Whitehouse":
            scene bg whitehouse
            show eileen vhappy
            with dissolve
            e "Whitehouse! Yay"
            $ choice_whitehouse = True # change to 'True'
            jump checking_all_choices
        "Go to ending":
            jump ending
    label checking_all_choices:
        if choice_washington==True and choice_whitehouse==True:
            $ is_click_all_choices = True
            jump ending
        else:
            jump choose_something
    label ending:
        if is_click_all_choices == True:
            e "Finally, we went to Washington."
            e "We also visited the whitehouse."
            "Good Ending."
        else:
            show eileen concerned
            with dissolve
            e "I want to visit all places."
            "Bad Ending."
    return