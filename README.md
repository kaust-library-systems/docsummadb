# docsummadb

Saving the summary of documents to a [Chromadb](https://docs.trychroma.com/docs/overview/introduction) database.


## Installation

Installing Chromadb:

```
uv pip install chromadb
```

## CLI

Installing the `chromadb` CLI:

```
curl -sSL https://raw.githubusercontent.com/chroma-core/chroma/main/rust/cli/install/install.sh | bash 
```

### Browsing the collection

Checking the collection first:

```
>>> db = chromadb.PersistentClient(path="./db/")
>>> collections = db.list_collections()
>>> print(collections)
[Collection(name=archives)]
>>> 
```

Loading the collection on the browser:

```
(docsummadb) mgarcia@PC-KL-26743:~/Work/docsummadb/db$ chroma browse archives --path "."

OpenTelemetry is not enabled because it is missing from the config.

(docsummadb) mgarcia@PC-KL-26743:~/Work/docsummadb/db$
```


