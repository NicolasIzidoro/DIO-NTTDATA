# A função é um bloco de codigo com um nome que se chama identificador, ou seja suponhamos que o codigo tenha 5 linhas e nós damos um nome para essas 5 linhas será o identificador 
# Alem desse nome e dessa agrupamento de codigo da FUNÇÂO, eu posso enviar  parametros para bloco de codigo, sendo que esses paramentros podem ou não ter um valor fixo ou padrão

# os parametro são as esntradas da função 
# e os retornos são as saidas das função


#progrmaar baseadoem funçao, é o mesmo que dizer que estamos programando de maneira estruturada
# Então def(DEFINIÇÃO) exibir_mensagem(É o nome de uma função) Quando ponho so dois pontoo estou abrindo obloco 
# da minha função e  tudo o que estiver identado faz parte dele e quando volta o recuo da identação não faz mas parte dessa função


def exibir_mensagem ():
    print("olá, mundo!")


# def exibir_mensagem1(nome):
#     print(f"Seja bem vindo: {nome}")
# exibir_mensagem1(nome = "José Carlos")

#### Se caso não passar nenhum valor na hora que for chamar a função sera retornado erro, mas caso você passe 
#### um outro parametro como o anonimo abaixo, (se caso não tiver passado um paramentro na hora de chamar a função)sera retornado o anonimo, como padrao
####
def exibir_mensagem1(nome = "Anonimo"):
    print(f"Seja bem vindo: {nome}")

exibir_mensagem1()