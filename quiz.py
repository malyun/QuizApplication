import sys;
import json;

print("*** Quiz ***\n")
name = raw_input("Please enter your name:").title()
print()

mammal_questions = 'Mammal Questions'
random_questions = 'Random Questions'
math_questions = 'Math Questions'

questions = [mammal_questions,random_questions,math_questions]


quiz = {mammal_questions: [("The baby of a cat is called a kitten", True),
                        ("wolves walk in a pack", True),
                        ("All men are animals", False)],

        random_questions: [("johanessbourg is the capital city of south africa", True),
                         ("My favourite color is orange", True),
                         ("Nimbus is a type of star", False)],

        math_questions: [("1+1 = 3", False),
                     ("the square root of 81 is 9", True),]
}


result = {"Correct": 0, "Incorrect": 0}

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(raw_input(
                'Choose the quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(mammal_questions,
                                                                                          random_questions,
                                                                                          math_questions)))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print "Invalid value, please try again\n"
            else:
                return quiz_number


def is_answer(question, correct_answer):
    while True:
        try:
            print "Q: {}".format(question)
            answer = int(raw_input("1 for True\n0 for False\nYour answer: "))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if answer is not 0 and answer is not 1:
                print "Invalid value, please try again\n"
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False


choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print "\nYou chose the {}\n".format(quiz_name)
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    print "Your answer is: {}\n".format(str(is_answer(q[0], q[1])))



question1 = "Where is andela located at?"
options1 = "a.githurai\nb. kawangware\nc. karen\nd. Kilimani\n"
print(question1)
print(options1)

while True:
    response = raw_input("Hit a, b, c or d for your answer\n")

    if response == "d":
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = raw_input("Hit a, b, c or d for your answer\n")

            if response == "d":
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break

# DO the same for the next questions of your round (copy-paste-copy-paste).
# At the end of the round, paste the following code for the bonus question.

# Now the program will ask the user to go for the bonus question or not

while True:
    bonus = raw_input("Would you like to try another question?\nHit y for yes and n for no.\n")

    if bonus == 'y':
        print("Who discovered gravity?")
        print("a. Me\nb. His Mother\nc. Isaak Newton\nd. Aliens")

        while True:
            response = raw_input("Hit a, b, c or d for your answer\n")

            if response == "c":
                stop = True
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = raw_input("Hit a, b, c or d for your answer\n")


                if response == "c":
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus =="n":
        break
    else:
        print("INVALID INPUT!!! Only hit y or n for your response")
print "Well Done, Please continue"

def questions(quiz):
    for q,a in quiz.items():
        if raw_input(q).lower() == a.lower():
            score += 1
            print("Correct.")
        else:
            print("Sorry, correct answer is \"{}\".".format(a))
        # return score
def main():
    qs = {"What's the capital of Kenya? ":"Nairobi",
    "Who is the king of the North in \"game of thrones\"? ":"Jon Snow",
    "Who is spongebob's bestfriend? ": "Patrick",
    "What is Andela's slogan ":"TIA",
    "Who is the president of \"USA\"? ": "Donald Trump",
   }
    
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(qs), len(qs)))
 
def quiz(qs):
    # """Returns a score. Asks questions from qs dictionary."""
    score = 0;
    # Use the .items() method to get the key / value pairs.
    for q,a in qs.items():
        if raw_input(q).lower() == a.lower():
            score += 1
            print("Correct.")
        else:
            print("Sorry, correct answer is \"{}\".".format(a))
            
    print score


if __name__ == "__main__":    
        main()
