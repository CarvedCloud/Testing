import openai
import PyPDF2
g_text=""

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    global g_text
    g_text = text

openai.api_key = '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' #Change key if expired

def summarize_with_chatgpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n{text}",
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

extract_text_from_pdf("C:\\Users\\srini\\Downloads\\Unit_1_Mech_Notes_1.pdf") #Change Path to local file address
summarize_with_chatgpt(g_text)