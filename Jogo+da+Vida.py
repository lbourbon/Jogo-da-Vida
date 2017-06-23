# coding: utf-8

'''JOGO DA VIDA ('John Conway´s Game of Life' por Lécio Bourbon)  para Jupyter Notebook
É um automato que tem por objetivo provar que a regras simples podem dar origem a mecanismos complexos'''

from time import sleep
from copy import deepcopy
from IPython.display import clear_output

#-> MODIFIQUE O GRID ABAIXO COMO QUISER,  1 SIGNIFICA CÉLULA VIVA,  0 SIGNIFICA CÉLULA MORTA

grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


def conta_vizinhos(grid, x, y):
    return sum(grid[x-1][y-1:y+2]) + sum(grid[x][y-1:y+2]) + sum(grid[x+1][y-1:y+2]) - grid[x][y]

def aplica_regras(grid):
    ''' Aplica as regras do Jogo da Vida. Ler readme'''
    temp = deepcopy(grid)
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            
            if grid[i][j] == 1 and (conta_vizinhos(grid, i, j) < 2 or conta_vizinhos(grid, i, j) > 3):
                temp[i][j] = 0
                
            elif conta_vizinhos(grid, i, j) == 3 or (grid[i][j] == 1 and conta_vizinhos(grid, i, j) == 2):
                temp[i][j] = 1
                
    return temp


gerações = int(input('Escolha o número de gerações. (ex: 100) '))
velocidade = int(input('Escolha a velocidade, de 1 a 10:  '))

for i in range(int(gerações/2)):
    temp = aplica_regras(grid)
    for linha in temp:
        print(linha)
    sleep(1/velocidade)
    clear_output(wait=True)
    grid = aplica_regras(temp)
    for linha in grid:
        print(linha)
    sleep(1/velocidade)
    clear_output(wait=True)

