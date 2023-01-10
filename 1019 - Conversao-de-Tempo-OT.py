import math
seconds = int(input())


def convertion(seconds):
    hours = seconds // 3600 # Uma hora tem 3600 segundos
    rest = seconds % 3600
    minutes = rest // 60 # Um minuto tem sessenta segundos
    seconds = rest % 60
    print(f'{hours}:{minutes}:{seconds}')


convertion(seconds)