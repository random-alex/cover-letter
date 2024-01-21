from langchain_openai import ChatOpenAI

from utils.arguments_parser import define_parser
from utils.config import OPENAI_MODEL_TYPE, OPENAI_MODEL_TEMPERATURE
from utils.general import get_local_gpt_api_key
from utils.openai_utils import get_structured_cv_info, get_structured_jd_info
from utils.prompts import PROMPT_MAIN_TASK, PROMPT_TEMPLATE


def get_cover_letter_openai(cv_info: str, job_description: str, is_pdf_cv: bool, is_url_jd: bool,
                            gpt_api_key: str = None):
    if not gpt_api_key:
        gpt_api_key = get_local_gpt_api_key()
    model = ChatOpenAI(temperature=OPENAI_MODEL_TEMPERATURE, model_name=OPENAI_MODEL_TYPE, openai_api_key=gpt_api_key)

    if is_pdf_cv:
        cv_info = get_structured_cv_info(cv_info=cv_info, is_pdf_cv=is_pdf_cv, model=model)

    if is_url_jd:
        job_description = get_structured_jd_info(job_description=job_description, is_url_jd=is_url_jd,
                                                 model=model)

    prompt_final = PROMPT_TEMPLATE.format(main_task_description=PROMPT_MAIN_TASK, cv_info=cv_info,
                                          job_description=job_description)

    result = model.invoke(prompt_final)
    return result.content


if __name__ == '__main__':
    parser = define_parser()
    # Parse the command-line arguments
    args = parser.parse_args()

    cover_letter = get_cover_letter_openai(cv_info=args.cv, job_description=args.job_description,
                                           is_pdf_cv=args.is_pdf_cv, is_url_jd=args.is_url_jd)
