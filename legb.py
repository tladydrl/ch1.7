# LEGB Rules

# 1. Local
# 2. Enclosing Function(내포한 함수) (부모함수..)
# 3. Global
# 4. Built-In

a = 1  # 이 변수는 글로벌이다.

def f():
    b = 1  # 이 함수(f) 의 로컬함수.  # 이건 인클로징 변수이다.

    def g():   # 확인 위해서..
        b = 100  # 이 함수 안에서 로컬이 된다ㅣ. # 로컬이다.
        print(b)
        print(__name__) # 내장변수(built in) 이건 빌트인이다. B. 모듈네임..
    b = 20
    g()

f()  # 이 함수를 실행시킨다..





