import Utils.tools
import random

questionList = Utils.tools.loadQuestionList(r"Utils\question.json")
random.shuffle(questionList)

highscore = 0
for question in questionList:
    print(question["frage"])
    Utils.tools.showChoice(question["antworten"])
    choice = int(Utils.tools.readInput
    ("Eingabe (1-4):", ["1", "2" ,"3" ,"4"]))
    if choice == question["lösung"]:
        highscore = highscore +1
        print("Die Antwort ist korrekt!")
    else: 
        print("Das war leider falsch!")

print("Du hast", highscore, "Punkte erreicht!")