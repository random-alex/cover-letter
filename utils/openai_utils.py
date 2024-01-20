from langchain_openai import ChatOpenAI

from utils.cv import cv_loader
from utils.job_description import job_description_loader
from utils.prompts import PROMPT_JD, PROMPT_CV


def get_structured_cv_info(cv_info: str, is_pdf_cv: bool, model: ChatOpenAI) -> str:
    cv_docs = cv_loader(is_pdf=is_pdf_cv, content=cv_info)
    cv_docs_content = [cv_doc.page_content for cv_doc in cv_docs]
    prompt_cv = '\n\n\n'.join([PROMPT_CV, '\n'.join(cv_docs_content)])
    res_no_rag = model.invoke(prompt_cv)
    return res_no_rag.content


def get_structured_jd_info(job_description: str, is_url_jd: bool, model: ChatOpenAI) -> str:
    jd_docs = job_description_loader(is_url=is_url_jd, content=job_description)
    jd_docs_content = [cv_doc.page_content for cv_doc in jd_docs]
    prompt_job_description = '\n\n\n'.join([PROMPT_JD, '\n'.join(jd_docs_content)])
    res_no_rag = model.invoke(prompt_job_description)
    return res_no_rag.content
