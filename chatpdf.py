import streamlit as st
import pdfplumber
from transformers import pipeline, CamembertTokenizer, CamembertForQuestionAnswering
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# tokenizer_gpt = GPT2Tokenizer.from_pretrained("antoiloui/belgpt2")
# model_gpt = GPT2LMHeadModel.from_pretrained("antoiloui/belgpt2")

# def generate_response(prompt):
#     inputs = tokenizer_gpt(prompt, return_tensors="pt")
#     outputs = model_gpt.generate(**inputs, max_length=50)
#     return tokenizer_gpt.decode(outputs[0], skip_special_tokens=True)

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

# Interface Streamlit avec une image de type icone centrée et un titre
with st.image("ico.webp", width=100):
    st.title("Chatbot avec intégration de PDF")

# Insertion d'une zone de chat avec historique, et petit bouton pour uploader un PDF
with st.chat_message("user"):
    # Initialisation de l'historique de chat
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    st.write("Yo bro, ca dit quoi aujourdhui? 👋")
    # petit bouton pour uploader un PDF

    uploaded_file = st.file_uploader("PDF", label_visibility="hidden")
    
# confirmation ou non de l'upload
if uploaded_file is not None:
    st.write("PDF uploadé avec succès !")
    st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
 
# saisie de l'utilisateur et ajout à l'historique
user_input = st.chat_input("Tu veux savoir quoi?", key="user_input",)
if user_input:
    # Affichage de la saisie dans la conversation
    st.write(user_input)
    # Mise à jour de l'historique de la conversation
    st.session_state.chat_history.append({"role": "User", "content": user_input})
    # reponse du chatbot et mise à jour de l'historique
    if "pdf_text" in st.session_state:
        result = pipe(question=user_input, context=st.session_state.pdf_text)
        response = result['answer']
    # sinon, répondre par défaut
    else:
        response = "Je suis un chatbot, pose-moi une question !"
    st.write(response)    
    st.session_state.chat_history.append({"role": "Chatbot", "content": response})

    
    




    # Affichage d'une siderbar montrant l'ensemble des chats
    # avec des boutons pour passer d'un chat à l'autre
    # On résume la conversation en cours pour avoir un nom de chat
    # et on ajoute un bouton pour passer à un nouveau chat
    # à chaque fois qu'un chat est commencé le nom et le bouton du chat apparait
    # dans la sidebar, et on peut cliquer dessus pour y revenir
# st.sidebar.title("Historique des chats")
# if len(st.session_state.chat_history) > 0:
#     chat_summary = f"{st.session_state.chat_history[-2]['content']} -> {st.session_state.chat_history[-1]['content']}"
#     st.sidebar.button(chat_summary, key=len(st.session_state.chat_history))
# if st.sidebar.button("Nouveau chat"):
#     st.session_state.chat_history = []





  
    
    







