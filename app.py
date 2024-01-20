import gradio as gr

from openai_generation import get_cover_letter_openai
from utils.config import DEMO_TITLE
from utils.general import is_valid_url, is_valid_openai_api_key


def run_generation(api_key, jd_info, cv_pdf, cv_text):
    is_valid_api_key = is_valid_openai_api_key(api_key)
    if not is_valid_api_key:
        raise gr.Error("API key is not valid! Please provide valid openAI API key")
    jd_info = jd_info.strip()
    is_url_jd = is_valid_url(jd_info)
    is_pdf_cv = False
    cv = cv_text

    if cv_pdf and cv_pdf.name:
        is_pdf_cv = True
        cv = cv_pdf.name
    letter = get_cover_letter_openai(cv_info=cv, job_description=jd_info, is_pdf_cv=is_pdf_cv, is_url_jd=is_url_jd,
                                     gpt_api_key=api_key)
    return letter


def main():
    with gr.Blocks() as demo:
        gr.Markdown(DEMO_TITLE)
        with gr.Accordion("Insert your OpenAI API key here", open=False):
            gpt_key = gr.Textbox(label="")
        with gr.Row(equal_height=False):
            with gr.Column():
                gr.Markdown("## Copy paste text description or insert URL to the job post")
                jd_info = gr.Textbox(label='Job description as Text or URL')
        with gr.Row(equal_height=False):
            with gr.Column():
                gr.Markdown("## Attach CV as PDF or type as a text. Submit ONLY one type at a time")
                with gr.Row():
                    cv_pdf = gr.File(label='CV PDF', file_count='single', file_types=['.pdf'], type='filepath')
                    cv_text = gr.TextArea(label='CV text', )
        pred_button = gr.Button("Generate Cover letter")
        with gr.Row():
            output_cover_letter = gr.Textbox(label='Cover Letter')
        pred_button.click(fn=run_generation, inputs=[gpt_key, jd_info, cv_pdf, cv_text],
                          outputs=[output_cover_letter])
    return demo


if __name__ == '__main__':
    app = main()
    app.launch()
