# 상호작용형 프로그램 자동 평가 시스템
주피터 노트북에서 **문제 제시, 코드 작성, 코드 평가**를 할 수 있는 모듈입니다.  
모듈에서 파일 경로는 **Colab**을 기준으로 작성하였으므로, **Colab**에서 사용하기 바랍니다.  

## 사용 방법
상호작용형 프로그램 자동 평가 시스템을 활용하기 위한 모듈은 Git에 공개하였습니다.  
**문제 제시**는 **Code cell**에서 문제 출력 함수를 실행하며, **Code cell output**에서 문제를 확인할 수 있습니다.  
**코드 작성**은 **Code cell**의 코드를 저장하는 매직 커멘드(%%writefile filename)을 사용하여 저장합니다.
**코드 평가**는 **code cell**에서 평가 함수를 실행하며, **Code cell output**에서 평가 결과를 확인할 수 있습니다.  
상호작용형 프로그램 자동 평가 시스템은 중앙 서버에서 평가하는 것이 아닌 **주피터 노트북(Kernel)**에서 평가합니다.  

___

### 초기 설정
**Code cell**에서 아래 코드를 실행하면 초기 설정이 완료됩니다.
``` python 
!git clone https://github.com/GoHakNeung/jupyter_judge.git
%run /content/jupyter_judge/code_check.py 
```

### 문제 제시
문제 출력 함수는 `Question(문제 변수)`로 정의했습니다.  
문제 변수는 `question_0000`이며 [문항 확인](https://github.com/GoHakNeung/jupyter_judge/tree/main/%EB%AC%B8%ED%95%AD)에서 확인할 수 있습니다.
이미지 넣기
### 코드 작성

### 평가
- 교사 입장
1. Colab 코드 셀에서 github에서 코드 다운로드 및 실행하면 초기 설정이 완료됩니다.  
2. Colab에서 코드 셀 3개를 이용해서 문제 제시, 평가 코드 작성, 코드 평가 함수를 제시할 수 있습니다.   
3. print(문제 번호)를 통해 문제를 제시할 수 있습니다.(문제를 따로 적지 않아도 됩니다.)
4. code_check(평가 코드 이름) 함수를 이용해서 학생에게 코드를 평가한 결과를 제공하고  
평가 결과는 구글 스프레드 시트로 전송됩니다.
5. 구글 클래스룸을 이용하면 학생들에게 학습 자료 제공 및 회수가 편해집니다. 
- 학생 입장
1. 교사가 제공한 github에서 코드 다운로드 및 실행 코드 셀을 실행하면 초기 설정이 완료됩니다. 
2. 텍스트 셀에서 설명, 실습할 수 있는 코드 셀, 평가할 수 있는 코드 셀이 한 페이지에 구성되어 있습니다.
3. `print(문제)` 출력 결과로 문제를 확인할 수 있습니다.  
4. `%%writefile 문제번호.py`이 적힌 코드 셀에 코드를 작성 후 실행하면 평가 코드가 완성됩니다.  
5. `code_check('문제번호.py')`가 작성된 코드 셀을 실행하면 코드가 평가됩니다. 

## 자동 평가 시스템의 구성
> 제공하는 코드는 크게 **2가지**로 구성되어 있습니다.  
>> 1. 문제, 정답 데이터, 메타 데이터
>> 2. 자동 평가 함수  

## 문제, 정답 데이터, 메타 데이터  
1. 문제  
: question_번호 변수에 문제가 저장되어 있습니다.  
: 문제, 입력 예시, 출력 예시를 제시합니다.  
``` python
question_1 = '''==================================================
이름을 입력하고 "Hello 이름"이 출력되도록 프로그램을 만듭니다.
입력 예시 : 가득
출력 예시 : Hello 가득
=================================================='''
```
2. 정답 데이터  
: 입력 데이터와 정답 데이터의 여러 묶음을 리스트로 저장되어 있습니다.  
: 입력 데이터와 정답 데이터는 딕셔너리로 저장합니다.  
: 딕셔너리로 작성된 데이터 세트는 key 값은 `input`, `output`이고, value 값은 `입력 데이터`, `정답 데이터`입니다.   
: 입력 데이터와 정답 데이터는 리스트로 입력합니다.  
- 입력과 출력이 있을 경우  
``` python
answer_1 = [
    {'input' : ['mango'], 'output' : ['Hellomango']},
    {'input' : ['go'], 'output' : ['Hellogo']},
    {'input' : ['good'], 'output' : ['Hellogood']}
]
```
- 출력만 있을 경우  
``` python
answer_3 = [
    {'input' : [], 'output' : [0,1,2,3,4,5,6,7,8,9]}
]
```
3. 메타 데이터  
: 평가할 파일 이름, 정답 데이터 번호, 문제 번호를 딕셔너리로 저장합니다.  
: 딕셔너리로 작성된 메타 데이터는 key 값은 `test_file`, `answer`, `question`이고  
: value 값은 `평가할 파일 이름`, `정답 데이터 번호`, `문제 번호` 입니다.  
``` python
test_set = [
    {'test_file' : '_1.py', 'answer' : answer_1, 'question' : question_1}
]
```

## 자동 평가 함수 원리
1. 코드에서 입력 받는 변수를 확인합니다. 
2. 코드를 변환합니다.  
    - 입력 받는 변수에 입력 데이터를 대입합니다. 
    - print()한 결과를 txt 파일에 저장하도록 표준 출력을 수정합니다. 
3. 변환한 코드를 실행하여 출력한 결과와 정답 데이터를 비교합니다. 
4. 코드에 대한 평가 또는 오류에 대한 피드백을 제공합니다. 

## 사용 방법
- 교사 입장
1. Colab을 이용해서 학습 자료(.ipynb)를 작성합니다.
2. 초기 설정 코드 셀에서 github에서 다운로드 및 실핼 코드를 제공합니다. 
``` python 
!git clone https://github.com/GoHakNeung/jupyter_judge.git
%run /content/jupyter_judge/code_check.py 
```
3. `print(문제번호)`, `%%writefile 평가코드.py`, `code_check('평가코드.py')`을 각각의 코드 셀에 입력 합니다.  
`print(문제번호)`만 실행한다. 
![교사 제공 파일](https://github.com/GoHakNeung/python/blob/main/python/%EA%B5%90%EC%82%AC%EA%B0%80%20%EC%A0%9C%EA%B3%B5%ED%95%98%EB%8A%94%20%ED%8C%8C%EC%9D%BC.jpg?raw=true)
4. 학습 자료(.ipynb)를 학생에게 제공합니다.(구글 클래스룸, 주피터 허브 등)

- 학생 입장
1. 초기 설정 코드를 실행 후 입력창에 이름을 입력합니다.  
![초기실행코드](https://github.com/GoHakNeung/python/blob/main/python/%EC%B4%88%EA%B8%B0%20%EC%8B%A4%ED%96%89%20%EC%BD%94%EB%93%9C.jpg?raw=true)  
2. 평가 코드 작성하기  
: `%%writefile 코드.py`의 코드 셀 하단에 평가할 코드를 작성합니다.  
: input() 괄호 안은 비워둡니다.  
![평가코드작성하기](https://github.com/GoHakNeung/python/blob/main/python/%ED%8F%89%EA%B0%80%20%EC%BD%94%EB%93%9C%20%EC%9E%85%EB%A0%A5%20%EB%B0%8F%20%EC%8B%A4%ED%96%89.jpg?raw=true)
3. code_check('코드.py') 코드를 실행하여 코드를 평가합니다. 
- 정답인 경우  
![코드 평가하기](https://github.com/GoHakNeung/python/blob/main/python/%ED%8F%89%EA%B0%80%20%EC%BD%94%EB%93%9C%20%EC%8B%A4%ED%96%89%20%EA%B2%B0%EA%B3%BC.jpg?raw=true)
- 오답인 경우  
![코드 오답](https://github.com/GoHakNeung/python/blob/main/python/%ED%8B%80%EB%A0%B8%EC%9D%84%20%EA%B2%BD%EC%9A%B0.jpg?raw=true)
- 오류인 경우  
![코드 오류](https://github.com/GoHakNeung/python/blob/main/python/%EC%98%A4%EB%A5%98%EC%9D%B8%20%EA%B2%BD%EC%9A%B0.jpg?raw=true)
