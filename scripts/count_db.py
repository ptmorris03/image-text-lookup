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
    result = db.runCommand({
        "count": collection_name
    })
    print(F"{result['n']} documents in {db_name}.{collection_name}")

if __name__ == "__main__":
    typer.run(main)
