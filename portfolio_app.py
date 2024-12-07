import streamlit as st

st.set_page_config(page_title="My portfolio", layout="wide")

# Main header
st.title("Hello, I'm Leandro Fabio de Oliviera 👋")

col1, col2, colvoid = st.columns([1,3,1])

with col1:
    st.image("images/leandro.jpg", use_container_width=True)

with col2:
    st.markdown("<br><br> Credit Analyst | Data Analyst | Future Data Scientist | Passionate about learning", unsafe_allow_html=True)
    st.write("2002-05-25 | Santa Catarina, Brazil - (GMT-3)")

# Dividing the page into tabs
st.sidebar.title("Index")
st.sidebar.write("Click to go:")
st.sidebar.markdown("[About me](#about-me)")
st.sidebar.markdown("[My Career](#my-career)")
st.sidebar.markdown("[My skills](#my-skills)")
st.sidebar.markdown("[My Projects](#projects)")

# About me section
st.markdown("## About me", unsafe_allow_html=True)
st.write("""
My life journey has been one of creativity and continuous learning. Since childhood, I found joy in transforming paper and cardboard into toys. The thrill of creating something new has always been at my heart, driving me to explore new tools and technologies.

I started my professional journey in 2019 as a trainee in the mechanical assembly sector, but my breakthrough came in 2020 when I transitioned to production planning and control (PPC). Excel played a key role in this transition. At that time, even with basic knowledge of the tool, I started by creating charts and gradually learning more about formulas. The first time I saw a VBA program running, my mind was "blown away." This led me to learn VBA by myself, which allowed me to optimize processes and develop solutions for the company.

A few years later, Excel was no longer enough to create the projects I wanted. So, in October 2023, I began a professional data scientist course, and since then, I have been improving my coding skills, learning about Python machine learning models, and a bit of statistics.

In February 2024, I experienced another breakthrough in my career when I joined a retail sales company as a data analyst. This not only significantly improved my analytical skills but also allowed me to apply the knowledge I developed in the Data Scientist course.

What started as simple toys has grown into a career rooted in innovation and problem-solving. Whether building with paper, coding VBA, or applying machine learning, my passion remains the same: creating and discovering new possibilities.
""")

## My Career section
st.markdown("## My Career", unsafe_allow_html=True)

st.markdown("### • Grupo Berlanda")
st.markdown("[*About Grupo Berlanda*](https://grupoberlanda.com.br/)")
st.markdown("##### Credit Analyst (2024-02 → now)")
st.text('here is the information about the job')


st.markdown("### • Mendes Máquinas")
st.markdown("[*About Mendes Máquina*](https://mendesmaquinas.com.br/)")

st.markdown("##### Cost Analyst Assistant (2023-09 → 2024-01)")
st.markdown(("• Performed calculation and analysis of production costs. <br>" +
             "• Monitored production cost reports. <br>" +
             "• Compared costs of previously produced items to evaluate production efficiency. <br>" +
             "• Prepared price quotes to determine sales pricing. <br>" +
             "• Conducted routine recalculations of hourly cost and rate. <br>" +
             "• Generated cost statistics for parts and machines using Power BI. <br>" + 
             "• Developed control and process optimization tools using Excel and VBA. <br><br>"), unsafe_allow_html=True)

st.markdown("##### Junior Cost Assistant (2022-05 → 2023-08)")
st.markdown(("• Calculated costs of existing parts and machines to assist the sales team in pricing strategies. <br>" +
             "• Conducted cost studies for quotes on new parts, machines, and projects. <br>" + 
             "• Participated in the 'TaskForce' team to analyze costs and sales in markets beyond the wood industry. <br><br>"), unsafe_allow_html=True)

st.markdown("##### Production Planning and Control Assistant (2021-04 → 2022-04)")
st.markdown(("• Analyzed costs of existing parts to assist the sales team with pricing. <br>" +
             "• Calculated costs for equipment refurbishments. <br>" + 
             "• Developed spreadsheets to streamline production control. <br>" +
             "• Created presentations on the progress of parts and machine timelines using PowerPoint. <br><br>"), unsafe_allow_html=True)

st.markdown("##### Production Planning and Control Trainee (2020-07 → 2021-03)")
st.markdown(("• Timed and monitored manufacturing processes for parts and assemblies. <br>" +
             "• Prepared production time charts using Excel. <br>" + 
             "• Conducted cost analyses for parts. <br><br>"), unsafe_allow_html=True)

st.markdown("##### Mechanical Assembly Trainee (2019-06 → 2020-06)")
st.markdown(("• Organized and maintained inventory control of manufactured parts for assembly of machinery and equipment. <br>" +
             "• Supported the assembly of equipment. <br>" + 
             "• Assisted in product loading, packaging, and preparation for transport. <br><br>"), unsafe_allow_html=True)

#st.markdown("## My Skills", unsafe_allow_html=True)
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
