
import os
from tkinter import filedialog

class Scaffold():
    def __init__(self):
        self.files = []
        self.layout_fields = []
        self.menu_options = ["Add/Remove", "Edit Layout", "Display", "Export", "Quit"]
        self.files_count = 0
            
        self.showMenu()
            
    def showMenu(self):
        mc = 1
        for menu in self.menu_options:
            print( str(mc)+". "+ menu )
            mc+=1
            
        opt = input('Option : ')
        if opt == 1:
            self.addRemoveScreen()
        elif opt == 2:
            self.editLayoutScreen()
        elif opt == 3:
            self.displayTableScreen()
        elif opt == 4:
            self.exportTable()
        else:
            pass
        
                
    def addRemoveScreen(self):
        self.files_count = input('How Many files (number) : ')
        
        for i in range(0, self.files_count):
            _file = filedialog.askopenfilename()
            self.files.append(_file)
    
            
    def editLayoutScreen(self):
        opt = 0
        self.ShowFiles()
        
    def displayTableScreen(self):
        pass
    def ShowFiles(self):
        print('------ Files ------')
        _i = 0
        for file in self.files:
            print( '['+str(_i)+'] ' + os.path.basename(file))
            _i+=1
        print('------------------')
    def exportTable(self):
        pass
    





Scaffold()