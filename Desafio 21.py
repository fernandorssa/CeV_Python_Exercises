from pygame import mixer

file = 'Desafio 21.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()
input()
