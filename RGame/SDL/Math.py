#----------------------------------
#----------------------------------
#            Imports
#----------------------------------
#----------------------------------
import decimal
import math
from decimal import Decimal

#----------------------------------
#----------------------------------
#            Vectors
#----------------------------------
#----------------------------------

class RG_Vector2D:
    
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    _length:Decimal = Decimal(0.0);
    X:Decimal = Decimal(0.0);
    Y:Decimal = Decimal(0.0);
    
    # ----------------------------------
    #             Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x:Decimal = Decimal(0.0), y:Decimal = Decimal(0.0)) -> None:
        
        # Initializing X and Y.
        self.X = Decimal(x);
        self.Y = Decimal(y);
        
        # Initializing the length.
        self.GetLength();
        pass;
        
    # To String
    def __str__(self) -> str:
        return "Vector 2D: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_Vector2D): return False;
        return other.X == self.X and other.Y ==  self.Y;
    
    #------------------------------------
    #             Functions:
    # -----------------------------------
    
    def ToVector(self):
        return self
    
    def ToVelocity(self):
        return RG_Velocity2D(self.X, self.Y)
    
    def GetLength(self) -> Decimal:
        # Get length squared
        LengthSqr = self.GetlengthSqr();

        # Check if anything changedS
        if(self._length * self._length == LengthSqr):
            return self._length;

        # Otherwise complete the square rooting of the length and store the result.
        self._length = Decimal.sqrt(Decimal(LengthSqr));
        return self._length;

    def GetlengthSqr(self) -> Decimal:
        return self.X * self.X + self.Y * self.Y;

    def SetLength(self, newLength):
        length = self.GetLength();
        if(newLength == length):
            return;
        if(length == 0):
            raise Exception("Cannot set the length of the 0 vector or a velocity with the speed of 0 to any other value than 0.")
        self.NormalizeOpt(length);
        h = self * newLength;
        self.X = h.X;
        self.Y = h.Y;
        self._length = h._length;
        pass;

    def Normalize(self):
        length = self.GetLength();
        if(length == 0):
            raise Exception("Cannot normalize the 0 vector or a velocity with the speed of 0.")
        h = self / length;
        self.X = h.X;
        self.Y = h.Y;
        pass;

    def NormalizeOpt(self, length):
        if(length == 0):
            raise Exception("Cannot normalize the 0 vector or a velocity with the speed of 0.")
        h = self / length;
        self.X = h.X;
        self.Y = h.Y;
        pass
    
    def DotProduct(self, other):
        return other.X * self.X + other.Y * self.Y
    
    # ----------------------------------
    #       Operator Overloading:
    # ----------------------------------
    # Plus: +
    def __add__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        
        # If point then return point
        if(tp is RG_Point2D or tp is RG_Position2D):
            x = self.X + Decimal(Right.X);
            y = self.Y + Decimal(Right.Y);
            return RG_Point2D(x, y);
        
        # If vector then return vector.
        elif(tp is RG_Vector2D or tp is RG_Velocity2D):
            x = self.X + Decimal(Right.X);
            y = self.Y + Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only add vectors with Points or other vectors (with the same number of dimensions)."+str(tp));
    
    # Subtract: -
    def __sub__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        
        # If point then return point
        if(tp is RG_Point2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Point2D(x, y);
        
        # If vector then return vector.
        elif(tp is RG_Vector2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only take away vectors with Points or other vectors (with the same number of dimensions).");
    
    # Multiply: *
    def __mul__(self, Right):
        
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        # If num then do num multiplication
        if(tp is float or tp is int ):
            x = self.X * Decimal(Right);
            y = self.Y * Decimal(Right);
            return RG_Vector2D(x, y);
        if(tp is Decimal ):
            x = self.X * Right;
            y = self.Y * Right;
            return RG_Vector2D(x, y);
        
        # If vector then do vector multiplication
        elif(tp is RG_Vector2D):
            x = self.X * Decimal(Right.X);
            y = self.Y * Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only multiply vectors by intigers, floats, Decimal, and other vectors (with the same number of dimensions)."+str(tp));
    
    # Divide: /
    def __truediv__(self, Right):
        
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        
        # If num then do num devision
        if(tp is float or tp is int or tp is decimal.Decimal):
            x = self.X / Decimal(Right);
            y = self.Y / Decimal(Right);
            return RG_Vector2D(x, y);
        
        # If vector then do vector division
        elif(tp is RG_Vector2D):
            x = self.X / Decimal(Right.X);
            y = self.Y / Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only divide vectors by intigers, floats, Decimal, and other vectors (with the same number of dimensions).");
    
    # Floor Divide: //
    def __floordiv__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        # Get Type.
        tp = type(Right);
        
        # If num then do num floor division
        if(tp is float or tp is int or tp is decimal.Decimal):
            x = self.X // Decimal(Right);
            y = self.Y // Decimal(Right);
            return RG_Vector2D(x, y);
        
        # If vector then do vector floor division
        elif(tp is RG_Vector2D):
            x = self.X // Decimal(Right.X);
            y = self.Y // Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only floor divide vectors by integers, floats, Decimal, and other vectors (with the same number of dimensions).");
    
    # Modulus: %
    def __mod__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        # Get Type.
        tp = type(Right);
        
        # If num then do num modulus
        if(tp is float or tp is int or tp is decimal.Decimal):
            x = self.X % Decimal(Right);
            y = self.Y % Decimal(Right);
            return RG_Vector2D(x, y);
        
        # If vector then do vector modulus
        elif(tp is RG_Vector2D):
            x = self.X % Decimal(Right.X);
            y = self.Y % Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only modulus vectors by integers, floats, Decimal and other vectors (with the same number of dimensions).");
    
    pass;

class RG_Velocity2D(RG_Vector2D):

    # ----------------------------------
    #           Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x:Decimal = Decimal(0.0), y:Decimal = Decimal(0.0)):
        super().__init__(x, y)
        pass;
    
    # To String
    def __str__(self)  -> str:
        return "Velocity: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other:RG_Vector2D) -> bool:
        return other.X == self.X and other.Y ==  self.Y;
    
    # ----------------------------------
    #             Wrappers:
    # ----------------------------------
    def SetSpeed(self, speed):
        self.SetLength(Decimal(speed));

    def GetSpeed(self):
        return float(self.GetLength());
    
    def ToVector(self):
        return RG_Vector2D(self.X, self.Y);
    
    def ToVelocity(self):
        return self
    
    def __add__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector()
        if(t is RG_Position2D):
            Right = Right.ToPoint()
        vec = super().__add__(Right)
        if (t is RG_Position2D):
            return RG_Position2D(vec.X,vec.Y)
        if (t is RG_Point2D):
            return RG_Point2D(vec.X,vec.Y)
        
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __sub__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector();
        if(t is RG_Position2D):
            Right = Right.ToPoint();
        vec = super().__sub__(Right)
        if (t is RG_Position2D):
            return RG_Position2D(vec.X,vec.Y)
        if (t is RG_Point2D):
            return RG_Point2D(vec.X,vec.Y)
        
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __mul__(self, Right):
        vec = super().__mul__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __truediv__(self, Right):
        vec = super().__truediv__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __floordiv__(self, Right):
        vec = super().__floordiv__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __mod__(self, Right):
        vec = super().__mod__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    pass;


#----------------------------------
#----------------------------------
#            Points
#----------------------------------
#----------------------------------

class RG_Point2D:
    
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    X:Decimal = Decimal(0.0);
    Y:Decimal = Decimal(0.0);
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x:Decimal = 0.0, y:Decimal = 0.0) -> None:
        self.X = Decimal(x);
        self.Y = Decimal(y);
        pass;
    
    # To String
    def __str__(self)  -> str:
        return "Point: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_Point2D): return False;
        return other.X == self.X and other.Y ==  self.Y;
    
    
    def ToPosition(self):
        return RG_Position2D(self.X, self.Y);
    
    def ToPoint(self):
        return self;
    
    # ----------------------------------
    #       Operator Overloading:
    # ----------------------------------
    # Plus: +
    def __add__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # If not vector then throw error
        if(not (type(Right) is RG_Vector2D or type(Right) is RG_Velocity2D)):
            raise TypeError("You can only add vectors to points (with the same number of dimensions)."+str(type(Right)));
        
        # Otherwise complete the addition
        x = self.X + Decimal(Right.X);
        y = self.Y + Decimal(Right.Y);
        return RG_Point2D(x, y);
    
    # Subtract: -
    def __sub__(self, Right):
        t = type(Right)
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        # If not point or vec then throw error
        
        if(t is RG_Point2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        elif(t is RG_Vector2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Point2D(x, y);
        
        else:
            raise TypeError("You can only subtract points and vectors from other points (with the same number of dimensions).");
        
        # Otherwise complete the subtraction
    
    pass;

class RG_Position2D(RG_Point2D):

    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x: Decimal = Decimal(0.0), y: Decimal = Decimal(0.0)) -> None:
        super().__init__(x, y)
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Position: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other:RG_Point2D) -> bool:
        return other.X == self.X and other.Y ==  self.Y;
    
    # ----------------------------------
    #             Functions:
    # ----------------------------------
    
    def ToPosition(self):
        return self;
    
    def ToPoint(self):
        return RG_Point2D(self.X, self.Y);
    
    def Move(self, velocity:RG_Velocity2D):
        newPos = velocity + self;
        self.X = newPos.X;
        self.Y = newPos.Y;
        
    def VectorTo(self, other) -> RG_Vector2D:
        return other - self;
    
        
    def __add__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector();
        vec = super().__add__(Right)
        return RG_Position2D(vec.X,vec.Y)
            
    def __sub__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector();
        if(t is RG_Position2D):
            Right = Right.ToPoint();
        vec = super().__sub__(Right)
        if (t is RG_Position2D):
            return RG_Vector2D(vec.X,vec.Y)
        if (t is RG_Point2D):
            return RG_Vector2D(vec.X,vec.Y)
        
        return RG_Position2D(vec.X,vec.Y)
 
        
    pass;
