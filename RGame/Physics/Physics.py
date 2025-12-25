# Imports
from ..SDL.Headers.Scripts import*
from ..SDL.Headers.PhysicsHeader import RG_Physics
from .PhysicsPy import RG_PyPhysics
from .PhysicsCpp import RG_CppPhysics
from ..SDL.Reference import*
from ..SDL.Exceptions import*
from ..SDL.Log import*
# End Imports

import enum

@enum.unique
class RG_PhysicsMode(enum.Enum):
    CPP = 0
    PYTHON = 1
    pass

class RG_MainPhysics(RG_Physics):
    _physicsMode:int = None
    _PyPhysics:RG_Physics = None
    _CppPhysics:RG_Physics = None
    _started:bool = False
    _autoSet:bool = False
    
    @property
    def PhysicsMode(self) -> RG_PhysicsMode:
        return self._physicsMode
    
    @PhysicsMode.setter
    def PhysicsMode(self, newValue:RG_PhysicsMode) -> None:
        if self._autoSet and newValue != RG_PhysicsMode.PYTHON:
            switchWarning = RG_TypeWarning(newValue, "The value has already automatically been (due to some error) set to python mode permanently.")
            Log(switchWarning.Message, switchWarning.Value, LogLevel.WARNING)
            return
        if self._started:
            raise RG_AccessError(newValue, "You cannot change the Physics mode after starting the simulation.")
        self._physicsMode = newValue
                
    
    def getPhysics(self) -> RG_Physics:
        match self.PhysicsMode:
            case RG_PhysicsMode.PYTHON:
                return self._PyPhysics
            case RG_PhysicsMode.CPP:
                return self._CppPhysics
            case _:
                accessError = RG_AccessError(None,
                                        "You probably accessed a private member of RG_MainPhysics (set a private member to None/called the private function getPhysics too early)!")
                raise accessError
    
    def __init__(self, mainScript:RG_MainScript, interval:float) -> None:
        
        if self.PhysicsMode == None: 
            self.PhysicsMode = RG_PhysicsMode.CPP
            
        self._PyPhysics = RG_PyPhysics(mainScript, interval)
        
        try:
            self._CppPhysics = RG_CppPhysics(mainScript, interval)
        except Exception as e:
            switchWarning = RG_FileExistsWarning(*e.args, "The Physics.dll could not be loaded so automatically setting physics mode permanently to Python")
            Log(switchWarning.Message, switchWarning.Value, LogLevel.WARNING)
            self.PhysicsMode = RG_PhysicsMode.PYTHON 
            self._autoSet = True

    def Start(self) -> None:
        if self._started: return
        self._started = True
        self.getPhysics().Start()
        
    def End(self) -> None:
        self.getPhysics().End()
    
    def Add(self, script:RG_Script) -> None:
        self.getPhysics().Add(script)
        
    def Exists(self, script: RG_Script) -> bool:
        return self.getPhysics().Exists(script)
    
    def Remove(self, script: RG_Script) -> None:
        self.getPhysics().Remove(script)
    
    @property
    def Interval(self) -> float:
        return self.getPhysics().Interval
    
    @Interval.setter
    def Interval(self, newValue:float) -> None:
        self.getPhysics().Interval = newValue
        
    @property
    def FailedTickFailsafe(self) -> int:
        return self.getPhysics().FailedTickFailsafe
    
    @FailedTickFailsafe.setter
    def FailedTickFailsafe(self, newValue:int) -> None:
        self.getPhysics().FailedTickFailsafe = newValue
        
    @property
    def Running(self) -> bool:
        return self.getPhysics().Running
    
    @property
    def Counter(self) -> int:
        return self.getPhysics().Counter
    
    @property
    def DeltaTime(self) -> float:
        return self.getPhysics().DeltaTime
    
    @property
    def FailedTickCount(self) -> int:
        return self.getPhysics().FailedTickCount
    
    @FailedTickCount.setter
    def FailedTickCount(self, newValue:int) -> int:
        self.getPhysics().FailedTickCount = newValue
