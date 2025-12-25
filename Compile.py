import os
import re

def Import(name):
    global pre
    path = os.path.join(pre,name)
    if(os.path.isdir(path)):
        print(path)
        ImportDir(name)
        return
    print(path+".py")
    ImportModule(name+".py")
    
def ImportDir(dir):
    global pre
    oldPre = pre
    pre = os.path.join(pre,dir)
    DoImportDir()
    pre = oldPre

def DoImportDir():
    global pre
    initFile = open(os.path.join(pre, "__init__.py"), "r")
    fileContent = initFile.read()
    initFile.close()
    fileContent = fileContent.strip()
    refs = GetReferences(fileContent)
    for ref in refs:
        Import(ref)
        
def GetReferences(fileContent):
    references = re.finditer(r"from \.(.(?!import))+\simport\*",fileContent)
    res = []
    for ref in references:
        span = ref.span()
        fullRef = fileContent[span[0]:span[1]]
        fullRef = fullRef.replace("from .", "")
        fullRef = fullRef.replace(" import*", "")
        res.append(fullRef)
    return res

def GetText(fileContent:str):
    references = re.finditer(r"# Imports((.|\s)(?!# End Imports))+\s# End Imports",fileContent)
    res = fileContent
    for ref in references:
        span = ref.span()
        fullRef = fileContent[span[0]:span[1]]
        res = res.replace(fullRef, "")
        res = res.strip()
    return res
        
def ImportModule(mod):
    global pre
    global result
    path = os.path.join(pre,mod)
    module = open(path, "r")
    fileContent = module.read()
    module.close()
    result += "\n"+GetText(fileContent)

result = ""
pre = os.path.join(".","")
Import("RGame")
resFile = open("RGameLib.py", "w+")
resFile.seek(0)
resFile.write(result)
resFile.close()
input("done: ")