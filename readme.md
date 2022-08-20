# 주피터 노트북에서 온라인 저지를 할 수 있는 judge 라이브러리입니다. 

## 사용방법
1. colab을 실행한다. 
2. !git clone https://github.com/GoHakNeung/jupyter_judge.git  
%run /content/jupyter_judge/code_check.py 을 실행한다. 
![실행결과](https://github.com/GoHakNeung/python/blob/main/python/%EC%A0%80%EC%A7%80%20%EC%8B%9C%EC%9E%91%20%EC%BD%94%EB%93%9C.jpg?raw=true)

## 저지할 수 있는 구조  
1. print()만 있는 경우
2. input()과 print()가 있는 경우  

## 저지 원리
1. input()에 임의의 값을 입력합니다.  
2. input()으로 받은 값을 작성한 알고리즘에 의해서 처리해 결과를 받습니다.  
3. 알고리즘에 의해서 얻은 결과와 답을 비교합니다. 
4. 3세트 정도 비교해서 모두 맞으면 정답으로 인정합니다. 
 

