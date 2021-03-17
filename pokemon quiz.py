#This is a quiz on first generation pokemon games (red/blue/yellow)

class Question: #we create and class called question so that we can input several types of data as one item
    def __init__(self, prompt, answer): #we set the values of the object as prompt and answer
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "How many pokemon are there in gen 1?\n(a) 150\n(b) 160\n(c) 151\n(d) 161\n\n",
    "What pokedex number is Venusaur?\n(a) #11\n(b) #6\n(c) #3\n(d) #7\n\n",
    "Who is the gym leader in Cerulean City?\n(a) Brock\n(b) Erika\n(c) Koga\n(d) Misty\n\n",
    "What badge do you get from Blaine?\n(a) Marsh Badge\n(b) Volcano Badge\n(c) Boulder Badge\n(d) Rainbow Badge\n\n",
    "What type is Scyther?\n(a) Bug/Flying\n(b) Grass\n(c) Bug/Grass\n(d) Bug\n\n",
    "How is Nidorina evolved into Nidoqueen?\n(a) Reach level 35\n(b) Trade\n(c) Reach level 40\n(d) Moon Stone\n\n",
    "Which pokemon is exclusive to Pokemon Red?\n(a) Sandshrew\n(b) Mankey\n(c) Ekans\n(d) Psyduck\n\n",
    "What item is used to activate elevators in the Rocket Hideout?\n(a) Secret Key\n(b) Card Key\n(c) Lift Key\n(d) Coin\n\n",
    "Which pokemon has the highest base speed?\n(a) Arbok\n(b) Fearow\n(c) Pidgeot\n(d) Butterfree\n\n",
    "Which pokemon is only female?\n(a) Jigglypuff\n(b) Ninetails\n(c) Rapidash\n(d) Kangaskhan\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "d"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "d")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Hello, Trainer! You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
