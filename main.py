class Objeto:
    def __init__(self, chave, nome):
        self.chave = chave
        self.nome = nome

    def get_chave(self):
        return self.chave

    def get_nome(self):
        return self.nome


class HashTable:
    def __init__(self, capacidade_total):
        self.n = capacidade_total
        # Primeiro nível: vetor de 10 ponteiros para o segundo nível
        self.primeiro_nivel = [None] * 10

    # Função hash para o primeiro nível (mapeia para 0-9)
    def hash_primeiro_nivel(self, chave):
        return chave % 10

    # Função hash para o segundo nível (diferente da primeira)
    def hash_segundo_nivel(self, chave, tamanho_segundo_nivel):
        return (chave // 10) % tamanho_segundo_nivel

    def inserir(self, chave, nome):
        indice_primeiro_nivel = self.hash_primeiro_nivel(chave)

        # Se a tabela do segundo nível ainda não foi criada
        if self.primeiro_nivel[indice_primeiro_nivel] is None:
            tamanho_segundo_nivel = self.n // 10
            if tamanho_segundo_nivel < 1:
                tamanho_segundo_nivel = 1
            self.primeiro_nivel[indice_primeiro_nivel] = [[] for _ in range(tamanho_segundo_nivel)]

        # Referência para a tabela do segundo nível
        segundo_nivel = self.primeiro_nivel[indice_primeiro_nivel]

        # Cálculo do índice no segundo nível
        indice_segundo_nivel = self.hash_segundo_nivel(chave, len(segundo_nivel))

        # Insere o objeto na lista
        segundo_nivel[indice_segundo_nivel].append(Objeto(chave, nome))

        print(f"Objeto '{nome}' com chave {chave} inserido em [{indice_primeiro_nivel}][{indice_segundo_nivel}]")

    def buscar(self, chave):
        indice_primeiro_nivel = self.hash_primeiro_nivel(chave)

        # Verifica se a tabela do segundo nível existe
        if self.primeiro_nivel[indice_primeiro_nivel] is None:
            return None

        segundo_nivel = self.primeiro_nivel[indice_primeiro_nivel]

        # Calcula o índice no segundo nível
        indice_segundo_nivel = self.hash_segundo_nivel(chave, len(segundo_nivel))

        # Busca na lista
        for objeto in segundo_nivel[indice_segundo_nivel]:
            if objeto.get_chave() == chave:
                return objeto
        return None

    def imprimir(self):
        print("\n----- Estrutura da Tabela Hash -----")
        for i, tabela in enumerate(self.primeiro_nivel):
            print(f"Primeiro Nível [{i}]: ", end="")
            if tabela is None:
                print("Vazio")
                continue

            for j, lista in enumerate(tabela):
                print(f"  Segundo Nível [{j}]: ", end="")
                if not lista:
                    print("Vazio")
                else:
                    print("[", end=" ")
                    for obj in lista:
                        print(f"({obj.get_chave()}:{obj.get_nome()})", end=" ")
                    print("]")
        print("---------------------------------")




def main():
    # Exemplo de uso
    tabela = HashTable(100)

    # Inserindo objetos
    tabela.inserir(0, "Joao")
    tabela.inserir(1, "Maria")
    tabela.inserir(10, "Pedro")
    tabela.inserir(21, "Ana")
    tabela.inserir(20, "Lucas")
    tabela.inserir(30, "Mariana")
    tabela.inserir(42, "Rafael")
    tabela.inserir(81, "Beatriz")
    tabela.inserir(90, "Carlos")

    # Imprimir a tabela
    tabela.imprimir()

    # Buscar objetos através de suas chaves
    chave_busca = 21
    resultado = tabela.buscar(chave_busca)

    if resultado:
        print(f"\nObjeto encontrado com chave {chave_busca}: {resultado.get_nome()}")
    else:
        print(f"\nObjeto com chave {chave_busca} não encontrado.")

    chave_busca = 50
    resultado = tabela.buscar(chave_busca)

    if resultado:
        print(f"Objeto encontrado com chave {chave_busca}: {resultado.get_nome()}")
    else:
        print(f"Objeto com chave {chave_busca} não encontrado.")

if __name__ == "__main__":
    main()