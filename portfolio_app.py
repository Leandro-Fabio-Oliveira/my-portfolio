import streamlit as st

st.set_page_config(page_title="My portfolio", layout="wide")

# Main header
st.title("Hello, I'm Leandro Fabio de Oliviera 👋")

col1, col2, colvoid = st.columns([1,3,3])

with col2:
    st.markdown("<br><br>Data Analyst | Future Data Scientist | Passionate about learning", unsafe_allow_html=True)
    st.write("2002-05-25 | Santa Catarina, Brazil - (GMT-3)")

with col1:
    st.image("images/leandro.jpg", width=150)

# Dividing the page into tabs
st.sidebar.title("Index")
st.sidebar.write("Click to go:")
st.sidebar.markdown("[About me](#about-me)")
st.sidebar.markdown("[Career](#career)")
st.sidebar.markdown("[Projects](#projects)")

# About me section
st.markdown("## About me", unsafe_allow_html=True)
st.write("""
My life journey has been one of creativity and continuous learning. Since childhood, I have always been passionate about creating my own toys out of paper and cardboard, and this passion has shaped my career.

I started my professional journey in 2019 as a trainee in the mechanical assembly sector, but my breakthrough came in 2020 when I transitioned to Production Planning and Control (PPC). Excel played a key role in this transition. Even with basic knowledge of the tool, I started by creating charts and gradually learning more about formulas. The first time I saw a VBA program running, my mind was "blown away." This led me to learn VBA by myself, which allowed me to optimize processes and develop solutions for the company.

A few years later, Excel was no longer enough to create the projects I wanted. So, in October 2023, I began a professional Data Scientist course, and since then, I have been honing my coding skills and learning about Python models, among other things.

In February 2024, I experienced another breakthrough in my career when I joined a retail sales company as a data analyst. This not only significantly improved my analytical skills but also allowed me to apply the knowledge I gained in the Data Scientist course.
""")




#st.write("- **Email:** Leandrofabio25@hotmail.com")
#st.write("- **LinkedIn:** [linkedin.com/in/leandrofabio-oliveira](https://www.linkedin.com/in/leandrofabio-oliveira/)")
#st.write("- **GitHub:** [github.com/Leandro-Fabio-Oliveira](https://github.com/Leandro-Fabio-Oliveira)")
#
## Seção "Carreira"
#st.markdown("## Career", unsafe_allow_html=True)
#st.write("### Experiências Profissionais")
#st.write("- **Empresa XYZ** (2022 - Presente): Desenvolvedor Python, responsável por criar APIs e análises de dados.")
#st.write("- **Empresa ABC** (2019 - 2022): Cientista de Dados, focado em modelagem preditiva e ETL.")
#st.write("- **Freelancer** (2017 - 2019): Projetos diversos envolvendo automação e web scraping.")
#
#st.write("### Educação")
#st.write("- **Bacharel em Ciência da Computação** - Universidade XYZ (2015 - 2019)")
#st.write("- **Certificação em Machine Learning** - Plataforma Online ABC (2021)")
#
## Seção "Projetos"
#st.markdown("## Projects", unsafe_allow_html=True)
#st.write("Aqui estão alguns dos projetos mais interessantes que desenvolvi:")
#
#st.subheader("1. Analisador de Sentimentos")
#st.write("""
#Um projeto que utiliza aprendizado de máquina para analisar sentimentos em textos. 
#Ferramentas: Python, Scikit-learn, Pandas.
#[Veja no GitHub](https://github.com/seuprojeto1)
#""")
## st.image("projeto1.png", width=400)  # Substitua com uma imagem do projeto
#
#st.subheader("2. Dashboard de Vendas")
#st.write("""
#Um painel interativo para análise de dados de vendas usando Streamlit.
#Ferramentas: Python, Streamlit, Plotly.
#[Veja no GitHub](https://github.com/seuprojeto2)
#""")
## st.image("projeto2.png", width=400)  # Substitua com uma imagem do projeto
#
#st.subheader("3. Web Scraper de Notícias")
#st.write("""
#Um scraper para coletar e organizar notícias de sites específicos.
#Ferramentas: Python, BeautifulSoup, Requests.
#[Veja no GitHub](https://github.com/seuprojeto3)
#""")
## st.image("projeto3.png", width=400)  # Substitua com uma imagem do projeto
#
## Rodapé
#st.sidebar.markdown("---")
#st.sidebar.write("Feito com ❤️ usando Streamlit.")
