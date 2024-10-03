##TIMEDELTA

from datetime import datetime, timedelta


tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60 
data_atual = datetime.now()


if tipo_carro == 'P':
    data_estimada = data_atual +timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às: {data_estimada}')

elif tipo_carro == 'M':
     data_estimada = data_atual +timedelta(minutes=tempo_medio)
     print(f'O carro chegou: {data_atual} e ficará pronto às: {data_estimada}')

else:
    data_estimada = data_atual +timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto às: {data_estimada}')



## como pegar somente hora ou data 

resultado = datetime(2023,6, 25, 23, 15, 25) - timedelta(hours= 1)
print(resultado)


print(datetime.today().date())
print(datetime.today().time())