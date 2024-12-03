
# Documentação do Programa de Árvore Geradora Mínima (AGM)

Este programa permite calcular a **Árvore Geradora Mínima (AGM)** de um grafo utilizando dois algoritmos: **Prim** e **Kruskal**. O usuário escolhe o algoritmo desejado e fornece a matriz de adjacência do grafo para que o programa calcule a solução.

---

## Requisitos
- Python 3.x instalado na máquina
- Um editor de texto ou IDE para criar e editar arquivos Python

---

## Como usar o programa


### 1. Executar o programa
1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta onde salvou o arquivo `agm.py`.
3. Execute o programa com o comando:
   ```bash
   python agm.py
   ```

### 2. Interagir com o programa
Siga as instruções do console:
1. Escolha o algoritmo (1 para Prim ou 2 para Kruskal).
2. Insira a matriz de adjacência linha por linha. Exemplo:
   ```
   0 15 19 17 0 0 0 0 0 0
   15 0 10 0 17 0 0 0 0 0
   19 10 0 16 12 0 0 0 0 0
   17 0 16 0 20 0 0 13 0 0
   0 17 12 20 0 14 0 0 0 0
   0 0 0 0 14 0 6 4 0 0
   0 0 0 0 0 6 0 3 9 11
   0 0 0 13 0 4 3 0 4 0
   0 0 0 0 0 0 9 4 0 2
   0 0 0 0 0 0 11 0 2 0
   ```
   Pressione Enter duas vezes para finalizar a entrada.

3. (Apenas para Prim) Escolha o vértice inicial (começando do índice 0).

### 3. Ver o resultado
O programa exibirá as arestas da Árvore Geradora Mínima e o peso total.

---

## Exemplo de saída

### Algoritmo de Prim:
```
Árvore Geradora Mínima usando Prim:
Aresta 0 -> 1 com peso 15
Aresta 1 -> 2 com peso 10
Aresta 2 -> 4 com peso 12
Aresta 4 -> 5 com peso 14
Aresta 5 -> 7 com peso 4
Aresta 7 -> 6 com peso 3
Aresta 7 -> 8 com peso 4
Aresta 8 -> 9 com peso 2
Aresta 7 -> 3 com peso 13
Peso total da AGM: 77
```

### Algoritmo de Kruskal:
```
Árvore Geradora Mínima usando Kruskal:
Aresta 8 -> 9 com peso 2
Aresta 7 -> 6 com peso 3
Aresta 5 -> 7 com peso 4
Aresta 7 -> 8 com peso 4
Aresta 1 -> 2 com peso 10
Aresta 2 -> 4 com peso 12
Aresta 7 -> 3 com peso 13
Aresta 4 -> 5 com peso 14
Aresta 0 -> 1 com peso 15
Peso total da AGM: 77
```
