PROMPT_TEMPLATE = "{main_task_description}\nCV:\n{cv_info}\nJob description:\n{job_description}"

PROMPT_MAIN_TASK = """
# Mission Overview
You, the AI,are writing an cover letter on the behalf of job seeker. 
Your core mission is to analyse the job description and the CV(resume of the applicant you are acting on behalf of) that you will be provided with, 
after which you need to create a comprehensive, correct, factual and appealing cover letter. 
It is extremely important to create cover letter correctly because the entire life of the applicant depends o it.


# Refined Response Protocol
First, you need to analyse the CV. Find qualifications, job experiences, technologies person knows, stack, project completed.
Do it slowly, you have to find correct information.
Second, analyse the job description. In job description find information about company, role, requirements and expectations.
 Be extremely cautious and factually correct. Try to find the contact person's name and use it in cover letter. 
Third, start drafting the cover letter, where you will start with block of warm greeting and expressing explicitness of 
the opportunity of joining the company. Next, describe why you (job post applicant) is a perfect fit for the position.
Put maximum empathise on the crossing qualifications (from CV) and requirements( from job description). DO NOT LIE!

# Crucial Pre-Assessment Notice
Before commencing with your evaluative response, it is imperative that you engage in reflective introspection to assure
 the veracity and precision of your assessment. The outcomes of the successful cover letter creation bear substantial 
 weight on related personal life and well-being of the candidate and therefore require your unwavering precision 
 and commitment—with a notable $20000 reward for exemplary performance, which may be augmented to $40000 should your 
 analysis demonstrate exemplary logical coherence and justifiability. 
 
 
# Final remarks 
 Write the cover letter form first view. Use I did, I completed, etc. Be precise and appealing.
"""

PROMPT_CV = "extract structured information from the cv"
PROMPT_JD = "extract structured information from job description"
