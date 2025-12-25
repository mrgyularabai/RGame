# Imports
from RGame.SDL.Math import*
from RGame.SDL.Headers.Scripts import RG_Script
from .PyRendering import*
# End Imports

from enum import Enum
from tkinter import*
from concurrent.futures import ThreadPoolExecutor

class RG_WindowMode(Enum):
    TKINTER = 0
    PYGAME = 0

class RG_MainWindow:
    WindowTitle:str = "RGame"
    WindowHeight:int = 500
    WindowWidth:int = 800
    WindowBackground:str = "White"
    WindowIcon:str = None
    FrameRate:ref = ref(30);
    FailedRenderFailsafe:ref = ref(3)
    RenderingManager:RG_RenderingManager = None
    SpriteRender:ref = ref([])
    Appearances:ref = ref([])
    Activate:bool = True
    
    
    def __init__(self, mainScr, frameRate = ref(30)):
        if(mainScr == None) : return;
        self.MainScript = mainScr;
        self.FrameRate = frameRate;
        print("Main\\Init\\MainWindow> Started  | creating -> Window");
        self.Window = Tk()
        print("Main\\Init\\MainWindow> Finished | creating -> Window");
        print("Main\\Init\\MainWindow> Started  | creating -> Rendering");
        try:
            self.RenderingManager = RG_RenderingManager(
                self.MainScript, self.Window,
                self.FrameRate, self.SpriteRender, self.FailedRenderFailsafe,
                self.WindowWidth, self.WindowHeight, self.WindowBackground,
                self.Appearances
                )
        except Exception as e:
            print("Failed to initialize RenderingManager.\n\n")
            raise e;
        print("Main\\Init\\MainWindow> Finished | creating -> Rendering");
        self.Mouse = RG_Mouse(self.RenderingManager.HandleExp,self.WindowHeight)
        self.Mouse.bindEvents(self.Window)
    
    
    
    def Start(self):
        print("Main\\Start up> starting | MainWindow")
        if(not self.Activate):
            print("Main\\Start up\\MainWindow> Report   | MainWindow.Activate is set to False so window will not start)");
            
            self.Window.after(1,self.Window.destroy)
            mainloop()
            print("Main> Finished | Start up");
            return;
        
        self.CreateWindow()
        
        
        self.RenderingManager.StartRendering(self.WindowWidth, self.WindowHeight, self.WindowBackground);
        pass;
    
    
    
    def CreateWindow(self):
        print("\nMain\\Start up\\MainWindow> Started  | configuring -> Window\n");
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Title");
        self.Window.title(self.WindowTitle);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Title");
        #photo = PhotoImage(file = self.WindowIcon);
        #self.MainWindow.iconphoto(False, photo);
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Icon");
        if(self.WindowIcon != None):
            self.Window.iconbitmap(self.WindowIcon);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Icon");
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Max Size (will be separate to min in a future update)");
        self.Window.maxsize(self.WindowWidth,self.WindowHeight);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Max Size");
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Min Size");
        self.Window.minsize(self.WindowWidth,self.WindowHeight);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Min Size");
        print("\nMain\\Start up\\MainWindow> Finished | configuring -> Window");
        pass;
    
    
    
    def Add(self, script:RG_Script): 
        self.SpriteRender.Value.append(script)
        self.Appearances.Value.append(script)
        pass;
    
    def Exists(self, script:RG_Script): 
        return 0 < self.SpriteRender.Value.count(script)
    
    def Remove(self, script): 
        if(len(self.SpriteRender.Value) == 0): return
        self.SpriteRender.Value.remove(script)
        self.Appearances.Value.remove(script)
        pass;
    
    def Bind(self,BindKey, Bind):
        self.Window.bind(BindKey,Bind)
    
    
    
    
            
        
    @property
    def Screen(self):
        return self.RenderingManager.Screen
    
class RG_Mouse:
    
    def __init__(self, handleExp, height):
        self.winH = height
        self._handleExp = handleExp
        self.executor = ThreadPoolExecutor()
    
    Left = False
    Middle = False
    Right = False
    ScrollDelta = 0
    DoubleClickDelta = 0.5
    DoubleClickTimePoint = RG_TimePoint()
    OnSecondClick = False
    DragDeltaMovement = 3
    Drag = False
    
    def BindLeftDown(self, bind):
        self._leftDown.append(bind)
        
    def BindLeftUp(self, bind):
        self._leftUp.append(bind)
        
    def BindMiddleDown(self, bind):
        self._middleDown.append(bind)
        
    def BindMiddleUp(self, bind):
        self._middleUp.append(bind)
        
    def BindRightDown(self, bind):
        self._rightDown.append(bind)
        
    def BindRightUp(self, bind):
        self._rightUp.append(bind)
        
    def BindDoubleClick(self, bind):
        self._doubleClick.append(bind)
        
    def BindMove(self, bind):
        self._move.append(bind)
        
    def BindDrag(self, bind):
        self._drag.append(bind)
        
    def BindScroll(self, bind):
        self._scroll.append(bind)
    
    def bindEvents(self, window):
        window.bind("<1>",self.leftDown)
        window.bind("<ButtonRelease-1>",self.leftUp)
        window.bind("<2>",self.middleDown)
        window.bind("<ButtonRelease-2>",self.middleUp)
        window.bind("<3>",self.rightDown)
        window.bind("<ButtonRelease-3>",self.rightUp)
        window.bind("<Motion>",self.move)
        window.bind("<MouseWheel>",self.scroll)
    
    _leftDown:list = []
    def leftDown(self, args):
        self.Left = True
        for func in self._leftDown:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
            
    _doubleClick:list = []
    def doubleClick(self, args):
        if not (self.OnSecondClick):
            self.OnSecondClick = True
            self.DoubleClickTimePoint.Now()
            return
        self.OnSecondClick = False
        
        if (self.DoubleClickTimePoint.Diff() > self.DoubleClickDelta):
            return
        
        for func in self._doubleClick:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _leftUp:list = []
    def leftUp(self, args):
        self.Left = False
        self.Drag = False
        self.executor.submit(self.doubleClick, args)
        for func in self._leftUp:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
            
    _middleDown:list = []
    def middleDown(self, args):
        self.Middle = True
        for func in self._middleDown:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _middleUp:list = []
    def middleUp(self, args):
        self.Middle = False
        for func in self._middleUp:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
            
    _rightDown:list = []
    def rightDown(self, args):
        self.Right = True
        for func in self._rightDown:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _rightUp:list = []
    def rightUp(self, args):
        self.Right = False
        for func in self._rightUp:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
                
    _drag:list = []
    LastPos = RG_Position2D()
    Position = RG_Position2D()
    DeltaMovement = RG_Vector2D()
    def drag(self, args):
        if not (self.Left): return
        if not(self.Drag):
            if not (self.DeltaMovement.GetlengthSqr() > self.DragDeltaMovement*self.DragDeltaMovement): return
        self.Drag = True
        for func in self._drag:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
                
    _move:list = []
    def move(self, args):
        self.LastPos = self.Position
        self.Position = RG_Position2D(args.x, self.winH-args.y)
        self.DeltaMovement = self.LastPos.VectorTo(self.Position)
        self.drag(args)
        for func in self._move:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _scroll:list = []
    def scroll(self, args):
        self.ScrollDelta += args.delta
        for func in self._scroll:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return