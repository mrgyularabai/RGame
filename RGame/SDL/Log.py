# Imports
from .Exceptions import*
# End Imports

from enum import Enum
import traceback

class LogLevel(Enum):
    FATAL = 5
    ERROR = 4
    WARNING = 3
    MESSAGE = 2
    DEBUG = 1
    pass

def Log(message:str, value = None, level:LogLevel = LogLevel.DEBUG):
    match level:
        case LogLevel.FATAL:
            LogFatal(message, value)
            
        case LogLevel.ERROR:
            LogError(message, value)
            
        case LogLevel.WARNING:
            LogWarning(message, value)
            
        case LogLevel.MESSAGE:
            LogMessage(message)
            
        case LogLevel.DEBUG:
            LogDebug(message, value)
        case _:
            LogMessage(message)

def LogFatal(message, value = None):
    print()
    print(f" {GetConsoleStyle(0,7,1)}>-------------------------Error-------------------------<{EndStyle()}")
    print()
    print(f" > Level: {GetConsoleStyle(0,7,1)}Fatal{EndStyle()}")
    if not (value is None):
        print(" > Value of cause: ", value)
    print(" > Message:")
    print(GetConsoleStyle(0,1,0))
    print(message + EndStyle())
    print()
    print(" > Where the problem ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,7,1)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def LogError(message, value = None):
    
    print()
    print(f" {GetConsoleStyle(0,1)}>-------------------------Error-------------------------<{EndStyle()}")
    print()
    print(f" > Level: {GetConsoleStyle(0,1)}Error{EndStyle()}")
    if not (value is None):
        print(" > Value of cause: ", value)
    print(" > Message:")
    print(GetConsoleStyle(3,1))
    print(message,EndStyle())
    print()
    print(" > Where the problem ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,1)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def LogWarning(message, value = None):
    
    print()
    print(f" {GetConsoleStyle(0,3)}>------------------------Warning------------------------<{EndStyle()}")
    print()
    print(f" > Level: {GetConsoleStyle(0,3)}Warning{EndStyle()}")
    if not (value is None):
        print(" > Value of cause: ", value)
    print(" > Message:")
    print(GetConsoleStyle(3,3))
    print(message,EndStyle())
    print()
    print(" > Where the problem ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,3)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def LogMessage(message):
    
    print()
    print(f" >------------------------Message------------------------<")
    print(" > Message:")
    print(GetConsoleStyle(3,0))
    print(message,EndStyle())
    print()
    print(" >-------------------------------------------------------<")
    print()
    
    pass


def LogDebug(message, value = None):
    
    print()
    print(f" {GetConsoleStyle(0,4)}>------------------------Debug------------------------<{EndStyle()}")
    print()
    if not (value is None):
        print(" > Value: ", value)
    print(" > Message:")
    print(GetConsoleStyle(3,4))
    print(message,EndStyle())
    print()
    print(" > Where the message ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,4)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def GetConsoleStyle(style:int = None, color:int = None, background:int = None):
    
    if (style is None):
        style = 0
    elif not (type(style) is int):
        raise RG_TypeError(style,
                             " The argument 'style' for function 'SDL.GetConsoleStyle' must only have int inputs.")
    elif (style < 0 or style > 5):
        raise RG_ValueError(style,
                             " The argument 'style' for function 'SDL.GetConsoleStyle' must only be from 0 - 5\n To see the styles available call 'PrintConsoleStyles' (any where)")
            
    if (color is None):
        color = 7
    elif not (type(color) is int):
        raise RG_TypeError(color,
                             " The argument 'color' for function 'SDL.GetConsoleStyle' must only have int inputs.")
    elif (color < 0 or color > 7):
        raise RG_ValueError(color,
                             " The argument 'color' for function 'SDL.GetConsoleStyle' must only be from 0 - 7\n To see the colors available call 'PrintConsoleStyles' (any where)")
        
    if (background is None):
        background = 0
    elif not (type(background) is int):
        raise RG_TypeError(background,
                             " The argument 'background' for function 'SDL.GetConsoleStyle' must only have int inputs.")
    elif (background < 0 or background > 7):
        raise RG_ValueError(background,
                             " The argument 'background' for function 'SDL.GetConsoleStyle' must only be from 0 - 7\n To see the background colors available call 'PrintConsoleStyles' (any where)")
    
    escape = "\033["
    color += 30
    background += 40
    return escape + str(style) + ";" + str(color) + ";" + str(background) + "m"

def EndStyle():
    return "\033[0;37;40m"

def PrintConsoleStyles():
    print(f" {GetConsoleStyle(4)}Styles:{EndStyle()}" +"        "+ f"{GetConsoleStyle(0,6)}Colors:{EndStyle()}" + "    " + f"{GetConsoleStyle(0,0,3)}Background:{EndStyle()}")
    print(EndStyle())
    print(" "+GetConsoleStyle(0)+"Normal:    0"+EndStyle() +"  "+ f"{GetConsoleStyle(0,0,7)}Black:  0{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,0)}Black:  0{EndStyle()}")
    print(" "+GetConsoleStyle(1)+"Bold:       1"+EndStyle() +"  "+ f"{GetConsoleStyle(0,1,0)}Red:    1{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,1)}Red:    1{EndStyle()}")
    print(" "+GetConsoleStyle(2)+"Light:      2"+EndStyle() +"  "+ f"{GetConsoleStyle(0,2,0)}Green:  2{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,2)}Green:  2{EndStyle()}")
    print(" "+GetConsoleStyle(3)+"Italicized: 3"+EndStyle() +"  "+ f"{GetConsoleStyle(0,3,0)}Yellow: 3{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,3)}Yellow: 3{EndStyle()}")
    print(" "+GetConsoleStyle(4)+"Underlined: 4"+EndStyle() +"  "+ f"{GetConsoleStyle(0,4,0)}Blue:   4{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,4)}Blue:   4{EndStyle()}")
    print(" "+GetConsoleStyle(5)+"Blink:      5"+EndStyle() +"  "+ f"{GetConsoleStyle(0,5,0)}Purple: 5{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,5)}Purple: 5{EndStyle()}")
    print(GetConsoleStyle(0)+"              "+EndStyle() +"  "+ f"{GetConsoleStyle(0,6,0)}Cyan:   6{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,6)}Cyan:   1{EndStyle()}")
    print(GetConsoleStyle(0)+"              "+EndStyle() +"  "+ f"{GetConsoleStyle(0,7,0)}White:  7{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,0,7)}White:  1{EndStyle()}")
    pass
