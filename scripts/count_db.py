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
    count = col.count_documents({})
    print(F"{count} documents in {db_name}.{collection_name}")

    result = col.find({}).limit(10)
    print(dir(result))

if __name__ == "__main__":
    typer.run(main)
