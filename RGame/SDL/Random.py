import random;

#Random
def RandomInt(min:int = 0, max:int = 100):
    random.seed();
    return random.randint(min,max);

def RandomFloat(min:int = -1, max:int = 1):
    random.seed();
    if(min < 0 and max > 0):
        val = random.random() * 2 -1;
    elif(max < 1):
        val = random.random() * -1;
    else:
        val = random.random();
    if(not(min < -1 or max > 1)): return val;
    intval = RandomInt(min,max);
    return intval + val;