import streamlit as st
import google.generativeai as genai

# Configuración
st.set_page_config(page_title="AI Product Lister | Fast Descriptions", page_icon="✍️")

# Conectar con la IA (Necesitarás tu clave de API de Google AI Studio)
# Para desarrollo puedes pegarla aquí, pero lo ideal es usar st.secrets
genai.configure(api_key="AIzaSyDav8Oy92eVAfmauTdy0jsbMIolqufTc5o")
model = genai.GenerativeModel('gemini-pro')

# Sidebar de Monetización
st.sidebar.image("https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg", width=150)
st.sidebar.markdown(
    f"""
    <a href="https://buymeacoffee.com/yojimbomrp" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
        alt="Buy Me A Coffee" style="height: 50px !important;width: 180px !important;" >
    </a>
    """,
    unsafe_allow_html=True
)
st.sidebar.divider()
st.sidebar.info("Support this free AI tool to keep it online!")

# Interfaz Principal
st.title("AI Product Description Generator ✍️")
st.write("Generate high-converting descriptions for Amazon, Shopify or eBay in seconds.")

product_name = st.text_input("Product Name", placeholder="e.g. Ergonomic Office Chair")
keywords = st.text_area("Key Features (one per line)", placeholder="Lumbar support\nBreathable mesh\n360-degree swivel")
tone = st.selectbox("Tone of voice", ["Professional", "Persuasive", "Minimalist", "Funny"])

if st.button("Generate Description ✨"):
    if product_name and keywords:
        prompt = f"Write a {tone} product description for {product_name}. Features: {keywords}. Format it with a catchy headline and bullet points."
        
        with st.spinner('AI is writing...'):
            response = model.generate_content(prompt)
            st.subheader("Result:")
            st.write(response.text)
            st.balloons()
    else:
        st.error("Please provide at least a name and some features.")
