define e = Character("Eileen")
label start:
    scene bg room
    show eileen happy
    e "You've created a new Ren'Py game."
    e "Choose Something." # change from Myanmar font to English
    default choice_no_1 = False # add 'False' value to variable choice_no_1
    menu choose_something: # add choose_something label
        "It's No 1.":
            e "Wow. You chose the lable no 1."
            $ choice_no_1 = True # change to 'True'
            jump choose_something
        "It's No 2.":
            e "Wow. You chose the lable no 2."
            jump choose_something
        "It's No 3.":
            e "Wow. You chose the lable no 3."
            jump choose_something
        "Go to ending":
            jump ending
    label ending:
        if choice_no_1 == True:
            "You chose No. 1 lable, right?"
        "Good job!!!"
    return