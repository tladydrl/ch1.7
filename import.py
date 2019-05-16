# 다양한 import

#import math

# print(math.sin(math.pi/6), math.cos(math.pi/6))

# from mymath import pi
# from math import  sin, cos, pi # 이렇게 하면 굳이 math 안써도 된다.
#from mymath import pi
#print(sin(pi/6), cos(pi/6))
#print(pi)  # 마지막에 임포트한애가 이긴다..

#from math import *  # 뭐가있는지간에 다 임포트 하겠다.
#print(sin(pi/6), cos(pi/6))

#import math as m  # math 대신에 m으로 부른다.
#print(m.sin(m.pi/6), m.cos(m.pi/6))  #이름 긴 모듈 줄여버리기..  이거랑 * 방식 많이 쓴다.


from math import sin as mysin, cos as mycos  # 함수이름을 바꿔서 받기.. 웬만하면 원래그대로 씀.
import mymath as m
print(m.pi, mysin(m.pi/6), mycos(m.pi/6))
print(m.pi)  # 마지막에 임포트한애가 이긴다..






