# CLI Lembrete de Hidratação 💧

## Descrição do Problema Real
A desidratação leve e crônica afeta a saúde de milhares de pessoas, causando fadiga, dores de cabeça e perda de foco. Muitas vezes, isso ocorre simplesmente porque as pessoas (especialmente quem trabalha no computador o dia todo) esquecem de beber água durante a rotina corrida.

## Proposta da Solução
Criar uma aplicação de Linha de Comando (CLI) rápida e sem distrações que permita ao usuário registrar a quantidade de água ingerida ao longo do dia e acompanhar o progresso em relação a uma meta diária saudável, tudo isso sem precisar sair do terminal.

## Público-Alvo
Desenvolvedores, profissionais de TI, estudantes e qualquer pessoa que passe a maior parte do dia na frente de um computador e prefira ferramentas de terminal para manter a produtividade.

## Funcionalidades Principais
* **Registrar Consumo:** Permite adicionar quantidades de água (em ml) ao total consumido no dia.
* **Acompanhamento de Status:** Exibe o total de água consumido e informa quanto falta para atingir a meta diária (padrão de 2000ml).

## Tecnologias Utilizadas
* Python 3.13
* Biblioteca padrão `argparse` (para a interface CLI)
* `pytest` (para testes automatizados)
* `flake8` (para linting/análise estática)
* GitHub Actions (para CI - Integração Contínua)

## Instruções de Instalação
Clone este repositório e instale as dependências usando o pip:
```bash
git clone [https://github.com/TheGNL/Bootcamp-Entrega-inicial.git](https://github.com/TheGNL/Bootcamp-Entrega-inicial.git)
cd Bootcamp-Entrega-inicial
pip install -r requirements.txt

Instruções de Execução
Para registrar que você bebeu água (exemplo: 250ml):
python src/tracker.py --adicionar 250

Para verificar o seu progresso diário:
python src/tracker.py --status

Instruções para Rodar os Testes
Para garantir que as regras de negócio estão funcionando, execute:
pytest tests/

Instruções para Rodar o Lint
Para verificar a formatação e a qualidade do código segundo a PEP 8, execute:
flake8 src/ tests/

Informações do Projeto
Versão Atual: 1.0.0

Nome do Autor: Guilherme Neves Lourenço

Repositório Público: https://www.google.com/url?sa=E&source=gmail&q=https://github.com/TheGNL/Bootcamp-Entrega-inicial
