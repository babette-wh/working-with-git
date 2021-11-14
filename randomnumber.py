import random



def randomNum(amount, minRange, maxRange):

    result=[]

    

    for i in range(amount):

        temp = random.randint(minRange, maxRange)

        result.append(temp)

    

    return result





amount = int(input('How many numbers generate list ? '))

minRange = int(input('Starting Range ? '))

maxRange = int(input('End range ? '))



print('Generated list :{0}' .format(randomNum(amount, minRange, maxRange)))
