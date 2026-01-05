# Imports
from RGame.SDL.Exceptions import*
from RGame.SDL.Headers.Scripts import*
from RGame.SDL.Headers.PhysicsHeader import RG_Physics
from RGame.SDL.Reference import ref
# End Imports

from threading import Thread
from ctypes import*


class RG_CppPhysics(RG_Physics):
    _tis = None
    _scrCounter = 0
    _interval = 0
    _failedTickFailsafe = ref(3)
    _failedTickCount = 0
    _referenceKeeper = {}
    
    def __init__(self, mainScript:RG_MainScript, interval:float) -> None:
        self._mainScript = mainScript
        mainScriptTick = self._mainScript.tick
        
        self.C_Physics = cdll.LoadLibrary(__file__+"\\RGame\\Physics.dll");
        
        self._interval = interval
        
        self.MainScriptTick = CFUNCTYPE(None,c_double)(mainScriptTick);
        
        self.C_Physics.New_CRG_Physics.argtypes = [CFUNCTYPE(None,c_double),c_double,c_char_p];
        self.C_Physics.New_CRG_Physics.restype = c_void_p;
        
        self.C_Physics.Del_CRG_Physics.argtypes = [c_void_p];
        self.C_Physics.Del_CRG_Physics.restype = None;
        
        self.C_Physics.CRG_Physics_Start.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_Start.restype = None;
        
        self.C_Physics.CRG_Physics_End.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_End.restype = None;
        
        self.C_Physics.CRG_Physics_SetInterval.argtypes = [c_void_p, c_double];
        self.C_Physics.CRG_Physics_SetInterval.restype = None;
        
        self.C_Physics.CRG_Physics_Add.argtypes = [c_void_p,CFUNCTYPE(None,c_double)];
        self.C_Physics.CRG_Physics_Add.restype = None;
        
        self.C_Physics.CRG_Physics_Remove.argtypes = [c_void_p,CFUNCTYPE(None,c_double)];
        self.C_Physics.CRG_Physics_Remove.restype = None;
        
        self.C_Physics.CRG_Physics_Exists.argtypes = [c_void_p,CFUNCTYPE(None,c_double)];
        self.C_Physics.CRG_Physics_Exists.restype = c_bool;
        
        self.C_Physics.CRG_Physics_Running.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_Running.restype = c_bool;
        
        
        self.C_Physics.CRG_Physics_GetCounter.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_GetCounter.restype =  c_longlong;
        
        self.C_Physics.CRG_Physics_GetDeltaTime.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_GetDeltaTime.restype =  c_double;
        
        name = "MainPhysicsThread"
        self._tis = self.C_Physics.New_CRG_Physics(self.MainScriptTick,interval,c_char_p(name.encode('utf-8')))
        
        pass;
    
    def __del__(self):
        if(self._tis == None):return
        self.End()
        self.C_Physics.Del_CRG_Physics(self._tis)
        del self._tis
        del self._referenceKeeper
        del self.C_Physics
        
    def Start(self):
        try:
            self.t = Thread(target=self.waiter, name="PhyThread")
            self.t.start()
        except Exception as e:
            print(e)
        pass;
    
    def waiter(self):
        while not self._mainScript.Started: pass
        self.C_Physics.CRG_Physics_Start(self._tis)
    
    def End(self):
        self.C_Physics.CRG_Physics_End(self._tis);
        pass;
    
    def Add(self, script:RG_Script):
        script._id = self._scrCounter
        self._scrCounter += 1
        self._referenceKeeper[script._id] = CFUNCTYPE(None,c_double)(script.Tick)
        self.C_Physics.CRG_Physics_Add(self._tis, self._referenceKeeper[script._id])
    
    def Exists(self, script:RG_Script) -> bool:
        return script._id in self._referenceKeeper
    
    def Remove(self, script:RG_Script):
        try:
            self.C_Physics.CRG_Physics_Remove(self._tis, self._referenceKeeper[script._id]);
        except Exception as e:
            if(e.args[0] != "invalid command name \".!canvas\""):
                return
            else: raise e

        del self._referenceKeeper[script._id];
        pass;
    
    
    @property
    def Interval(self):
        return self._interval;
    
    @Interval.setter
    def Interval(self,newValue):
        self.C_Physics.CRG_Physics_SetInterval(self._tis,newValue);
        self._interval = newValue
        pass
    
    @property
    def FailedTickFailsafe(self) -> int:
        return self._failedTickFailsafe.Value
    
    @FailedTickFailsafe.setter
    def FailedTickFailsafe(self, newValue:int) -> None:
        self._failedTickFailsafe.Value = newValue
        
    @property  
    def Running(self):
        return self.C_Physics.CRG_Physics_Running(self._tis)
    
    @property
    def Counter(self):
        return self.C_Physics.CRG_Physics_GetCounter(self._tis);
    
    @property
    def DeltaTime(self):
        return self.C_Physics.CRG_Physics_GetDeltaTime(self._tis);
    
    @property
    def DeltaTime(self):
        return self.C_Physics.CRG_Physics_GetDeltaTime(self._tis);
    
    @property
    def FailedTickCount(self) -> int:
        return self._failedTickCount
    
    @FailedTickCount.setter
    def FailedTickCount(self, newValue:int) -> int:
        self._failedTickCount = newValue
