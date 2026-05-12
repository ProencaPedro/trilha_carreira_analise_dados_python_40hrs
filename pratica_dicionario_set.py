'''
Desafio.
Como desenvolvedor em uma empresa de consultoria, você continua alocado para atender um cliente que precisa fazer a ingestão de dados de uma nova fonte e tratá-las. Você já fez uma entrega na qual implementou uma solução que faz o dedup em uma lista
de CPFs, retorna somente a parte numérica do CPF e verifica se eles possuem 11 dígitos.
Os clientes aprovaram a solução, mas solicitaram que a lista de CPFs válidos fosse entregue em ordem crescente para facilitar o cadastro. Eles enfatizaram a necessidade de ter uma solução capaz de fazer o trabalho para grandes volumes de dados, no
melhor tempo possível. Uma vez que a lista de CPFs pode crescer exponencialmente, escolher os algoritmos mais adequados é importante nesse caso.
Portanto, nesta nova etapa, você deve tanto fazer as transformações de limpeza e validação nos CPFs (remover ponto e traço, verificar se tem 11 dígitos e não deixar valores duplicados) quanto fazer a entrega em ordem crescente. Quais algoritmos
você vai escolher para implementar a solução? Você deve apresentar evidências de que fez a escolha certa!
'''
# Foi decidido usar o algoritmo de ordenação merge sort, vendo que para o caso, é o que tem menor complexidade de tempo;

# Parte 1 - Implementar o algoritmo de ordenação merge sort

def executar_merge_sort(lista, inicio = 0, fim = None):
    
    if not fim:
        
        fim = len(lista)
        
    if fim - inicio > 1:
        
        meio = (inicio + fim) // 2
        executar_merge_sort(lista, inicio, meio)
        executar_merge_sort(lista, meio, fim)
        executar_merge(lista, inicio, meio, fim)
        
    return lista
    
def executar_merge(lista, inicio, meio, fim):
    
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda = topo_direita = 0
    for p in range(inicio, fim):
        
        if topo_esquerda >= len(esquerda):
            
            lista[p] = direita[topo_direita]
            topo_direita += 1
            
        elif topo_direita >= len(direita):
            
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
            
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
            
        else:
            
            lista[p] = direita[topo_direita]
            topo_direita += 1
            
# Parte 2 - Implementar o algoritmo de busca binária

def executar_busca_binaria(lista, valor):
    
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            
            maximo = meio - 1
            
        elif valor > lista[meio]:
            
            minimo = meio + 1
            
        else:
            
            return True
            
    return False

# Parte 3 - Implementar a função que faz a verificação do cpf, o dedup e devolve o resultado esperado

def criar_lista_dedup_ordenada(lista):
    
    lista = [str(cpf).replace('.', '').replace('-', '') for cpf in lista]
    lista = [cpf for cpf in lista if len(cpf) == 11]
    lista = executar_merge_sort(lista)
    
    lista_dedup = []
    for cpf in lista:
        
        if not executar_busca_binaria(lista_dedup, cpf):
            
            lista_dedup.append(cpf)
            
    return lista_dedup
    
    
# Parte 4 - Criar uma função de teste

def testar_funcao(lista_cpfs):
    
    lista_dedup = criar_lista_dedup_ordenada(lista_cpfs)
    print(lista_dedup)
    
lista_cpfs = ['96318274195', '111.111.111-11', '11111111111', '222.222.222.-22', '333.333.333.-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)
    
