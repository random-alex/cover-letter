from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document


def job_description_loader(is_url: bool, content: str) -> list[Document]:
    if is_url:
        return WebBaseLoader(content).load()
    else:
        return [Document(page_content=content, metadata={"source": "local"})]
