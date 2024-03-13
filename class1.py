class livingthings:
    is_alive = True
    type = None
    is_alive = True
    strenght = 50


    def die(self):
        self.is_alive = False
    def eat(self, food):

        food.die()
        self.strenght += food.strenght
        food.strenght = 0

    def __init__(self, type, strenght):
        self.type = type
        self.strenght = strenght
class Bird(livingthings):
    is_flying = False
    def fly(self):
        self.is_flying = True
    def stop_flying(self):
        self.is_flying = False
        print("Flying")
        print(bird.is_alive)

class chicken(Bird):    
    pass


    

bird = Bird("Bird", 50)
human = livingthings("human", 100)
horse = livingthings("horse", 40)
chicken = chicken("chicken", 60)
cow = livingthings("cow", 40)
print(human.type, horse.type, cow.type)
print(bird.is_alive)
chicken

# print (type(human))
# print(human.is_alive)

# human.die()
# print(human.is_alive)

# horse.die
# print(horse.is_alive)
print(human.is_alive, horse.is_alive, cow.is_alive)
print(human.strenght, horse.strenght, cow.strenght)

cow.eat(horse)

print(human.is_alive, horse.is_alive, cow.is_alive)
print(human.strenght, horse.strenght, cow.strenght)

human.eat(cow)
print(human.is_alive, horse.is_alive, cow.is_alive)
print(human.strenght, horse.strenght, cow.strenght)


