import sys, random, math, os, traceback
#------------------------------------------------------------------------------#
#문제 입력
question_1 = '이름을 입력하고 "Hello이름"이 출력되도록 프로그램을 만듭니다.\n입력 예시 : 가득\n출력 예시 : Hello가득'
question_2 = '"Hello World"를 출력하는 프로그램을 만듭니다.\n입력 예시 : 없음\n출력 예시 : Hello World'
answer_1 = [[['mango'], ['Hellomango']], 
            [['go'], ['Hellogo']], 
            [['good'], ['Hellogood']]]
answer_2 = ['Hello World']
answer_4 = [[[3,4], ['4 3']],
            [[156,1532], ['1532 156']], 
            [[-5456, 456], ['456 -5456']]]
test_set = [['_1.py', 'answer_1', question_1], ['_2.py', 'answer_2', question_2], ['_4.py', 'answer_4']]
#------------------------------------------------------------------------------#
#출력할 때 글씨 색
reset = '\033[0m'
tc_red = '\033[38;2;255;0;0m'
tc_green = '\033[38;2;0;255;0m'
#------------------------------------------------------------------------------#
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

  # print(f'code 리스트 : {code}, code 개수 : {len(code)}')
  # print(f'input 리스트 : {code_input}, input 개수 : {len(code_input)}')
  # print(f'output 리스트 : {code_output}, output 개수 : {len(code_output)}')

#------------------------------------------------------------------------------#
# 리스트에 있는 코드를 평가 코드로 수정하기
def code_convert0(answer_input) : 
  global convert_error
  convert_error = False
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

#------------------------------------------------------------------------------#
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

#------------------------------------------------------------------------------#
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

#------------------------------------------------------------------------------#


def code_test0(answer_input) : 
  global user_answer0
  user_answer0 = []
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
      user_answer0.append(float(line))
    elif line != '' and answer_type == int : 
      user_answer0.append(int(line))
    elif line != '' and answer_type == str : 
      user_answer0.append(str(line))
    elif line != '' and answer_type == bool : 
      user_answer0.append(bool(line))
  f.close()

  if len(code_input) == 0 : 
    if user_answer0 == answer_input : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)    
  else : 
    if user_answer0 == answer_input[0][1] : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)
#------------------------------------------------------------------------------#

def code_test1(answer_input) : 
  global user_answer1
  user_answer1 = []
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
      user_answer1.append(float(line))
    elif line != '' and answer_type == int : 
      user_answer1.append(int(line))
    elif line != '' and answer_type == str : 
      user_answer1.append(str(line))
    elif line != '' and answer_type == bool : 
      user_answer1.append(bool(line))
  f.close()

  if len(code_input) == 0 : 
    if user_answer1 == answer_input : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)    
  else : 
    if user_answer1 == answer_input[1][1] : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False) 

#------------------------------------------------------------------------------#

def code_test2(answer_input) : 
  global user_answer2
  user_answer2 = []
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
      user_answer2.append(float(line))
    elif line != '' and answer_type == int : 
      user_answer2.append(int(line))
    elif line != '' and answer_type == str : 
      user_answer2.append(str(line))
    elif line != '' and answer_type == bool : 
      user_answer2.append(bool(line))
  f.close()

  if len(code_input) == 0 : 
    if user_answer2 == answer_input : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)    
  else : 
    if user_answer2 == answer_input[2][1] : 
#      print('정답입니다.')
      result.append(True)
    else : 
#      print('틀렸습니다')
      result.append(False)
#------------------------------------------------------------------------------#
# syntax 오류 외 코드 출력창에 코드 불러오는 것
def code_print(py_name) :  
  file_name = '/content/'+py_name
  f = open(file_name, 'r')  # '/content/____.py  << 이 부분은 함수 매개변수로 불러와야 함.
  lines = f.readlines()
  error_count = error_line()
  code_count = 1

  for line in lines[4:-2] : 
    if error_count == code_count : 
      print(tc_red+line[:-1]+reset)
      code_count += 1
    else : 
      print(line[:-1])
      code_count += 1
  f.close()
#------------------------------------------------------------------------------#
# syntax 오류 외 코드 출력창에 코드 불러오는 것
def code_print_syntax(py_name) :  
  file_name = '/content/'+py_name
  f = open(file_name, 'r')  # '/content/____.py  << 이 부분은 함수 매개변수로 불러와야 함.
  lines = f.readlines()
  error_count = error_line()
  code_count = 1

  for line in lines[4:-2] : 
    print(line[:-1])
  f.close()
#------------------------------------------------------------------------------#
# syntax 외 오류 라인 검출

def error_line() : 
  trace = traceback.format_exc()
  error = ''
  line = ''
  for i in trace.split('\n') :  
    if i.find('string') >= 0 : 
      error = i.strip()    
  for i in error.split(',') : 
    if i.find('line') >= 0 : 
      line = i.strip()
  return int(line[line.find('e')+2:])-4
#------------------------------------------------------------------------------#
#에러에 따른 정보를 알려주는 함수
def name_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 변수 또는 명령어 이름을 확인하거나, 문자열에 따옴표가 붙어 있는지 확인하세요.')
  print("="*40)
  code_print(test_py)

def type_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 숫자나 문자를 바르게 입력했나요?')
  print('또는 ()안에 알맞은 숫자를 입력했나요?')
  print("="*40)
  code_print(test_py)

def attribute_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 라이브러리의 속성 또는 메서드를 바르게 입력했나요?')
  print("="*40)
  code_print(test_py)

def value_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 숫자나 문자를 바르게 입력했나요?')
  print("="*40)
  code_print(test_py)

def index_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 리스트나 튜플의 길이를 확인해주세요.')
  print("="*40)
  code_print(test_py)

def indentation_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 띄어쓰기를 확인해주세요.')     
  print("="*40)
  code_print(test0.py)  

def zerodivision_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 숫자를 0으로 나누면 안되요.')           
  print("="*40)
  code_print(test_py)

def overflow_error(test_py) : 
  sys.stdout = original   
  print(error_line(), '번째 줄에 너무 큰 수는 표현할 수 없어요')
  print("="*40)
  code_print(test_py)

def keyboard_interrupt(test_py) : 
  sys.stdout = original   
  print('사용자가 작동 정지함.')

def syntax_error(test_py) : 
  sys.stdout = original   
  print('문법오류입니다. ":", "()"를 확인하세요')
  print("="*40)
  code_print_syntax(test_py)

def modulenotfound_error(test_py) : 
  sys.stdout = original       
  print(error_line(), '번째 줄에 라이브러리를 확인해주세요.')
  print("="*40)
  code_print(test_py)

def else_error(test_py) : 
  sys.stdout = original   
  print('코드 오류입니다.') 
  print("="*40)
  code_print(test_py)

def error_check(test_py) : 
  global compile_error
  compile_error = False
  try : 
    exec(open(test_py).read())
  except NameError : 
    name_error(test_py)
    compile_error = True
    return
  except TypeError : 
    type_error(test_py)
    compile_error = True
    return
  except AttributeError : 
    attribute_error(test_py)
    compile_error = True
    return
  except ValueError : 
    value_error(test_py)
    compile_error = True
    return
  except IndexError : 
    index_error(test_py)
    compile_error = True
    return
  except IndentationError : 
    indentation_error(test_py)
    compile_error = True
    return
  except ZeroDivisionError : 
    zerodivision_error(test_py)
    compile_error = True
    return
  except OverflowError : 
    overflow_error(test_py)
    compile_error = True
    return
  except KeyboardInterrupt : 
    keyboard_interrupt(test_py)
    compile_error = True
    return
  except SyntaxError : 
    syntax_error(test_py)
    compile_error = True
    return
  except ModuleNotFoundError : 
    modulenotfound_error(test_py)
    compile_error = True
    return
  except : 
    else_error(test_py)
    compile_error = True
    return

#------------------------------------------------------------------------------#
#코드의 정답 여부를 확인하는 함수
def code_check(py) :
  for i in range(len(test_set)) :
    if test_set[i][0] == py :
      global answer 
      answer = test_set[i][1]
      global question
      question = test_set[i][2]      

  code_arrange(py)
  code_convert0(answer)
  if convert_error == True :
    print('입력/출력을 확인하세요')     
    return
  code_convert1(answer)
  code_convert2(answer)

  error_check('test0.py')
  if compile_error == True : 
    return
  error_check('test1.py')
  error_check('test2.py')

  code_test0(answer)      
  code_test1(answer)  
  code_test2(answer)  
#___________________________________________________________________________#
  # print(result)
  if result[0] and result[1] and result[2] == True:
    print(tc_green+'정답입니다.'+reset) 
  else : 
    print(question, '\n')
    if len(code_input) == 0 : 
      if result[0] == False :       
        print(user_answer0,'가 출력됩니다.')
      if result[1] == False :       
        print(user_answer1,'가 출력됩니다.')
      if result[2] == False :       
        print(user_answer2,'가 출력됩니다.')

    else : 
      if result[0] == False : 
        print(eval(answer)[0][0][0], '을 입력하면 ', user_answer0, '가 출력됩니다. ')
      if result[1] == False : 
        print(eval(answer)[1][0][0], '을 입력하면 ', user_answer1, '가 출력됩니다. ')
      if result[2] == False : 
        print(eval(answer)[2][0][0], '을 입력하면 ', user_answer2, '가 출력됩니다. ')  
    print(tc_red+'틀렸습니다.'+reset)
