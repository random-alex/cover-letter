from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from utils.cv import cv_loader
from utils.job_description import job_description_loader
from utils.prompts import PROMPT_CV, PROMPT_JD


def get_structured_cv_info(cv: str, is_pdf_cv: bool, model: ChatOpenAI, embedding: OpenAIEmbeddings) -> str:
    cv_docs = cv_loader(is_pdf=is_pdf_cv, content=cv)
    vectordb = Chroma.from_documents(cv_docs, embedding=embedding)
    cv_qa = RetrievalQA.from_chain_type(
        model,
        retriever=vectordb.as_retriever(),
        chain_type="stuff",
    )
    result_cv_info = cv_qa.invoke(PROMPT_CV)
    return result_cv_info['result']


def get_structured_jd_info(job_description: str, is_url_jd: bool, model: ChatOpenAI,
                           embedding: OpenAIEmbeddings) -> str:
    jd_docs = job_description_loader(is_url=is_url_jd, content=job_description)
    vectordb = Chroma.from_documents(jd_docs, embedding=embedding)
    jd_qa = RetrievalQA.from_chain_type(
        model,
        retriever=vectordb.as_retriever(),
        chain_type="stuff",
    )
    result_jd_info = jd_qa.invoke(PROMPT_JD)
    return result_jd_info['result']
