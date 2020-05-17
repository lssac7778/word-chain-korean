# 끝말잇기 인공지능

사용시 모든 책임은 본인에게 있습니다

## 실행
```
python main.py
```

## 모드 선택
main.py의 마지막줄을 수정하면 됩니다.

공격모드 : 공격단어 위주 선택
```
main("attack", 0.00001)
```

긴 단어 모드 : 긴 단어 위주 선택
```
main("long", 0.00001)
```

두 번째 인자는 interval로, 단어를 입력하는 타자 속도를 조절합니다. 


## 사용법
1. 첫 글자를 입력한다.
2. 숫자 키 "1" 을 누른다.
3. 자동으로 단어가 입력된다.

예시
```
아1 => 아시아나에어라인스맥스웰하우스원두분쇄커피
```


숫자 키 "2" 를 누르면 최근 입력된 첫 글자로 시작하는 단어가 입력됩니다. 

숫자 키 "9" 를 누르면 이미 사용한 단어 목록이 초기화됩니다. 

숫자 키 "0" 을 누르면 프로그램이 종료됩니다.

## Requirements
pyautogui, pynput
