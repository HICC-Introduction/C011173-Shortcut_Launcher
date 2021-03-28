import tkinter

window=tkinter.Tk() #윈도우 창 생성

# 윈도우 기본 크기 및 환경설정
window.title("My Shortcut Launcher")
window.geometry("800x200+100+100") #윈도우 창의 너비와 높이, 초기 화면 위치의 x좌표와 y좌표를 설정
window.resizable(False, False) #윈도우 창의 창 크기 조절 가능 여부를 설정,True로 설정시 조절가능



##윈도우창에 위젯 설정하기
##main program
#메모장 실행
label=tkinter.Label(window, text="메모장")
label.pack()

#계산기 실행
label=tkinter.Label(window, text="계산기")
label.pack()

#폴더 C:\ 열기
label=tkinter.Label(window, text="폴더 C:\"")
label.pack()

#google.com 열기
label=tkinter.Label(window, text="구글")
label.pack()

window.mainloop()
