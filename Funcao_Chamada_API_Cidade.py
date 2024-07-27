import requests


class localizacao:
    def __init__(self) -> None:
        self.url = url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
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
            print(f"Erro Connect:{errc}")
        except requests.exceptions.Timeouta as errt:
            print(f"Errp Timeout: {errt}")
        except requests.exceptions.RequestException as errr:
            print(f"Erro:{errr}")
