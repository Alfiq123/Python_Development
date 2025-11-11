question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# TODO: Question Model
class Question:
    def __init__(self, quest, answer):
        self.quest = quest
        self.answer = answer

question_bank = []

for data in question_data:
    setting = Question(data["text"], data["answer"])
    question_bank.append(setting)

# TODO: Quiz Brain
class QuizBrain:
    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Retrieve the current question from the question_list
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Use the input() function to show the user the Question text and ask for the user's answer
        user_answer = str(input(f"Q.{self.question_number}: {current_question.quest} (True/False): ")).lower()

        # You can add logic here to check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"🔹 Score: {self.score} / {self.question_number}\n\n")

# Example usage:
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"🔹 Your final score was {quiz.score} / {quiz.question_number}")
