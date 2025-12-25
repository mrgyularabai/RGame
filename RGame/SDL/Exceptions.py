class RG_Exception(Exception):
    
    Message:str = None
    
    def __init__(self, message = None) -> None:
        self.Message = message
        pass
    pass

class RG_Warning(RG_Exception):
    
    pass

class RG_TypeError(TypeError,RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_TypeWarning(TypeError,RG_Warning):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_ValueError(ValueError,RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_FileExistsError(FileExistsError,RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_FileExistsWarning(FileExistsError,RG_Warning):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_AccessError(RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_AccessWarning(RG_Warning):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass
