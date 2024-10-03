from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2023-11-24 10:45'
mascara_ptbr = '%d/%m/%y %a %H:%M '
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

data_converitda = datetime.strptime(data_hora_str, mascara_en)

print(data_converitda)
print(type(data_converitda))