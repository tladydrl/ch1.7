# module name: mymod2

import mymod

def main():
    print("독립실행시, 출력됩니다.")

# 모듈 임포트 잘되는지 확인용..
def power(x, y):  #마이 모드의 멀티플라이.
    r = 1
    for i in range(y): # 0에서부터 y ㅂ바로 앞까지.. 2라면 0, 1 두번하게됨.
        r = mymod.multiply(r, x)

    return r

if __name__ == '__main__':
    main()
else:
    print('모듈이름:' + __name__)







