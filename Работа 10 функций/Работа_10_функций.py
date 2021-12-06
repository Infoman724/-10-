word="python"
word_list=list(word)
print("наше слово",word)
print("наше слово в виде списка",word_list)
while True:
    print("1- функция isdigit-Состоит ли строка из цифр")
    print("2- функция isalpha-Состоитли строка из букв")
    print("3- функция isalnum()-Состоит ли строка из цифр или букв")
    print("4- функция istitle()-Начинается ли строка с заглавной буквы")
    print("5- фунцкия upper()-Преобразование строки к верхнему регистру")
    print("6- фунцкия lower()-Преобразование строки к нижнему регистру")
    print("7- фунцкия capitalize()-Переводит первый символ строки в верхний регистр, а все остальные в нижний")
    print("8- фунцкия len()-Длина строки")
    print("9- фунцкия isspace()- Состоит ли строка из неотображаемых символов")
    print("10- фунцкия startswith(str)-Начинается ли строка S с шаблона str")
    var=int(input())
    if var==1:
      print("ответ на isdigit",word.isdigit())
    elif var==2:
        print("ответ на isaplha",word.isalpha())
    elif var==3:
        print("ответ на isalnum",word.isalnum())
    elif var==4:
        print("ответ на istitle",word.istitle())
    elif var==5:
        print("отевет на upper",word.upper())
    elif var==6:
        print("отевет на lower",word.lower())
    elif var==7:
        print("отевет на capitalize",word.capitalize())
    elif var==8:
        print("длина строки=)",len(word))
    elif var==9:
        print("отевет на isspace",word.isspace())
    elif var==10:
        print("отевет на startswith(str)",word.startswith())
    


