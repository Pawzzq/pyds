import numpy as np

def random_predict(number:int=1) -> int:
    """ Guess a number

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: number of attempts
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
        if number == predict_number:
            break # out from cycle
    return(count)

print(f'Number of attempts: {random_predict()}')

def score_game(random_predict) -> int:
    """How many attempts in average

    Args:
        random_predict ([type]): Guess function

    Returns:
        int: Attempts count
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Your algorithm find the number in {score} attempts')
    return(score)

# RUN
score_game(random_predict)