define e = Character("Eileen")
label start:
    scene bg room
    show eileen happy
    e "You've created a new Ren'Py game."
    e "Choose Something." # change from Myanmar font to English

    menu choose_something: # add choose_something label
        "It's No 1.":
            e "Wow. You chose the lable no 1."
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
        "Good job!!!"
    return