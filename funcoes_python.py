                                    #IMPLEMENTANDO SOLUÇÕES EM PYTHON MEDIANTE FUNÇÕES
def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")
    
imprimir_mensagem("Python", "ADS")

'''
  Para que o resultado de uma função possa ser guardado em uma variável, a função precisa ter o comando "return".
  A instrução "return", retorna um valor de uma função.
'''
def imprimir_mensagem(disciplina, curso):
  return f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}."

mensagem = imprimir_mensagem("Python", "ADS")
print(mensagem)

'''
  Em vez de imprimir a mensagem, a função retorna (return) um valor para quem a invocou.
  O uso do "return" depende da solução e das ações que se deseja para a função. Por exemplo,
  podemos criar uma função que limpa os campos de um formulário, esse trecho pode simplesmente limpar os campos e não retornar nada,
  mas também pode retornar um valor booleano como True, para informar que a limpeza aconteceu com sucesso.
  Portanto, o retorno deve ser analisado, levando em consideração o que se espera da função e como se pretende tratar o retorno, quando necessário.
'''

'''
                Exemplificando:
Vamos implementar uma função que recebe uma data no formato dd/mm/aaaa e converte o mês para extenso.
Então, ao se receber a data 10/05/2020, a função deverá retornar: 10 de maio de 2020. Observe a implementação a seguir.

'''
def converter_mes_para_extenso(data): # Definimos o nome da função e os parâmetros que ela recebe.
  mes = '''janeiro fevereiro março  
  abril maio junho julho agosto 
  setembro outubro novembro
  dezembro'''.split() # Criamos uma lista com os meses, por extenso. Criamos uma string e usamos a função split(), que "quebra" a string a cada espaço em branco, criando uma lista e elementos.

  d,m,a = data.split('/')  #Usamos novamente a função split(), mas agora passando como parâmetro o caractere '/', isso quer dizer que a string será cortada sempre que ele aparecer. Nessa linha também usamos a atribuição múltipla. Ao cortar a string 'dd/mm/aaaa', temos uma lista com três elementos: ['dd', 'mm', 'aaaa'], ao usar a atribuição múltipla, cada valor da lista é guardado dentro de uma variável, na ordem em que foram declaradas. Então d = 'dd', m = 'mm', a = 'aaaa'. O número de variáveis tem que ser adequado ao tamanho da lista, senão ocorrerá um erro.
  mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0! #Aqui estamos fazendo a conversão do mês para extenso. Veja que buscamos na lista "mes" a posição m - 1, pois, a posição inicia em 0. Por exemplo, para o mês 5, o valor "maio", estará na quarta posição a lista "mes".
  return f'{d} de {mes_extenso} de {a}' # Retornamos a mensagem, agora com o mês em extenso.

print(converter_mes_para_extenso('10/05/2021')) # Invocamos a função, passando como parâmetro a data a ser convertida.




#DESAFIO
'''
Após uma primeira reunião, a equipe fez um levantamento de requisitos e concluiu que a função a ser construída precisa considerar os seguintes itens:

O valor do produto (obrigatório).
A quantidade do produto (obrigatório).
A moeda em que deve ser feito o cálculo (obrigatório, sendo padrão o real).
A porcentagem do desconto que será concedida na compra (opcional).
A porcentagem de acréscimo, que depende da forma de pagamento (opcional).
'''
def calcular_valor(valor_prod, qtde, moeda = "real", desconto = None, acrescimo = None):
  v_bruto = valor_prod * qtde

  if desconto:
    v_liquido = v_bruto - (v_bruto * (desconto / 100))
  elif acrescimo:
    v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
  else:
    v_liquido = v_bruto

  if moeda == 'real':
    return v_liquido
  elif moeda == 'dolar':
    return v_liquido * 5
  elif moeda == 'euro':
    return v_liquido * 5.7
  else:
    print("Moeda não cadastrada!")
    return 0

valor_a_pagar = calcular_valor(valor_prod = 32, qtde = 5, desconto = 5)
print(f"O valor final da conta é {valor_a_pagar}")



  
  
