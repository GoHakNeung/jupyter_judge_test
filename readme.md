# 주피터 노트북에서 온라인 저지를 할 수 있는 judge 라이브러리입니다. 
> 제공하는 코드는 저지할 수 있는 파일입니다.  
> 문제와 정답은 따로 입력해야 합니다.(아래 설명)

## 저지할 수 있는 구조  
1. print()만 있는 경우
2. input()과 print()가 있는 경우  
(주의사항은 `a = int(input())` 입력과 자료형 변환을 한 코드로 작성하면 안됩니다.  
`a = input()`, `a = int(a)` 입력 후 자료형 변환을 해야 합니다. 

## 저지 원리
1. input()에 임의의 값을 입력합니다.  
2. input()으로 받은 값을 작성한 알고리즘에 의해서 처리합니다.  
3. 알고리즘에 의해서 얻은 결과와 답을 비교합니다. 
4. 3세트 정도 비교해서 모두 맞으면 정답으로 인정합니다. 
 
## 사용 방법
1. colab을 실행한다. 
2. 주피터에서 저지 파일을 다운로드 받고 1회 실행합니다.  
``` python 
!git clone https://github.com/GoHakNeung/jupyter_judge.git
%run /content/jupyter_judge/code_check.py 
```
을 실행합니다.  
![실행결과](https://github.com/GoHakNeung/python/blob/main/python/%EC%A0%80%EC%A7%80%20%EC%8B%9C%EC%9E%91%20%EC%BD%94%EB%93%9C.jpg?raw=true)  

3. `print(question_1)`을 실행하면 문제가 나옵니다.    
4. `%%writefile _1.py` 아래 알고리즘 코드를 작성합니다.  
5. `code_check('_1.py')`을 실행하면 결과를 확인할 수 있습니다. 
- 문제 출력  
![프린트 문제](https://github.com/GoHakNeung/python/blob/main/python/%EB%AC%B8%EC%A0%9Cprint.jpg?raw=true)  
- input이 있는 경우  
![입력이 있는 경우](https://github.com/GoHakNeung/python/blob/main/python/input%EC%9D%B4%20%EC%9E%88%EB%8A%94%20%EA%B2%BD%EC%9A%B0.jpg?raw=true)  
- input이 없는 경우  
![입력이 없는 경우](https://github.com/GoHakNeung/python/blob/main/python/input%EC%9D%B4%20%EC%97%86%EB%8A%94%20%EA%B2%BD%EC%9A%B0.jpg?raw=true)  


## 문제 입력하기(**중요**)
> code_check.py 상단에 있는 question_1, answer_1, test_set을 입력합니다.  

>주피터 노트북에서 온라인 저지를 사용하려면 문제를 입력해야 합니다.  
>문제 세트 입력한 것을 푸시해주거나 개인적으로 다운로드 받아서 문제를 입력합니다.  
``` python
import sys, random, math
question_1 = '이름을 입력하고 "Hello이름"이 출력되도록 프로그램을 만듭니다.\n입력 예시 : 가득\n출력 예시 : Hello가득'
question_2 = '"Hello World"를 출력하는 프로그램을 만듭니다.\n입력 예시 : 없음\n출력 예시 : Hello World'
answer_1 = [[['mango'], ['Hellomango']], 
            [['go'], ['Hellogo']], 
            [['good'], ['Hellogood']]]
answer_2 = ['Hello World']
test_set = [['_1.py', 'answer_1', question_1], ['_2.py', 'answer_2', question_2]]
```
1. 필요한 라이브러리를 불러옵니다.  
2. question_1, answer_1, _1.py가 한 세트입니다.  
3. question_1에는 문제를 입력합니다.  
`print(question_1)`로 문제를 불러옵니다.    
4. answer_1에는 답을 입력합니다.  
- input이 있는 경우  
``` python
answer_1 = [[[입력1], [정답1]], 
            [[입력2], [정답2]], 
            [[입력3], [정답3]]]
```
- input이 없는 경우  
``` python
answer_2 = [정답]
```  
5. test_set에는 문제와 답을 리스트로 저장합니다.  
```
test_set = [['문제1', '정답1', question_1], ['_1.py', 'answer_1', question_2]]
```
