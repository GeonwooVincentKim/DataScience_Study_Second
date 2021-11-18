import enum, random


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

"""
def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])
"""
def random_kid():
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_girl = 0

# random.seed(0)

print(random_kid().value)
