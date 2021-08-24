define e = Character("Eileen")
label start:
  scene bg room
  show eileen happy
  e "You've created a new Ren'Py game."
  e "Once you add a story, pictures, and music, you can release it to the world!"
  e "I just add a new line ." # new line
  e "တစ်ခုခု ရွေးချယ်ပါ။"

    menu:
        "It's No 1.":
            jump label_1

        "It's No 2.":
            jump label_2
        "It's No 3.":
            jump label_3
    label label_1:
        e "Wow. You chose the lable no 1."
        jump ending

    label label_2:
        e "Wow. You chose the lable no 2."
        jump ending
    label label_3:
        e "Wow. You chose the lable no 3."
        jump ending
    label ending:
        "Good job!!!"
        
  return