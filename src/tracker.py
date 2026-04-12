import argparse
import json
import os

ARQUIVO_DADOS = "dados_agua.json"


def carregar_dados():
    """Carrega os dados salvos ou retorna o padrão."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    return {"total_ml": 0, "meta_ml": 2000}


def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados, f)


def adicionar_agua(ml):
    """Adiciona a quantidade de água bebida."""
    if ml <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    dados = carregar_dados()
    dados["total_ml"] += ml
    salvar_dados(dados)
    return dados["total_ml"]


def verificar_status():
    """Retorna o total bebido e a meta."""
    dados = carregar_dados()
    return dados["total_ml"], dados["meta_ml"]


def main():
    desc = "CLI de Autocuidado: Lembrete de Hidratação"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        '--adicionar',
        type=int,
        help="Adiciona água em ml (ex: 250)"
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help="Mostra o status atual de hidratação"
    )

    args = parser.parse_args()

    if args.adicionar:
        try:
            novo = adicionar_agua(args.adicionar)
            print(f"✅ Adicionado {args.adicionar}ml. Total: {novo}ml.")
        except ValueError as e:
            print(f"❌ Erro: {e}")

    elif args.status:
        total, meta = verificar_status()
        print("💧 Status de Hidratação:")
        print(f"Bebido: {total}ml / Meta: {meta}ml")
        if total >= meta:
            print("🎉 Parabéns! Você atingiu sua meta diária!")
        else:
            print(f"Faltam {meta - total}ml para a sua meta. Beba água!")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()