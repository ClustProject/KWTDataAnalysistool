from ast import Pass
import threading

import tkinter
import tkinter.font
import tkinter.ttk as ttk

import pandas as pd
from urllib import request
import os


class BackgroundTask():

    def __init__( self, taskFuncPointer ):
        self.__taskFuncPointer_ = taskFuncPointer
        self.__workerThread_ = None
        self.__isRunning_ = False

    def taskFuncPointer( self ) : return self.__taskFuncPointer_

    def isRunning( self ) : 
        return self.__isRunning_ and self.__workerThread_.isAlive()

    def start( self ): 
        if not self.__isRunning_ :
            self.__isRunning_ = True
            self.__workerThread_ = self.WorkerThread( self )
            self.__workerThread_.start()

    def stop( self ) : self.__isRunning_ = False

    class WorkerThread( threading.Thread ):
        def __init__( self, bgTask ):      
            threading.Thread.__init__( self )
            self.__bgTask_ = bgTask

        def run( self ):
            try :
                self.__bgTask_.taskFuncPointer()( self.__bgTask_.isRunning )
            except Exception as e: print (repr(e))
            self.__bgTask_.stop()

def center_window(root, width, height):
  screenwidth = root.winfo_screenwidth()
  screenheight = root.winfo_screenheight()
  size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
  root.geometry(size)

def tkThreadingTest():
    from tkinter import Tk, Label, Button, StringVar, Frame, messagebox, filedialog
    from time import sleep
     
    class UnitTestGUI:
           
        def __init__( self, master ):
            global font, font2, font3, font4, menubar
            font = tkinter.font.Font(family="Malgun Gothic", size=23, weight="bold")
            font2 = tkinter.font.Font(family="Malgun Gothic", size=8, slant="italic", weight="bold", overstrike = 'TRUE')
            font3 = tkinter.font.Font(family="Malgun Gothic", size=8, slant="italic", weight="bold")
            font4 = tkinter.font.Font(family="Times", size=9, slant="italic", weight="bold")

            
 
            self.master = master
            master.title( "Analysis tool" )


            self.testFame = Frame( background = "white",
                                         relief='ridge',
                                          height=100,
                                          width=80) 
            self.testFame.pack(side='bottom', fill='both')

            
            self.titleLabelVar = StringVar()
            self.titleLabel = Label( master, text = "데이터 다운 및 전처리 자료 생성",
                                  font=font, 
                                  foreground='white',
                                  background='gray20',
                                  relief="flat",
                                  bd = 3,
                                  padx = 40,
                                  pady = 3)
            self.titleLabel.pack(fill='both')

            self.fileLabelVar = StringVar()
            self.fileLabel = Label( master, 
                                       bg = 'white',
                                       foreground='black',
                                       pady=4,
                                       font=("Malgun Gothic", 8, "bold"),
                                       borderwidth=2)
            self.fileLabel.pack(fill='both')

            self.testLabelVar = StringVar()
            self.testLabel = Label( self.testFame, 
                                       bg = 'white',
                                       foreground='black',
                                       pady=4,
                                       font=("Malgun Gothic", 8, "bold"),
                                       borderwidth=2)
            self.testLabel.pack()

            self.test2LabelVar = StringVar()
            self.test2Label = Label( master, 
                                       font = font4,
                                       bg = 'white',
                                       foreground='black',
                                       pady=4,
                                       borderwidth=2)
            self.test2Label.configure(text="Made By. Yong-Lim")
            self.test2Label.place(x=390, y=420)


            self.fileButton = Button( 
                self.master, 
                text="Load MetaData", 
                background = 'white',
                fg = 'black',
                activebackground = 'gray',
                relief = 'raised',
                bd = 2.5,
                activeforeground = 'white',
                overrelief = 'groove',
                width = 15, 
                height = 3,
                font=font3,
                command=self.onFileClicked )
            self.fileButton.pack(pady = 5)

            self.threadedButton = Button( 
                self.master, 
                text="Data Download", 
                background = 'white',
                fg = 'black',
                activebackground = 'gray',
                relief = 'sunken',
                bd = 2.5,
                activeforeground = 'white',
                overrelief = 'groove',
                width = 15, 
                height = 3,
                state = 'disabled',
                font=font2,
                command=self.onThreadedClicked )
            self.threadedButton.pack(pady = 5)

            self.hourButton = Button( 
                self.master, 
                text="Hour Average", 
                background = 'white',
                fg = 'black',
                activebackground = 'gray',
                relief = 'sunken',
                bd = 2.5,
                activeforeground = 'white',
                overrelief = 'groove',
                width = 15, 
                height = 3,
                state = 'disabled',
                font=font2,
                command=self.onThreaded4Clicked )
            self.hourButton.pack(pady = 5)

            self.dayButton = Button( 
                self.master, 
                text="Daily Average", 
                background = 'white',
                fg = 'black',
                activebackground = 'gray',
                relief = 'sunken',
                bd = 2.5,
                activeforeground = 'white',
                overrelief = 'groove',
                width = 15, 
                height = 3,
                state = 'disabled',
                font=font2,
                command=self.onThreaded3Clicked )
            self.dayButton.pack(pady = 5)

            self.weekButton = Button( 
                self.master, 
                text="Weekly Average", 
                background = 'white',
                fg = 'black',
                activebackground = 'gray',
                relief = 'sunken',
                bd = 2.5,
                activeforeground = 'white',
                overrelief = 'groove',
                width = 15, 
                height = 3,
                state = 'disabled',
                font=font2,
                command=self.onThreaded2Clicked )
            self.weekButton.pack(pady = 5)


            self.bgTask = BackgroundTask( self.APIProcess )

        def close( self ) :
            MsgBox = messagebox.askquestion ('Exit App','Really Quit?',icon = 'info')
            if MsgBox == 'yes':
               try: self.bgTask.stop()
               except: pass
               try: self.bg2Task.stop()
               except: pass
               self.master.quit()
            else:
               messagebox.showinfo('Welcome Back','Welcome back')


        def onFileClicked( self ):
            global metadata
            root.file = filedialog.askopenfile(
            initialdir='path', 
            title='select file', 
            filetypes=(('csv files', '*.csv'), 
            ('all files', '*.*')))
    
            A = "Load Complete!"   
            B = '0126'

            vvv = str(root.file)
            self.weekButton['state'] = tkinter.DISABLED
            self.dayButton['state'] = tkinter.DISABLED
            self.hourButton['state'] = tkinter.DISABLED
            if(vvv == 'None'):
                messagebox.showerror("Load...",'Cansle')
  
            else:
                self.fileLabel.configure(text="Metadata path: " + root.file.name)
                self.fileLabel['relief'] = tkinter.FLAT
                self.fileLabel['background'] = 'light gray'
                metadata = root.file.name
                metadata = pd.read_csv(metadata, dtype=str, encoding='CP949')
                messagebox.showinfo("Metadata Load...",A)
                AA = 1

                if(B == '0126'):
                     self.threadedButton['state'] = tkinter.NORMAL 
                     self.threadedButton['relief'] = tkinter.RAISED
                     self.threadedButton['font'] = font3
                     
                else:
                     self.threadedButton['state'] = tkinter.DISABLED  
        

        def onThreadedClicked( self ):
            try: self.bgTask.start()
            except: pass

        def onThreaded2Clicked( self ):
            try: self.bg2Task.start()
            except: pass

        def onThreaded3Clicked( self ):
            try: self.bg3Task.start()
            except: pass

        def onThreaded4Clicked( self ):
            try: self.bg4Task.start()
            except: pass

        def APIProcess( self, isRunningFunc=None) :
            global metadata
            try:
               if not isRunningFunc() :
                   return
            except : pass

            self.threadedButton['state'] = tkinter.DISABLED
            self.fileButton['state'] = tkinter.DISABLED
            self.weekButton['state'] = tkinter.DISABLED
            self.dayButton['state'] = tkinter.DISABLED
            self.hourButton['state'] = tkinter.DISABLED

            aaa = metadata.columns
            aaa = str(aaa)[6:-17]
            bbb = ['측정기시리얼넘버', '시작일(YYYY-MM-DD)', '종료일(YYYY-MM-DD)']
            bbb = str(bbb)
            if (aaa == bbb):
                A = 0
                h = metadata.shape[0]
        
                if (h < 1):
                     try:
                        if not isRunningFunc() :
                            return
                     except : pass
                     messagebox.showerror("ERROR",'DATA EMPTY')
                     self.threadedButton['state'] = tkinter.NORMAL
                     self.fileButton['state'] = tkinter.NORMAL
            
                else:
                     path = './'
                     file_list = os.listdir(path)
                     file_list_py = [file for file in file_list if file.endswith('.xlsx')]

                     search = ".xlsx"
                     for i, word in enumerate(file_list_py):
                        if search in word: 
                            file_list_py[i] = word.strip(search)
                     a=0
                     while(a < len(file_list_py)):
                        metadata = metadata[~metadata['측정기시리얼넘버'].str.contains(file_list_py[a], na=False, case=False)]
                        a = a + 1
                     metadata = metadata.reset_index()
                     self.testLabel.configure(text="Data Downloading... ")  
                     progressbar = ttk.Progressbar(self.testFame, style='yong.Horizontal.TProgressbar', length=150, maximum=150, mode="indeterminate")
                     progressbar.start(10)
                     progressbar.pack(pady = 8)  
                     if(metadata.shape[0] != 0):       
                        while A < metadata.shape[0]:
                            try:
                                if not isRunningFunc() :
                                    return
                            except : pass
    
        
                            check = metadata['종료일(YYYY-MM-DD)'][A]
                            
                            if(pd.isna(check)):
                                Z = A + 1
                                Z = str(Z)
                                
                            else:
                                Z = A + 1
                                Z = str(Z)

                                main_url = '*'  #보안사항 가명 처리
        
                                serial = metadata.측정기시리얼넘버 [A]
                                serial1 = 'serial'+ '=' + serial                                           #시리얼번호
            
                                from datetime import datetime
        
                                startTime = metadata['시작일(YYYY-MM-DD)'][A]
                                startTime = datetime.strptime(startTime, '%Y-%m-%d').strftime('%Y/%m/%d')
                                startTime = 'startTime=' + startTime + '-00:00:00'                                      #시작시간
        
                                endTime = metadata['종료일(YYYY-MM-DD)'][A]
                                endTime = datetime.strptime(endTime, '%Y-%m-%d').strftime('%Y/%m/%d')
                                endTime = 'endTime=' + endTime + '-23:59:59'                                           #종료시간

                                
                                #standard = 'standard=sum'                                                         #시간평균 설정
                                standard = 'standard=5m-avg-none'                                                         #시간평균 설정
                                #standard = 'standard=1h-avg-none' 
                                #standard = 'standard=1d-avg-none' #정확도가 떨어짐
        
                                deviceType = 'deviceType=iaq'                                                     #장비종료
            
        
                                variable = startTime + '&' +  endTime + '&' + standard + '&' + serial1 + '&' + deviceType
        
                                api_url = main_url + '?' + variable
        
                                file = serial
                                file = './' + file + '.' + 'xlsx'
            
                                request.urlretrieve(api_url, file)
                            try:
                                if not isRunningFunc() :
                                    return
                            except : pass
    
                            A = A + 1 
                        progressbar.destroy()
                        progressbar = ttk.Progressbar(self.testFame,  length=150, maximum=150, value=150)
                        self.testLabel.configure(text="Done!")
                        progressbar.pack(pady = 8)
                        A = "Data Download Complete!"
                        messagebox.showinfo("File Load",A)
                     else:
                        progressbar.destroy()
                        self.testLabel.configure(text="Done!")
                        progressbar = ttk.Progressbar(self.testFame,  length=150, maximum=150, value=150)
                        progressbar.pack(pady = 8)
                        A = "Data already exists!"
                        messagebox.showinfo("File Load",A)
                
                progressbar.destroy()
                self.testLabel.configure(text="")
                self.threadedButton['state'] = tkinter.NORMAL
                self.fileButton['state'] = tkinter.NORMAL
                self.weekButton['state'] = tkinter.NORMAL
                self.weekButton['relief'] = tkinter.RAISED 
                self.weekButton['font'] = font3
                self.dayButton['state'] = tkinter.NORMAL
                self.dayButton['relief'] = tkinter.RAISED 
                self.dayButton['font'] = font3
                self.hourButton['state'] = tkinter.NORMAL
                self.hourButton['relief'] = tkinter.RAISED 
                self.hourButton['font'] = font3
                
            else:
                 messagebox.showerror("Data Download...","Data Download Fail\nIt doesn't fit the style.\nPlease fill it out according to the form.") 
                 metadataaa = pd.DataFrame([], columns=['측정기시리얼넘버',
                                                                                           '시작일(YYYY-MM-DD)',
                                                                                           '종료일(YYYY-MM-DD)'])
                 metadataaa.to_csv('./[SAMPLE] MetaData.CSV' ,index=False, encoding='cp949')
                 self.threadedButton['state'] = tkinter.NORMAL
                 self.fileButton['state'] = tkinter.NORMAL


        

    root = Tk()    
    root.configure(bg='white')
    s = ttk.Style()
    s.theme_use('alt')
    s.configure("yong.Horizontal.TProgressbar", foreground='#458577', background='#458577')
    center_window(root, 500, 450)
    root.resizable(width=False, height=False)
    gui = UnitTestGUI( root )
    root.protocol( "WM_DELETE_WINDOW", gui.close )
    root.mainloop()

if __name__ == "__main__": 
    tkThreadingTest()