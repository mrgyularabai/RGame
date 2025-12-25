# Imports
from RGame.SDL.Exceptions import RG_TypeError
from RGame.SDL.Log import LogWarning
# End Imports

from decimal import Decimal

class RG_Size:
    
    _width:Decimal = 100;
    _height:Decimal = 100;
    
    @property
    def Width(self):
        return self._width;
    
    @Width.setter
    def Width(self,newVal): 
        self._width = Decimal(newVal);
        pass;
    
    @property
    def Height(self):
        return self._height;
    
    @Height.setter
    def Height(self,newVal): 
        self._height = Decimal(newVal);
        pass
    
    def __init__(self, width:Decimal | float = None, height:Decimal | float = None) -> None:
        
        # width
        if (width is None):
            width = Decimal(25)
        elif not ((type(width) is Decimal) or (type(width) is int)):
            if(type(width) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'width'(first argument) of the class 'RG_Size'")
                width = Decimal(width)
            else:
                raise RG_TypeError(width,
                                " 'RG_Size' must have a 'Decimal' as the argument 'width' (first argument).")
                            
        # height
        if (height is None):
            height = Decimal(25)
        elif not ((type(height) is Decimal) or (type(height) is int)):
            if(type(height) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'height'(second argument) of the class 'RG_Size'")
                height = Decimal(height)
            else:
                raise RG_TypeError(height,
                                " 'RG_Size' must have a 'Decimal' as the argument 'height' (second argument).")
            
        self.Width = width
        self.Height = height
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_Size): return False;
        return self.Width == other.Width and self.Height == other.Height;
    
    def __str__(self) -> str:
        return "Size: (Width: " + str(self.Width) + ", Height: " + str(self.Height) + ")";
    
    pass;