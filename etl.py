from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "usuarios.csv"
OUTPUT_FILE = BASE_DIR / "resultado.csv"


def extract(file_path: Path) -> pd.DataFrame:
    """Extract: read user data from CSV."""
    return pd.read_csv(file_path)


def gerar_mensagem(nome: str) -> str:
    """Transform helper: create a personalized marketing message."""
    primeiro_nome = str(nome).split()[0]
    return (
        f"Olá, {primeiro_nome}! Temos uma novidade especial para você. "
        "Aproveite nossos benefícios exclusivos e conte com a gente para "
        "transformar sua experiência digital."
    )


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transform: enrich data with personalized messages."""
    resultado = df.copy()
    resultado["mensagem"] = resultado["nome"].apply(gerar_mensagem)
    return resultado


def load(df: pd.DataFrame, output_path: Path) -> None:
    """Load: save the transformed data to a new CSV file."""
    df.to_csv(output_path, index=False)


def main() -> None:
    usuarios = extract(INPUT_FILE)
    usuarios_transformados = transform(usuarios)
    load(usuarios_transformados, OUTPUT_FILE)

    print("Processo ETL finalizado com sucesso!")
    print(f"Arquivo gerado em: {OUTPUT_FILE}")
    print("\nPrévia do resultado:")
    print(usuarios_transformados)


if __name__ == "__main__":
    main()
