from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


def retrieve_documents(
    query: str,
    vector_store: FAISS,
    top_k: int = 5
) -> List[Document]:

    retrieved_docs = vector_store.similarity_search(
        query=query,
        k=top_k
    )

    return retrieve_documents