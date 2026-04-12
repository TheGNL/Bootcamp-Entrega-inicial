import pytest
import os
import sys

# Ensina o Python a achar a pasta 'src'
caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.insert(0, caminho)

import tracker  # noqa: E402


@pytest.fixture(autouse=True)
def preparar_ambiente():
    tracker.ARQUIVO_DADOS = "dados_teste.json"
    if os.path.exists(tracker.ARQUIVO_DADOS):
        os.remove(tracker.ARQUIVO_DADOS)
    yield  # Aqui os testes rodam
    if os.path.exists(tracker.ARQUIVO_DADOS):
        os.remove(tracker.ARQUIVO_DADOS)


def test_adicionar_agua_com_sucesso():
    """Testa se adicionar água atualiza o total."""
    novo_total = tracker.adicionar_agua(250)
    assert novo_total == 250


def test_impedir_agua_negativa():
    """Testa se o sistema bloqueia valores negativos."""
    msg = "A quantidade de água deve ser maior que zero"
    with pytest.raises(ValueError, match=msg):
        tracker.adicionar_agua(-50)


def test_status_inicial_sem_dados():
    """Testa a primeira vez que abre (sem dados criados)."""
    total, meta = tracker.verificar_status()
    assert total == 0
    assert meta == 2000
    