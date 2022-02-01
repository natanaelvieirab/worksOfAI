from pandas import read_csv
from numpy import random
from matplotlib import pyplot as plt

alpha = 0.001
epocas = 1000
data = read_csv('ex1data1.txt',header=None).values

omega = random.randn()
omega0 = random.randn()
mse = [] # Mean Square Error


for epoca in range(epocas):
    sum_mse = 0 
    random.shuffle(data)
    sample_length = random.randint(1, len(data))

    for i in range(sample_length):
        [x, y] = data[i]

        y_esp = omega * x + omega0
        error = y - y_esp
        
        sum_mse += error * error
        omega0 += alpha * error
        omega += alpha * error * x
    mse.append(sum_mse/sample_length)


print(omega)
print(omega0)


plt.plot(mse)
plt.title('EQM x Épocas')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.show()
