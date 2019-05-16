import mymod2
import mymod

# 마이모드 두번 임포트 되버림..  # 결론: 걱정없이 중복되는거 상관없이 쓰면된다...
#
print(mymod.add(10,20))
print(mymod.subtract(10,20))
print(mymod.multiply(10,20))
print(mymod.divide(10,20))
print(mymod2.power(10,20))





