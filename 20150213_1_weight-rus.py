import datetime

nowDate = datetime.date.today()
print ('Сегодня ' + str(nowDate))

for line in open("journal.txt", "r"):
        last_line = line
print('На прошлой тренировке Вы подняли ' + str(last_line[-6:-1]))

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

    

