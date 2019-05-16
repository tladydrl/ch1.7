# 정적으로 패스 추가: 프로젝트 세팅즈에 인터프리터 패스 추가 하면 된다.
# 1. 동적으로 설정.
# 2. 파이참 환경 안에다가 설정.

#import sys
#print(sys.path)
#sys.path.append('/PythonStudy/PycharmProjects/python_modules') # 역슬래시 바꿀수 있고 \ 할수 있고, D:생략가능.
# 현재 드라이브: d 드라이브라서 ,, 자동으로 잡아준다.

import mymath  # 없어서 안됨..  # 정적으로 에러,,  # 위에 패스 추가는 동적으로 추가.
print(mymath.pi)
print(mymath.area_circle(10))

# zip : venv에 있는 라이브러리이다..

# math 는 내부모듈과 ,, 사용자 정의 모듈이 있다..