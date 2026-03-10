# Quiz game


questions = ("no. of elements?",
             "no. of f1 teams?",
             "how many planets in solar system?",
             "why is venus so hot?")
options = (("A. 114", "B. 115", "C. 116", "D. 118"),
           ("A. 12", "B. 13", "C. 21", "D. 22"),
           ("A. 8", "B. 9", "C. 10", "D. 6"),
           ("A. idk", "B. ik", "C. maybe because of the sun?", "D. none of the above"))



answers = ("D", "D", "A", "D")
guesses = []
score = 0
question_num = 0


for question in questions:
    print()
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input ("Enter (A, B, C, D): ").upper()
    guesses.append(guess)   
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")

    else:
        print("INCORECT!")
        print(f"{answers[question_num]} is correct.")
    question_num += 1   

print(" ----------------------- ")
print(" RESULTS ")
print(" ----------------------- ")

print("Answer: ", end = " ")  
for answer in answers:
    print(answer, end=" ")
print()

print ("guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print ()

score = int(score/len(questions)*100)
print(f"YOUR SCORE IS: {score}%")