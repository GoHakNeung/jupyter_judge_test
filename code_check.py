import sys, random, math
answer1 = [[[4,5,6],[(4+5+6)/3]],[[1,2,3],[(1+2+3)/3]], [[3,4,5],[(4+5+3)/3]], [[1,3,5],[(1+3+5)/3]], [[5, 8, 2],[(5+8+2)/3]], [[10,20,30],[(10+20+30)/3]]]
answer2 = ['안녕하세요.', '반갑습니다.','안녕하세요.', '반갑습니다.','안녕하세요.', '반갑습니다.','안녕하세요.', '반갑습니다.','안녕하세요.', '반갑습니다.']
answer3 =  [[[1,2,3],[(1+2-10)/3]],[[2,10,4],[(2+10-10)/4]],[[34,2345,23],[(34+2345-10)/23]],[[32412,5463,123],[(32412+5463-10)/123]],[[12,34,56],[(12+34-10)/56]],[[-1243,345,-565],[(-123+345-10)/-562]],[[(-123+345-10)/-562]]]
answer4 = [[['안녕','하세요'], ['안녕 하세요']], [['만나서', '반갑습니다.'], ['만나서 반갑습니다.']], [['매우', '덥습니다.'], ['매우 덥습니다.']]]
answer5 = ['안녕하세요.', '안녕하세요.', '안녕하세요.']
answer6 = ['틀렸습니다.']
answer7 = ['안녕하세요.']
answer8 = [[[1],['정답']], [[2],['땡']], [[3],['땡']]]
answer9 = [[[1,2],['2 1']], [[453,1535],['1535 453']], [[-534,24323],['24323 -534']]]
answer10 = [[[153, 453], [153+453]], [[51,54], [51+54]], [[-78645,456],[-78645+456]]]
answer_1 = [[['mango'], ['Hellomango']], [['go'], ['Hellogo']], [['good'], ['Hellogood']]]
answer_2 = [[[50000, 5],[50000/5]], [[30000, 9],[30000/9]], [[542352,45],[542352/45]]]
answer_3 = [[[45],['투표가능']], [[17],['할로윈가능']], [[18],['운전가능']]]
answer_4 = [[['mango'],['MANGO']], [['hi'],['HI']], [['bad'],['BAD']]]
answer_5 = [[['ab', 'c'],['ABC']],[['dfefF', 'd'],['dfeff']],[['medffDnu', 'df'],['medffdnu']]]
answer_6 = [[['학능', '망고', '몰라', 'ㅋㅋ'],['ㅋㅋ']],[['고학능', '능','ㄱ','ㄱ'],['ㄱ']],[['능','고학능','ㅋ','ㅎㅎ'],['hi']]]
answer_7 = [[[3],[(3**2)*math.pi]],[[123],[(123**2)*math.pi]],[[6546],[(6546**2)*math.pi]]]
answer_8 = [[[3],[3,6,9,12,15]],[[7],[7,14,21,28,35]],[[-6],[-6,-12,-18,-24,-30]]]
answer_9 = [10,11,12,13,14]
answer_10 = [[[5],[5,10,15,20,25,30,35,40,45]],[[2],[2,4,6,8,10,12,14,16,18]],[[-9],[-9,-18,-27,-36,-45,-54,-63,-72,-81]]]
answer_11 = [[[5, '안녕'],['안녕','안녕','안녕','안녕','안녕']],[[2,'메롱'],['메롱','메롱']],[[3,'큭'],['큭','큭','큭']]]
test_set = [['average.py', 'answer1'],['for2.py', 'answer2'],['cal.py', 'answer3'], ['str_add.py', 'answer4'], ['for.py', 'answer5'],['input_if.py','answer6'],['if_else.py','answer7'], ['input_if.py', 'answer8'],['change.py', 'answer9'], ['test.py', 'answer10'], 
            ['_1.py', 'answer_1'], ['_2.py', 'answer_2'], ['_3.py', 'answer_3'], ['_4.py', 'answer_4'], ['_5.py', 'answer_5'], 
            ['_6.py', 'answer_6'], ['_7.py', 'answer_7'], ['_8.py', 'answer_8'], ['_9.py', 'answer_9'], ['_10.py', 'answer_10'], 
            ['_11.py', 'answer_11']]
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
