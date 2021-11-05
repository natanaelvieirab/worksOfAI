## Descrição

O jogo dos 15 é uma matriz de tamanho 4x4, onde há 15 números (1 a 15) embaralhados, mais um espaço em branco, representado por 0. O objetivo é mover o espaço em branco na matriz, para que chegue no estado final, que é os números ordenados, e o espaço em branco na ultima posição.
<br/>
Por exemplo, a tabela abaixo seria o estado inicial, com os números embaralhados.
<br/>

|   |   |   |   |
|---|---|---|---|
| 1 | 2 | 3 |4 |
| 5 | 6 | 8 |12 |
| 13 | 9 | 0 |7 |
| 14 | 11 | 10 |15 |

<br/>
E essa seria a representação do estado final após os movimentos da peça em branco (0):
<br/>

|   |   |   |   |
|---|---|---|---|
| 1 | 2 | 3 |4  |
| 5 | 6 | 7 |8  |
| 9 | 10 | 11 |12 |
| 13 | 14 | 15 |0 |

<br/>

## Regras de movimentação
Para chegar no estado final, só é possível realizar movimentação do estado em branco para cima, direita, baixo e esquerda, somente.

## Como executar

Nesta pasta há arquivos ".py", que representão cada uma das busca solicitada pelo trabalho. A tabela abaixo, faz um mapeamento da busca e sua representação em ".py".


| Algoritmo             | Arquivo         |
| --------------------- | --------------- |
| Busca em largura      | WideSearch.py   |
| Busca em profundidade | DeepSearch.py   |
| Busca Gulosa          | GreedySearch.py |
| A\*                   | AStar.py        |


Para executar qualquer algoritmo execute `python nome-da-busca.py` e tenha certeza de estar usando python em sua versão 3.

