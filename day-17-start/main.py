from question_model import Question
from data import question_data 
from quiz_brain import Brain

question_bank = [] 

for item in question_data:
   question = item.get("text")
   ans = item.get( "answer")
   new_Q = Question(question, ans )
   question_bank.append(new_Q)

quiz = Brain(question_bank)

while(quiz.still_has_questions()):
   quiz.next_question()





#-----------------Without creating multiple methods for QUIZ_BRAIN.----------------------------
# right_count = 0
# wrong_count = 0

# for object in question_bank:
#    ans = object.answer
#    userAns = input(object.text + "\nTrue or False: ")

#    if(ans.lower() == userAns.lower()):
#       print("Correct!\n")
#       right_count+=1 
#    else: 
#       print("That is the wrong answer\n")
#       wrong_count+=1

# print("Out of "  + str(right_count + wrong_count) + f" questions you got {right_count} correct. " 
#       + str((right_count / (right_count + wrong_count)) * 100) +"%")