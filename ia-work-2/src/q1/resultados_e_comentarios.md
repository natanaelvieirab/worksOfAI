# Coeficientes
omega = 1.1423103719327796
omega0 = -3.840547821861966


# Comentários

## Um modelo de regressão linear parece ser adequado para os dados em questão? 
- Sim, pois só é utilizado uma variável como parâmetro, no caso a variável 2 (coluna 2) é utilizado como base para a variável 1 (coluna 1).


## Através do gráfico “épocas x EQM” é possível verificar que o algoritmo está “aprendendo” ? Comente.
- Sim, pois o erro quadrado médio diminui a cada época, o que significa que o y_esp está cada vez mais próximo do y. 
  No entanto, em alguns testes, notou-se alguns valores de erros altos nas últimas épocas. Acreditamos que isso acontece, devido a aleatoriedade da quantidade de dados avaliados nas interações.
