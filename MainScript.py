from Script import*
from RGame import*

# This is the rest of the code
# Do not worry if you do not understand any of it
# We will cover this later.

class Player(RG_Script):
    
    def Start(self):
        self.Speed = 7.5
        self.MainWindow.Bind("w", self.Up)
        self.MainWindow.Bind("<KeyRelease-w>", self.UpR)
        self.MainWindow.Bind("s", self.Down)
        self.MainWindow.Bind("<KeyRelease-s>", self.DownR)
        self.MainWindow.Bind("d", self.Right)
        self.MainWindow.Bind("<KeyRelease-d>", self.RightR)
        self.MainWindow.Bind("a", self.Left)
        self.MainWindow.Bind("<KeyRelease-a>", self.LeftR)
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.gun = Gun(self.MainScript,appearance=RG_App_Circle(self.MainWindow.Screen))
        self.gun.Position = self.Position
        self.gun.rateOfFire = 1
        self.gun.reloadSpeed = 2
        self.gun.magSize = 6
        self.gun.ammo = RandomInt(0, 6)
        pass
    
    def Up(self, args):
        self.up = True
        
    def UpR(self, args):
        self.up = False
        
    def Down(self, args):
        self.down = True
        
    def DownR(self, args):
        self.down = False
        
    def Right(self, args):
        self.right = True
        
    def RightR(self, args):
        self.right = False
        
    def Left(self, args):
        self.left = True
        
    def LeftR(self, args):
        self.left = False
        
    def PhysicsTick(self, deltaTime):
        self.Bounce()
        if(self.MainScript.GameOverTxt.Activated): 
            self.Velocity.SetSpeed(0)
            return
        if(self.up):
            self.Velocity.Y = 1
        if(self.down):
            self.Velocity.Y = -1
        if not (self.up or self.down):
            self.Velocity.Y = 0
        if(self.right):
            self.Velocity.X = 1
        if(self.left):
            self.Velocity.X = -1
        if not (self.left or self.right):
            self.Velocity.X = 0
        if(self.Velocity.GetlengthSqr() != 0):
            self.Velocity.SetSpeed(self.Speed)
        
        if(self.MainWindow.Mouse.Left):
            self.gun.Shoot(self.MainWindow.Mouse.Position)
        if self.MainScript.gun is None:
            return
        if self.MainScript.gun.Position.VectorTo(self.Position).GetLength() < 25 and not (self.MainScript.gun is self.gun):
            self.gun.Deactivate()
            self.gun = self.MainScript.gun
            self.gun.Position = self.Position
        
    def Render(self):
        if self.gun.Appearance.Visible:
            self.gun.Appearance.Visible = False
        pass
        
    pass

class Zombie(RG_Script):
    
    def Start(self):
        self.Speed = 3
        pass
    
    def PhysicsTick(self, deltaTime):
        if(self.MainScript.GameOverTxt.Activated): 
            self.Velocity.SetSpeed(0)
            return
        self.Velocity = self.Position.VectorTo(self.MainScript.Player.Position)
        self.Velocity = self.Velocity.ToVelocity()
        
        if not (self.Velocity.GetLength() < self.Appearance.Dimensions.Radius + self.MainScript.Player.Appearance.Dimensions.Radius):
            self.Velocity.SetSpeed(self.Speed)
        else:
            self.Velocity.SetSpeed(0)
            self.Position = self.MainScript.Player.Position
            self.MainScript.GameOverTxt.Activate()
        pass
        
    def Render(self):
        pass
        
    pass

class Bullet(RG_Script):
    
    def Start(self):
        self.Speed = 10
        pass
    
    def PhysicsTick(self, deltaTime): 
        self.Velocity.SetSpeed(6)
        zombs = self.MainScript.Zombies
        for Zomb in zombs:
            if(self.Position.VectorTo(Zomb.Position).GetLength() < Zomb.Appearance.Dimensions.Radius):
                Zomb.Deactivate()
                self.MainScript.Zombies.remove(Zomb)
                self.Deactivate()
                self.MainScript.Bullets.remove(self)
                return
        if(self.Bounce()):
            self.Deactivate()
            self.MainScript.Bullets.remove(self)
        pass
        
    def Render(self):
        pass
        
    pass

class Gun(RG_Script):

    ROFTimer = RG_TimePoint()
    reloadTimer = RG_TimePoint()
    startedReload = False
    
    rateOfFire = 2
    reloadSpeed = 1
    magSize = 3
    ammo = 3
    bulletSpeed = 25
        
    
    def PhysicsTick(self, deltaTime):
        
        if(self.ammo == 0 and not self.startedReload):
            self.startedReload = True
            self.reloadTimer.Now()
            
        if(self.reloadSpeed > self.reloadTimer.Diff() and self.startedReload):
            return
        
        if(self.startedReload):
            self.ammo = self.magSize
            self.startedReload = False

        
        
    
    def Shoot(self, targetPosition):
        
        if(self.reloadSpeed > self.reloadTimer.Diff() and self.startedReload):
            return
        
        if self.ammo == 0: 
            return
        if self.ROFTimer.Diff() < (1/self.rateOfFire): return
        
        self.ammo -= 1
        self.Pos = RG_Position2D(self.Position.X, self.Position.Y)
        self.Vel = self.Position.VectorTo(targetPosition).ToVelocity()
        self.Vel.SetSpeed(self.bulletSpeed)
        self.MainScript.Bullets.append(
            Bullet(self.MainScript,
                    position = self.Pos,
                    velocity = self.Vel,
                    appearance = RG_App_Circle(self.MainWindow.Screen, radius = 2, color = "grey")))
        
        self.ROFTimer.Now()
        
        

def PlayerSetUp(self):
        
    # Making an appearance (a circle)
    playerApp = RG_App_Circle(
            self.MainWindow.Screen,
            radius = 25,
            color = "light yellow",
            outlineWidth = 1,
            offset = RG_Vector2D(25,25)
            )
        
    # Making a position (the centre of the screen)
    playerPos = RG_Position2D(
            self.MainWindow.WindowWidth/2,
            self.MainWindow.WindowHeight/2)
        
    # Creating the actual player with the position and appearance
    self.Player = Player(self, 
            position = playerPos, 
            appearance = playerApp)
        
def TextsSetUp(self):
        
    self.LvlTxtPos = RG_Position2D(335, self.MainWindow.WindowHeight - 10)
    self.LvlTxt = RG_Label(self, self.LvlTxtPos, fontSize=23, text = "Level 1")

    # Same thing with the number of ammo remaining
    self.AmmoTxtPos = RG_Position2D(335, self.MainWindow.WindowHeight-52)
    self.AmmoTxt = RG_Label(self, self.AmmoTxtPos, fontSize=17, text = "Ammo: 1")

    # Time left before next level
    self.TimeTxtPos = RG_Position2D(335, self.MainWindow.WindowHeight - 35)
    self.TimeTxt = RG_Label(self, self.TimeTxtPos, fontSize=17, text = "0")
    
    # Rate of Fire
    self.FireRatePos = RG_Position2D(485, self.MainWindow.WindowHeight - 52)
    self.FireRate = RG_Label(self, self.FireRatePos, fontSize=17, text = "1")

    # The Game Over text
    self.GameOverTxtPos = RG_Position2D(self.MainWindow.WindowWidth/2-100, self.MainWindow.WindowHeight/2)
    self.GameOverTxt = RG_Label(self, self.GameOverTxtPos , fontSize=50, text = "Game Over!", fontColor="Red")
    self.GameOverTxt.Deactivate()

def CreateZombie(self):
    height = RandomInt(0,self.MainWindow.WindowHeight)
    zombPos = RG_Position2D(0, height)
    zombApp = RG_App_Circle(self.MainWindow.Screen,
                            radius = 25,
                            color = "green",
                            outlineWidth = 2,
                            offset = RG_Vector2D(25,25))
    zomb = Zombie(self,
                    position = zombPos,
                    appearance = zombApp
                        )
    zomb.Speed = self.ZombieSpeed
    self.Zombies.append(zomb)
    
def DataInit(self):
    self.level = 1 
    self.TimePoint = RG_TimePoint() # The timer used to measure the time elapsed since the level started

    self.spawned = False # weather the zombies have been spawned for the level
    self.Zombies = [] # A list to store the zombies in

    self.Bullets = []# A list to store the bullets in
    self.ZombieSpeed = 1 
    self.gun = None
    
def CreateGun(self, position):
    self.oldGun = self.Player.gun
    self.gun = Gun(self, position = position, appearance=RG_App_Rectangle(self.MainWindow.Screen, RG_Size(20,10),color="Grey"))


# Saying that this bit of code and memory is called MainScript
# and also that MainScript is a type of 'RG_MainScript' meaning it
# can be run



# The first thing that happens in the program
def Main(self):
    # Setting up window
    self.MainWindow.WindowTitle = "The Zombie Game"
    self.MainWindow.WindowBackground = "light green"
    
    PlayerSetUp(self) # Making a player
    TextsSetUp(self) # Making all the texts
    
    # Making variables
    DataInit(self)
    self.levelDuration = 10 # The time in seconds for how long a level lasts
    
    

    
def PhysicsTick(self, deltatime):
    
    # If zombies have not been spawned spawn them
    if not self.spawned:
        
        # Do this code for how many numbers there are between 0 and 'self.level':
        # I.e. Do this 'self.level' times. I.e. create that many zombies
        for x in range(self.level):
            CreateZombie(self) # Creating a zombie
        
        self.spawned = True

def Render(self):
    
    # check if we need to move onto the next level
    NoZombiesLeft = len(self.Zombies) == 0
    NoTimeLeft = self.TimePoint.Diff() >= self.levelDuration
    
    if NoTimeLeft or NoZombiesLeft:
        # Do stuff to set up next level
        self.level += 1
        self.LvlTxt.Appearance.Text = "Level " + str(self.level)
        self.spawned = False
        self.TimePoint.Now() 
        if (not (self.gun is self.Player.gun)) and self.gun != None:
            self.gun.Deactivate()
        SpawnGun(self, RG_Position2D(
            RandomInt(0,self.MainWindow.WindowWidth),
            RandomInt(0,self.MainWindow.WindowHeight)))
        self.ZombieSpeed += 0.3

    # Display the amount of ammo remaining
    self.AmmoTxt.Appearance.Text = "Ammo: " + str(self.Player.gun.ammo) + f"/{self.Player.gun.magSize}"
    self.FireRate.Appearance.Text = "Fire Rate: " + str(self.Player.gun.rateOfFire)
    
    # Display the time left before next level.
    timeLeft = self.levelDuration - self.TimePoint.Diff()
    self.TimeTxt.Appearance.Text =  "Time Remaining: "+ format(timeLeft, ".2f")


def SpawnGun(self, position):
    CreateGun(self, position)
    self.gun.rateOfFire = self.oldGun.rateOfFire + 1
    self.gun.magSize = self.oldGun.rateOfFire + 1
    self.gun.ammo = RandomInt(0,self.gun.magSize)
    self.gun.reloadSpeed = 2
    pass

Run(RG_MainScript(None, Main, PhysicsTick, Render))