class Brain: 
    def __init__(self, question_List) -> None:
        self.question_num = 0 
        self.score = 0 
        self.question_list = question_List
    

    def still_has_questions(self) ->bool: 
        return self.question_num < len(self.question_list) 
    

    def next_question(self) -> str:
        index_num = self.question_num 

        curr_question = self.question_list[index_num]
        self.question_num+=1 
        user_ans = input("Q." + str(self.question_num ) + f": {curr_question.text}" + "\nTrue or False: " )
        self.check_answer(user_ans, curr_question.answer)


    def check_answer(self, user_in, correct_ans):
        if(user_in.lower() == correct_ans.lower()):
            self.score+=1
            print("Correct")
        else:
            print("Incorrect\n") 

        print(f"Your current score is : {self.score} / {self.question_num}\n")


        if(self.still_has_questions() == False): 
          print("Out of "  + str(len(self.question_list)) + f" questions you got {self.score} correct. " 
                + str(  int((self.score / (len(self.question_list) * 100))) )  +"%")