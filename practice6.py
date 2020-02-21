vocabulary = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"} 
def ask_user(vocabulary):
    
    while True:
        user_say = input("задайте свой вопрос: ")
        for key in list(vocabulary.keys()):
            if user_say == key:
                print(vocabulary[key])
                break
        else: 
            print("я не знаю ответ на этот вопрос")
                
ask_user(vocabulary)
#print(vocabulary.keys(0))        