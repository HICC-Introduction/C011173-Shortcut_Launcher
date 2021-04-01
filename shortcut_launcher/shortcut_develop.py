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


###main program

##버튼 button

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
#root = Tk()
photo1 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\notepad.png")
photo2 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\calc.png")
photo3 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\폴더C.png")
photo4 = PhotoImage(file=r"C:\Users\Leejieun\Pictures\pythongui_img\google.png")


# 윈도우창에 버튼 설정하기
button1=tkinter.Button(window, text="메모장", command= Notepad ,image = photo1)
button2=tkinter.Button(window, text="계산기", command= Calc ,image = photo2)
button3=tkinter.Button(window, text="폴더 C:\\", command= Folder_C ,image = photo3)
button4=tkinter.Button(window, text="구글", command= Google, image = photo4)
button5=tkinter.Button(window, text="5")
button6=tkinter.Button(window, text="6")
button7=tkinter.Button(window, text="7")
button8=tkinter.Button(window, text="8")

# 버튼 위치와 크기 조정
button1.place(x=10, y=0 ,width=180, height=80)
button2.place(x=210, y=0, width=180, height=80)
button3.place(x=410, y=0 ,width=180, height=80)
button4.place(x=610, y=0, width=180, height=80)
button5.place(x=10, y=100 ,width=180, height=80)
button6.place(x=210, y=100, width=180, height=80)
button7.place(x=410, y=100 ,width=180, height=80)
button8.place(x=610, y=100, width=180, height=80)


## 라벨 label

# 윈도우창에 라벨 설정하기
label1=tkinter.Label(window, text="메모장",  fg="red", relief="solid")
label2=tkinter.Label(window, text="계산기",  fg="orange", relief="solid")
label3=tkinter.Label(window, text="폴더 C:\\",  fg="green", relief="solid")
label4=tkinter.Label(window, text="구글",  fg="blue", relief="solid")
label5=tkinter.Label(window, text="5",  fg="red", relief="solid")
label6=tkinter.Label(window, text="6",  fg="orange", relief="solid")
label7=tkinter.Label(window, text="7",  fg="green", relief="solid")
label8=tkinter.Label(window, text="8",  fg="blue", relief="solid")
#label.pack()

# 라벨 위치와 크기 조정
label1.place(x=10, y=80, width=180, height=20)
label2.place(x=210, y=80, width=180, height=20)
label3.place(x=410, y=80, width=180, height=20)
label4.place(x=610, y=80, width=180, height=20)
label5.place(x=10, y=180, width=180, height=20)
label6.place(x=210, y=180, width=180, height=20)
label7.place(x=410, y=180, width=180, height=20)
label8.place(x=610, y=180, width=180, height=20)

window.mainloop()
