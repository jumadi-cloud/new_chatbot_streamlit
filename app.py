# import library
import streamlit as st
import openai
from streamlit_chat import message
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Mahira - Demo",
    page_icon="🤖"
)

# Navigasi
selected = option_menu(None, ["Mahira", "About"], 
        icons=['house', "list-task"], 
        menu_icon="cast", default_index=0, orientation="horizontal",)

# Awal Content Chatbot 

# Cara memangil API dan Konfigurasi
openai.api_key = st.secrets["model"]

if selected == "Mahira":
 st.markdown("""# 🤖 Tanya Mahira
### Hai, aku Mahira👋
""", True)
 
 if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
 if "messages" not in st.session_state:
    st.session_state.messages = []

# Untuk menampilkan riwayat obrolan saat dijalankan ulang aplikasi
 for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
 prompt = st.chat_input("What is up?")
 if prompt:
    # Respone Chatbot
    with st.chat_message("user"):
          st.markdown(prompt)
    # menambahkan chat ke riwayat obrolan
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
              model=st.session_state["openai_model"],
              messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                    ],
                    stream=True,
        ):
              full_response += response.choices[0].delta.get("content", "")
              message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if selected == "About":
    st.markdown("""# 🤖 Mahira
### Hallo Sahabat Mahira 👋

🤖 Aku Mahira👋

Aku adalah asisten virtual **[Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar)** yang dibuat menggunakan **Model ChatGPT** yang dilatih oleh **[OpenAI](https://openai.com/blog/chatgpt/)**
Mahira bisa memberikanmu informasi apapun yang saat ini kamu butuhkan dan bisa jadi temen curhat :dancer:
Kamu bisa tau proses pembuatan mahira dan teknologi yang digunakan di **ABOUT**, Pepatah bilang Tak Kenal Maka Ta Sayang :dancer:

Dukung **Channel Youtube [Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar) dengan cara Subscribe, Like, Share and Comment**

Website kami: https://kelasawanpintar.netlify.app/

""", True)
    st.write("---")
    st.markdown("""
    ### Teknologi Yang Ada di Mahira 🤖
    Seperti yang telah disebutkan, **Mahira** merupakan chatbot yang dapat berkomunikasi dalam format percakapan dan dirancang untuk bisa berinteraksi selayaknya interaksi antar manusia🤗.       
    Pondasi dibalik teknologi chatbot sendiri adalah teknologi Artificial Intelligence (AI), 
    cabang ilmu komputer yang berkaitan dengan pemecahan masalah-masalah selayaknya manusia seperti berbicara, 
    memahami, ataupun berpikir🥳.

    Salah satu bidang dalam AI yang membuat chatbot dapat memproses bahasa alami manusia adalah Natural Language Processing (NLP). **Model ChatGPT** ini dapat digunakan tujuan yang beragam, seperti membuat obrolan otomatis di aplikasi percakapan, 
    membantu dalam pembuatan konten, atau bahkan membantu dalam penerjemahan berbagai bahasa dengan tingkat akurasi yang berbeda-beda untuk tiap bahasa.
    **Model ChatGPT** dilatih dengan menggunakan milyaran kalimat dari berbagai sumber, sehingga model ini dapat menangkap berbagai gaya bahasa dan konteks percakapan. 
    Selain itu, **Model ChatGPT** juga dapat dioptimalkan melalui **fine-tunning** dengan cara menambahkan data latih yang spesifik untuk tugas tertentu, sehingga hasilnya lebih akurat.

    **Model ChatGPT** ini masih memiliki batasan-batasan. **Model ChatGPT** tidak selalu dapat memberikan jawaban yang benar untuk pertanyaan yang bersifat subjektif, atau yang memerlukan pengetahuan yang spesifik dan up-to-date. 
    **Model ChatGPT** juga belum mampu memberikan informasi atau memahami konteks dari peristiwa setelah tahun 2021. 
    Selain itu, **Model ChatGPT** juga membutuhkan data latih yang cukup banyak untuk dapat berfungsi dengan baik.[Sumber](https://id.wikipedia.org/wiki/ChatGPT)
    
    """, True)
    st.write("---")

    st.markdown("""
    ### 📑Proses Pembuatan Mahira
    Dalam proses pembuatan Mahira, Tentu Mahira tidak akan jelaskan disini hanya saja Mahira sudah siapkan Playlistnya🥳.                                                                                            
    Supaya sahabat Mahira juga bisa Godain Mahira💃 dan Sahabat Mahira lebih santai untuk mengikuti step by stepnya☕️.                                                                                                                               
    
    Apabila sahabat Mahira berhasil dengan mengikuti step by step, boleh @Mention kami di sosial Media LinkedIn [`Jumadi`](https://www.linkedin.com/in/jumadi-01/) Instagram [`Jumadi`](https://www.instagram.com/jumadijumadi470/) atau `Comment` di video tutorial 
    
    
    """, True)

    st.write("---")
    st.header("📺 Playlist Belajar Membuat Aplikasi Web Dengan Streamlit [Python]")
    
    col1, col2, col3 = st.columns(3)
    with col1:
            st.subheader("01a - Cara Membuat Chatbot Menggunakan Model ChatGPT Dengan Streamlit")
            st.video('https://www.youtube.com/watch?v=MaheNAPbBGU&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=1&t=4s')

    with col2:
            st.subheader("01b - Cara Membuat Chatbot Menggunakan Model ChatGPT Dengan Streamlit")
            st.video('https://www.youtube.com/watch?v=DxWPH34MAx8&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=2')

    with col3:
            st.subheader("01c - Deploy Chatbot Menggunakan Model ChatGPT Dengan Streamlit")
            st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')

    st.write("---")
    st.header("Playlist Belajar Streamlit Bahasa Indonesia [Dasar]")
    col1, col2, col3 = st.columns(3)

    with col1:
            st.subheader("Introduction di Aplikasi Streamlit")
            st.video('https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l')

    with col2:
            st.subheader("Cara menampilkan teks")
            st.video('https://www.youtube.com/watch?v=tPA0x_wToXQ&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=2')

    with col3:
            st.subheader("Cara Menampilkan Data")
            st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')

    st.header("[Daftar Video Playlist Belajar Streamlit Bahasa Indonesia [Dasar]](https://www.youtube.com/c/Avra_b)")

    st.write("---")
    
    st.markdown("""
    ### ⭐ ☕️🤗 Support channel youtube Kelas Awan Pintar !  
    [Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar)
    -------------
        """, False)
# Akhir Content About

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)