# Imports
from RGame.SDL.Headers.Scripts import *
from ..SDL.Headers.PhysicsHeader import RG_Physics
from ..SDL.Time import Pause, TimeInit
from RGame.SDL.Reference import ref
# End Imports

from threading import Thread;
import time
from multiprocessing import*

class RG_PyPhysics(RG_Physics):
    _mainScript:RG_MainScript = None
    _interval:float = None
    _referenceKeeper = None
    _running:bool = False
    _counter:int = None
    _timePoint:int = None
    _waitLimit:int = None
    _failedTickCount:int = None
    _failedTickFailsafe:ref = None
    
    def __init__(self, mainScript:RG_MainScript, interval:float) -> None:
        self._mainScript = mainScript
        self._interval = interval
        self._referenceKeeper = []
        self._failedTickFailsafe = ref(3)
    
    def Start(self):
        self._pyThread = Thread(target=self.doStart)
        self._pyThread.start()
        
    def doStart(self):
        self._running = True
        self._counter = 0
        self._timePoint = time.perf_counter_ns()
        self._waitLimit = time.perf_counter_ns() - self._timePoint
        self._failedTickCount = 0
        while not self._mainScript.Started: pass
        while self._running:
            self.doTick()
    
    def doTick(self):
        self._counter += 1
        
        self._mainScript.tick(self.DeltaTime)
        for obj in self._referenceKeeper:
            obj(self.DeltaTime)
        
        self._timePoint = time.perf_counter_ns()
        if(self._interval*(1-self.DeltaTime) > self._waitLimit/1000000000) : 
            Pause(self._interval*(1-self.DeltaTime))
    
    def End(self):
        self._running = False
    
    def Add(self, script:RG_Script):
        self._referenceKeeper.append(script.Tick)
    
    def Remove(self, script):
        if(len(self._referenceKeeper) == 0): return
        self._referenceKeeper.remove(script.Tick)
    
    def Exists(self, script) -> bool:
        return 0 < self._referenceKeeper.count(script.PhysicsTick)
    
    @property
    def Interval(self) -> float:
        return self._interval
    
    @Interval.setter
    def Interval(self, newValue:float):
        self._interval = newValue
    
    @property
    def FailedTickFailsafe(self) -> int:
        return self._failedTickFailsafe.Value
    
    @FailedTickFailsafe.setter
    def FailedTickFailsafe(self, newValue:int) -> None:
        self._failedTickFailsafe.Value = newValue
    
    @property
    def Running(self) -> bool:
        return self._running
    
    @property
    def Counter(self) -> int:
        return self._counter
    
    @property
    def DeltaTime(self) -> float:
        if(self._interval == 0): return time.perf_counter_ns()-self._timePoint
        return (time.perf_counter_ns()-self._timePoint)/(self._interval*1000000000)
    
    @property
    def FailedTickCount(self) -> int:
        return self._failedTickCount
    
    @FailedTickCount.setter
    def FailedTickCount(self, newValue:int) -> int:
        self._failedTickCount = newValue
