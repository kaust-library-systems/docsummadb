import logging as lg

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

    with open(csv_file, newline='', encoding='utf-8') as ff:
        csv_reader = reader(ff, dialect='unix')
        for row in csv_reader:
            fname = Path(row[0]).name
            fname_id = sha1(fname.encode()).hexdigest()
            print(f"File: {fname}, ID: {fname_id}")

if __name__ == "__main__":
    main()

