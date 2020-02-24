# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
tabuleiro = ['''

>>>>>>>>>> JOGO DA FORCA <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class JogoForca:

	# Método Construtor
	def __init__(self, palavra):
        # recebe a palavra e inicializa um objeto
		self.palavra = palavra
        
        # lista para as letras erradas
		self.letras_erradas = []
        
        # lista para as letras certas
		self.letras_certas = []
		
	# Método para adivinhar a letra
	def advinha(self, letra):
		if letra in self.palavra and letra not in self.letras_certas:
        # se a letra estiver dentro da palavra e a letra não estiver na lista de letras certas
			self.letras_certas.append(letra)
            
		elif letra not in self.palavra and letra not in self.letras_erradas:
        # se a letra não estiver dentro da palavra e a letra não estiver na lista de letras erradas
			self.letras_erradas.append(letra)
            
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def fim_jogo(self):
        # retorna se venceu ou perdeu o jogo
		return self.jogo_vencido() or (len(self.letras_erradas) == 6)
		
	# Método para verificar se o jogador venceu
	def jogo_vencido(self):
        # se não houver mais letras ocultas 
		if '_' not in self.palavra_oculta():
			return True
		return False

	# Método para não mostrar a letra no tabuleiro
	def palavra_oculta(self):
		rtn = ''
		for letra in self.palavra:
			if letra not in self.letras_certas:
				rtn += '_'
			else:
				rtn += letra
		return rtn

	# Método para checar o status do game e imprimir o board na tela
	def print_status_jogo(self):
		print (tabuleiro[len(self.letras_erradas)])
		print ('\nPalavra: ' + self.palavra_oculta())
		print ('\nLetras erradas: ',)
		for letra in self.letras_erradas:
			print (letra,)
		print ()
		print ('Letras corretas: ',)
		for letra in self.letras_certas:
			print (letra,)
		print ()

# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
        with open("palavras.txt", "rt") as f:
                banco_palavras = f.readlines()
        return banco_palavras[random.randint(0,len(banco_palavras))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = JogoForca(palavra_aleatoria())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.fim_jogo():
		game.print_status_jogo()
		input_usuario = input('\nDigite uma letra: ')
		game.advinha(input_usuario)

	# Verifica o status do jogo
	game.print_status_jogo()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.jogo_vencido():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.palavra)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
