from datetime import date, datetime, timedelta
from datas_br import DatasBR

cadastro = DatasBR()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())

