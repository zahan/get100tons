#Get100tons Трейнинг ситэмс %)

#Блок содания даты
import datetime
nowDate = datetime.date.today() #Получаем сегоднящнюю дату без времени
print ('Сегодня ' + str(nowDate)) #Выводим ее на экран

#Блок рекомендованного веса
for line in open("journal.txt", "r"): #Открываем журнал тренировок и ищем в нем последнюю строку неведомым способом
        last_line = line
lastWeight = last_line[-7:-3] #Находим с помощью среза в последей строке вес
rekomendWeight = int(lastWeight) * 1.2 #Переводим его в число и умножаем на 20%
print('На прошлой тренировке Вы подняли ' + str(last_line[-7:-1]))
print('Рекомендуемый вес на этой тренировке ' + str(rekomendWeight))

forLog = open('journal.txt', 'a') # Открываем журнал для записи
forLog.write('\n' + '=' * 23 + '\n' + 'Тренировка от ' + str(nowDate) + '\n' + '=' * 23 + '\n')

weight = 24 #Вес отягощения
totalCounter = 0

setCounter = 0

while True:
        choice = input('Ввести подход? y/n\n')
        if choice == 'y':
               currentReps = int(input('Введите количество повторений \n'))
               totalCounter += currentReps

               currentTotalWeight = currentReps * weight #Вес поднятый в текущем подходе
               totalCounterWeight = totalCounter * weight #Вес поднятых за все тренировку

               setCounter += int(1) #Записываем номер подхода

               print('В этом подъеме Вы подняли %d кг' %currentTotalWeight)
               print('Всего подянто %d кг' %totalCounterWeight)

               forLog.write('Подход №' + str(setCounter) + '; ' + 'Вес' + ' - ' + str(currentTotalWeight) + 'кг' + '\n') #Записываем каждый подход в журнал

        elif choice == 'n':
               forLog.write('=' * 23 + '\n' + 'Суммарный вес - ' + str(totalCounterWeight) + 'кг' + '\n') #Записываем в журнал суммарный вес за треню
               forLog.close()

               print('Тренировка закончена. Вы подняли %d кг' %totalCounterWeight)
               break

        else:
                print ('Введите корректное значение "у" или "n"')

    

