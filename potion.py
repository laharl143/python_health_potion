import random

health = 50

difficulty = 1   #1 for easy, 2 for intermediate, 3 for hard

potion_health = random.randint(25,50) / difficulty

health = health + potion_health

print(health) 


