import sys, random, math
question_1 = '이름을 입력하고 "Hello이름"이 출력되도록 프로그램을 만듭니다.\n입력 예시 : 가득\n출력 예시 : Hello가득'
question_2 = '"Hello World"를 출력하는 프로그램을 만듭니다.\n입력 예시 : 없음\n출력 예시 : Hello World'
answer_1 = [[['mango'], ['Hellomango']], 
            [['go'], ['Hellogo']], 
            [['good'], ['Hellogood']]]
answer_2 = ['Hello World']
test_set = [['_1.py', 'answer_1'], ['_2.py', 'answer_2']]
#--------------------------------------------------------------------------------------------------------#
# 코드를 input /output 리스트에 넣기
def code_arrange(py_name) : 
  global result, code, code_input, code_output
  result= []
  code = []
  code_input = []
  code_output = []

  file_name = '/content/'+py_name

  f = open(file_name, 'r')  # '/content/____.py  << 이 부분은 함수 매개변수로 불러와야 함.
  lines = f.readlines()
  for line in lines : 
  #  line = line.strip()
    if line != '' : 
      code.append(line)    
      if line.find('input') >= 0 : 
        code_input.append(code.index(line))
      if line.find('print') >= 0 : 
        code_output.append(code.index(line))

  f.close()

  for i in range(len(code)) : 
    if code[i].find('\n') >= 0 : 
      code[i] = code[i][:-1]
    code[i] = code[i].rstrip()

  print(f'code 리스트 : {code}, code 개수 : {len(code)}')
  print(f'input 리스트 : {code_input}, input 개수 : {len(code_input)}')
  print(f'output 리스트 : {code_output}, output 개수 : {len(code_output)}')

#--------------------------------------------------------------------------------------------------------#
# 리스트에 있는 코드를 평가 코드로 수정하기
def code_convert0(answer_input) : 
  f = open('test0.py', 'w')  
  original = sys.stdout
  sys.stdout = f

  print('import sys')
  print("f = open('answer0.txt', 'w')")
  print('original = sys.stdout')
  print('sys.stdout = f')
  try : 
    order = 0  
    answer_input = eval(answer_input)
    count = 0
    for order in range(len(code)) : 
      if order in code_input : 
        print(code[order][:code[order].find('=')+1],'"'+str(answer_input[0][0][count])+'"')
        count += 1  
      elif order in code_output : 
        print(code[order])
      else : 
        print(code[order])

    print('sys.stdout = original')
    print('f.close()')

    # 파이썬 코드로 실행해야 함. 원상복구
    sys.stdout = original   
    f.close()                   
  except :  
    print('sys.stdout = original')
    print('f.close()')
    
    sys.stdout = original   
    f.close()
    print('입력/출력을 확인하세요')    
#--------------------------------------------------------------------------------------------------------#
# 리스트에 있는 코드를 평가 코드로 수정하기
def code_convert1(answer_input) : 
  f = open('test1.py', 'w')  
  original = sys.stdout
  sys.stdout = f

  print('import sys')
  print("f = open('answer1.txt', 'w')")
  print('original = sys.stdout')
  print('sys.stdout = f')
  try : 
    order = 0  
    answer_input = eval(answer_input)
    count = 0
    for order in range(len(code)) : 
      if order in code_input : 
        print(code[order][:code[order].find('=')+1],'"'+str(answer_input[1][0][count])+'"')
        count += 1  
      elif order in code_output : 
        print(code[order])
      else : 
        print(code[order])

    print('sys.stdout = original')
    print('f.close()')

    # 파이썬 코드로 실행해야 함. 원상복구
    sys.stdout = original   
    f.close()                   
  except :  
    print('sys.stdout = original')
    print('f.close()')

    sys.stdout = original   
    f.close()
    print('입력/출력을 확인하세요')  
#--------------------------------------------------------------------------------------------------------#
# 리스트에 있는 코드를 평가 코드로 수정하기
def code_convert2(answer_input) : 
  f = open('test2.py', 'w')  
  global original
  original = sys.stdout
  sys.stdout = f

  print('import sys')
  print("f = open('answer2.txt', 'w')")
  print('original = sys.stdout')
  print('sys.stdout = f')
  try : 
    order = 0  
    answer_input = eval(answer_input)
    count = 0
    for order in range(len(code)) : 
      if order in code_input : 
        print(code[order][:code[order].find('=')+1],'"'+str(answer_input[2][0][count])+'"')
        count += 1  
      elif order in code_output : 
        print(code[order])
      else : 
        print(code[order])

    print('sys.stdout = original')
    print('f.close()')

    # 파이썬 코드로 실행해야 함. 원상복구
    sys.stdout = original   
    f.close()                   
  except :  
    print('sys.stdout = original')
    print('f.close()')

    sys.stdout = original   
    f.close()
    print('입력/출력을 확인하세요')  
#--------------------------------------------------------------------------------------------------------#


def code_test0(answer_input) : 
  user_answer = []
  answer_input = eval(answer_input)
  answer_type = ''
  if len(code_input) == 0 : 
    answer_type = type(answer_input[0])
  else : 
    answer_type = type(answer_input[0][1][0]) 

  f = open('/content/answer0.txt', 'r')
  lines = f.readlines()

  for line in lines :  # 결과를 자료형에 맞게 저장한다. 5.0과 5는 다르므로 테스트 셋에서 결과에 식 그대로 넣어야 한다.
    line = line.strip()
    if line != '' and answer_type == float : 
      user_answer.append(float(line))
    elif line != '' and answer_type == int : 
      user_answer.append(int(line))
    elif line != '' and answer_type == str : 
      user_answer.append(str(line))
    elif line != '' and answer_type == bool : 
      user_answer.append(bool(line))
  f.close()

  if len(code_input) == 0 : 
    if user_answer == answer_input : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)    
  else : 
    if user_answer == answer_input[0][1] : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)
#--------------------------------------------------------------------------------------------------------#

def code_test1(answer_input) : 
  user_answer = []
  answer_input = eval(answer_input)
  answer_type = ''
  if len(code_input) == 0 : 
    answer_type = type(answer_input[0])
  else : 
    answer_type = type(answer_input[1][1][0]) 
  f = open('/content/answer1.txt', 'r')
  lines = f.readlines()

  for line in lines :  # 결과를 자료형에 맞게 저장한다. 5.0과 5는 다르므로 테스트 셋에서 결과에 식 그대로 넣어야 한다.
    line = line.strip()
    if line != '' and answer_type == float : 
      user_answer.append(float(line))
    elif line != '' and answer_type == int : 
      user_answer.append(int(line))
    elif line != '' and answer_type == str : 
      user_answer.append(str(line))
    elif line != '' and answer_type == bool : 
      user_answer.append(bool(line))
  f.close()

  if len(code_input) == 0 : 
    if user_answer == answer_input : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)    
  else : 
    if user_answer == answer_input[1][1] : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False) 

#--------------------------------------------------------------------------------------------------------#

def code_test2(answer_input) : 
  user_answer = []
  answer_input = eval(answer_input)
  answer_type = ''
  if len(code_input) == 0 : 
    answer_type = type(answer_input[0])
  else : 
    answer_type = type(answer_input[2][1][0]) 
  f = open('/content/answer2.txt', 'r')
  lines = f.readlines()

  for line in lines :  # 결과를 자료형에 맞게 저장한다. 5.0과 5는 다르므로 테스트 셋에서 결과에 식 그대로 넣어야 한다.
    line = line.strip()
    if line != '' and answer_type == float : 
      user_answer.append(float(line))
    elif line != '' and answer_type == int : 
      user_answer.append(int(line))
    elif line != '' and answer_type == str : 
      user_answer.append(str(line))
    elif line != '' and answer_type == bool : 
      user_answer.append(bool(line))
  f.close()

  if len(code_input) == 0 : 
    if user_answer == answer_input : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)    
  else : 
    if user_answer == answer_input[2][1] : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)
#--------------------------------------------------------------------------------------------------------#

#@title
def code_check(py) :
  for i in range(len(test_set)) :
    if test_set[i][0] == py :
      global answer 
      answer = test_set[i][1]

  code_arrange(py)
  code_convert0(answer)
  code_convert1(answer)
  code_convert2(answer)
  try : 
    exec(open('test0.py').read())
  except : 
    sys.stdout = original   
    print('코드 오류입니다.')
  code_test0(answer)
  try : 
    exec(open('test1.py').read())
  except : 
    sys.stdout = original
    print('코드 오류입니다.')
  code_test1(answer)
  try : 
    exec(open('test2.py').read())
  except : 
    sys.stdout = original
    print('코드 오류입니다. ')
  code_test2(answer)
  print(result)
  if result[0] and result[1] and result[2] == True:
    print('정답입니다.') 
  else : 
    print('틀렸습니다.')
