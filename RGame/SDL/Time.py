# Imports
from RGame.SDL.Exceptions import RG_FileExistsWarning
from RGame.SDL.Log import Log, LogLevel
# End Imports

from ctypes import *
import time



class RG_Counter:
    
    def __init__(self, trigger, recurring = False) -> None:
        self._trigger = trigger;
        self._recurring = recurring;
        self._count = 0;
        pass
    
    @property
    def Finished():
        pass;
    
    @Finished.getter
    def Finished(self):
        if(self._count == -1):return False;
        
        self._count += 1;
        
        if(self._count == self._trigger): 
            
            if(not self._recurring): 
                self._count = -1;
                return True;
            
            self._count = 0;
            return True;
        
        return False; 
           
    pass;

class RG_Timer:
    def __init__(self,mainScript, done = None, trigger:int = 1) -> None:
        self.Done = done;
        self.MainScript = mainScript;
        self._trigger = trigger;
        self.Count = 0
        self._id = 0
        pass
    
    def Tick(self,deltaTime):
        self.Count += deltaTime * self.MainScript.MainPhysics.Interval;
        if(self.Count >= self._trigger and self.Done != None):
            self.Done();
            self.UnSubscribe()
        pass;
    
    def Reset(self):
        self.Count = 0
        pass;
    
    def Subscribe(self):
        self.MainScript.MainPhysics.Add(self);
        pass;
    
    def UnSubscribe(self):
        self.MainScript.MainPhysics.Remove(self);
        del self;
        pass;
    
    pass;


def IsDefined():
    global py
    try:
        a = py
    except:
        return False
    return True

def TimeInit():
    if(IsDefined()):
        return
    global tim;
    global py;
    try:
        from pathlib import Path
        dllPath = Path(__file__).parent / "\\RGame\\Time.dll"
        tim = cdll.LoadLibrary(dllPath)
        tim.Pause.argtypes = [c_double];
        #tim.PauseUntil.argtypes = [c_void_p]
        tim.Del_CRG_TimePoint.argtypes = [c_void_p]
        tim.CRG_TimePoint_Difference.argtypes = [c_void_p,c_void_p]
        tim.CRG_TimePoint_Difference.restype = c_double
        tim.CRG_TimePoint_Increament.argtypes = [c_void_p,c_double]
        tim.CRG_TimePoint_Decreament.argtypes = [c_void_p,c_double]
        tim.CRG_Now.restype = c_void_p
        py = False
    except Exception as e:
        tim = None
        py = True
        switchWarning = RG_FileExistsWarning(*e.args, "The Time.dll could not be loaded so automatically switching form C++ to Python code for time module")
        Log(switchWarning.Message, switchWarning.Value, LogLevel.WARNING)
    pass;


def Pause(length):
    global tim;
    global py;
    if(length <= 0):return;
    if(py):
        time.sleep(length)
        return
    tim.Pause(length);
    pass;


class RG_TimePoint:
    Tis = None
    pTis = None
    def Now(self):
        if not (IsDefined()):
            TimeInit()
        global tim
        global py
        if(py):
            self.pTis = time.perf_counter_ns()/1000000000
            return
        self.Tis = tim.CRG_Now()
        
    def Diff(self):
        global tim
        global py
        if(py): return time.perf_counter_ns()/1000000000 - self.pTis
        return tim.CRG_TimePoint_Difference(tim.CRG_Now(), self.Tis)
    
    def __init__(self):
        self.Now()
    
    def __del__(self):
        global tim
        global py
        if(py):return
        tim.Del_CRG_TimePoint(self.Tis)
        
    def __sub__(self, other):
        global tim
        global py
        if(py):
            if(other is RG_TimePoint):
                return self.pTis - other.pTis
            self.pTis -= other
            return
        if(other is RG_TimePoint):
            return tim.CRG_TimePoint_Difference(self.Tis, other.Tis)
        tim.CRG_TimePoint_Decreament(self.Tis, other)
        
    def __add__(self, other):
        global tim
        global py
        if(py):
            self.pTis += other
            return
        tim.CRG_TimePoint_Increament(self.Tis, other)