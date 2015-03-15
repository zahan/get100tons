weight = 24 
totalCounter = 0

while True:
        choice = input('Ввести подход? y/n\n')
        if choice == 'y':
               currentReps = int(input('Введите количество повторений \n'))
               totalCounter += currentReps

               currentTotalWeight = currentReps * weight
               totalCounterWeight = totalCounter * weight

               print('В этом подъеме Вы подняли %d кг' %currentTotalWeight)
               print('Всего подянто %d кг' %totalCounterWeight)

               forLog = open('journal.txt', 'a')
               forLog.write(str(currentTotalWeight) + '\n')
               forLog.close()

        elif choice == 'n':
               forLog = open('journal.txt', 'a')
               forLog.write('total - ' + str(totalCounterWeight) + '\n')
               forLog.close()

               print('Тренировка закончена. Вы подняли %d кг' %totalCounterWeight)
               break

        else:
                print ('Введите корректное значение "у" или "n"')

    

