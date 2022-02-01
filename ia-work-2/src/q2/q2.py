from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt


data_file = read_csv('ex1data2.txt',sep=' ',header=None) 
data_file.columns = ['X1', 'X2', 'Y']

alpha = 0.01
epocas = 100
data = data_file.values

omega = np.random.randn()
omega0 = np.random.randn()
omega1 = np.random.randn()
mse = [] # Mean Square Error


for epoca in range(epocas):
    sum_mse = 0
    np.random.shuffle(data)
    sample_length = np.random.randint(1, len(data))

    for i in range(sample_length):
        [x0, x1, y] = data[i]

        y_esp = omega + omega0 * x0 + omega1 * x1
        error = y - y_esp
        
        sum_mse += error * error
        omega += alpha * error
        omega0 += alpha * error * x0
        omega1 += alpha * error * x1
    mse.append(sum_mse/sample_length)

print('\nCoeficientes usando EQM')
print(omega)
print(omega0)
print(omega1)


plt.plot(mse)
plt.title('EQM x Épocas')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.show()



# Método dos Mínimos Quadrados.
data = np.append(np.ones((47, 1)), data_file.values, axis=1)
x = data[: , 0:3] # pega as 3 primeiras colunas (x0, x1, x2)
y = data[: , 3] # ultima coluna

matrix1 = np.matmul(x.T,x)
matrix1_inv = np.linalg.inv(matrix1)
matrix2 = np.matmul(matrix1_inv, x.T)
coefficients = np.matmul(matrix2, y)

print('\nCoeficientes do Método dos Mínimos Quadrados')
print(coefficients)
