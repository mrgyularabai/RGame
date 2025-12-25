# Imports
from ._size import*
# End Imports

class RG_SizeSquare(RG_Size):
    
    @property
    def Side(self):
        return self.Width
    
    @Side.setter
    def Side(self,newVal): 
        self.Width = Decimal(newVal);
        self.Height = Decimal(newVal);
        pass;
    
    def __init__(self, side:Decimal | float = None) -> None:
        #side
        if (side is None):
            side = Decimal(25)
        elif not ((type(side) is Decimal) or (type(side) is int)):
            if(type(side) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'side'(second argument) of the class 'RG_Size'")
                side = Decimal(side)
            else:
                raise RG_TypeError(side,
                                " 'RG_SizeSquare' must have a 'Decimal' as the argument 'side' (second argument).")
        self.Side = side
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_SizeSquare): return False;
        return self.Side == other.Side
    
    def __str__(self) -> str:
        return "Square Size: (Size: " + str(self.RadiusX) + ")";
    
    pass;

class RG_SizeEllipse(RG_Size):
    
    @property
    def RadiusX(self):
        return self.Width / 2
    
    @RadiusX.setter
    def RadiusX(self,newVal): 
        self.Width = Decimal(newVal)*2
        pass;
    
    @property
    def RadiusY(self):
        return self.Height / 2
    
    @RadiusY.setter
    def RadiusY(self,newVal): 
        self.Height = Decimal(newVal)*2
        pass;
    
    
    def __init__(self, radiusX:Decimal | float = None, radiusY:Decimal | float = None) -> None:
        # radius X
        if (radiusX is None):
            radiusX = Decimal(25)
        elif not ((type(radiusX) is Decimal) or (type(radiusX) is int)):
            if(type(radiusX) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'radiusX'(first argument) of the class 'RG_Size'")
                radiusX = Decimal(radiusX)
            else:
                raise RG_TypeError(radiusX,
                                " 'RG_SizeEllipse' must have a 'Decimal' as the argument 'radiusX' (first argument).")
                     
        self.RadiusX = radiusX;
               
        # radius Y
        if (radiusY is None):
            radiusY = Decimal(25)
        elif not ((type(radiusY) is Decimal) or (type(radiusY) is int)):
            if(type(radiusY) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'radiusY'(second argument) of the class 'RG_Size'")
                radiusY = Decimal(radiusY)
            else:
                raise RG_TypeError(radiusY,
                                " 'RG_Size' must have a 'Decimal' as the argument 'radiusY' (second argument).")
                
        self.RadiusY = radiusY;
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_SizeEllipse): return False;
        return self.Width == other.Width and self.Height == other.Height;
    
    def __str__(self) -> str:
        return "Ellipse Size: (RadiusX: " + str(self.RadiusX) + ", RadiusY: " + str(self.RadiusY) + ")";
    
    pass;

class RG_SizeCircle(RG_SizeEllipse):
    
    @property
    def Radius(self):
        return self.RadiusX;
    
    @Radius.setter
    def Radius(self,newVal): 
        self.RadiusX = Decimal(newVal);
        self.RadiusY = Decimal(newVal);
        pass;
    
    
    def __init__(self, radius:Decimal | float = None) -> None:
        # radius 
        if (radius is None):
            radius = Decimal(25)
        elif not ((type(radius) is Decimal) or (type(radius) is int)):
            if(type(radius) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'radius'(second argument) of the class 'RG_Size'")
                radiusY = Decimal(radius)
            else:
                raise RG_TypeError(radius,
                                " 'RG_SizeCircle' must have a 'Decimal' as the argument 'radius' (second argument).")
        self.Radius = radius;
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_SizeCircle): return False;
        return self.Radius == other.Radius;
    
    def __str__(self) -> str:
        return "Circle Size: (Radius: " + str(self.Radius) + ")";
    
    pass;