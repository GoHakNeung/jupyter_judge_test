# 상호작용형 프로그램 자동 평가 시스템
**상호작용형 프로그램 자동 평가 시스템은** 주피터 노트북에서 설명, 실습, 평가를 할 수 있는 모듈입니다.
- 설명 : Text cell을 이용한 설명  
- 실습 : Code cell을 이용한 코드 작성 및 결과 확인
- 평가 : Code cell을 이용해서 문제 제시, 코드 작성, 코드 평가 실시  
(주피터 노트북에서 활용할 수 있으나, 모듈에서 파일 경로는 **Colab**을 기준으로 작성하였으므로, **Colab**에서 사용하는 것을 추천합니다.)  

## 사용 방법
상호작용형 프로그램 자동 평가 시스템은 중앙 서버에서 평가하는 것이 아닌 개별 **주피터 노트북(Kernel)**에서 평가합니다.  

- **초기 설정** : Code cell에서 **Git**에 공개한 자동 평가 모듈을 다운로드 받고 실행합니다.
- **문제 제시** : Code cell에서 **문제 출력 함수**를 실행하며, Code cell output에서 문제를 확인할 수 있습니다.  
- **코드 작성** : Code cell의 코드를 저장하는 **매직 커멘드(%%writefile filename)**을 사용하여 저장합니다.
- **코드 평가**는 Code cell에서 **평가 함수**를 실행하며, Code cell output에서 평가 결과를 확인할 수 있습니다.

___
___

### 초기 설정
Code cell에 **자동 평가 모듈**을 **다운로드** 받고 **실행**하기 위하여 아래 코드를 실행합니다.  
- 초기 설정 코드
``` python 
!git clone https://github.com/GoHakNeung/jupyter_judge.git
%run /content/jupyter_judge/code_check.py 
```
코드 설명 : Git에 공개한 자동 평가 모듈을 다운로드 하는 **shell command**와 자동 평가 모듈을 실행하는 **매직 커멘드(%run filename)**를 실행합니다.  

___


### 문제 제시
Code cell에 **문제 변수**를 매개변수로한 **문제 출력 함수**를 실행합니다.  
문제 출력 함수는 `Question()`, 문제 변수는 `question_0000`이며 [문항 확인](https://github.com/GoHakNeung/jupyter_judge/tree/main/%EB%AC%B8%ED%95%AD)에서 확인할 수 있습니다.  
- 문제는 아래와 같이 출력됩니다.  
![문제 출력 예시](https://github.com/GoHakNeung/python/blob/main/%EB%AC%B8%EC%A0%9C%20%EC%98%88%EC%8B%9C.png?raw=true)

설명 : 문제는 **문제 설명, 입력·출력 데이터 설명, 입력·출력 데이터 예시**를 구분하여 출력합니다. 이를 위해 문제변수는 **HTML 태그**를 포함하여 저장하며, 문제 출력함수는 HTML 태그를 **렌더링**하여 출력하도록 정의했습니다.
- 문제 출력 함수  
``` python
from IPython.display import display, HTML
def Question(question_) : 
  display(HTML(question_))
```
- 문제 예시
``` python
question_6201 ='''<h2 style = "background-color:yellow; ">문제 설명</h2>
<p>입력 받은 1개의 <span style = "background-color : #E0E0E0">숫자(각도)</span>가 예각인지, 직각인지, 둔각인지 출력하도록 프로그램을 만들어봅시다.</p>
<HR>
<h2> 입력
</h2>
<p>1 ~ 179 사이 숫자가 입력됩니다.</p>
<h2> 출력
</h2>
<p>예각, 직각, 둔각 중 하나를 출력합니다.</p>
<HR>
<div style = "float:left;width:50%">
<h2> 입력 예시 </h2>
<p>56</p>
</div>
<div style = "float:right;width:50%">
<h2> 출력 예시 </h2>
<p>예각</p>
</div>
'''
```

___


### 코드 작성
Code cell에 코드를 저장하는 **%%매직 커멘드(%%writefile filename)**를 상단에 작성하고, 그 아래 문제에 대한 코드를 작성한 후 실행합니다.    
- 코드 작성 예시  
![코드작성 예시](https://github.com/GoHakNeung/python/blob/main/%EC%BD%94%EB%93%9C%20%EC%A0%80%EC%9E%A5.png?raw=true)
(코드가 저장되는 경로는 Colab 기준 `/content/`에 저장됩니다. )

___


### 코드 평가
Code cell에 **코드를 저장한 파일 이름**을 매개변수로 한 **평가 함수**를 실행합니다.  

평가할 수 있는 영역과 평가 함수는 아래와 같습니다.  
- **문자·숫자 데이터** : `code_check('filename')`
- **Turtle 라이브러리로 그린 이미지** : `turtle_check('filename')`
- **matplotlib 라이브러리로 그린 그래프** : `plot_check('filename')` 

평가 방식은 채점데이터(또는 모범답안)를 학생이 작성한 코드에 입력한 뒤 실행시켜 평가하고, 평가 결과는 Code cell output에 출력합니다.  
- 문자·숫자 데이터 평가 결과
![문자·숫자](https://github.com/GoHakNeung/python/blob/main/%EB%AC%B8%EC%9E%90%20%EC%88%AB%EC%9E%90%20%EA%B2%B0%EA%B3%BC.png?raw=true)
- turtle 라이브러리 평가 결과
![turtle](https://github.com/GoHakNeung/python/blob/main/turtle%20%EA%B2%B0%EA%B3%BC.png?raw=true)
- matplotlib 라이브러리 평가 결과
![plot](https://github.com/GoHakNeung/python/blob/main/plot%20%EC%98%88%EC%8B%9C.png?raw=true)
