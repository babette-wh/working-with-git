import random




def randomNum(amount, minRange, maxRange):

    result=[]

    

    for i in range(amount):

        temp = random.randint(minRange, maxRange)

        result.append(temp)

    

    return result

#Three Inputs with amount,minRange,maxRange
amount = int(input('How many numbers generate list ? '))

minRange = int(input('Starting Range of the random Number ? '))

maxRange = int(input('End range of the random Number ? '))


#print the random Numbers
print('Generated list with all Random Numbers :{0}' .format(randomNum(amount, minRange, maxRange)))


