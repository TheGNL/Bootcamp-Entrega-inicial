import pytest
from src.tracker import obter_temperatura_cidade

def test_api_conexao_real():
    """Valida se a aplicação consegue buscar a temperatura real de uma cidade."""
    cidade = "Sao Paulo"
    temperatura = obter_temperatura_cidade(cidade)
    
    # O teste passa se o retorno for um número (float ou int)
    assert temperatura is not None
    assert isinstance(temperatura, (int, float))
    print(f"\n✅ Teste de integração: Temperatura em {cidade} é {temperatura}°C")