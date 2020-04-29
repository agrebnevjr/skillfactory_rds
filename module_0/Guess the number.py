import numpy
def game_core_v2(number):
    count = 1
    lower_limit = 0
    upper_limit = 101
    predict =  round((lower_limit + upper_limit)/2)
    while number != predict:
        count+=1
        if number > predict: 
            lower_limit = predict
        elif number < predict: 
            upper_limit = predict
        predict =  round((lower_limit + upper_limit)/2)
    return(count) 


def score_game(game_core_v2):
    count_ls = []
    numpy.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = numpy.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(numpy.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2 = game_core_v2)