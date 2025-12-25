import random

def RGBtoColor(r:int, g:int, b:int):
    return "#%02x%02x%02x" % (r, g, b);

def RandomColor():
    random.seed()
    return "#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255));

def GetTypeStr(thing):
    return thing.__class__.__name__
    
    

