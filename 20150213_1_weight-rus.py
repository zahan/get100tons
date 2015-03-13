def idealWeight(x, sex): #Определяем функцию для расчета идеального веса 
    if sex == 'муж':
        return (x - 100) - (x - 170) / 2 # Если выбрали "М" то счтиаем по формуле
    elif sex == 'жен':
        return (x - 100) - (x - 150) / 2 # Если выбрали "Ж" то по другой формуле


choice = input('Хотите узнать свой идеальный вес? да/нет\n') # Вообще не нужен вопрос, но можно записать тех кто не хочет сотрудничать



while choice == 'да': #Если выбрали да то запускаем калькулятор
    pol = input('Выберите Ваш пол муж/жен\n')
    yourWeight = int(input('Введите ваш текущий вес в "кг"\n'))
        
    if pol == 'жен': #Если выбрали женщину то считаем по формуле 1
            currentHeight = int(input("Введите свой рост в 'см'\n")) 
            calc = int(idealWeight(currentHeight, pol)) #Отправляем текущий рост и пол в функцию ИдеальныйВес считаем идеальный вес
            rekomend = yourWeight - calc #Вычисляем рекомендуемый вес вычитаем из того что ввели в начеле идеальный
            print ("Ваш идеальный вес %d," %calc)
            if rekomend < 0: 
                plusRec = abs(rekomend) #Если рекомендация со знаком минус то убираем его с помощью модуля, хотя можно умножить на -1
                print('Вам нужно набрать %d' %plusRec)
            else: print('Вам нужно сбросить %d' %rekomend)
            
            name = input('Введите Ваше имя\n')
            print('Всего доброго %s' %name)
            
            forLog = open('log.txt', 'a') #Открываем файл лог для добавления строк
            forLog.write(name + ' - ' + str(yourWeight) + ' - ' + str(calc) + ' - ' + str(rekomend) + '\n' )
            forLog.close() # Выше формируем нужную запись и закрываем документ тем самым сохраняя его
            
            toStart = input('Поробовать еще? да/нет\n') #Спрашиваем хочет ли человек попробовать еще
            if toStart == 'да':
                print('Начнем сначала') #Если да то програма просто возращается к началу цикла
            elif toStart == 'нет':
                print('Программа завершена') #Если нет то обрываем цикл
                break
            
    elif pol == 'муж': #Если выбрали мужчину то считаем по формуле 2
            currentHeight = int(input("Введите свой рост в см\n"))
            calc = int(idealWeight(currentHeight, pol))
            rekomend = yourWeight - calc
            print ("Ваш идеальный вес %d" %calc)
            if rekomend < 0:
                plusRec = abs(rekomend)
                print('Вам нужно набрать %d' %plusRec)
            else: print('Вам нужно сбросить %d' %rekomend)
            
            name = input('Введите Ваше имя\n')
            print('Всего доброго %s' %name)
            forLog = open('log.txt', 'a')
            forLog.write(name + ' - ' + str(yourWeight) + ' - ' + str(calc) + ' - ' + str(rekomend) + '\n' )
            forLog.close()
            
            toStart = input('Поробовать еще? да/нет\n')
            if toStart == 'да':
                print('Начнем сначала')
            elif toStart == 'нет':
                print('Программа завершена')
                break

    else: print('НЕВЕРНОЕ ЗНАЧЕНИЕ. Введите значение "жен" или "муж"')

if choice == 'нет': #Если пользователь отвечает нет в начале програмы
    name = input('Введите Ваше имя\n')
    print('Всего доброго %s' %name)
    forLog = open('log.txt', 'a')#Открываем файл лог для добавления строк
    forLog.write(name + ' - Отказался сотрудничать с администрацией\n')
    forLog.close()# Выше формируем нужную запись и закрываем документ тем самым сохраняя его
    print('Программа завершена')
    
else:
    print('Неверно!')
    print('Программа завершена!')
    

