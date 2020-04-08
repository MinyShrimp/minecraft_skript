import random

def slot():
    for k in range(10):
        arr = [0, 0, 0]
        for i in range(10000):
            _tmp = [0, 0, 0]
            for j in range(3):
                r = random.randint(0, 9)
                if r < 1:
                    pass
                elif r < 6:
                    _tmp[0] += 1
                elif r < 9:
                    _tmp[1] += 1
                else:
                    _tmp[2] += 1
            
            for j in range(3):
                if _tmp[j] == 3:
                    arr[j] += 1
            
        print("{}회차 슬롯머신 10000회 반복".format(k))
        print(arr)
        print('{}% {}% {}%'.format(arr[0] / 100, arr[1] / 100, arr[2] / 100))
        _result = arr[0] + arr[1] * 15 + arr[2] * 150
        print('{} {}'.format(_result, 10000 - _result))

def finder():
    r = random.randint(0, 8)
    _money = 0
    if r < 3:
        _money += 1