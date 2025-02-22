import streamlit as st
import pdfplumber
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

tokenizer = GPT2Tokenizer.from_pretrained("antoiloui/belgpt2")
model = GPT2LMHeadModel.from_pretrained("antoiloui/belgpt2")

# Charger le modèle et le tokenizer

qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Fonction pour extraire le texte d'un PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Interface Streamlit
st.title("ChatbotMyPDF")
st.write("Vous pouvez charger un document et le questionner.")
st.markdown("### ChatbotMyPDF")

uploaded_file = st.file_uploader("Uploader un fichier PDF", type="pdf")
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    question = st.text_input("Posez votre question ici :")
    if question:
        # Recherche de la réponse dans le texte
        result = qa_pipeline(question=question, context=text)
        st.write("Réponse :")
        st.write(result['answer'])