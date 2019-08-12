import sys
import random

if len(sys.argv) != 3:
    print('Needs 2 arguments')
    sys.exit(1)

_num = int(sys.argv[1])
_sum = int(sys.argv[2])

mid = int(_sum / _num)

if mid == 0:
    mid = 1
 
out = []
for i in range(_num):
    distance = random.randint(0, mid * (i+1))
    out.append(distance)


rand_sum = sum(out)
print(f'rand_sum: {rand_sum}\nog_sum: {_sum}')

differenc = rand_sum - _sum
print(f'differenc: {differenc}')

leftover = differenc % _num
print(f'leftover: {leftover}')

while differenc != 0:
    if differenc > 0:
        if leftover == 0:
            dif_mid = int(abs(differenc) / _num)
            print(f'Subtracting {dif_mid} from all.')
            out = [a - dif_mid for a in out]
        else:
            sub_range =_num - leftover
            dif_mid = int(abs(differenc) / sub_range)
            if dif_mid == 0:
                dif_mid = 1
            print(f'Subtracting {dif_mid} from {sub_range} number of elements.')
            for i in range(sub_range):
                out[i] -= dif_mid
    elif differenc < 0:
        if leftover == 0:
            dif_mid = int(abs(differenc) / _num)
            print(f'Adding {dif_mid} to all.')
            out = [a + dif_mid for a in out]
        else:
            sub_range =_num - leftover
            dif_mid = int(abs(differenc) / sub_range)
            if dif_mid == 0:
                dif_mid = 1
            print(f'Adding {dif_mid} to {sub_range} number of elements.')
            for i in range(sub_range):
                out[i] += dif_mid
    rand_sum = sum(out)
    differenc = rand_sum - _sum
    leftover = differenc % _num
    print(f'differenc: {differenc}')
        
print(out)
