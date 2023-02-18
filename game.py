import json


with open("E:\\Hayk\\Basic IT\\Quiz Game\\questions.json", encoding="utf-8") as q:
    quest = json.load(q)

with open("E:\\Hayk\\Basic IT\\Quiz Game\\users.json", encoding="utf-8") as u:
    user = json.load(u)



#User 

n_e = input("Hello, please write your name: ")
name = n_e.upper()

for names in user:
    if name in user:
        break
    else:
        add = {name: 0}
        user.update(add)

        print("You didn't have an account, but you have successfully registered :)", "\n")

        with open("E:\\Hayk\\Basic IT\\Quiz Game\\users.json", "w") as uu:
            json.dump(user, uu, indent=2)
        break
            
right_answers = user[name]

#Choosing category

print(f"Hello {n_e.title()}, you have {right_answers} right answers, choose the category you like")

while True:
    print("""
    A: Geography 
    B: History
    """)

    categ = input("Choose: ")
    categ_upper = categ.upper()

    if categ_upper == "A" or categ_upper == "B":
        category = categ_upper

        #Starting
        if category == "A":
            print("All right, you have chosen Geography, let's go", "\n")
        elif category == "B":
            print("All right, you have chosen History, let's go", "\n")
        #Starting

        break
    else:
        print("No such category!!")

   

#Game

number = 1
stop = 0
print("Remember, if you want to stop the game, just print <<exit>>")
print("\n")


while stop == 0:
    for i in quest:

        if number == 9:
            print(f"The quiz is over {n_e.title()}, now you have {right_answers} right answers, Good luck!")
            stop += 1
            break
        
        question_number = str(number)
        print(quest[category][0][question_number]["q"])
        print("\n")
        print(quest[category][0][question_number]["A"])
        print(quest[category][0][question_number]["B"])
        print(quest[category][0][question_number]["C"])
        print("\n")

        answer = input("Your answer: ")
        print("\n")

        if answer.upper() == quest[category][0][question_number]["right"]:
            number += 1
            print("It's right!!", "\n")
            right_answers += 1
            user[name] = right_answers
            with open("E:\\Hayk\\Basic IT\\Quiz Game\\users.json", "w") as uu:
                json.dump(user, uu, indent=2)


        elif answer == "exit":
            print(f"The quiz is over {n_e.title()}, now you have {right_answers} right answers, Good luck!")
            stop += 1
            break
        else:
            print("Wrong answer!", "\n")
            number += 1

    
    
