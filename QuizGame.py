#declaring the questions
questions = ("What is the largest planet in our solar system?",
             "How many bones are there in the human body?",
             "Who wrote the play Romeo and Juliet?")

#declaring the answers
options = (("A.Earth ","B.Jupiter ", "C.Mars "),
           ("A.206 ","B.156 ", "C.302 "),
           ("A.Charles Dickens ","B.Mark Twain ", "C.William Shakespeare "))

#declaring the correct answers
answers = ("b", "a", "c")

guesess = []
score = 0

#declare index of number of questions(start with 0)
question_num = 0

#looping for questions
for question in questions:
    print("----------------------")
    print(question)
    #nested loop in question, question_num is the parameter
    for option in options[question_num]:
        print(option)
    #input the guess
    guess = input("Enter your answer (a, b, c): ").lower()
    #adding the guess into the guesses    
    guesess.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    #to make sure options tally with questions,if not add this,
    #each question will have same options which is 1st option. 
    question_num += 1

#print the total score
print("-----------------------")
print("         RESULT        ")  
print("-----------------------") 
print(f"Your total score is: {score}/3") 

#print the correct answers
print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

#print the guessed
print("guesses:", end="")
for guess in guesess:
    print(guess, end=" ")
print()