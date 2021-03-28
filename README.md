# Python GUI - Shortcut Launcher

## 목표 및 목적
- GUI 기능과 주어진 라이브러리를 이용해 단축키 실행 프로그램을 개발한다.
- 만들어진 프로그램은 지정된 명령어를 클릭 한 번으로 바로 실행하는 역할을 한다.
##
- 프로그램은 2행 4열 그리드의 버튼으로 구성되어 있다.
- 프로그램은 단일 윈도우로 되어 있다.
- 프로그램의 버튼을 클릭하면 지정된 명령어를 실행한다.

### 문제 분석
  
* 최종 목적 : 단축키 실행 프로그램인 Shortcut Launcher를 완성한다.
    * 상위 목적 : GUI에 버튼을 구현한다.
        * 하위 목적 : 
        * 윈도우 창 생성- 너비와 높이, 초기 위치 설정, 창 크기 조절 가능 여부 설정
        * 2행 4열의 그리드 버튼 생성
        * 파라미터를 사용하여 버튼의 속성 설정
    * 상위 목적 : GUI에 버튼을 눌렀을 때, 응용프로그램을 실행시킨다.
        * 하위 목적 : 
        * 응용프로그램 이름과 이미지 삽입
        * 응용 프로그램 명령어 설정
        * 버튼 동작 설정

## 개발 사양

### 하드웨어
* CPU : 프로세서	Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz, 3401Mhz, 4 코어, 4 논리 프로세서
* RAM : 설치된 실제 메모리(RAM)	8.00GB
* HDD/SSD : 모델	SAMSUNG SSD 830 Series
* GPU : Intel(R) HD Graphics

### 소프트웨어
* OS : OS 이름	Microsoft Windows 10 Pro 버전	10.0.19041 빌드 19041
* 개발 스택 : Tkinter (선택이유 : 유튜브나 블로그에 관련 자료가 많고 잘 정리되어있다)
* 개발 프로그램 : Pycharm
* 개발 언어 : Python v3.9.2

### 코드룰
* 예시 프로그램

```
    # 변수명
    test_variable = 13

    # 클래스명
    class TestClass:
        def __init__(self):
            # 프로퍼티명
            self.test_property = 41

        # 메소드명
        def TestMethod(self):
            print(self.test_property)
    
    if __name__ == "__main__":
        test_variable = TestClass(43)
        test_variable.TestMethod()
```
