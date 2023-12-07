import random
import mymodule
random_int = random.randint(1,100)
print(random_int)

print(mymodule.num)

random_float = random.random()
# the .random() will only generate a random number between a 0 AND 1
print(random_float)
random_floats = random.random()
random_floate = random_floats*5
print(random_floate)