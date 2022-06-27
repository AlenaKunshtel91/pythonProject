class Live(object):
 max_life_span = 1
is_there_food = False

def __init__(self, age):
 self.age = age

@property
def is_dead(self):
 return self.age > self.max_life_span or not self.is_there_food

def try_eating(self, is_there_food):
 self.is_there_food = is_there_food
# print the state of the living being after trying to eat
 self.print_state()

def print_state(self):
    if self.is_dead:
      print(f"{self.name()} is alive.")
    else:
      print(f"{self.name()} is dead.")

def name(self):
 return type(self).__name__


class Fox(Live):
 max_life_span = 14


class Rabbit(Live):
 max_life_span = 12


class Live(object):
    max_life_span = 1
    is_there_food = False

    def __init__(self, age: int = 0):

        # check age is valid
        if age < 0:
            raise Exception("age must be a positive number")

        self.age = age
        self.print_age()

    @property
    def is_dead(self) -> bool:
        return self.age > self.max_life_span or not self.is_there_food

    @property
    def name(self):
        return self.__class__.__name__

    def try_eating(self, is_there_food: bool = True):
        self.is_there_food = is_there_food
        # print state of a living being after trying to eat
        self.print_state()

    def print_state(self):
        if self.is_dead:
            print(f"{self.name} is dead.")
        else:
            print(f"{self.name} is alive.")

    def print_age(self):
        print(f"Age of {self.name} has been set to {self.age}")

    def print_max_life_span(self):
        print(f"Max lifespan of {self.name} is {self.max_life_span}")


class Fox(Live):
    max_life_span = 14


class Rabbit(Live):
    max_life_span = 12


class Plant(Live):
    max_life_span = 1000

    def do_absorb(self):
        """There is always sun and the plant absorbs sunlight
        """
        return self.try_eating(is_there_food=True)


plant = Plant(age=15)
rabbit = Rabbit(age=14)
fox = Fox(age=25)

plant.do_absorb()
rabbit.try_eating(is_there_food=not plant.is_dead)
fox.try_eating(is_there_food=not rabbit.is_dead)