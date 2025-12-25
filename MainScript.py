from Script import*
from RGameLib import*


def Main(self):
    self.res = 1
    self.resS = 0.25
    self.resMax = 5
    self.MainWindow.WindowBackGround = "White";
    self.MyBalls:list[ScriptTest] = []
    for x in range(0,50):
        vel = RG_Velocity2D( RandomFloat(-3,3), RandomFloat(-3,3));
        pos = RG_Position2D(self.MainWindow.WindowWidth/2-25, self.MainWindow.WindowHeight/2-25)
        radius = RandomInt(10,30);
        if(x % 2 == 0): color = "Orange" 
        else: color = "Blue" 
        self.MyBalls.append(ScriptTest(self,pos,vel, RG_App_Circle(self.MainWindow.Screen,radius,color,"Blue",2,RG_Vector2D(radius,radius)),str(x)));
    for ball in self.MyBalls:
        ball.Appearance.Render()
        pass
    self.text = RG_Label(self,RG_Position2D(500,500),None,"Hello World","Calibri",20,"blue",True,True,True,True)
    self.text.Appearance.Render()
    self.timer = RG_TimePoint()
    self.line = RG_Line(self,RG_Position2D(275,475),None,[RG_Vector2D(25,25),RG_Vector2D(75,-25),RG_Vector2D(125,25),RG_Vector2D(175,-25),RG_Vector2D(200,0)],"Red",3,True)
    self.im = RG_Image(self,RG_Position2D(100,100))
    pass;

def PhysicsTick(self, deltatime):
    self.line.Appearance.Resolution = int(self.res)
    self.res += self.resS
    if(self.res > self.resMax):
        self.resS *= -1
    elif(1 > self.res):
        self.resS *= -1

    pass;
    self.Switched = False
    if(int(self.timer.Diff())%2 and not self.Switched):
        self.text.Appearance.Underline = not self.text.Appearance.Underline
        if(self.text.Appearance.Color == "Red"): self.text.Appearance.Color = "Blue"
        else:self.text.Appearance.Color = "Red"
        self.Switched = True
    else: self.Switched = False
    self.Switched2 = False
    if(not int(self.timer.Diff())%2 and not self.Switched2):
        self.text.Appearance.Weight = not self.text.Appearance.Weight
        self.text.Appearance.Overstrike = not self.text.Appearance.Overstrike
        self.Switched2 = True
    else:
        self.Switched2 = False

def Render(self):
    self.im.Appearance.Render()
    pass;

mainScript = RG_MainScript(main=Main, physicsTick=PhysicsTick, render=Render)
Run(mainScript)