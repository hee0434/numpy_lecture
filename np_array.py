import numpy as np

a = np.arange(15).reshape(3, 5) #class내에서 method를 이용해서 행렬 만들어주는 것
b = np.array([2,3,4])

print(a)
print(type(a))
print(a.shape) #행렬의 차원 확인
print(a.ndim) #차원 숫자를 나타낸다
print(a.dtype.name)

print(type(b))

n_arr = np.array(range(1,11), dtype='int32')
n_arr.size
print(n_arr.size)
data_size=n_arr.size*n_arr.itemsize
print(data_size)
print(n_arr.itemsize)
print(n_arr)

p_num = np.random.rand(6)
print(p_num)


#사용자로부터 2이상의 수 n을 입력으로 받아서, 입력된 수를 바탕으로 다음과 같은 nxn 크기의 다차원 배열 a를 생성하는 프로그램을 작성하시오. 이 때 배열의 내용은 0과 1의 값이 체크 판 패턴으로 교차하여 나타나도록 하여라. #
n = int(input('n을 입력하세요!'))
a = np.zeros((n,n), dtype='int64')    #or ones
#a[2,1] = 10 #2행 2열이 10으로 바뀜
for i in range(n) :
    for j in range(n):
        # or a[i,j] = 10
        if (i+j)%2 == 0:
            a[i,j] = 1

print(a)
