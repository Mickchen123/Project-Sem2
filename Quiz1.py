questions = ["1) Which of the following is a bird?\na) Dog\nb) Cat\nc) Sparrow\nd) Fish",
             "2) Which animal is known as the 'King of the Jungle'?\na) Lion\nb) Tiger\nc) Elephant\nd) Giraffe",
             "3) Which of these animals can live both on land and in water?\na) Cow\nb) Frog\nc) Horse\nd) Sheep",
             "4) Which animal has a long neck?\na) Rabbit\nb) Camel\nc) Kangaroo\nd) Giraffe",
             "5) Which of these is a nocturnal animal?\na) Eagle\nb) Owl\nc) Duck\nd) Pigeon"]
answers = ["c", "a", "b", "d", "b"]
score = 0

for i in range(len(questions)):
    user_answer = input(questions[i]).strip().lower()
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print("\nQuiz completed!")
print(f"You got {score}/{len(questions)} questions correct.")
