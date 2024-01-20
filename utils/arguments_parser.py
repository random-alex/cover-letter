import argparse

from utils.config import DEFAULT_CV_PATH, DEFAULT_JD_PATH


def define_parser():
    parser = argparse.ArgumentParser(description="Process CV and Job Description information.")

    # Define the command-line arguments
    parser.add_argument('--cv', type=str, help='Path to PDF or text version of CV',
                        default=DEFAULT_CV_PATH)
    parser.add_argument('--job_description', type=str, help='URL or text version of Job Description',
                        default=DEFAULT_JD_PATH)
    parser.add_argument('--is_pdf_cv', action='store_true', help='Specify if CV is in PDF format')
    parser.add_argument('--is_url_jd', action='store_true', help='Specify if Job Description is a URL')
    return parser
