# Vantagens da Computação em Nuvem

## Descrição
Este script apresenta ao usuário uma lista de vantagens da computação em nuvem e permite que ele selecione uma para ver a descrição detalhada.

## Funcionamento
1. O script exibe uma lista de opções de vantagens para o usuário escolher.
2. O usuário insere o número correspondente à vantagem desejada.
3. O script converte a escolha do usuário na vantagem correspondente.
4. Uma função é chamada para descrever a vantagem selecionada e a descrição é exibida ao usuário.

## Código
```python
# Apresenta as opções de vantagens para o usuário selecionar
print("Escolha uma das seguintes vantagens:")
print("1. Economia de custos")
print("2. Infraestrutura global")
print("3. Alta disponibilidade")
print("4. Elasticidade")
print("5. Agilidade")

# Recebe a escolha do usuário
opcao = input("Digite o número correspondente à vantagem desejada: ")

# Converte a opção para a vantagem correspondente
if opcao == "1":
    entrada = "economia de custos"
elif opcao == "2":
    entrada = "infraestrutura global"
elif opcao == "3":
    entrada = "alta disponibilidade"
elif opcao == "4":
    entrada = "elasticidade"
elif opcao == "5":
    entrada = "agilidade"
else:
    print("Opção inválida.")
    exit()

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "economia de custos":
        return "Otimização de gastos por meio de modelos de preços flexíveis."
    elif vantagem == "infraestrutura global":
        return "Ampla infraestrutura distribuída globalmente para melhor desempenho e escalabilidade."
    elif vantagem == "alta disponibilidade":
        return "Garantia de que o serviço estará sempre disponível e acessível."
    elif vantagem == "elasticidade":
        return "Capacidade de dimensionar recursos de forma dinâmica de acordo com a demanda."
    elif vantagem == "agilidade":
        return "Rápida adaptação às mudanças e implementação de novos recursos."
    else:
        return "Vantagem não reconhecida."

# Imprime a descrição da vantagem selecionada pelo usuário
print(descrever_vantagem(entrada))
```

## Como Usar
1. Execute o script em um ambiente Python.
2. Selecione a vantagem digitando o número correspondente e pressionando Enter.
3. Veja a descrição da vantagem selecionada.



Este script é uma ferramenta simples para entender melhor as vantagens da computação em nuvem, ideal para iniciantes e participantes do Bootcamp AWS do Santander.
