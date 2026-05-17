import unittest
from unittest.mock import patch
# Importe a função do seu arquivo correspondente
from seu_arquivo_principal import obter_frase_motivacional 

class TestIntegracaoAPI(unittest.TestCase):

    @patch('requests.get')
    def test_obter_frase_motivacional_sucesso(self, mock_get):
        """Valida se a aplicação processa corretamente o retorno de sucesso da API."""
        # Simula uma resposta JSON bem-sucedida da API ZenQuotes
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"q": "Learning never exhausts the mind.", "a": "Leonardo da Vinci"}
        ]
        
        resultado = obter_frase_motivacional()
        
        self.assertIn("Learning never exhausts the mind.", resultado)
        self.assertIn("Leonardo da Vinci", resultado)

    @patch('requests.get')
    def test_obter_frase_motivacional_falha(self, mock_get):
        """Garante que a aplicação não quebra caso a API fique fora do ar."""
        # Simula uma falha de conexão na requisição
        mock_get.return_value.status_code = 500
        
        resultado = obter_frase_motivacional()
        
        # Deve retornar a frase padrão de contingência
        self.assertEqual(resultado, "Mantenha o foco nos seus estudos hoje!")

if __name__ == '__main__':
    unittest.main()
