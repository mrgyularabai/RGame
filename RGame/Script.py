# Imports
from .Graphics.GFX import*
from .SDL.Math import*
from .SDL.Log import*
# End Imports

#MainScr class
class RG_Script:
    Activated = False;
    Velocity:RG_Velocity2D = RG_Velocity2D(0,0);
    Position:RG_Position2D = RG_Position2D(0,0);
    Name:str = "Script";
    _id = 0;
    rending = True;

    
    def __init__(self,mainScript, position:RG_Position2D = None, velocity:RG_Velocity2D = None, appearance:RG_AppearanceType = None, name:str = "Script") -> None:
        
        self.Before();
        
        #mainScript
        self.MainScript = mainScript;
        
        #pos
        if (position is None):
            position = RG_Position2D()
        elif not (type(position) is RG_Position2D):
            raise RG_TypeError(position,
                                " 'RG_Script' must have an RG_Position2D as the argument 'position' (second argument).")
        self.Position = position;
        
        #vel
        if (velocity is None):
            velocity = RG_Velocity2D()
        elif not (type(velocity) is RG_Velocity2D):
            raise RG_TypeError(velocity,
                                " 'RG_Script' must have an RG_Velocity2D as the argument 'velocity' (third argument).")
        self.Velocity = velocity;
        
        self.MainWindow = self.MainScript.MainWindow;
        #appearance
        if (appearance is None):
            appearance = None
        elif not issubclass(type(appearance), RG_AppearanceType):
            raise RG_TypeError(appearance,
                                " 'RG_Script' must have an RG_AppearanceType the argument 'appearance' (fourth argument).")
        self.Appearance = appearance;
        
        #name
        if (name is None):
            name = "script"
        elif not (type(name) is str):
            raise RG_TypeError(name,
                                " 'RG_Script' must have a string as the argument 'name' (last argument).")
        self.Name = name;
        
        self.ScreenWidth = self.MainWindow.WindowWidth;
        self.ScreenHeight = self.MainWindow.WindowHeight;
        self.MainPhysics = self.MainScript.MainPhysics;
        self.Start();
        self.Activate()
        pass
    
    def MoveTo(self,x,y):
        self.Position.X = x;
        self.Position.Y = y;
        if not (self.Appearance is None):
            self.Appearance.MoveTo(x,y)
        pass;
    
    def Activate(self):
        if(self.Activated): return
        self.Activated = True;
        if not (self.Appearance is None):
            self.Appearance.Show();
        self.MainWindow.Add(self);
        self.MainPhysics.Add(self);
        pass;
    
    def Deactivate(self):
        if not (self.Activated): return
        self.Activated = False;
        self.MainPhysics.Remove(self);
        if not (self.Appearance is None):
            self.Appearance.Hide();
        self.MainWindow.Remove(self);
        self.rending = False;
        pass;
    
    
    # ----------------------------------
    #          Bounce:
    # ----------------------------------
    
    def Bounce(self):
        pos = self.Position - self.Appearance.OffSet;
        bounced = False;
        if(pos.X < 0 ): 
            self.Position.X += 0 - pos.X;
            self.Velocity.X *= -1;
            bounced = True;

        if(pos.X + self.Appearance.Dimensions.Width >  self.ScreenWidth): 
            self.Position.X += (self.ScreenWidth - self.Appearance.Dimensions.Width)-pos.X;
            self.Velocity.X *= -1;
            bounced = True;

        if(pos.Y < 0): 
            self.Position.Y += 0 - pos.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        if( self.Appearance.Dimensions.Height + pos.Y >  self.ScreenHeight): 
            self.Position.Y += (self.ScreenHeight - self.Appearance.Dimensions.Height)-pos.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        return bounced;
    
    # axial bounce
    def BounceY(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.Y < 0): 
            self.Position.Y = self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        if(pos.Y >=  self.ScreenHeight - self.Appearance.Dimensions.Height): 
            self.Position.Y = self.ScreenHeight + self.Appearance.Dimensions.Height + self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;
        
        return bounced;
    
    def BounceX(self):
        pos = self.Position+ self.Appearance.OffSet;
        bounced = False;
        
        if(pos.X < 0 ): 
            self.Position.X = self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;

        if(pos.X >=  self.ScreenWidth - self.Appearance.Dimensions.Width): 
            self.Position.X = self.ScreenWidth - self.Appearance.Dimensions.Width + self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;
        
        return bounced;
    
    # sides bounce
    def BounceRight(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.X >=  self.ScreenWidth - self.Appearance.Dimensions.Width): 
            self.Position.X = self.ScreenWidth - self.Appearance.Dimensions.Width + self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;

        
        return bounced;
    
    def BounceLeft(self):
        
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.X < 0 ): 
            self.Position.X = self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;

        
        return bounced;
    
    def BounceBottom(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;

        if(pos.Y >=  self.ScreenHeight - self.Appearance.Dimensions.Height): 
            self.Position.Y = self.ScreenHeight - self.Appearance.Dimensions.Height + self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        
        return bounced;
    
    def BounceTop(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.Y < 0): 
            self.Position.Y = self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;
            
        
        return bounced;
    
    
    def Before(self):
        pass;
    
    def Start(self):
        pass;
    
    def Tick(self,deltaTime):
        if not (self.MainWindow.RenderingManager.Run):return
        if not (self.MainPhysics.Running):return
        vel =  self.Velocity*deltaTime;
        self.Position.Move(vel);
        try:
            self.PhysicsTick(self.MainPhysics.DeltaTime)
        except Exception as e:
            if(issubclass(type(e),RG_Exception)):
                LogError(e.Message,e.Value)
                pass
            else:LogError(e.args[0])
            self.MainPhysics.FailedTickCount  += 1;
            if(self.MainPhysics.FailedTickCount == self.MainPhysics.FailedTickFailsafe): 
                text = f" > Max Failed PhysicsTick count surpassed. Current failsafe: {self.MainPhysics.FailedTickFailsafe}.\n > The error:\n\n"
                if(issubclass(type(e),RG_Exception)):
                    LogFatal(text + e.Message,e.Value)
                    pass
                else:LogFatal(text + e.args[0])
                self.MainWindow.RenderingManager.End()
        if self.MainWindow.RenderingManager.Run:
            self.MoveTo(self.Position.X,self.Position.Y)
        pass;
    
    def PhysicsTick(self,deltaTime):
        
        pass;
            
    def Render(self):
        if not (self.Appearance is None):
            self.Appearance.Render()
        pass;
    
    pass;

class RG_Circle(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, radius:float = None, color:str = None, OffSet:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Circle(mainScript.MainWindow.Screen, radius, color,OffSet ), name=name)
        
class RG_Ellipse(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, radiusX:float = None, radiusY:float = None, color:str = None, OffSet:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Ellipse(mainScript.MainWindow.Screen, radiusX, radiusY, color,offset=OffSet  ), name=name)

class RG_Rectangle(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, width:float = None, height:float = None, color:str = None, OffSet:RG_Vector2D = None, name: str = None) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Rectangle(mainScript.MainWindow.Screen, RG_Size(width, height), color ,offset=OffSet ), name=name)

class RG_Line(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, points:list[RG_Vector2D] = None, color:str = None, width:int = None, smooth:bool = None, resolution:int = None, Offset:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Line(mainScript.MainWindow.Screen, points, color, width, smooth, resolution, Offset), name=name)
        
class RG_Label(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, text:str = None, fontType:str = None, fontSize:int = None, fontColor:str = None, bold:bool = None, italic:bool = None, underline:bool = None, overstrike:bool = None, Offset:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Label(mainScript.MainWindow.Screen, text, fontType, fontSize,fontColor, bold, italic, underline, overstrike, Offset), name=name)

class RG_Image(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, fileLocation:str = None, OffSet:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Shader(screen = mainScript.MainWindow.Screen,fileLocation= fileLocation,offset=OffSet ), name=name)