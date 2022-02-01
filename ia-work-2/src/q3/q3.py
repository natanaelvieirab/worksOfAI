from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

def print_info(coefficients, mse_train, mse_test):
    print("Valores finais dos coeficientes: ")
    for coef in coefficients:
        print(coef)

    plt.plot(mse_train)
    plt.title('EQM x λ no conjunto de Treinamento')
    plt.ylabel('Erro quadrático médio')
    plt.xlabel('λ')
    plt.show()

    plt.plot(mse_test)
    plt.title('EQM x λ no conjunto de Teste')
    plt.ylabel('Erro quadrático médio')
    plt.xlabel('λ')
    plt.show()

def getCoefficientValue(x, y, modified_identify):
    matrix1 = np.matmul(x.T,x)
    matrix2 = matrix1 + modified_identify
    matrix2_inv = np.linalg.inv(matrix2)
    matrix3 = np.matmul(matrix2_inv, x.T)
    coefficients = np.matmul(matrix3, y)

    return coefficients

def mse(y, x, w):
    y_result = np.matmul(x, w)
    error = y - y_result
    squared_error = error **2
    mean_squared_error = sum(squared_error) / len(y)
    return mean_squared_error


df = read_csv('ex1data3.txt',sep=' ',header=None)
df.columns = ['x1','x2','x3','x4','x5','y']
df.insert(loc = 0, column = 'x0', value = 1)


train_length = 30
variables_number = 6


train = df.values[:train_length, :]
test = df.values[train_length:, :]

x_train = train[:, :variables_number]
y_train = train[:, variables_number]

x_test = test[:, :variables_number]
y_test = test[:, variables_number]

coefficients = []
mse_train = [] # Mean Square Error
mse_test = []

identity = np.identity(variables_number, dtype=int)
identity[0][0] = 0


# Treino
for lamb in range(variables_number):
    w = getCoefficientValue(x_train, y_train, lamb * identity)
    mse_train.append(mse(y_train, x_train, w))
    coefficients.append(w)

# Teste
for coefficient in coefficients:
    mse_test.append(mse(y_test, x_test, coefficient))


print_info(coefficients, mse_train, mse_test)
