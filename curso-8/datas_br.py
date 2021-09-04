from datetime import datetime, timedelta


class DatasBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dias_semana = [
            "segunda", "terça", "quarta", "quinta",
            "sexta", "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    # Simulando dias de cadastro com o timedelta
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=21, hours=13)) - self.momento_cadastro
        return tempo_cadastro
