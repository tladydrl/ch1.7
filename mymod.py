# module name: mymod

#print('mymod.py의 모듈이름: ' +  __name__)

def main():
    print('최상의 모듈(실행모듈, 독립실행)시 출력 합니다.')

def add(a, b):
    return a + b # 사칙연산

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == '__main__': #독립실행이라면
    main()  # 메인함수호출,, 여기정의
else:
    print('모듈이름: ' + __name__)  #호출당했으면 여기가 출력된다.

# 모듈 패스가 되야지 임포트 가능하다..
# 모듈 모아놓는 패스가 잡혀있어야 한다.

# 모듈패스 출력해보기.












