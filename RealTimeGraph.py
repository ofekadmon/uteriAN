import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import numpy as np
from tkinter import StringVar
from tkinter.ttk import Combobox

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open("Desktop\\Project\\ExampleDataFile1.txt","r").read()
    dataList = pullData.split('\n')
    #count = dataList[1].count(',')
#print(count)
#print(dataList[1])
    dataList = np.delete(dataList, (0), axis=0)
#print(dataList[0])

    meanList = []
    columns = []
    for j in range (0,len(dataList)):
        if len(dataList[j]) > 1:
            columns=dataList[j].split(',')
            for i in range(0, len(columns)): 
                columns[i] = int(columns[i])
            meanList.append(np.mean(columns[0:8]))

    #print(meanList)
    #print(len(meanList))

 #   pullData = open("Desktop\\Project\\sampleText.txt","r").read()
  #  dataList = pullData.split('\n')
   # xList = []
    #yList = []
    #for eachLine in dataList:
     #   if len(eachLine) > 1:
      #      x, y = eachLine.split(',')
       #     xList.append(int(x))
        #    yList.append(int(y))

    a.clear()
    a.plot(meanList)

    
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "UteriAN Real Time Monitoring")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="The name of the patient :",font=('calibri', 14))
        label.place(x=self.winfo_screenmmheight()/2 + 50 , y=50)
        e = tk.Entry(self)
        e.place(x=self.winfo_screenmmheight()/2+250,y=55,height=25,width=150)

        label = tk.Label(self, text="The name of the test :",font=('calibri', 14))
        label.place(x=self.winfo_screenmmheight()/2 + 50, y=80)
        e = tk.Entry(self)
        e.place(x=self.winfo_screenmmheight()/2+250,y=85,height=25,width=150)

        label = tk.Label(self, text="The date of the test :",font=('calibri', 14))
        label.place(x=self.winfo_screenmmheight()/2 + 50, y=110)
        var=StringVar()
        var.set("1")
        data=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',
        '16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        cb=Combobox(self, values=data)
        cb.place(x=self.winfo_screenmmheight()/2+250,y=115,height=25,width=40)  
        var.set("January")
        data=(' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June',  
                          ' July',  
                          ' August',  
                          ' September',  
                          ' October',  
                          ' November',  
                          ' December')
        cb=Combobox(self, values=data)
        cb.place(x=self.winfo_screenmmheight()/2+292,y=115,height=25,width=90)  
        var.set("2020")
        data=(' 2020',' 2021',' 2022')
        cb=Combobox(self, values=data)
        cb.place(x=self.winfo_screenmmheight()/2+384,y=115,height=25,width=60)  
        #e = tk.Entry(self)
        #e.place(x=self.winfo_screenmmheight()/2+250,y=115,height=25,width=150)

        label = tk.Label(self, text="The type of the test :",font=('calibri', 14))
        label.place(x=self.winfo_screenmmheight()/2 +50, y=140)
        #var=StringVar()
        var.set("one")
        data=("one", "two", "three", "four")
        cb=Combobox(self, values=data)
        cb.place(x=self.winfo_screenmmheight()/2+250,y=145,height=25,width=150)  

        #e = tk.Entry(self)
        #e.place(x=self.winfo_screenmmheight()/2+250,y=145,height=25,width=150)

        #button = ttk.Button(self, text="Visit Page 1",
        #                    command=lambda: controller.show_frame(PageOne))
        #button.pack()

        #button2 = ttk.Button(self, text="Visit Page 2",
        #                    command=lambda: controller.show_frame(PageTwo))
        #button2.pack()

        # style = ttk.Style()
        style = ThemedStyle(self)
        style.set_theme("plastik")
        style.configure('TButton', font = ('calibri', 20, 'bold'), borderwidth = '10',
                        foreground='blue',width=20)
        button = ttk.Button(self, text="Start Monitoring",
                    command=lambda: controller.show_frame(PageThree))
        button.place(x=self.winfo_screenmmheight()+20,y=self.winfo_screenmmwidth()-40)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
width_2 = app.winfo_screenwidth()/2
height = app.winfo_screenheight()
app.wm_geometry(str(int(width_2)) + 'x' + str(int(height)) + '+0+0')
#style.use('dark_background')
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()