# 1 - Define a função calcular_imc que recebe peso e altura
def calcular_imc(peso, altura):
    # 2 - Docstring: documentação da função
    """
    Calcula o IMC com base no peso e altura
    
    Args:
        peso: peso em kg
        altura: altura em metros
    
    Returns:
        IMC calculado
    """
    # 3 - Retorna o resultado da divisão do peso pela altura ao quadrado
    # 4 - altura ** 2 é o mesmo que altura * altura
    return peso / (altura ** 2)

# 5 - Define a função classificar_imc que recebe o IMC
def classificar_imc(imc):
    # 6 - Docstring da função
    """
    Classifica o IMC de acordo com a tabela da OMS
    
    Args:
        imc: valor do IMC calculado
    
    Returns:
        Classificação e grau de obesidade
    """
    # 7 - Verifica se o IMC é menor que 18.5
    if imc < 18.5:
        # 8 - Retorna tupla com classificação, categoria e grau
        return "Abaixo do peso", "Magreza", 0
    # 9 - Senão, verifica se o IMC está entre 18.5 e 24.9
    elif 18.5 <= imc < 25:
        # 10 - Retorna classificação "Peso normal"
        return "Peso normal", "Saudável", 0
    # 11 - Senão, verifica se o IMC está entre 25 e 29.9
    elif 25 <= imc < 30:
        # 12 - Retorna classificação "Sobrepeso"
        return "Sobrepeso", "Sobrepeso", 1
    # 13 - Senão, verifica se o IMC está entre 30 e 34.9
    elif 30 <= imc < 35:
        # 14 - Retorna classificação "Obesidade grau 1"
        return "Obesidade grau 1", "Obesidade", 2
    # 15 - Senão, verifica se o IMC está entre 35 e 39.9
    elif 35 <= imc < 40:
        # 16 - Retorna classificação "Obesidade grau 2"
        return "Obesidade grau 2", "Obesidade severa", 2
    # 17 - Senão (IMC maior ou igual a 40)
    else:
        # 18 - Retorna classificação "Obesidade grau 3"
        return "Obesidade grau 3", "Obesidade mórbida", 3

# 19 - Define a função calcular_peso_ideal que recebe altura e IMC atual
def calcular_peso_ideal(altura, imc_atual):
    # 20 - Docstring da função
    """
    Calcula a faixa de peso ideal
    
    Args:
        altura: altura em metros
        imc_atual: IMC atual
    
    Returns:
        Tupla com peso mínimo ideal, peso máximo ideal e IMC ideal
    """
    # 21 - Define o IMC mínimo ideal da OMS
    imc_min_ideal = 18.5
    # 22 - Define o IMC máximo ideal da OMS
    imc_max_ideal = 24.9
    
    # 23 - Calcula o peso mínimo ideal (IMC min * altura²)
    peso_min_ideal = imc_min_ideal * (altura ** 2)
    # 24 - Calcula o peso máximo ideal (IMC max * altura²)
    peso_max_ideal = imc_max_ideal * (altura ** 2)
    
    # 25 - Retorna os valores arredondados com 1 casa decimal
    return round(peso_min_ideal, 1), round(peso_max_ideal, 1)

# 26 - Define a função exibir_recomendacoes que recebe IMC e classificação
def exibir_recomendacoes(imc, classificacao):
    # 27 - Docstring da função
    """
    Exibe recomendações baseadas no IMC
    
    Args:
        imc: valor do IMC
        classificacao: classificação do IMC
    """
    # 28 - Imprime uma linha separadora com 50 "="
    print("\n" + "="*50)
    # 29 - Imprime o título "RECOMENDAÇÕES DE SAÚDE:"
    print("RECOMENDAÇÕES DE SAÚDE:")
    # 30 - Imprime linha separadora
    print("="*50)
    
    # 31 - Verifica se o IMC é menor que 18.5
    if imc < 18.5:
        # 32 - Imprime recomendação para ganho de peso
        print("• Consulte um nutricionista para ganho de peso saudável")
        # 33 - Imprime recomendação para aumentar ingestão calórica
        print("• Aumente a ingestão de alimentos nutritivos e calóricos")
        # 34 - Imprime recomendação para fortalecimento muscular
        print("• Pratique exercícios de fortalecimento muscular")
    # 35 - Senão, verifica se o IMC está entre 18.5 e 24.9
    elif 18.5 <= imc < 25:
        # 36 - Imprime recomendação para manter alimentação equilibrada
        print("• Mantenha uma alimentação equilibrada")
        # 37 - Imprime recomendação para continuar atividades físicas
        print("• Continue praticando atividades físicas regularmente")
        # 38 - Imprime recomendação para check-ups médicos
        print("• Faça check-ups médicos periódicos")
    # 39 - Senão, verifica se o IMC está entre 25 e 29.9
    elif 25 <= imc < 30:
        # 40 - Imprime recomendação para dieta equilibrada
        print("• Adote uma dieta mais equilibrada e reduza calorias")
        # 41 - Imprime recomendação para aumentar exercícios aeróbicos
        print("• Aumente a prática de exercícios aeróbicos")
        # 42 - Imprime recomendação para consultar nutricionista
        print("• Considere consultar um nutricionista")
    # 43 - Senão (obesidade)
    else:
        # 44 - Imprime recomendação para orientação médica
        print("• Procure orientação médica especializada")
        # 45 - Imprime recomendação para programa de emagrecimento
        print("• Inicie um programa de emagrecimento supervisionado")
        # 46 - Imprime recomendação para exercícios de baixo impacto
        print("• Pratique exercícios de baixo impacto regularmente")

# 47 - Define a função consultar_imc (função principal)
def consultar_imc():
    # 48 - Docstring da função
    """
    Função principal para consulta de IMC
    """
    # 49 - Imprime linha separadora
    print("="*50)
    # 50 - Imprime título "CALCULADORA DE IMC"
    print("CALCULADORA DE IMC")
    # 51 - Imprime linha separadora
    print("="*50)
    
    # 52 - Inicia um loop infinito (while True)
    while True:
        # 53 - Inicia bloco try para capturar exceções
        try:
            # 54 - Solicita o nome e remove espaços extras com strip()
            # 55 - title() coloca a primeira letra de cada palavra em maiúscula
            nome = input("\nDigite seu nome: ").strip().title()
            # 56 - Solicita a idade e converte para inteiro
            idade = int(input("Digite sua idade: "))
            
            # 57 - Verifica se a idade está fora do intervalo permitido
            if idade < 2 or idade > 120:
                # 58 - Imprime mensagem de erro
                print("❌ Idade inválida! Deve estar entre 2 e 120 anos.")
                # 59 - Volta ao início do loop (continua)
                continue
            
            # 60 - Solicita o peso e converte para float
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            # 61 - Solicita a altura e converte para float
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))
            
            # 62 - Verifica se o peso está fora do intervalo permitido
            if peso <= 0 or peso > 500:
                # 63 - Imprime mensagem de erro
                print("❌ Peso inválido! Deve estar entre 1 e 500 kg.")
                # 64 - Volta ao início do loop
                continue
            
            # 65 - Verifica se a altura está fora do intervalo permitido
            if altura <= 0 or altura > 2.5:
                # 66 - Imprime mensagem de erro
                print("❌ Altura inválida! Deve estar entre 0.5 e 2.5 metros.")
                # 67 - Volta ao início do loop
                continue
            
            # 68 - Chama a função calcular_imc passando peso e altura
            imc = calcular_imc(peso, altura)
            # 69 - Chama a função classificar_imc e desempacota o retorno
            classificacao, categoria, grau_obesidade = classificar_imc(imc)
            # 70 - Chama a função calcular_peso_ideal e desempacota o retorno
            peso_min_ideal, peso_max_ideal = calcular_peso_ideal(altura, imc)
            
            # 71 - Imprime linha separadora
            print("\n" + "="*50)
            # 72 - Imprime o resultado com o nome em maiúsculas
            print(f"RESULTADO PARA {nome.upper()}")
            # 73 - Imprime linha separadora
            print("="*50)
            # 74 - Imprime a idade
            print(f"Idade: {idade} anos")
            # 75 - Imprime o peso com 1 casa decimal
            print(f"Peso: {peso:.1f} kg")
            # 76 - Imprime a altura com 2 casas decimais
            print(f"Altura: {altura:.2f} m")
            # 77 - Imprime o IMC com 1 casa decimal
            print(f"IMC: {imc:.1f} kg/m²")
            # 78 - Imprime a classificação
            print(f"Classificação: {classificacao}")
            # 79 - Imprime a categoria
            print(f"Categoria: {categoria}")
            # 80 - Imprime o grau de obesidade
            print(f"Grau de obesidade: {grau_obesidade}")
            # 81 - Imprime a faixa de peso ideal
            print(f"Faixa de peso ideal: {peso_min_ideal} kg - {peso_max_ideal} kg")
            
            # 82 - Verifica se o peso está abaixo do mínimo ideal
            if peso < peso_min_ideal:
                # 83 - Calcula a diferença
                diferenca = peso_min_ideal - peso
                # 84 - Imprime quanto precisa ganhar
                print(f"Você precisa ganhar aproximadamente {diferenca:.1f} kg para atingir o peso ideal mínimo")
            # 85 - Senão, verifica se o peso está acima do máximo ideal
            elif peso > peso_max_ideal:
                # 86 - Calcula a diferença
                diferenca = peso - peso_max_ideal
                # 87 - Imprime quanto precisa perder
                print(f"Você precisa perder aproximadamente {diferenca:.1f} kg para atingir o peso ideal máximo")
            
            # 88 - Chama a função para exibir recomendações
            exibir_recomendacoes(imc, classificacao)
            
            # 89 - Imprime linha separadora
            print("\n" + "="*50)
            # 90 - Pergunta se deseja fazer nova consulta
            # 91 - strip() remove espaços, lower() converte para minúsculo
            continuar = input("Deseja fazer uma nova consulta? (s/n): ").strip().lower()
            
            # 92 - Verifica se a resposta não é 's'
            if continuar != 's':
                # 93 - Imprime mensagem de encerramento
                print("\nPrograma encerrado. Cuide da sua saúde! 💪")
                # 94 - Sai do loop (break)
                break
                
        # 95 - Captura exceção de valor inválido
        except ValueError:
            # 96 - Imprime mensagem de erro de entrada
            print("❌ Entrada inválida! Por favor, digite números válidos.")
        # 97 - Captura exceção de divisão por zero
        except ZeroDivisionError:
            # 98 - Imprime mensagem de erro de altura zero
            print("❌ Altura não pode ser zero!")
        # 99 - Captura qualquer outra exceção
        except Exception as e:
            # 100 - Imprime erro inesperado
            print(f"❌ Erro inesperado: {e}")

# 101 - Define a função cadastrar_historico
def cadastrar_historico():
    # 102 - Docstring da função
    """
    Função para cadastrar múltiplas consultas e salvar em arquivo
    """
    # 103 - Cria uma lista vazia para armazenar o histórico
    historico = []
    
    # 104 - Inicia loop infinito
    while True:
        # 105 - Cria um dicionário vazio para a consulta atual
        consulta = {}
        # 106 - Imprime linha separadora
        print("\n" + "="*50)
        # 107 - Imprime título "CADASTRO DE CONSULTAS - HISTÓRICO"
        print("CADASTRO DE CONSULTAS - HISTÓRICO")
        # 108 - Imprime linha separadora
        print("="*50)
        
        # 109 - Inicia bloco try para capturar exceções
        try:
            # 110 - Solicita o nome e armazena no dicionário
            consulta['nome'] = input("Nome do paciente: ").strip().title()
            # 111 - Solicita a data e armazena no dicionário
            consulta['data'] = input("Data da consulta (DD/MM/AAAA): ").strip()
            # 112 - Solicita o peso e armazena no dicionário
            consulta['peso'] = float(input("Peso (kg): "))
            # 113 - Solicita a altura e armazena no dicionário
            consulta['altura'] = float(input("Altura (m): "))
            
            # 114 - Calcula o IMC e armazena no dicionário
            consulta['imc'] = calcular_imc(consulta['peso'], consulta['altura'])
            # 115 - Classifica o IMC e armazena no dicionário
            consulta['classificacao'] = classificar_imc(consulta['imc'])[0]
            
            # 116 - Adiciona a consulta ao histórico
            historico.append(consulta)
            
            # 117 - Pergunta se deseja cadastrar mais uma consulta
            continuar = input("\nCadastrar mais uma consulta? (s/n): ").strip().lower()
            # 118 - Verifica se a resposta não é 's'
            if continuar != 's':
                # 119 - Sai do loop
                break
                
        # 120 - Captura exceção de valor inválido
        except ValueError:
            # 121 - Imprime mensagem de erro
            print("❌ Dados inválidos!")
    
    # 122 - Verifica se o histórico não está vazio
    if historico:
        # 123 - Imprime linha separadora
        print("\n" + "="*50)
        # 124 - Imprime título "HISTÓRICO DE CONSULTAS"
        print("HISTÓRICO DE CONSULTAS")
        # 125 - Imprime linha separadora
        print("="*50)
        
        # 126 - Loop para percorrer o histórico
        # 127 - enumerate(historico, 1) começa a contagem em 1
        for i, consulta in enumerate(historico, 1):
            # 128 - Imprime o número da consulta
            print(f"\nConsulta {i}:")
            # 129 - Imprime o nome do paciente
            print(f"  Paciente: {consulta['nome']}")
            # 130 - Imprime a data da consulta
            print(f"  Data: {consulta['data']}")
            # 131 - Imprime o peso com 1 casa decimal
            print(f"  Peso: {consulta['peso']:.1f} kg")
            # 132 - Imprime a altura com 2 casas decimais
            print(f"  Altura: {consulta['altura']:.2f} m")
            # 133 - Imprime o IMC com 1 casa decimal
            print(f"  IMC: {consulta['imc']:.1f} kg/m²")
            # 134 - Imprime a classificação
            print(f"  Classificação: {consulta['classificacao']}")

# 135 - Define a função menu_principal
def menu_principal():
    # 136 - Docstring da função
    """
    Menu principal do sistema
    """
    # 137 - Inicia loop infinito
    while True:
        # 138 - Imprime linha separadora
        print("\n" + "="*50)
        # 139 - Imprime título "SISTEMA DE CONSULTA DE IMC"
        print("SISTEMA DE CONSULTA DE IMC")
        # 140 - Imprime linha separadora
        print("="*50)
        # 141 - Imprime opção 1 do menu
        print("1. Consulta individual")
        # 142 - Imprime opção 2 do menu
        print("2. Cadastrar histórico de consultas")
        # 143 - Imprime opção 3 do menu
        print("3. Informações sobre IMC")
        # 144 - Imprime opção 4 do menu
        print("4. Sair")
        
        # 145 - Solicita a opção do usuário e remove espaços
        opcao = input("\nEscolha uma opção (1-4): ").strip()
        
        # 146 - Verifica se a opção é '1'
        if opcao == '1':
            # 147 - Chama a função consultar_imc
            consultar_imc()
        # 148 - Senão, verifica se a opção é '2'
        elif opcao == '2':
            # 149 - Chama a função cadastrar_historico
            cadastrar_historico()
        # 150 - Senão, verifica se a opção é '3'
        elif opcao == '3':
            # 151 - Chama a função exibir_informacoes_imc
            exibir_informacoes_imc()
        # 152 - Senão, verifica se a opção é '4'
        elif opcao == '4':
            # 153 - Imprime mensagem de encerramento
            print("\nSistema encerrado. Obrigado por usar! 👋")
            # 154 - Sai do loop
            break
        # 155 - Senão (opção inválida)
        else:
            # 156 - Imprime mensagem de erro
            print("❌ Opção inválida! Escolha entre 1 e 4.")

# 157 - Define a função exibir_informacoes_imc
def exibir_informacoes_imc():
    # 158 - Docstring da função
    """
    Exibe informações sobre o IMC
    """
    # 159 - Imprime linha separadora
    print("\n" + "="*50)
    # 160 - Imprime título "INFORMAÇÕES SOBRE IMC"
    print("INFORMAÇÕES SOBRE IMC")
    # 161 - Imprime linha separadora
    print("="*50)
    # 162 - Imprime informação sobre o que é o IMC
    print("\nO Índice de Massa Corporal (IMC) é uma medida internacional")
    # 163 - Continua a informação
    print("usada para calcular se uma pessoa está no peso ideal.")
    # 164 - Imprime a fórmula do IMC
    print("\nFÓRMULA: IMC = Peso (kg) / Altura² (m)")
    # 165 - Imprime título da classificação
    print("\nCLASSIFICAÇÃO SEGUNDO A OMS:")
    # 166 - Imprime linha separadora
    print("-"*50)
    # 167 - Imprime classificação: Abaixo do peso
    print("IMC < 18.5          → Abaixo do peso")
    # 168 - Imprime classificação: Peso normal
    print("18.5 ≤ IMC < 25     → Peso normal")
    # 169 - Imprime classificação: Sobrepeso
    print("25 ≤ IMC < 30       → Sobrepeso")
    # 170 - Imprime classificação: Obesidade grau 1
    print("30 ≤ IMC < 35       → Obesidade grau 1")
    # 171 - Imprime classificação: Obesidade grau 2
    print("35 ≤ IMC < 40       → Obesidade grau 2")
    # 172 - Imprime classificação: Obesidade grau 3
    print("IMC ≥ 40           → Obesidade grau 3 (mórbida)")
    # 173 - Imprime aviso sobre as limitações do IMC
    print("\n⚠️  Importante: O IMC não leva em consideração a composição")
    # 174 - Continua o aviso
    print("corporal (massa muscular vs gordura). Consulte um profissional")
    # 175 - Finaliza o aviso
    print("de saúde para uma avaliação completa.")

# 176 - Verifica se o script está sendo executado diretamente
# 177 - __name__ é o nome do módulo
# 178 - "__main__" significa que o script está sendo executado diretamente
if __name__ == "__main__":
    # 179 - Imprime mensagem de boas-vindas
    print("🏥 Bem-vindo ao Sistema de Consulta de IMC! 🏥")
    # 180 - Chama a função menu_principal para iniciar o programa
    menu_principal()