weight = 24 
totalCounter = 0

while True:
        choice = input('Ввести подход? y/n\n')
        if choice == 'y':
               currentReps = int(input('Введите количество повторений'))
               totalCounter += currentReps

               currentTotalWeight = currentReps * weight
               totalCounterWeight = totalCounter * weight

               print('В этом подъеме Вы подняли %d кг' %currentTotalWeight)
               print('Всего подянто %d кг' %totalCounterWeight)
               
        



"""
while choice == 'да': 
    numberOfreps = int(input('Введите количество повторов \n'))
        
    calc = int(totalWeight(weight, numberOfreps)) 
    print ("В этом подходе вы подняли %d, кг." %calc)
    
    forLog = open('log.txt', 'a') 
    forLog.write(str(calc) + '\n')
    forLog.close() 
                
else:
    print('Неверно!')
    print('Программа завершена!')
"""
    

