from datetime import date, datetime, timedelta
from datas_br import DatasBR

'''hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=12)

print(amanha-hoje)'''

hoje = DatasBR()
print(hoje.tempo_cadastro())
