# Imports
from RGame.MainScr import*
from RGame.SDL.Log import*
# End Imports


class Run:
    def __init__(self, main:RG_MainScript) -> None:
        """
        Run is a functor which runs your program with your custom main class

        :param main: Your Main class which derives from RG_MainScript
        """
        
        import os
        os.system("color 00")
        try:
            main.StartRGame()
            print("Started | Main\n")
            if(main.Started):
                main.MainPhysics.End()
        except RG_Exception as e:
            if not (e.Value is None):
                LogFatal(e.Message, e.Value)
            else: 
                LogFatal(e.Message)
        except Exception as e:
            if(len(e.args)>0):
                LogFatal(e.args[0])
        input("\nFinished | Main (press enter to close window): ")