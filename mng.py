class Bloco:
    def __init__(self, dado):
        self.dado = dado
        self.proximo_bloco = None

class Disco:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [Bloco('') for _ in range(tamanho)]
        self.espaco_livre = [Bloco('') for _ in range(tamanho)]
        self.espaco_livre[0] = self.dados[0]
        self.espaco_livre[0].proximo_bloco = self.dados[1]
        for i in range(1, tamanho - 1):
            self.espaco_livre[i] = self.dados[i]
            self.espaco_livre[i].proximo_bloco = self.dados[i + 1]

    def criar_arquivo(self, palavra):
        if len(palavra) > self.espaco_livre_disponivel():
            print("Memória insuficiente para criar o arquivo.")
            return

        bloco_atual = self.espaco_livre[0]
        for char in palavra:
            bloco_atual.dado = char
            if bloco_atual.proximo_bloco:
                bloco_atual = bloco_atual.proximo_bloco
            else:
                break

    def ler_arquivo(self):
        bloco_atual = self.dados[0]
        arquivo = ""
        while bloco_atual:
            arquivo += bloco_atual.dado
            bloco_atual = bloco_atual.proximo_bloco
        return arquivo

    def excluir_arquivo(self):
        bloco_atual = self.dados[0]
        while bloco_atual:
            bloco_atual.dado = ''
            bloco_atual = bloco_atual.proximo_bloco
        self.atualizar_espaco_livre()

    def espaco_livre_disponivel(self):
        espaco_disponivel = 0
        bloco_atual = self.espaco_livre[0]
        while bloco_atual:
            espaco_disponivel += 1
            bloco_atual = bloco_atual.proximo_bloco
        return espaco_disponivel

    def atualizar_espaco_livre(self):
        bloco_atual = self.dados[0]
        espaco_livre_index = 0
        while bloco_atual:
            if bloco_atual.dado == '':
                self.espaco_livre[espaco_livre_index] = bloco_atual
                espaco_livre_index += 1
            bloco_atual = bloco_atual.proximo_bloco
        while espaco_livre_index < self.tamanho:
            self.espaco_livre[espaco_livre_index] = None
            espaco_livre_index += 1

# Exemplo de uso
disco = Disco(32)
disco.criar_arquivo("exemplo")
print("Arquivo no disco:", disco.ler_arquivo())
disco.excluir_arquivo()
print("Espaço livre no disco:", disco.espaco_livre_disponivel())
