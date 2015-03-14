def totalWeight(weight, times): 
        return weight * times 

weight = 24
choice = input('Ввести подход? да/нет\n') 
totalCounter = 0


while choice == 'да': #Если выбрали да то запускаем калькулятор
    numberOfreps = int(input('Введите количество повторов \n'))
        
    calc = int(totalWeight(weight, numberOfreps)) 
    print ("В этом подходе вы подняли %d, кг." %calc)
    
    forLog = open('log.txt', 'a') 
    forLog.write(str(calc))
    forLog.close() 
                
else:
    print('Неверно!')
    print('Программа завершена!')
    

