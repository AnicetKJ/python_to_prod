import streamlit as st
import pdfplumber
from transformers import pipeline, CamembertTokenizer, CamembertForQuestionAnswering


tokenizer = CamembertTokenizer.from_pretrained("cmarkea/distilcamembert-base-qa")
model = CamembertForQuestionAnswering.from_pretrained("cmarkea/distilcamembert-base-qa")
pipe = pipeline("question-answering", model="cmarkea/distilcamembert-base-qa", tokenizer=tokenizer)

# Fonction pour extraire le texte d'un PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Initialisation de l'historique de chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Interface Streamlit
st.title("Chatbot avec intégration de PDF")

# Zone de chat
st.write("### Conversation")
for message in st.session_state.chat_history:
    st.write(f"**{message['role']}**: {message['content']}")

# Upload de PDF
uploaded_file = st.file_uploader("Uploader un fichier PDF", type="pdf")
if uploaded_file is not None:
    st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
    st.session_state.chat_history.append({"role": "Système", "content": "PDF uploadé et prêt à être analysé."})

# Champ de texte pour poser une question
user_input = st.text_input("Posez votre question ou discutez avec le chatbot :")

if user_input:
    # Ajouter la question de l'utilisateur à l'historique
    st.session_state.chat_history.append({"role": "Utilisateur", "content": user_input})

    # Répondre à la question
    if "pdf_text" in st.session_state:
        # Si un PDF est uploadé, répondre en fonction de son contenu
        result = pipe(question=user_input, context=st.session_state.pdf_text)
        response = result['answer']
    else:
        # Sinon, répondre à des questions générales (exemple simple)
        response = "Je suis un chatbot. Pour des réponses plus précises, veuillez uploader un PDF."

    # Ajouter la réponse du chatbot à l'historique
    st.session_state.chat_history.append({"role": "Chatbot", "content": response})

    # Rafraîchir l'affichage du chat
    st.experimental_user()