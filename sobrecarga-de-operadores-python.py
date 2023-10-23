class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


class Fisica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf


class Juridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self._cnpj = cnpj

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj


class Matriz:
    def __init__(self, dimensao, data, tipo):
        self.dimensao = dimensao
        self.data = data
        self.tipo = tipo

    def __add__(self, outra_matriz):
        if self.dimensao != outra_matriz.dimensao:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")
        nova_data = [[0 for _ in range(self.dimensao)] for _ in range(self.dimensao)]
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                nova_data[i][j] = self.data[i][j] + outra_matriz.data[i][j]
        return Matriz(self.dimensao, nova_data, self.tipo)

    def __mul__(self, outra_matriz):
        if self.dimensao != outra_matriz.dimensao:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem multiplicadas.")
        nova_data = [[0 for _ in range(self.dimensao)] for _ in range(self.dimensao)]
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                for k in range(self.dimensao):
                    nova_data[i][j] += self.data[i][k] * outra_matriz.data[k][j]
        return Matriz(self.dimensao, nova_data, self.tipo)

    def __str__(self):
        return f"Matriz {self.tipo} {self.dimensao}x{self.dimensao}: {self.data}"


# Exemplo de uso
matriz1 = Matriz(2, [[1, 2], [3, 4]], "A")
matriz2 = Matriz(2, [[5, 6], [7, 8]], "B")

print(matriz1)
print(matriz2)

matriz_soma = matriz1 + matriz2
print("Soma das matrizes:")
print(matriz_soma)

matriz_produto = matriz1 * matriz2
print("Produto das matrizes:")
print(matriz_produto)