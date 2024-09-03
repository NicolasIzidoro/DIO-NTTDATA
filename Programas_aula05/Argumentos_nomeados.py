def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso {marca}/ {modelo}/ {ano}/ {placa}")

salvar_carro("fiat", "Palio", 2000, "akd-483")

# Quando se coloca dois **(asterisco) que dizeer que vai vai receber um dicionario **KWARGS e um asterisco quer dizer que ira receber um argumento(tupla) *ARGS

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 2000, "placa":"akd-483"})