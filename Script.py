from RGameLib import *

class ScriptTest(RG_Script):
    color = [100,100,100]
    speedcoef = 0.1
    
    def PhysicsTick(self, deltaTime):
        self.speedcoef = 0.1
        self.Bounce()
        
    def Render(self):
        #R
        self.color[0] += self.speedcoef*1;
        if(self.color[0] > 254):
            self.color[0] = 0
        #G
        self.color[1] += self.speedcoef*2;
        if(self.color[1] > 254):
            self.color[1] = 0
        #B
        self.color[2] += self.speedcoef*1;
        if(self.color[2] > 254):
            self.color[2] = 0
        self.c = RGBtoColor(int(self.color[0]),int(self.color[1]),int(self.color[2]))
        self.Appearance.Color = self.c
