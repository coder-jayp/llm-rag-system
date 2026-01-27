from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}

def load_documents(data_dir: str) -> List[Document]:
    documents: List[Document] = []

    base_path = Path(data_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"Directory not found: {data_dir}")
    
    for file_path in base_path.iterdir():

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        if file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
            loaded_docs = loader.load()

        else:
            loader = TextLoader(str(file_path), encoding="utf-8")
            loaded_docs = loader.load()

        for doc in loaded_docs:
            doc.metadata["source"] = file_path.name
            doc.metadata["doc_type"] = file_path.suffix.lower()

        documents.extend(loaded_docs)

    return documents