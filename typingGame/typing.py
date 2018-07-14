import random
import time

# 단어 리스트 : 여기에 단어를 추가하면 문제가 나옵니다.
w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
n = 1
print('if u r ready, press, the enter key!')
input()
start = time.time()

q = random.choice(w)

while n <= 5:
    print('*문제', n)
    print(q)
    x = input()
    if q == x:
        print('pass !!')
        n += 1
        q  = random.choice(w)
    else:
        print("fail !! retry !!")

end = time.time()
et = end - start
et = format(et, ".2f")
print("typing time :", et, " 초")



