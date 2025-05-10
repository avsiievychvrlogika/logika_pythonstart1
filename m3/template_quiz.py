# кількість спроб
count = 0

def simple_question(question, right_answer):
    global count
    a = input(question)
    if a.lower() == right_answer.lower():
        count += 1
        print("Вірно!")
    else:
        print("Не вірно!")

def repeat_question(question, right_answer):
    a = ""
    right_answer = right_answer.lower()
    while a != right_answer:
        a = input(question)
        if a.lower() == right_answer:
            print("Вірно!")
        else:
            print("Не вірно!")
            
# перший варіант опитування
def simple_questionnaire():
    global count
    count = 0
    simple_question("Столиця України? ", "Київ")
    simple_question("Найбільша річка України? ", "Дніпро")
    simple_question("Найшвидша тварина у світі? ", "Гепард")
    simple_question("Найбільший острів у світі? ", "Гренландія")
    simple_question("Найменша пташка у світі? ", "Колібрі")

    print(f"Ви набрали {count} балів!")

# другий варіант опитування

def repeating_questionaire():
    repeat_question("Який океан є найглибшим? ", "Тихий")
    repeat_question("Яка столиця Австралії? ", "Канберра")
    repeat_question("Яка країна має найбільшу кількість населення? ", "Китай")
    repeat_question("Яке озеро є найглибшим у світі? ", "Байкал")
    repeat_question("Яка найвища гора у світі? ", "Еверест")

while True:
    print("1 - Опитування з підрахунком кількості балів")
    print("2 - Опитування з повтором питання, якщо відповідь неправильна")
    variant = input("Введіть тип опитування (1 - 2): ")

    if variant == "1":
        simple_questionnaire()
    elif variant == "2":
        repeating_questionaire()
    q = input("Чи бажаєте ви вийти? (y = True): ")
    if q.lower() == "y":
        break
