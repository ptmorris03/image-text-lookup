from pymongo import MongoClient
from tqdm import tqdm
import typer
import zreader
import ujson as json

from pathlib import Path


def parse_comment(comment):
    return {
        "_id": 0
    }

def insert_comments(db, comments):
    comments = map(parse_comment, comments)
    return db.comments.insert_many(comments, ordered=False)

def main(
    file: Path,
    host: str = "localhost", 
    port: int = 27017):
    #client = MongoClient(F"{host}:{port}")
    #db = client.reddit

    #result = insert_comments(db, comments)

    reader = zreader.Zreader(file)
    for line in reader.readlines():
        obj = json.loads(line)
        print(obj)
        break

if __name__ == "__main__":
    typer.run(main)
