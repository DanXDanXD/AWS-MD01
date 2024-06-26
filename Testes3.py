# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um cenário e retornar a estratégia indicada.
def escolher_estrategia(cenario):
    if "transicao de aplicativo sem valor comercial" in cenario:
        return "retire"  # Aposentar (Retire)
        
    elif "aplicativo com necessidade de adiar sua migracao para a nuvem" in cenario:
        return "retain"  # Reter (Retain)
        
    elif "mover aplicativos para a nuvem sem modifica-los" in cenario:
        return "rehost"  # Rehospedar (Rehost)
        
    elif "transferir servidores ou instancias para outra plataforma na nuvem" in cenario:
        return "relocate"  # Recolocar (Relocate)
        
    elif "substituir o aplicativo por uma versao ou produto diferente" in cenario:
        return "repurchase"  # Substituir (Repurchase)
        
    elif "introduzir otimizacoes no aplicativo para opera-lo de forma eficiente" in cenario:
        return "replatform"  # Replataforma (Replatform)
        
    elif "modificar a arquitetura do aplicativo" in cenario:
        return "refactor or re-architect"  # Refatorar ou Re-arquitetar (Refactor or Re-architect)
    
    else:
        return "estrategia desconhecida"

# Imprime a estratégia indicada para o cenário recebido na "entrada" através da função "escolher_estrategia".
print(escolher_estrategia(entrada))
