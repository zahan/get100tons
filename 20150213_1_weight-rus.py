import datetime

nowDate = datetime.date.today()
print (nowDate)



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

               forLog = open('journal.txt', 'a') #Записываем каждый подход в журнал
               forLog.write('Подход №' + str(setCounter) + '; ' + 'Вес' + ' - ' + str(currentTotalWeight) + '\n') 
               forLog.close()

        elif choice == 'n':
               forLog = open('journal.txt', 'a')
               forLog.write('=' * 21 + '\n' + ' - Суммарный вес - ' + str(totalCounterWeight) + '\n' + '=' * 21 + '\n') #Записываем в журнал суммарный вес за треню
               forLog.close()

               print('Тренировка закончена. Вы подняли %d кг' %totalCounterWeight)
               break

        else:
                print ('Введите корректное значение "у" или "n"')

    

