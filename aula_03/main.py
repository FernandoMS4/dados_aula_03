# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# data = [1,2,3,-4,5,6,-7,-9]
# list = []
# for dado in data:
#     if dado <= 0:
#         #print(f"Não pode conter valores negativos: {dado}")
#         list.append(dado)
#     else:
#         pass
# if len(list) >= 1:
#     print(f"Não pode conter valores negativos {list}")

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# # Temperatura < 18°C é 'Baixa'
# # Temperatura >= 18°C e <= 26°C é 'Normal'
# # Temperatura > 26°C é 'Alta'

# dicionario = {"CPU_SERVIDOR_INTERNO":28,"CPU_S3":13,"CPU_FIXA":23}
# result = {}
# for item in dicionario:
#     valor = item
#     if dicionario[valor] <18:
#         result[valor] = "Baixo"
#     elif dicionario[valor] > 18 and dicionario[valor] <26:
#         result[valor] = "Normal"
#     else:
#         result[valor] = "Alto"


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'.
#  Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'] == 'ERROR':
#     print(log['message'])
# else:
#     pass

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.


# try:
#     close = 0
#     while close < 4:
#         email = input("Digite seu email: ")
#         idade = input("Digite sua idade: ")
#         if close == 3:
#             print(f"Quantidade de tentativas excedidas, tentativas restantes: {close}")
#             exit()
#         elif len(email.strip()) == 0 or '@' not in email or '.com'not in email:
#             print("Não pode ser vazio ou é um email invalido digite novamente")
#             close += 1
#         elif idade <= 18 or idade >=65:
#             print("A idade não pode ser menor que 18 e maior que 65, digite novamente")
#             close += 1     
# except:
#     print("Dados validos")


# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

# data = {"user":{"id":1,"nome":"Fernando Martins","valor_transacao":7000,"hora":13},"user2":{"id":2,"nome":"Felipe Martins","valor_transacao":29000,"hora":13}}
# sus = {}
# try:
#     for u in data:
#         if data[u]["valor_transacao"] >= 10000 or data[u]["hora"]>=18 or data[u]["hora"]<=9:
#             print(f"Valor Suspeito para o cliente: {data[u]["nome"]} no valor de: {data[u]["valor_transacao"]}")
# except:
#     pass

#Treinamento pessoal: Em um site possuo um filtro que, dentro dele o usuário pode escolher variados tipos de filtros e dentro destes filtros possuem outros filtros 
#ex: https://www.netimoveis.com/venda/minas-gerais/belo-horizonte/apartamento?tipo=apartamento&transacao=venda&localizacao=BR-MG-belo-horizonte---&quartos=4&pagina=1
#montei uma estrutura similar aos filtros para pegar somente aqueles que o usuário supostamente marcou

# filtro_resultado = {"fernando":{"localizacao":"Belo Horizonte","tipo_do_imovel":"Apartamento","numero_de_quartos":{"1+":"","2+":"","3+":"3","4+":""},"valor":{"minimo":"265000","maximo":"300000"},"area":{"minimo":"24,00","maximo":"65,00"},"numero_vagas":{"1+":"1","2+":"","3+":"","4+":""}}}
# json = {}
# try:
#     for i in filtro_resultado:
#         for u in filtro_resultado[i]:
#             itens = filtro_resultado[i][u]
#             if type(itens) == dict:
#                 iten2 = {chave: valor for chave, valor in itens.items() if valor}
#                 print(iten2)
#                 json[u] = iten2
#             else:
#                 json[u] = itens
# except:
#     pass
# print(json)

