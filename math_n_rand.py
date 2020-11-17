import math
import random

value = 4.35
print(math.floor(value))


random.seed(101)

print(random.randint(0,100))

mylist = list(range(0,20))

print(random.choice(mylist))

# SAMPLE WITH REPLACEMENT

print(random.choices(population=mylist,k=10))

# Sample without replacement

print(random.sample(population=mylist,k=10))