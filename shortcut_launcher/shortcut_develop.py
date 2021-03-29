import tkinter

window=tkinter.Tk() #윈도우 창 생성

# 윈도우 기본 크기 및 환경설정
window.title("My Shortcut Launcher")
window.geometry("800x200+100+100") #윈도우 창의 너비와 높이, 초기 화면 위치의 x좌표와 y좌표를 설정
window.resizable(False, False) #윈도우 창의 창 크기 조절 가능 여부를 설정,True로 설정시 조절가능


##윈도우창에 위젯 설정하기
##main program
b1=tkinter.Button(window, text="메모장")
b2=tkinter.Button(window, text="계산기")
b3=tkinter.Button(window, text="폴더 C:\\")
b4=tkinter.Button(window, text="구글")
b5=tkinter.Button(window, text="5")
b6=tkinter.Button(window, text="6")
b7=tkinter.Button(window, text="7")
b8=tkinter.Button(window, text="8")

b1.place(x=0, y=0 ,width=100, height=100)
b2.place(x=100, y=0, width=100, height=100)
b3.place(x=200, y=0 ,width=100, height=100)
b4.place(x=300, y=0, width=100, height=100)
b5.place(x=0, y=100 ,width=100, height=100)
b6.place(x=100, y=100, width=100, height=100)
b7.place(x=200, y=100 ,width=100, height=100)
b8.place(x=300, y=100, width=100, height=100)

window.mainloop()
