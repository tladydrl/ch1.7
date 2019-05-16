# 필요할떄만 임포트한다;.. 조건이 될때만..

#import sys
#import math    # 메모리 많이 차지하게 된다. 임포트 다 하면,, 조금 느려질수도 있고.

# if []:
#   sys.exit(0)
#else:  # 여기서 동적으로,,
#   with.sin(pi)

###
# 동적 import를 위한 함수 __import__ 함수.

import sys

# 동적으로 pythonpath 잡기.
sys.path.append('../python_modules') # 마이매스 있다. # 패스 잡혀있어서 안해도 되는데.
m = __import__('mymath')
print(sys.path)

print(m.pi)
print(m.add(10, 20))
print(m.area_circle(5))



# 하나의 모듈을 두번 임포트 하게되면,, 파이썬은 어떻게 하는것인가.. 하나만 임포트..?






