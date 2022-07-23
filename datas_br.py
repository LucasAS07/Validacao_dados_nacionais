from datetime import datetime, timedelta


class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses = [
            '', 'janeiro', 'fevereiro', 'março', 'abril',
            'maio', 'junho', 'julho', 'agosto',
            'setembro', 'outubro', 'novembro', 'dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses[mes_cadastro]

    def dia_semana(self):
        dias_semana = [
            'segunda', 'terça', 'quarta', 'quinta', 'sexta',
            'sabado', 'domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%y %H:%M')
        return data_formatada

# timedelta foi usado aqui apenas para poder testar a funcionalidade
# uma vez que não estamos usando um banco de dados
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=257,
                          hours=15, minutes=45)) - self.momento_cadastro
        return tempo_cadastro
