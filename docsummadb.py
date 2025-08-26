import logging as lg
import chromadb

from pathlib import Path
from csv import reader
from hashlib import sha1

lg.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
               datefmt='%Y-%m-%dT%I:%M:%S',
               level=lg.INFO)

docs_dir = "data"
csv_file = Path(docs_dir) / "docsumma.csv"

def main():
    lg.info("Hello from docsummadb!")
    lg.info(f"CSV file path: {csv_file}")

    # Open the Chroma db
    db_dir = Path.cwd() / "db"
    db = chromadb.PersistentClient(path=db_dir)
    from chromadb.api.types import EmbeddingFunction

    collection = db.get_or_create_collection(name="archives")

    with open(csv_file, newline='', encoding='utf-8') as ff:
        csv_reader = reader(ff, dialect='unix')
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            fname = Path(row[0]).name
            fname_id = sha1(fname.encode()).hexdigest()
            lg.info(f"Processing file: {fname} with ID: {fname_id}")
            collection.add(
                ids=[fname_id],
                documents=[row[1]],
                metadatas=[{"name": fname}],
            )

if __name__ == "__main__":
    main()

