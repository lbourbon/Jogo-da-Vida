# JOGO DA VIDA ('John Conway´s Game of Life' por Lécio Bourbon) em Python3 para ser executado em Jupyter Notebook (.ipynb)


É um automato que tem por objetivo provar que regras simples podem dar origem a mecanismos complexos'''


#-> MODIFIQUE O GRID  COMO QUISER
#-> 1 SIGNIFICA CÉLULA VIVA
#-> 0 SIGNIFICA CÉLULA MORTA


  A função 'conta_vizinhos(grid, x, y)' está explicada pelo próprio nome, conta o número de vizinhos vivos da célula grid[x][y].


  A função 'aplica_regras(grid)' também pode ser entendida pelo próprio nome, ela aplica as 4 regras criadas por John Conway para 
o jogo da vida que são as seguintes:
  
  1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão
  2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
  3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
  4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.


Existem dois inputs que são escolhidos pelo usuário:
 -> gerações =  o número de vezes em que as regras são aplicadas, algumas configurações iniciais permitem sequencias infinitas outras
 terminam com poucas gerações
 -> velocidade = velocidade em que a 'animação' é executada. Recomendo escolher um número entre 1 e 10
