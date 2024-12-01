import streamlit as st

st.set_page_config(page_title="My portfolio", layout="wide")

# Main header
st.title("Hello, I'm Leandro Fabio de Oliviera 👋")
st.write("Data Analyst | Analytical Profile | Future Data Scientist | Passionate about learning")
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
My life journey has been one of creativity and continuous learning. Since childhood, I have always been passionate about creating my own toys out of paper and cardboard, and this passion for creating has shaped my career.

I started in the job market in 2019 as a trainee in the mechanical assembly sector, but my professional breakthrough came in 2020 when I transitioned to Production Planning and Control (PPC). Excel played a key role in this transition because, even with basic knowledge of the tool, I started by creating charts and increasingly sought to learn more about formulas. The first time I saw a VBA program running, my mind was "blown away." Because of this, I leaned by myself VBA, which allowed me to optimize processes and develop solutions for the company.

Few years after, excel was not enough to create the projects I wanted. So in october 2023, I started a profissional Data Scientist course, and since it, I've been improving my code skills, learning about python models and so on.

In February 2024, another breakthrough in career, I joined a retail sales company working as a Data Analyst. This not only improve a lot of my analytical skills, that make possible for me to apply the knowledge of the Data Scientist course.
""")




st.write("- **Email:** Leandrofabio25@hotmail.com")
st.write("- **LinkedIn:** [linkedin.com/in/leandrofabio-oliveira](https://www.linkedin.com/in/leandrofabio-oliveira/)")
st.write("- **GitHub:** [github.com/Leandro-Fabio-Oliveira](https://github.com/Leandro-Fabio-Oliveira)")

# Seção "Carreira"
st.markdown("## Career", unsafe_allow_html=True)
st.write("### Experiências Profissionais")
st.write("- **Empresa XYZ** (2022 - Presente): Desenvolvedor Python, responsável por criar APIs e análises de dados.")
st.write("- **Empresa ABC** (2019 - 2022): Cientista de Dados, focado em modelagem preditiva e ETL.")
st.write("- **Freelancer** (2017 - 2019): Projetos diversos envolvendo automação e web scraping.")

st.write("### Educação")
st.write("- **Bacharel em Ciência da Computação** - Universidade XYZ (2015 - 2019)")
st.write("- **Certificação em Machine Learning** - Plataforma Online ABC (2021)")

# Seção "Projetos"
st.markdown("## Projects", unsafe_allow_html=True)
st.write("Aqui estão alguns dos projetos mais interessantes que desenvolvi:")

st.subheader("1. Analisador de Sentimentos")
st.write("""
Um projeto que utiliza aprendizado de máquina para analisar sentimentos em textos. 
Ferramentas: Python, Scikit-learn, Pandas.
[Veja no GitHub](https://github.com/seuprojeto1)
""")
# st.image("projeto1.png", width=400)  # Substitua com uma imagem do projeto

st.subheader("2. Dashboard de Vendas")
st.write("""
Um painel interativo para análise de dados de vendas usando Streamlit.
Ferramentas: Python, Streamlit, Plotly.
[Veja no GitHub](https://github.com/seuprojeto2)
""")
# st.image("projeto2.png", width=400)  # Substitua com uma imagem do projeto

st.subheader("3. Web Scraper de Notícias")
st.write("""
Um scraper para coletar e organizar notícias de sites específicos.
Ferramentas: Python, BeautifulSoup, Requests.
[Veja no GitHub](https://github.com/seuprojeto3)
""")
# st.image("projeto3.png", width=400)  # Substitua com uma imagem do projeto

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("Feito com ❤️ usando Streamlit.")
