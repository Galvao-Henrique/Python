#Implemente uma pilha de inteiros utilizando vetor. Crie as operações push, pop, top e
#isEmpty.

class Pilha:
    def __init__(self):
        self.itens = []  # vetor que armazena os elementos da pilha

    def push(self, valor):
        """Insere um elemento no topo da pilha"""
        self.itens.append(valor)
        print(f"Push: {valor} adicionado")

    def pop(self):
        """Remove e retorna o elemento do topo da pilha"""
        if not self.isEmpty():
            valor = self.itens.pop()
            print(f"Pop: {valor} removido")
            return valor
        else:
            print("Pop falhou: pilha vazia")
            return None

    def top(self):
        """Retorna o elemento do topo sem removê-lo"""
        if not self.isEmpty():
            print(f"Topo da pilha: {self.itens[-1]}")
            return self.itens[-1]
        else:
            print("Topo não existe: pilha vazia")
            return None

    def isEmpty(self):
        """Verifica se a pilha está vazia"""
        return len(self.itens) == 0

    def __str__(self):
        """Representação em string da pilha"""
        return f"Pilha: {self.itens}"


if __name__ == "__main__":
    pilha = Pilha()

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    pilha.top()   # mostra o elemento do topo
    pilha.pop()   # remove o topo
    pilha.pop()
    pilha.pop()
    pilha.pop()   # tentativa em pilha vazia

    print(pilha)
