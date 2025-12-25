# Imports
from RGame.SDL.Log import LogError
from RGame.SDL.Math import*
from RGame.SDL.Exceptions import*
from ..Size import*
from ._appearance import*
# End Imports
from tkinter import*
import tkinter.font as tkFont
import os 
import math

#----------------------------------
#----------------------------------
#            Appearance
#----------------------------------
#----------------------------------        

class RG_App_Label(RG_AppearanceType):
    
    def GetFontTypes() -> tuple:
        return tkFont.families()
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, screen:Canvas = None, text:str = None, fontType:str = None, fontSize:int = None, fontColor:str = None, bold:bool = None, italic:bool = None, underline:bool = None, overstrike:bool = None, offset:RG_Vector2D = None) -> None:
        
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Label' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # text
        if (text is None):
            text = "Label text."
        elif not (type(text) is str):
            raise RG_TypeError(text,
                                " 'RG_App_Label' must have a string as the argument 'text' (second argument).")
            
        self.Text = text
        
        # fontType 
        if (fontType is None):
            fontType = "Calibri"
        elif not (type(fontType ) is str):
            raise RG_TypeError(fontType ,
                                " 'RG_App_Label' must have a string as the argument 'fontType' (third argument).")
        elif not (fontType in tkFont.families()):
            raise RG_ValueError(fontType,
                            " 'RG_App_Label' the argument 'fontType' (third argument) must be a font that exists.")
        
        self.FontType = fontType
        
        # fontSize
        if (fontSize is None):
            fontSize  = 12
        elif not (type(fontSize ) is int):
            raise RG_TypeError(fontSize ,
                                " 'RG_App_Label' must have an int as the argument 'fontSize' (fourth argument).")
        
        self.FontSize = fontSize
        
        # fontColor        
        if (fontColor is None):
            fontColor  = "Black"
        elif not (type(fontColor ) is str):
            raise RG_TypeError(fontColor ,
                                " 'RG_App_Label' must have a str as the argument 'fontColor' (fifth argument).")
        
        self.Color = fontColor
        
        # Bold      
        if (bold is None):
            bold = False
        elif not (type(bold) is bool):
            raise RG_TypeError(bold ,
                                " 'RG_App_Label' must have a bool as the argument 'bold' (sixth argument).")
        
        self.Weight = bold
        
        # Italic     
        if (italic is None):
            italic = False
        elif not (type(italic) is bool):
            raise RG_TypeError(italic,
                                " 'RG_App_Label' must have a bool as the argument 'italic' (seventh argument).")
            
        self.Slant = italic
        
        # Underline     
        if (underline is None):
            underline = False
        elif not (type(underline) is bool):
            raise RG_TypeError(underline,
                                " 'RG_App_Label' must have a bool as the argument 'underline' (eighth argument).")
            
        self.Underline = underline
        
        # Overstrike     
        if (overstrike is None):
            overstrike = False
        elif not (type(overstrike) is bool):
            raise RG_TypeError(overstrike,
                                " 'RG_App_Label' must have a bool as the argument 'overstrike' (ninth argument).")
            
        self.Overstrike = overstrike
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Label' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass
    
    # To String
    def __str__(self) -> str:
        return "Label: (ShapeID: " + str(self._canvasID) + ", Text: " + str(self.Text) + ", FontType: " + str(self.FontType) + ", FontColor: " + str(self.FontColor) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    
    def MoveTo(self, x, y):
        self._screen.moveto(self._canvasID, int(x-self.OffSet.X), (int(self._screen.winfo_height()-y+self.OffSet.Y)));
    
    def _createGfx(self, spritePosition:RG_Position2D):
        absolutePosition = spritePosition + self.OffSet
        if(self.Weight):
            weight = "bold"
        else:
            weight = "normal"
        if(self.Slant):
            slant = "italic"
        else:
            slant = "roman"
        font = tkFont.Font(
            family = str(self.FontType),
            size = self.FontSize, 
            weight = weight,
            slant = slant,
            underline = self.Underline,
            overstrike = self.Overstrike)
        try:
            ID = self._screen.create_text(
                absolutePosition.X, absolutePosition.Y, 
                fill=self.Color,
                font=font,
                text= self.Text
                )
        except Exception as e:
            LogError(" Could not create a label.")
        return ID;
    
    def _configureGfx(self):
        if(self.Weight):
            weight = "bold"
        else:
            weight = "normal"
        if(self.Slant):
            slant = "italic"
        else:
            slant = "roman"
        font = tkFont.Font(
            family = str(self.FontType),
            size = self.FontSize, 
            weight = weight,
            slant = slant,
            underline = self.Underline,
            overstrike = self.Overstrike)
        self._screen.itemconfigure(self._canvasID,
                fill=self.Color,
                font=font,
                text= self.Text)
        pass
    
    pass

class RG_App_Shape(RG_AppearanceType):
    
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    Color:str = "Black";
    Dimensions:RG_Size = RG_Size(50,50);
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, dimensions:RG_Size  = None, color:str = None, outlineColor:str = None, outlineWidth:int = None, offset:RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Shape' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        if (dimensions is None):
            dimensions  = RG_Size()
        elif not (issubclass(type(dimensions ),RG_Size) or type(dimensions ) is RG_Size):
            raise RG_TypeError(dimensions ,
                                " 'RG_App_Shape' must have a RG_Size as the argument 'dimensions' (second argument).")
        
        self.Dimensions = dimensions
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Shape' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Ellipse' must have a str as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Ellipse' must have an int as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Shape' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Shape: (ShapeID: " + str(self._canvasID) + ", Dimensions: " + str(self.Dimensions) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition:RG_Position2D):
        
        absolutePosition = spritePosition + self.OffSet;
        ID = self._screen.create_rectangle(
            absolutePosition.X, self._screen.winfo_height()-absolutePosition.Y, 
            absolutePosition.X + self.Dimensions.Width, (self._screen.winfo_height()-absolutePosition.Y) - self.Dimensions.Height,
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        self._screen.coords(self._canvasID,
            pos[0],pos[1],
            pos[0] + float(self.Dimensions.Width), pos[1] + float(self.Dimensions.Height))
        
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth)
        pass;
        
    pass;
    
class RG_App_Rectangle(RG_App_Shape):
    pass;

class RG_App_Line(RG_App_Shape):
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    Color:str = "Black";
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, points:list[RG_Vector2D] = None, color:str = None, width:int = None, smooth:bool = None, resolution:int = None, offset:RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Line' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        if (points is None):
            points  = [RG_Vector2D(25,25)]
        elif not (type(points ) is list):
            raise RG_TypeError(points ,
                                " 'RG_App_Line' must have a list of RG_Vector2Ds as the argument 'points' (second argument).")
        
        self.Points2 = points
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Line' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        # Width        
        if (width is None):
            width  = 1
        elif not (type(width ) is int):
            raise RG_TypeError(width ,
                                " 'RG_App_Line' must have a int as the argument 'width' (fourth argument).")
        
        self.Width = width
        
        # Smooth        
        if (smooth is None):
            smooth  = False
        elif not (type(smooth ) is bool):
            raise RG_TypeError(smooth ,
                                " 'RG_App_Line' must have a bool as the argument 'smooth' (fifth argument).")
        
        self.Smooth = smooth
        
        # Resolution        
        if (resolution is None):
            resolution = 12
        elif not (type(resolution ) is int):
            raise RG_TypeError(resolution ,
                                " 'RG_App_Line' must have a int as the argument 'resolution' (sixth argument).")
        
        self.Resolution = resolution
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Line' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Line: (ShapeID: " + str(self._canvasID) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition:RG_Position2D):
        
        absolutePosition = spritePosition + self.OffSet;
        res = [absolutePosition.X, self._screen.winfo_height()-absolutePosition.Y]
        for point in self.Points2:
            res.append(absolutePosition.X + point.X)
            res.append(self._screen.winfo_height() - (absolutePosition.Y + point.Y))
        ID = self._screen.create_line(
            *res,
            fill=self.Color,width =self.Width, smooth=self.Smooth, splinesteps=self.Resolution
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        res = [pos[0], pos[1]]
        for point in self.Points2:
            res.append(pos[0] + float(point.X))
            res.append(pos[1] - float(point.Y))
            
        self._screen.coords(self._canvasID,
            *res)
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,width =self.Width, smooth=self.Smooth, splinesteps=self.Resolution)
        pass;
    
    def MoveTo(self,x,y):
        res = [x,self._screen.winfo_height()-int(y)]
        for point in self.Points2:
            res.append(x + int(point.X))
            res.append(self._screen.winfo_height() - int(y) - int(point.Y))
            
        self._screen.coords(self._canvasID,
            *res)
        pass
    pass;

class RG_App_Polygon(RG_App_Shape):
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    Color:str = "Black";
    Rotation = 0
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, points:list[RG_Vector2D] = None, color:str = None, outlineColor:str = None, outlineWidth:int = None, smooth:bool = None, resolution:int = None, offset:RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Polygon' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        if (points is None):
            points  = [RG_Vector2D(25,25)]
        elif not (type(points ) is list):
            raise RG_TypeError(points ,
                                " 'RG_App_Polygon' must have a list of RG_Vector2Ds as the argument 'points' (second argument).")
        
        self.Points2 = points
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Polygon' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Polygon' must have a str as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Polygon' must have an int as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
                
        # Smooth        
        if (smooth is None):
            smooth  = False
        elif not (type(smooth ) is bool):
            raise RG_TypeError(smooth ,
                                " 'RG_App_Polygon' must have a bool as the argument 'smooth' (fifth argument).")
        
        self.Smooth = smooth
        
        # Resolution        
        if (resolution is None):
            resolution = 12
        elif not (type(resolution ) is int):
            raise RG_TypeError(resolution ,
                                " 'RG_App_Polygon' must have a int as the argument 'resolution' (sixth argument).")
        
        self.Resolution = resolution
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Polygon' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Polygon: (ShapeID: " + str(self._canvasID) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition:RG_Position2D):
        
        absolutePosition = spritePosition + self.OffSet;
        res = [absolutePosition.X, self._screen.winfo_height()-absolutePosition.Y]
        c = Decimal(math.cos(self.Rotation))
        s = Decimal(math.sin(self.Rotation))
        for point in self.Points2:
            temp = RG_Vector2D()
            temp.X = point.X * c - point.Y * s
            temp.Y = point.X * s + point.Y * c
            res.append(absolutePosition.X + point.X)
            res.append(self._screen.winfo_height() - (absolutePosition.Y + point.Y))
        ID = self._screen.create_polygon(
            *res,
            fill=self.Color,width =self.OutlineWidth, outline= self.OutlineColor , smooth=self.Smooth, splinesteps=self.Resolution, 
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,width =self.OutlineWidth, outline= self.OutlineColor, smooth=self.Smooth, splinesteps=self.Resolution)
        pass;
    
    def MoveTo(self,x,y):
        res = [x,self._screen.winfo_height()-int(y)]
        c = Decimal(math.cos(self.Rotation))
        s = Decimal(math.sin(self.Rotation))
        for point in self.Points2:
            temp = RG_Vector2D()
            temp.X = point.X * c - point.Y * s
            temp.Y = point.X * s + point.Y * c
            res.append(x + int(temp.X))
            res.append(self._screen.winfo_height() - int(y) - int(temp.Y))
            
        self._screen.coords(self._canvasID,
            *res)
        pass
    
    def Rotate(self, angle:float, centre:RG_Point2D, spritePosition:RG_Position2D, clockwise=True):
        coef = -1
        if not (clockwise):
            coef = 1
        c = Decimal(math.cos(angle*coef))
        s = Decimal(math.sin(angle*coef))
        spritePosition.X -= centre.X
        spritePosition.Y -= centre.Y
        x = spritePosition.X * c - spritePosition.Y * s
        y = spritePosition.X * s + spritePosition.Y * c
        spritePosition.X = x
        spritePosition.Y = y
        spritePosition.X += centre.X
        spritePosition.Y += centre.Y
        self.Rotation += angle*coef
        return spritePosition
    pass

class RG_App_Ellipse(RG_App_Shape):
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, radiusX:Decimal | float = None, radiusY:Decimal | float = None, color:str = None, outlineColor:str = None, outlineWidth:int = None, offset: RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Ellipse' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        self.Dimensions = RG_SizeEllipse(radiusX,radiusY)
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Ellipse' must have a str as the argument 'color' (fourth argument).")
        
        self.Color = color
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Ellipse' must have a str as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Ellipse' must have an int as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Ellipse' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Ellipse: (ShapeID: " + str(self._canvasID) + ", Dimensions: " + str(self.Dimensions) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";

    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition: RG_Position2D) -> str:
        absolutePosition = spritePosition + self.OffSet;
        ID = self._screen.create_oval(
            absolutePosition.X, (self._screen.winfo_height()-absolutePosition.Y), 
            absolutePosition.X + Decimal(self.Dimensions.Width), (self._screen.winfo_height()-absolutePosition.Y) - Decimal(self.Dimensions.Width),
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        self._screen.coords(self._canvasID,
            pos[0],pos[1],
            pos[0] + float(self.Dimensions.Width), pos[1] + float(self.Dimensions.Height),)
        
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth)
        pass;
    
    pass;
    
class RG_App_Circle(RG_App_Ellipse):
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, radius:Decimal | float = None, color: str = None, outlineColor:str = None, outlineWidth:int = None, offset: RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Circle' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        self.Dimensions = RG_SizeCircle(radius)
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Circle' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Ellipse' must have an int as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Ellipse' must have a str as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Circle' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    pass;


class RG_App_Shader(RG_AppearanceType):
    
    _location:str = "RGame\\RGamePic.png"
    
    @property
    def Location(self):
        return self._location
    
    @Location.setter
    def Location(self, fileLocation):
        if (fileLocation is None):
            fileLocation = "RGame\\RGamePic.png"
        elif not (type(fileLocation) is str):
            raise RG_TypeError(fileLocation ,
                                " 'RG_App_Shader' must have a string as the parameter 'fileLocation'.")
        elif not (os.path.exists(fileLocation)):
            raise RG_FileExistsError(fileLocation,
                            " 'RG_App_Shader' the parameter 'fileLocation' must be a file that exists.")
        self._location = fileLocation
        self.Image = PhotoImage(file = self.Location)
        self.Dimensions = RG_Size(self.Image.width(),self.Image.height())

    
    
    def __init__(self,screen:Canvas, fileLocation:str = None, offset: RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Shader' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        self._screen = screen
        
        self.Location = fileLocation
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Shader' must have an RG_Vector2D as the argument 'offset' (last argument).")
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Shader: (ShaderID: " + str(self._canvasID) + ", File Location: " + str(self.Location) + ", OffSet: " + str(self.OffSet) + ")";

    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition: RG_Position2D) -> str:
        absolutePosition = spritePosition + self.OffSet;
        ID = self._screen.create_image(
            absolutePosition.X, (self._screen.winfo_height()-absolutePosition.Y),
            image=self.Image
            );
        return ID;
    
    
    
    def _configureGfx(self):
        
        self._screen.itemconfigure(self._canvasID,
            image=self.Image)
        pass;
    
    def Resize(self, x, y):
        xst = str(x)
        if not ("." in xst):
            xz = x
            xs = 1
        else:
            decs = xst.split(".")[1]
            xs = 10**len(decs)
            xz = xs*x
        yst = str(y)
        if not ("." in yst):
            yz = y
            ys = 1
        else:
            decs = yst.split(".")[1]
            ys = 10**len(decs)
            yz = ys*y
        self.Image = self.Image.zoom(int(xz),int(yz))
        self.Image = self.Image.subsample(int(xs),int(ys))
        self._screen.itemconfigure(self._canvasID,
            image=self.Image)
        pass;
    
    pass;