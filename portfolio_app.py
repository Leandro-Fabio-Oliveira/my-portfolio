import streamlit as st

#st.image(".\images\leandro.jpg", width=200)
#
#st.header("I'm Leandro Fabio de Oliveira")
#
#st.sidebar.markdown("## Leandro Fabio de Oliveira")
#st.sidebar.markdown("____")
#st.sidebar.markdown("")
#st.sidebar.markdown("About me")





st.set_page_config(page_title="My portfolio", layout="wide")

# Cabeçalho princip al
st.title("Hello, I'm Leandro Fabio de Oliviera 👋")
st.write("Python Dev | Data Scientist | analytical profile | Passionate about learning")
st.image("images/leandro.jpg", width=150)

# Dividindo a página em abas
st.sidebar.title("Navegação")
aba = st.sidebar.radio("Go to:", ["About me", "Career", "Projects"])

# Aba "Sobre Mim"
if aba == "About me":
    st.header("About me")
    st.write("""
    Olá! Sou um desenvolvedor apaixonado por criar soluções inovadoras usando Python e outras tecnologias.
    Tenho experiência em desenvolvimento de software, ciência de dados e aprendizado de máquina.
    """)
    st.write("- **Email:** Leandrofabio25@hotmail.com")
    st.write("- **LinkedIn:** [linkedin.com/in/seuperfil](https://www.linkedin.com/in/leandrofabio-oliveira/)")
    st.write("- **GitHub:** [github.com/seuperfil](https://github.com/Leandro-Fabio-Oliveira)")

# Aba "Carreira"
elif aba == "Career":
    st.header("Career")
    st.write("### Experiências Profissionais")
    st.write("- **Empresa XYZ** (2022 - Presente): Desenvolvedor Python, responsável por criar APIs e análises de dados.")
    st.write("- **Empresa ABC** (2019 - 2022): Cientista de Dados, focado em modelagem preditiva e ETL.")
    st.write("- **Freelancer** (2017 - 2019): Projetos diversos envolvendo automação e web scraping.")

    st.write("### Educação")
    st.write("- **Bacharel em Ciência da Computação** - Universidade XYZ (2015 - 2019)")
    st.write("- **Certificação em Machine Learning** - Plataforma Online ABC (2021)")

# Aba "Projetos"
elif aba == "Projects":
    st.header("Projects")
    st.write("Aqui estão alguns dos projetos mais interessantes que desenvolvi:")

    st.subheader("1. Analisador de Sentimentos")
    st.write("""
    Um projeto que utiliza aprendizado de máquina para analisar sentimentos em textos. 
    Ferramentas: Python, Scikit-learn, Pandas.
    [Veja no GitHub](https://github.com/seuprojeto1)
    """)
    #st.image("projeto1.png", width=400)  # Substitua com uma imagem do projeto

    st.subheader("2. Dashboard de Vendas")
    st.write("""
    Um painel interativo para análise de dados de vendas usando Streamlit.
    Ferramentas: Python, Streamlit, Plotly.
    [Veja no GitHub](https://github.com/seuprojeto2)
    """)
    #st.image("projeto2.png", width=400)  # Substitua com uma imagem do projeto

    st.subheader("3. Web Scraper de Notícias")
    st.write("""
    Um scraper para coletar e organizar notícias de sites específicos.
    Ferramentas: Python, BeautifulSoup, Requests.
    [Veja no GitHub](https://github.com/seuprojeto3)
    """)
    #st.image("projeto3.png", width=400)  # Substitua com uma imagem do projeto

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("Feito com ❤️ usando Streamlit.")
