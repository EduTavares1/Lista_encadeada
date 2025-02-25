#Classe que representa um nó na lista encadeada
class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def obter_tamanho(self):
        return self.tamanho
    # Retorna o valor do nó em uma posição especifica da lista
    def obter_elemento(self, pos):
        if pos < 1 or pos > self.tamanho:
            print("Posicao invalida!")
            return None
        atual = self.cabeca
        for _ in range(1, pos):
            atual = atual.prox
        return atual.dado
     # Modifica o valor de um nó existente na lista
    def modificar_elemento(self, pos, novo_valor):
        if pos < 1 or pos > self.tamanho:
            print("Posicao invalida!")
            return
        atual = self.cabeca
        for _ in range(1, pos):
            atual = atual.prox
        atual.dado = novo_valor
    # Insere um novo nó na posição especificada
    def inserir_elemento(self, pos, valor):
        if pos < 1 or pos > self.tamanho + 1:
            print("Posicao invalida!")
            return
        novo_no = No(valor)
        if pos == 1:
            novo_no.prox = self.cabeca
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            for _ in range(1, pos - 1):
                atual = atual.prox
            novo_no.prox = atual.prox
            atual.prox = novo_no
        self.tamanho += 1

    def remover_elemento(self, pos):
        if pos < 1 or pos > self.tamanho:
            print("Posicao invalida!")
            return
        if pos == 1:
            self.cabeca = self.cabeca.prox
        else:
            atual = self.cabeca
            for _ in range(1, pos - 1):
                atual = atual.prox
            atual.prox = atual.prox.prox
        self.tamanho -= 1
     # Printa a lista na ordem de encadeamento dos nós
    def imprimir_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.prox
        print("NULL")

# Teste das funções
lista = ListaEncadeada()
print ("A lista está vazia",lista.esta_vazia())
lista.inserir_elemento(1, 10)
lista.inserir_elemento(2, 20)
lista.inserir_elemento(3, 30)

print ("Elementos na lista:" ,lista.obter_tamanho())
lista.imprimir_lista()

lista.modificar_elemento(2, 25)
lista.imprimir_lista()

lista.remover_elemento(2)
lista.imprimir_lista()

print("Elemento na posicao 2:", lista.obter_elemento(2))
