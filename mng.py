class Bloco:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.conteudo = None
        self.proximo = None

class DiscoVirtual:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.espaco_livre = tamanho
        self.primeiro_bloco = Bloco(tamanho)
        self.primeiro_bloco.conteudo = "Espaco Livre"
        self.primeiro_bloco.proximo = None

    def criar_arquivo(self, palavra):
        if len(palavra) > self.espaco_livre:
            print("Erro: Memória insuficiente para criar o arquivo.")
            return

        bloco_atual = self.primeiro_bloco
        while bloco_atual:
            if bloco_atual.conteudo == "Espaco Livre":
                if len(palavra) <= bloco_atual.tamanho:
                    if len(palavra) == bloco_atual.tamanho:
                        bloco_atual.conteudo = palavra
                    else:
                        novo_bloco = Bloco(bloco_atual.tamanho - len(palavra))
                        novo_bloco.conteudo = "Espaco Livre"
                        novo_bloco.proximo = bloco_atual.proximo
                        bloco_atual.tamanho = len(palavra)
                        bloco_atual.conteudo = palavra
                        bloco_atual.proximo = novo_bloco
                    self.espaco_livre -= len(palavra)
                    print(f"Arquivo '{palavra}' criado com sucesso.")
                    return
            bloco_atual = bloco_atual.proximo

        print("Erro: Não foi possível criar o arquivo.")

    def ler_arquivo(self, palavra):
        bloco_atual = self.primeiro_bloco
        while bloco_atual:
            if bloco_atual.conteudo == palavra:
                print(f"Conteúdo do arquivo '{palavra}': {bloco_atual.conteudo}")
                return
            bloco_atual = bloco_atual.proximo

        print(f"Arquivo '{palavra}' não encontrado.")

    def mostrar_lista_encadeada(self):
        bloco_atual = self.primeiro_bloco
        while bloco_atual:
            print(f"Endereço: {bloco_atual}, Tamanho: {bloco_atual.tamanho}, Conteúdo: {bloco_atual.conteudo}")
            bloco_atual = bloco_atual.proximo

    def excluir_arquivo(self, palavra):
        bloco_atual = self.primeiro_bloco
        while bloco_atual:
            if bloco_atual.conteudo == palavra:
                bloco_atual.conteudo = "Espaco Livre"
                self.espaco_livre += len(palavra)
                # Verificar se o bloco seguinte também é "Espaco Livre" e unir os blocos livres adjacentes
                proximo_bloco = bloco_atual.proximo
                if proximo_bloco and proximo_bloco.conteudo == "Espaco Livre":
                    bloco_atual.tamanho += proximo_bloco.tamanho
                    bloco_atual.proximo = proximo_bloco.proximo
                print(f"Arquivo '{palavra}' excluído com sucesso.")
                return
            bloco_atual = bloco_atual.proximo

        print(f"Arquivo '{palavra}' não encontrado.")

    def listar_blocos_livres(self):
        bloco_atual = self.primeiro_bloco
        blocos_livres = []
        while bloco_atual:
            if bloco_atual.conteudo == "Espaco Livre":
                blocos_livres.append((bloco_atual.tamanho, bloco_atual))
            bloco_atual = bloco_atual.proximo
        return blocos_livres


# Exemplo de uso:
disco = DiscoVirtual(32)

disco.criar_arquivo("texto1")
disco.criar_arquivo("texto2")
disco.criar_arquivo("texto3")

disco.ler_arquivo("texto2")

disco.excluir_arquivo("texto2")

disco.criar_arquivo("texto4")

disco.ler_arquivo("texto4")

disco.criar_arquivo("texto5")
disco.criar_arquivo("texto6")
disco.criar_arquivo("maguire")

blocos_livres = disco.listar_blocos_livres()
print("Blocos Livres:")
for tamanho, bloco in blocos_livres:
    print(f"Tamanho: {tamanho}, Endereço: {bloco}")

disco.mostrar_lista_encadeada()
