# Automatic cover letter generation
Simple app for generating cover letter based on CV and job description
In order to use the app, please provider a valid OpenAI API key.

# How to use solution 
### Locally (CLI)
1. Install the dependencies:
   
   `pip install -r requirements.txt`
2. Create a file called `gpt_api.py` under `utils` folder with variable `GPT_API_KEY = "correct_openai_key"`
3. Run the command:
   
    `python main.py --cv=test_assets/cvs/test_cv1.pdf --job_description='https://www.linkedin.com/jobs/view/3793239233/?alternateChannel=search&refId=9LsNBvo7h3zfuWe5C98kwQ%3D%3D&trackingId=LJyOI1ULOamcnhv9V6KXsw%3D%3D' --is_pdf_cv --is_url_jd`
### Locally (Gradio demo)
1. Install the dependencies:
   
   `pip install -r requirements.txt`
2. Run the command:
    
    `python app.py`

# Examples of generated cover letters


