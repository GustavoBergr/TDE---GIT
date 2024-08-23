


#Aluno Gustavo Berg Ribeiro, turma B-Período 2-BCC




import os

print(''' 
      

    

╔═══╦═╗╔═╦═══╦═══╦═══╦══╦═══╦══╦═══╗  ─╔╗─  ────  ╔═══╦═══╦═╗─╔╗─╔╦╗─╔╦═╗─╔╦════╦═══╦═══╗
║╔══╩╗╚╝╔╣╔══╣╔═╗║╔═╗╠╣╠╣╔═╗╠╣╠╣╔═╗║  ╔╝║─  ────  ║╔═╗║╔═╗║║╚╗║║─║║║─║║║╚╗║║╔╗╔╗║╔═╗║╔═╗║
║╚══╗╚╗╔╝║╚══╣╚═╝║║─╚╝║║║║─╚╝║║║║─║║  ╚╗║─  ────  ║║─╚╣║─║║╔╗╚╝║─║║║─║║╔╗╚╝╠╝║║╚╣║─║║╚══╗
║╔══╝╔╝╚╗║╔══╣╔╗╔╣║─╔╗║║║║─╔╗║║║║─║║  ─║║─  ╔══╗  ║║─╔╣║─║║║╚╗║╠╗║║║─║║║╚╗║║─║║─║║─║╠══╗║
║╚══╦╝╔╗╚╣╚══╣║║╚╣╚═╝╠╣╠╣╚═╝╠╣╠╣╚═╝║  ╔╝╚╗  ╚══╝  ║╚═╝║╚═╝║║─║║║╚╝║╚═╝║║─║║║─║║─║╚═╝║╚═╝║
╚═══╩═╝╚═╩═══╩╝╚═╩═══╩══╩═══╩══╩═══╝  ╚══╝  ────  ╚═══╩═══╩╝─╚═╩══╩═══╩╝─╚═╝─╚╝─╚═══╩═══╝
      
      
      ''')


class OperacaoDosConjuntos: #define a classe para posteriormente realizar as operações 
    def processamentos_dos_arquivos(self, nome_do_arquivo):
        if not os.path.isfile(nome_do_arquivo):
            raise FileNotFoundError(f"O arquivo '{nome_do_arquivo}' não foi encontrado, insira um arquivo válido!!") #processa o arquivo e verifica se não possui erro
        
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines() 
            #abre o arquivo e faz a leitura das linhas 

        num_operacoes = int(linhas[0].strip())
        i = 1
        resultados = [] 
        #lê e obtém a quantidade de operações para armazenas os resultados em resultados

        for _ in range(num_operacoes):
            tipo_da_operacao = linhas[i].strip()
            conjA = set(linhas[i+1].strip().split(","))
            conjB = set(linhas[i+2].strip().split(","))
            resultado = set()
            descricao = "" 
            #encontra a operação atual, cria os conjuntos e inicia o resultado

            if tipo_da_operacao == "U":
                resultado = conjA.union(conjB)
                descricao = "União"
            elif tipo_da_operacao == "I":
                resultado = conjA.intersection(conjB)
                descricao = "Interseção"
            elif tipo_da_operacao == "D":
                resultado = conjA.difference(conjB)
                descricao = "Diferença"
            elif tipo_da_operacao == "C":
                produto = {f"({x},{y})" for x in conjA for y in conjB}
                resultado = produto
                descricao = "Produto Cartesiano"
                 #realiza as operações (Operações que estão inseridas na documentação oficial do Python), podendo até colocar um else para possíveis erros de leitura da operação

            resultado_formatado = ",".join(sorted(resultado)) if tipo_da_operacao != "C" else ",".join(resultado)
            resultado_final = (f"{descricao}: conjunto A {{{','.join(sorted(conjA))}}}, "
                               f"conjunto B {{{','.join(sorted(conjB))}}}, Resultado: {{{resultado_formatado}}}")
            resultados.append(resultado_final)
            i += 3
             #ordena e junta os pares
        return resultados

    def processando_arquivos(self, arquivos):
        for nome_do_arquivo in arquivos:
            print(f"Arquivo inserido para análise: {nome_do_arquivo}")
            resultados = self.processamentos_dos_arquivos(nome_do_arquivo)
            for resultado in resultados:
                print(resultado)
            print("\n")
            #para cada arquivo na lista, imprime, processa (podendo encontrar erros com FileNotFoundError, porém não coloquei por eu ter feito o arquivo)

if __name__ == "__main__":
    arquivos = ["arquivo_de_texto1.txt", "arquivo_de_texto2.txt", "arquivo_de_texto3.txt"]
    processador = OperacaoDosConjuntos()
    processador.processando_arquivos(arquivos)
    #define como bloco principal, cria uma instância para classe e chama o método para o processamento do arquivo
