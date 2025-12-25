# Imports
from RGame.SDL.Log import *
from RGame.SDL.Time import TimeInit
from .Physics.Physics import RG_MainPhysics
from .Graphics.Windows.Tkinter.MainWin import RG_MainWindow
from .SDL.Reference import ref
# End Imports

#MainScr class
class RG_MainScript:
    _beforeOverride = False
    _mainOverride = False
    _physicsTickOverride = False
    _renderOverride = False
    
    def __init__(self, before = None, main = None, physicsTick = None, render = None) -> None:
        if not before is None:
            self.Before = before
            self._beforeOverride = True
        if not main is None:
            self.Main = main
            self._mainOverride = True
        if not physicsTick is None:
            self.PhysicsTick = physicsTick
            self._physicsTickOverride = True
        if not render is None:
            self.Render = render
            self._renderOverride = True
        self.Started = False
        self.Stop = False
    
    def StartRGame(self):
        
        TimeInit()
        try:    
            if self._beforeOverride:
                self.Before(self)
            else: self.Before()
        except Exception as e:
            print("In Before - before everything.\n")
            raise e
        
        if(self.Stop):
            return
        self.Started = True
        
        print("Main> Started  | Init ( initialization - where things get first created )")
        self.INIT()
        print("Main> Finished | Init")
        try:    
            if self._mainOverride:
                self.Main(self)
            else: self.Main()
        except Exception as e:
            print("In MainScript Main\n")
            raise e;
        
        print("Main> Started  | Start up ( where physics and rendering are first started )")
        self.Exp = None;
        self.Start();
    
    def INIT(self):
        print()
        # Intervals
        # physics
        self.TickInterval =  0.05;
        print("Main\\Init> Done     | setting  -> Physics Tick Interval.")
        
        # rendering
        self.FrameRate = ref( 10 );
        print("Main\\Init> Done     | setting  -> Frame Rate.")
        
        # Managers
        # physics
        print("Main\\Init> Started  | creating -> Main Physics");
        self.MainPhysics = RG_MainPhysics(self, self.TickInterval);
        print("Main\\Init> Finished | creating -> Main Physics")
        
        # rendering
        print("Main\\Init> Started  | creating -> Main Window");
        self.MainWindow = RG_MainWindow(self, self.FrameRate);
        print("Main\\Init> Finished | creating -> Main Window");
        print()
    
        
        pass;
    
    def Before(self):
        pass;
    
    def Main(self):
        pass;
    
    def Start(self):
        self.MainPhysics.Interval = self.TickInterval;
        print()
        print("Main\\Start up> Starting | Main Physics Tick")
        self.MainPhysics.Start()
        print("Main\\Start up> Started  | Main Physics Tick")
        print("Main\\Start up> Starting | Main Window Rendering")
        self.MainWindow.Start()
        pass;
    
    
    def tick(self, deltatime):
        if not (self.MainPhysics.Running):return
        try:
            
            if self._physicsTickOverride:
                self.PhysicsTick(self, deltatime)
            else: self.PhysicsTick(deltatime)
        except Exception as e:
            if(issubclass(type(e),RG_Exception)):
                LogError(e.Message,e.Value)
                pass
            else:LogError(e.args[0])
            self.MainPhysics.FailedTickCount += 1
            if(self.MainPhysics.FailedTickCount == self.MainPhysics.FailedTickFailsafe): 
                text = f" > Max Failed PhysicsTick count surpassed. Current failsafe: {self.MainPhysics.FailedTickFailsafe}.\n > The error:\n\n"
                if(issubclass(type(e),RG_Exception)):
                    LogFatal(text + e.Message,e.Value)
                    pass
                else:LogFatal(text + e.args[0])
                self.MainWindow.RenderingManager.End()
    
    
    def PhysicsTick(self,deltatime):
        pass
    
    def render(self):
        if self._physicsTickOverride:
            self.Render(self)
        else: self.Render()
        
    def Render(self):
        pass;
    
    def End(self):
        self.MainWindow.RenderingManager.End()
    
    pass;