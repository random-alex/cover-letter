from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def cv_loader(is_pdf: bool, content: str) -> list[Document]:
    if is_pdf:
        return PyPDFLoader(content).load()
    else:
        return [Document(page_content=content, metadata={"source": "local"})]
