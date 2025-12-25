import os;
import shutil
try:
    paths = ["x64\\Release"];

    print("Hello (cleaner) \n");

    user = input("Please enter an additional path or exit (e): ");
    print();

    while (user != "e" and user != ""):
        
        if(os.path.exists(user)):
            
            if(not os.path.isfile(user)):
                
                paths.append(user);
                print("Path added.");
                
            else:
                
                print(user, " is not a directory but a file.");
                print();
                
                pass;
                
        else:
            
            print("Folder does not exist.");
            print();
            
            pass;
        
        user = input("Please enter an additional path or exit (e): ");
        print();
        pass;

    GoodExtentions = ["dll","lib","exp"];
    print()
    if(os.path.exists("CleanedBin")): shutil.rmtree("CleanedBin")

    os.mkdir("CleanedBin")

    for path in paths:
        
        files = os.listdir(path);
        
        for file in files:
            if(file == "All.dll"): continue;
            fileExtention = file.split(".")[-1];
            
            for extention in GoodExtentions:
                
                if(fileExtention == extention): 
                    shutil.copyfile(path + "\\" + file,"CleanedBin\\" + file);
                    print(path, ">\tCoppied: ", file);
                    break;
                
                pass;
            pass;
        
        print("\nChecked directory: ", path );
        print();
        pass;

    print("Organising...")
    print();

    files = os.listdir("CleanedBin");
    os.mkdir("CleanedBin\\dlls")

    for file in files:
        
        fileNameParts = file.split(".");
        fileNameParts.remove(fileNameParts[-1])
        fileName = ""
        for x in range(len(fileNameParts)-1):
            fileName += fileNameParts[x] + ".";
            pass;
        fileName += fileNameParts[-1];
        if(not os.path.exists("CleanedBin\\"+fileName)): os.mkdir("CleanedBin\\"+fileName);
        if(file.split(".")[-1] == "dll"): shutil.copyfile("CleanedBin\\" + file,"CleanedBin\\dlls\\" + file)
        os.rename("CleanedBin\\" + file,"CleanedBin\\" + fileName + "\\" + file)
        pass;

    print("Organising finished.")

    print("Started Physics.dll 's transfer");
    shutil.copyfile("CleanedBin\\dlls\\Physics.dll","..\\Physics\\Physics.dll")
    print("Physics.dll 's transfed\n")
    print("Started Time.dll 's transfer");
    shutil.copyfile("CleanedBin\\dlls\\Time.dll","..\\SDL\\Time.dll")
    print("Time.dll 's transfed\n")
except Exception as e:
    print(e)

input("Cleaner has ended: ");