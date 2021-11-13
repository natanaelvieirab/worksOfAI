# Descrição

Desenvolver um algoritmo genético para encontrar um individuo(s) que assume valor mínimo para a função f(x)= x\*\*2 - 3x + 4, com as seguintes restrições:

- x deve estar no intervalo [-10,10];
- população deve ser restringida a 4 indivíduos;
- usar seleção dos individuos deve ser por torneio;
- a taxa para o crossover deve ser de 60%;
- a taxa de mutação deve ser de 1%;
- executar somente em 5 gerações;

## Executando

Clone este repositorio em sua maquina, dentro da pasta **Trabalho 02**, rode o seguinte comando: `python Genetic.py`;

## Sobre

**Individuo**: a classe _Individual_ é uma representação das caracteristicas em que o individuo possa ter. No cenário, atual, temos duas caracteristicas (atributos) :

- value: número decimal;
- identification : representação em binário do _value_ ;

**Operation**: nesta classe esta presente todas as operações necessária que o algoritmo genético irá utilizar, as principais são:

- bestBoys : que irá obter os individuos mais significativos para realizar a operação de cross-over;
- mutation: é responsável por realizar mutação nos individuos da geração;
- fitnessFunction: responsável por aplicar a função estabelecida ;
