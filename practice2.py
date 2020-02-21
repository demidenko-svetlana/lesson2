def comparison(str1,str2):
    if type(str1) ==str and type(str2) ==str: 
        if str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3     
    else:
        return 0
print(comparison(1 , "kjhkjhk"))
print(comparison ('jhkjhkjh','jhoiu'))
print(comparison('yuio','learn'))
print(comparison('python','python'))