a = input('Введите свой возраст (количество полных лет):')
age = int(a)
def purpose(age):
    if 0 <= age <= 2  :
        return "Ты только родился: наслаждайся!"
    elif  3 <= age <= 6: 
        return "Время детского сада"
    elif 7<= age <= 16: 
        return "Золотая школьная пора" 
    elif 17<= age <=22:
        return "Увлекательные студенческие годы"
    elif 23<= age <=65:    
        return "Кризис среднего возраста не за горами: пора на работу"
    else: 
        return "Наконец возраст дожития и дачных каникул!"    
your_purpose = purpose(age)
print(your_purpose)         

                
