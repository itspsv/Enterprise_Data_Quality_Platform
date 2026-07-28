from edqp.ingestion.ingestion_engine import IngestionEngine


def main():
    engine = IngestionEngine()

    df = engine.read("datasets/raw/customers.csv")

    print("=" * 50)
    print("Customers Dataset")
    print("=" * 50)
    print(df)


if __name__ == "__main__":
    main()