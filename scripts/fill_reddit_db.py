from pymongo import MongoClient
from tqdm import tqdm
import typer
import zreader
import ujson as json

from pathlib import Path


skip_text = ['[removed]', '[deleted]']
def filter_comment(comment):
    return comment['body'] in skip_text


def parse_comment(comment):
    return {
        "_id": comment['id'],
        "text": comment['body'],
        "subreddit": comment['subreddit'],
    }


def insert_comments(db, comments):
    comments = filter(filter_comment, comments)
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
        print(filter_comment(obj))
        print(parse_comment(obj))
        break

if __name__ == "__main__":
    typer.run(main)
