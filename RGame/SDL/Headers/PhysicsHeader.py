# Imports
from .Scripts import*
from ..Reference import ref
# End Imports

import abc

class RG_Physics(metaclass = abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'Start') and 
                callable(subclass.Start) and 
                hasattr(subclass, 'End') and 
                callable(subclass.End) and
                hasattr(subclass, 'Add') and 
                callable(subclass.Add) and
                hasattr(subclass, 'Exists') and 
                callable(subclass.Exists) and
                hasattr(subclass, 'End') and 
                callable(subclass.End) and
                hasattr(subclass, 'Remove') and 
                callable(subclass.Remove) and
                hasattr(subclass, 'Interval') and 
                hasattr(subclass, 'FailedTickFailsafe') and 
                hasattr(subclass, 'Running') and 
                hasattr(subclass, 'Counter') and 
                hasattr(subclass, 'DeltaTime') and 
                hasattr(subclass, 'FailedTickCount') or 
                NotImplemented)
    
    _interval:float = None
    _failedTickCount:int = None
    _failedTickFailsafe:ref = None
    
    @abc.abstractmethod
    def Start(self) -> None:
        pass
    
    @abc.abstractmethod
    def End(self) -> None:
        pass
    
    @abc.abstractmethod
    def Add(self, script:RG_Script) -> None:
        pass
    
    @abc.abstractmethod
    def Exists(self, script:RG_Script) -> bool:
        return False
    
    @abc.abstractmethod
    def Remove(self, script:RG_Script) -> None:
        pass
    
    @property
    @abc.abstractmethod
    def Interval(self) -> float:
        return self._interval
    
    @Interval.setter
    @abc.abstractmethod
    def Interval(self, newValue:float) -> None:
        self._interval= newValue
        
    @property
    @abc.abstractmethod
    def FailedTickFailsafe(self) -> int:
        return self._failedTickFailsafe.Value
    
    @FailedTickFailsafe.setter
    @abc.abstractmethod
    def FailedTickFailsafe(self, newValue:int) -> None:
        self._failedTickFailsafe.Value = newValue
        
    @property
    @abc.abstractmethod    
    def Running(self) -> bool:
        return self.C_Physics.CRG_Physics_Running(self.Tis)
    
    @property
    @abc.abstractmethod
    def Counter(self) -> int:
        return self.C_Physics.CRG_Physics_GetCounter(self.Tis)
    
    @property
    @abc.abstractmethod
    def DeltaTime(self) -> float:
        return self.C_Physics.CRG_Physics_GetDeltaTime(self.Tis)
    
    @property
    @abc.abstractmethod
    def FailedTickCount(self) -> int:
        return self._failedTickCount
    
    @FailedTickCount.setter
    @abc.abstractmethod
    def FailedTickCount(self, newValue:int) -> int:
        self._failedTickCount = newValue