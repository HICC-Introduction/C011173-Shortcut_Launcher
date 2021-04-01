import tkinter
from tkinter import filedialog
import subprocess
import webbrowser
from tkinter import *

window=tkinter.Tk() #윈도우 창 생성

# 윈도우 기본 크기 및 환경설정
window.title("My Shortcut Launcher")
window.geometry("800x200+100+100") #윈도우 창의 너비와 높이, 초기 화면 위치의 x좌표와 y좌표를 설정
window.resizable(False, False) #윈도우 창의 창 크기 조절 가능 여부를 설정,True로 설정시 조절가능


##main program

# 버튼 동작 설정 함수
def Notepad():
    subprocess.Popen('C:/windows/system32/notepad.exe')

def Calc():
    subprocess.Popen('C:/windows/system32/calc.exe')

def Folder_C():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("PPTX files", "*.pptx"),
                                                     ("all files", "*.*")))
    print(filename)

def Google():
    url = 'http://google.com'
    webbrowser.open(url)

# 버튼 이미지 삽입
root = Tk()
photo1 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\notepad.png")
photo2 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\calc.png")
photo3 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\폴더C.png")
photo4 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\google.png")


## 윈도우창에 버튼 설정하기
b1=tkinter.Button(window, text="메모장", command= Notepad ,image = photo1)
b2=tkinter.Button(window, text="계산기", command= Calc ,image = photo2)
b3=tkinter.Button(window, text="폴더 C:\\", command= Folder_C ,image = photo3)
b4=tkinter.Button(window, text="구글", command= Google, image = photo4)
b5=tkinter.Button(window, text="5")
b6=tkinter.Button(window, text="6")
b7=tkinter.Button(window, text="7")
b8=tkinter.Button(window, text="8")

# 버튼 위치와 크기 조정
b1.place(x=0, y=0 ,width=90, height=80)
b2.place(x=100, y=0, width=90, height=80)
b3.place(x=200, y=0 ,width=90, height=80)
b4.place(x=300, y=0, width=90, height=80)
b5.place(x=0, y=100 ,width=90, height=80)
b6.place(x=100, y=100, width=90, height=80)
b7.place(x=200, y=100 ,width=90, height=80)
b8.place(x=300, y=100, width=90, height=80)

window.mainloop()
