# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um pilar e retornar sua respectiva descrição.
def descrever_pilar(pilar):
    if pilar == "excelencia operacional":
        return "execucao e monitoramento de sistemas e melhoria continua"
        
    elif pilar == "seguranca":
        return "protecao de dados, sistemas e ativos atraves da implementacao de controles de seguranca"
        
    elif pilar == "confiabilidade":
        return "recuperacao rapida de falhas e atendimento a requisitos de disponibilidade"
        
    elif pilar == "eficiencia de performance":
        return "uso eficiente de recursos computacionais para atender requisitos de sistema"
        
    elif pilar == "otimizacao de custos":
        return "gerenciamento eficiente dos custos para evitar despesas desnecessarias"
        
    elif pilar == "sustentabilidade":
        return "minimizacao dos impactos ambientais e promocao da eficiencia energetica"
    
    else:
        return "Pilar desconhecido"

# Imprime a descrição do pilar recebido na "entrada" através da função "descrever_pilar".
print(descrever_pilar(entrada))
