from pymongo import MongoClient
import typer


def main(
    db_name: str = "reddit",
    collection_name: str = "comments",
    host: str = "localhost", 
    port: int = 27017,
    batch: int = 500
    ):
    client = MongoClient(F"{host}:{port}")
    db = getattr(client, db_name)
    col = getattr(db, collection_name)
    print(type(col))
    count = col.count()
    print(F"{count} documents in {db_name}.{collection_name}")

if __name__ == "__main__":
    typer.run(main)
