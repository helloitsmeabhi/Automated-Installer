
import tkinter.ttk as ttk
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from modules.logic import *
import customtkinter
import tkinterDnD
import os


class UiDesign(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        #initial Code And Heading
        self.after(250, lambda :self.iconbitmap('./resources/icons/Paradox.ico')) 
        self.resizable(0,0)
        self.title("Programming Tools Installer")
        self.geometry(f"{1100}x{580}")

        
        self.grid_rowconfigure(0, weight=1)
        

   
        
        self.logo_image = customtkinter.CTkImage(Image.open( "./resources/icons/Paradox.png"), size=(75, 50))
        #Navigation Frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.ide_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="IDE's",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.ide_button_event)
        self.ide_button.grid(row=2, column=0, sticky="ew")
        
        self.gemini_button = customtkinter.CTkButton(self.navigation_frame,corner_radius=0, height=40, border_spacing=10, text="Gemini",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.gemini_button_event)
        self.gemini_button.grid(row=3, column=0, sticky="ew")

        
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=5, fg_color="transparent")
        self.labelfont = customtkinter.CTkFont("Consolas",50)
        self.buttonfont= customtkinter.CTkFont("Consolas",25)
       
        self.home_label= customtkinter.CTkLabel(self.home_frame,text="Programming\nLanguages\n",font=self.labelfont,anchor="center")
        self.home_label.grid(row=0,column=2,pady=(20,0))
        self.home_button1 = customtkinter.CTkButton(self.home_frame,width=100,height=100, text="Java",font=self.buttonfont,command=install_java)
        self.home_button1.grid(row=1, column=0, padx=(20,80), pady=10)
        self.home_button2 = customtkinter.CTkButton(self.home_frame,width=100,height=100, text="Python",font=self.buttonfont)
        self.home_button2.grid(row=1, column=1, padx=(5,5), pady=10)
        self.home_button3 = customtkinter.CTkButton(self.home_frame,width=100,height=100, text="C/C++",font=self.buttonfont,command=install_cpp_c)
        self.home_button3.grid(row=1, column=2, padx=(5,5), pady=10)
        self.home_button4 = customtkinter.CTkButton(self.home_frame,width=100,height=100, text="Node.JS",font=self.buttonfont,command=install_node)
        self.home_button4.grid(row=1, column=3, padx=(5,5), pady=10)
        self.home_button5 = customtkinter.CTkButton(self.home_frame,width=100,height=100, text="C#",font=self.buttonfont)
        self.home_button5.grid(row=1, column=4, padx=(80,20), pady=10)
        
        #IDE Frame
        self.ide_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ide_label = customtkinter.CTkLabel(self.ide_frame,text="IDE's\n\n",font=self.labelfont,anchor="center")
        self.ide_label.grid(row=0,column=2,pady=(20,0))
        self.ide_button1 = customtkinter.CTkButton(self.ide_frame,width=100,height=100,text="Visual\nStudio Code",font=self.buttonfont,anchor="center",command=vscode)
        self.ide_button1.grid(row=1, column=0, padx=(50,20), pady=10)
        self.ide_button2 = customtkinter.CTkButton(self.ide_frame,width=100,height=100,text="Visual\n Studio ",font=self.buttonfont,anchor="center")
        self.ide_button2.grid(row=1, column=1, padx=(20,20), pady=10)
        self.ide_button3 = customtkinter.CTkButton(self.ide_frame,width=100,height=100,text=" PyCharm ",font=self.buttonfont,anchor="center")
        self.ide_button3.grid(row=1, column=2, padx=(20,20), pady=10)
        self.ide_button4 = customtkinter.CTkButton(self.ide_frame,width=100,height=100,text="Jupyter\nNoteBook",font=self.buttonfont,anchor="center")
        self.ide_button4.grid(row=1, column=3, padx=(20,20), pady=10)
        self.ide_button5 = customtkinter.CTkButton(self.ide_frame,width=100,height=100,text="Eclipse",font=self.buttonfont,anchor="center")
        self.ide_button5.grid(row=1, column=4, padx=(20,20), pady=10)
        #Gemini Frame
        self.gemini_frame=customtkinter.CTkFrame(self,corner_radius=0,fg_color="transparent")
        self.gemini_label=customtkinter.CTkLabel(self.gemini_frame,text="Gemini",font=self.labelfont,anchor="center")
        self.gemini_label.grid(row=0,column=0,padx=(20,0))
        self.gemini_outlabel=customtkinter.CTkLabel(self.gemini_frame,text="Output",font=self.buttonfont,anchor="center")
        self.gemini_outlabel.grid(row=1,column=0,padx=(20,0))
        self.gemini_outtextbox=customtkinter.CTkTextbox(self.gemini_frame,width=500,font=(customtkinter.CTkFont("Consolas",15)))
        self.gemini_outtextbox.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.gemini_inplabel=customtkinter.CTkLabel(self.gemini_frame,text="Input",font=self.buttonfont,anchor="center")
        self.gemini_inplabel.grid(row=3,column=0,padx=(20,0))
        self.gemini_inptextbox=customtkinter.CTkTextbox(self.gemini_frame,width=250, height=50,font=(customtkinter.CTkFont("Consolas",15)))
        self.gemini_inptextbox.grid(row=4, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.gemini_inpbutton=customtkinter.CTkButton(self.gemini_frame,text="Send",font=self.buttonfont,width=80, height=50,command=self.respond)
        self.gemini_inpbutton.grid(row=4,column=2,padx=(20,0),pady=(20,0),sticky="nsew")
        #Defaults
        self.appearance_mode_menu.set("Dark")
        self.select_frame_by_name("home")
        
        #Event of side bar for Home Frame and 2nd Frame
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.ide_button.configure(fg_color=("gray75", "gray25") if name == "ide" else "transparent")
        self.gemini_button.configure(fg_color=("gray75", "gray25") if name == "gemini" else "transparent")
        
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "ide":
            self.ide_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ide_frame.grid_forget()
        if name =="gemini":
            self.gemini_frame.grid(row=0, column=1,sticky="nsew")
        else:
            self.gemini_frame.grid_forget()
            
    def home_button_event(self):
        self.select_frame_by_name("home")

    def ide_button_event(self):
        self.select_frame_by_name("ide")
        
    def gemini_button_event(self):
        self.select_frame_by_name("gemini")
            

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def respond(self):
        self.gemini_outtextbox.delete("0.0",END)
        self.inp=self.gemini_inptextbox.get("0.0",END)
        response =gemini(10,2,self.inp)
        self.gemini_outtextbox.insert("0.0",str(response))
        self.gemini_inptextbox.delete("0.0",END)

    
    def run(self):
        self.mainloop()

