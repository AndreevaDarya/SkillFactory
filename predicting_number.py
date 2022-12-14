import random

random.seed(1)
rand_num = random.randint(1, 101)

def random_predict(num:int=1) -> int:
    """Guessing predicted number

        Args:
            num (int, optional): predicted number. Defaults to 1.

        Returns:
            int: Amount of guessing attempts
    """
    
    
    count = 0
    start = 1
    stop = 100

     
    while True:
        count += 1
        predict_num = (start + stop) // 2
        
        if predict_num == rand_num:
            #print('The number', predict_num, 'was guessed in', count, 'attempts!')
            break
        
        elif predict_num > rand_num:
            stop = predict_num
            
        else:
            start = predict_num
            
    return count



def count_attempts(random_predict) -> int:
    """Average amount of attempts to guess the number

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average number of attempts
    """
    

    attempts = []
    
    for i in range (1, 1001):   
        attempts.append(random_predict(rand_num))

    average = sum(attempts)/len(attempts)

    print('Average amount of attempts for this function is', average, '!')
    return average

print(count_attempts(random_predict))


if __name__ == '__main__':
    count_attempts(random_predict)