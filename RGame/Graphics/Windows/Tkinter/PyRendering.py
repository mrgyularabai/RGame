# Imports
from RGame.SDL.Log import*
from RGame.SDL.Reference import*
from RGame.SDL.Time import*
# End Imports

from tkinter import*
from threading import*
from multiprocessing import*
from concurrent.futures import ThreadPoolExecutor

class RG_RenderingManager:

    # Variables
    # window
    Window:Tk = None;
    Screen:Canvas = None;
    
    #Frame rate
    FrameRate:ref = ref(24);
    _pause:float = 1/FrameRate.Value;
    
    #Running
    BlockRender:bool = False;
    Run:bool = True
    FailedRenderCount:int = 0;
        
    Ended = False;
    Exceptions = []
    

    # Constructor (Where it starts)
    def __init__(self, mainScript, window:Tk, frameRate:ref = ref(30), scripts:ref = ref([]), failedRenderFailsafe:ref = ref(10), width:int=600, height:int=400, backGround:ref = ref("Black"), appearances:ref = ref([])):
        
        print("Main\\Init\\MainWindow> Started  | creating -> Render");
        
        print("\nMain\\Init\\MainWindow\\Render> Started  | creating -> General Values");
        try:
            self._mainScript = mainScript;
            self.Window = window;
            self._renderList = scripts;
            self._appearances = appearances;
            self._width = width;
            self._height = height;
            self._backGround = backGround;
            self._failedRenderFailsafe = failedRenderFailsafe;
        except Exception as e:
            print("Failed initializing general input variables.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | creating -> General Values");
        
        print("Main\\Init\\MainWindow\\Render> Started  | setting -> Frame Rate ");
        try:
            self.FrameRate = frameRate;
            self._oldFrameRate = self.FrameRate.Value;
            self._pause = 1/frameRate.Value;
        except Exception as e:
            print("Failed to initialize frame rate.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | setting -> Frame Rate ");
        
        print("Main\\Init\\MainWindow\\Render> Started  | creating -> Canvas");
        try:
            self.Screen = Canvas(self.Window, width = width, height = height, bg = backGround);
        except Exception as e:
            print("Failed to create Canvas.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | creating -> Canvas");
        
        print("Main\\Init\\MainWindow\\Render> Started  | printing -> Canvas");
        try:
            self.Screen.pack();
        except Exception as e:
            print("Failed to put Canvas on window.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | printing -> Canvas");
        
        print("\nMain\\Init\\MainWindow> Finished | creating -> Render");
        self.timer = RG_Timer(self._mainScript)
        self.executor = ThreadPoolExecutor(cpu_count())

    def StartRendering(self, width:int=600, height:int=400, backGround:ref = ref("Black")):
        
        print("Main\\Start up\\MainWindow> Started  | configuring -> Canvas");
        self.Screen.config(width = width, height = height, bg = backGround);
        print("Main\\Start up\\MainWindow> Finished | configuring -> Canvas");
        print("Main\\Start up\\MainWindow> Starting | Render");
        
        try:
            self.p = Thread(target = self.StartRender);
            self.p.start()
            self.Window.protocol("WM_DELETE_WINDOW", self.End);
            self.Window.mainloop()
        except Exception as e:
            print("Failed to start the rendering.\n\n");
            raise e;

        pass;
    
    
    #Render
    def StartRender(self):
        print("Main\\Start up\\MainWindow> Started  | Render");
        print("\nMain\\Start up> Started  | MainWindow");
        print("\nMain> Finished  | Start up\n");
        self._mainScript.Started = True;
        self.Render();
    
    def Render(self):
        self.timer.Subscribe()
        while self.Run:
            try:
                if(self.Ended) : return;
                Pause(self._pause-self.timer.Count);
                self.timer.Reset()
                self.DoRender()
            except Exception as e:
                if self.HandleExp(e): return
        pass;
    
    def HandleExp(self,e):
        if(self.Ended) : return True;
        print("Failed Render.");
        if(not self.Run): return True;
        if(issubclass(type(e),RG_Exception)):
            LogError(e.Message,e.Value)
            pass
        elif(len(e.args)>0):LogError(e.args[0])
        else:LogError("There was an exception raised without a message.")
        self.FailedRenderCount += 1;
        if(self.FailedRenderCount == self._failedRenderFailsafe.Value): 
            text = f" > Max Failed Render count surpassed. Current failsafe: {self._failedRenderFailsafe.Value}.\n > The error:\n\n"
            
            if(issubclass(type(e),RG_Exception)):
                LogFatal(text + e.Message,e.Value)
                pass
            elif(len(e.args)>0):LogFatal(text + e.args[0])
            else:LogFatal(text + "There was an exception raised without a message.")
            self.End()
    
    def DoRender(self):
        if(self.Ended) : return;
        if(self._oldFrameRate != self.FrameRate.Value):
            self._oldFrameRate = self.FrameRate.Value
            self._pause = 1/self.FrameRate.Value
        self._mainScript.render()
        self.DoRend()
        self.executor.map(self.Display, self._appearances.Value)
        for e in self.Exceptions:
            raise e
    
    def DoRend(self):
        if(self.Ended) : return
        for Src in self._renderList.Value:
            Src.Render()
            pass

    def Display(self,Src):
        try:
            Src.Appearance.Render()
        except Exception as e:
            self.Exceptions.append(e)
    
    def End(self):
        if(self.Ended) : return;
        self.Ended  = True;
        self.Run = False;
        print("\nMain> Started  | Ending .")
        print("Main\\Ending> Started  | ending  -> physics.")
        self._mainScript.MainPhysics.End();
        while self._mainScript.MainPhysics.Running:pass
        print("Main\\Ending> Finished | ending  -> physics.")
        print("Main> Finished | Ending.")
        self.Window.destroy()

    async def des(self):
        pass
    pass;


