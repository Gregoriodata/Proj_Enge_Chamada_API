import requests

# cidade = 'Curitiba'


class Clima:
    def __init__(self, cidade):
        self.cidade = cidade
        self.api_key = '08dcfb72931ed589d85b8d6b3cb63861'
        self.url = (f'https://api.openweathermap.org/data/2.5/weather?q={self.cidade}'
                    f'&lang=pt_br&appid={self.api_key}'
                    )
        self.dados = None

    def consulta(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.dados = response.json()
            return (self.dados)
        except requests.exceptions.HTTPError as errh:
            print(f"Erro HTTP:{errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Erro de Connect:{errc}")
        except requests.exceptions.Timeout as errt:
            print(f"timeout:{errt}")
        except requests.exceptions.RequestException as errr:
            print(f"Erro:{errr}")
