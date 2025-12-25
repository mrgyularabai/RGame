# Imports
from RGame.SDL.Math import*
# End Imports

from tkinter import*

#----------------------------------
#----------------------------------
#            Appearance
#----------------------------------
#----------------------------------        
class RG_AppearanceType:
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    _ended = True
    _created:bool = False;
    @property
    def Created(self):
        return self._created;
    
    @Created.setter
    def Created(self,new):
        raise ValueError("Created is readonly.")
    
    _canvasID:str = "";
    OffSet:RG_Vector2D = RG_Vector2D(0,0);
    _visible = True;
    
    @property
    def Visible(self):
        return self._visible
    
    @Visible.setter
    def Visible(self, new):
        if not (type(new) is bool): raise TypeError("Cannot set visible to a value that is not bool: " + str(new))
        if(new):
            self.Show()
        else:
            self.Hide()
    
    Dimensions:object = None;
        
    def __init__(self, canvas:Canvas, spritePosition:RG_Position2D) -> None:
        self._screen:Canvas = canvas;
        self.CreateGraphics(spritePosition)
        pass;
    
    def __del__(self):
        self.DeleteGraphics()
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def CreateGraphics(self):
        if(self.Created):return;
        self._visible = True;
        self._created = True;
        self._canvasID = self._createGfx( RG_Position2D(0,0) );
        
        pass;
    
    def _createGfx(self, spritePosition:RG_Position2D) -> str:
        
        pass;
    
    def _configureGfx(self):
        
        pass;
    
    
    def DeleteGraphics(self):
        if not (self.Created): return;
        self._created = False;
        self._visible = False;
        try:
            self._screen.delete(self._canvasID);
        except Exception as e:
            if(e.args[0] == "invalid command name \".!canvas\""):
                return
            else:
                raise e
            
        self._canvasID = "";
        pass;
    
    def Hide(self):
        try:
            self._screen.itemconfigure(self._canvasID, state = "hidden");
        except Exception as e:
            if(e.args[0] == "invalid command name \".!canvas\""):
                return
            else:
                raise e
        self._visible = False;
        pass;
    
    def Show(self):
        self._screen.itemconfigure(self._canvasID, state = "normal");
        self._visible = True;
        pass;
    
    def MoveTo(self,x,y):
        try:
            self._screen.moveto(self._canvasID, int(x-self.OffSet.X), (int(self._screen.winfo_height()-y+self.OffSet.Y-self.Dimensions.Height)));
        except Exception as e:
            if(e.args[0] == "invalid command name \".!canvas\""):
                return
            else:
                raise e
        
    def Render(self):
        if(not self.Created): self.CreateGraphics()
        if(not self.Visible): return;
        self._configureGfx()
        pass;
    
    
    pass;