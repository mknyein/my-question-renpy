define e = Character("Eileen")
label start:
    scene bg room
    show eileen happy
    e "You've created a new Ren'Py game."
    e "Choose Something." # change from Myanmar font to English
    default choice_no_1 = False
    default choice_no_2 = False 
    default choice_no_3 = False 
    default is_click_all_choices = False 
    menu choose_something:
        "It's No 1.":
            e "Wow. You chose the lable no 1."
            $ choice_no_1 = True # change to 'True'
            jump checking_all_choices
        "It's No 2.":
            e "Wow. You chose the lable no 2."
            $ choice_no_2 = True # change to 'True'
            jump checking_all_choices
        "It's No 3.":
            e "Wow. You chose the lable no 3."
            $ choice_no_3 = True # change to 'True'
            jump checking_all_choices
        "Go to ending":
            jump ending
        label checking_all_choices:
            if choice_no_1 == True and choice_no_2 == True and choice_no_3 == True:
                $ is_click_all_choices = True
                jump ending
            else:
                jump choose_something
        label ending:
             if is_click_all_choices == True:
                 "You click all the choices"
        "Good job!!!"
    return