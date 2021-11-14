import random
import numpy



def randomNum(amount, minRange, maxRange):

    result=[]

    

    for i in range(amount):

        temp = random.randint(minRange, maxRange)

        result.append(temp)

    

    return result





amount = int(input('How many numbers generate list ? '))

minRange = int(input('Starting Range of the random Number ? '))

maxRange = int(input('End range of the random Number ? '))



print('Generated list :{0}' .format(randomNum(amount, minRange, maxRange)))


