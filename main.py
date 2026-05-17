import requests

def obter_frase_motivacional():
    """Consome a API pública ZenQuotes para buscar uma frase inspiradora."""
    try:
        # Requisição HTTP GET para a API pública
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        
        if response.status_code == 200:
            dados = response.json()
            # A API retorna uma lista com um dicionário. Ex: [{'q': 'Frase', 'a': 'Autor'}]
            frase = dados[0]['q']
            autor = dados[0]['a']
            return f'"{frase}" — {autor}'
        return "Mantenha o foco nos seus estudos hoje!"
    except requests.RequestException:
        # Caso ocorra erro de conexão, a aplicação não quebra e retorna uma frase padrão
        return "Estude com dedicação e colha os frutos amanhã."

# Exemplo de como incluir no início ou no menu da sua CLI:
def iniciar_cli():
    print("=" * 50)
    print("       STUDYORGANIZER - SEU GERENCIADOR DE ESTUDOS     ")
    print("=" * 50)
    print("\n[Inspiração do Dia]")
    print(obter_frase_motivacional())
    print("\n" + "=" * 50)
    # Restante do seu código de cadastro de matérias/tempos...
