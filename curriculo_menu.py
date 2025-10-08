# --- Importar --- #
import streamlit as st

# --- Configuração da página --- #
st.set_page_config(
    page_title="Currículo - Silmar Tolotto",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Menu lateral interativo --- #
menu = st.sidebar.selectbox(
    "📂 Navegue pelo Currículo",
    ["Resumo", "Formação", "Experiência Profissional", "Habilidades", "Certificações", "Atividades e Voluntariado"]
)

# --- Dados básicos na barra lateral --- #
st.sidebar.image(
    r"C:/Users/SilmarTolotto/OneDrive - Conversys/Documentos/Pessoal/Silmar1.png",
    caption="Silmar Tolotto",
    use_container_width=True
)

st.sidebar.markdown("📧 silmar.tolotto@gmail.com")
st.sidebar.markdown("📱 (11) 9 8928-1468")
st.sidebar.markdown("🎂 09 março de 1969")
st.sidebar.markdown("🏠 São Paulo, SP")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silmartolottoa227716)")

st.markdown("## 💼 Currículo Profissional")
st.markdown("---")

# --- Seções dinâmicas --- #
if menu == "Resumo":
    st.header("👋🏻 Resumo Profissional")
    st.markdown("""
    Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados.  
    Sólida experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis.  
    Profissional com forte espírito de equipe e foco em inovação e melhoria contínua.
    """)

elif menu == "Formação":
    st.header("🎓 Formação Acadêmica")
    st.markdown("""
    **UNINOVE - Universidade Nove de Julho**  
    📘 *Administração de Redes de Computadores e Internet*
    """)

elif menu == "Experiência Profissional":
    st.header("💼 Experiência Profissional")

    st.subheader("CONVERSYS IT SOLUTIONS (01/2025 - atual)")
    st.markdown("""
    - Analista de Infraestrutura de TI Pleno  
    - Gestão de ambientes corporativos complexos com foco em desempenho e segurança  
    - Especialista em servidores, redes, virtualização e automação
    """)

    st.subheader("Fundo Social do Estado de SP / Centro Paula Souza (10/2023 - 01/2025)")
    st.markdown("""
    - Professor nas áreas de Administração, Empreendedorismo e Informática
    """)

    st.subheader("9NET TI, TELECOM E SERVIÇOS (07/2022 - 10/2023)")
    st.markdown("""
    - Gerente de Projetos: gestão técnica e operacional de infraestrutura de TI  
    - Projetos: CIA Matarazzo, ALUBAR, BP Bunge  
    - Aplicação de metodologias ágeis, governança e KPIs
    """)

    st.subheader("TFA Tecnologia (10/2020 - 07/2022)")
    st.markdown("""
    - Coordenador de Tecnologia  
    - Gestão de equipe com Scrum e Kanban  
    - Desenvolvimento de ERP para inventário de TI
    """)

    st.subheader("Sherwin-Williams do Brasil (05/2014 - 08/2019)")
    st.markdown("""
    - Analista de Suporte  
    - Implantação de PABX IP Cisco, rede Wi-Fi e linhas móveis  
    - Gestão de contas operadoras e atualização de equipamentos de TI
    """)

elif menu == "Habilidades":
    st.header("🧩 Habilidades")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - Gestão de Projetos  
        - Liderança e Trabalho em Equipe  
        - Comunicação Assertiva  
        - Resolução de Problemas  
        - Organização e Planejamento
        """)

    with col2:
        st.markdown("""
        - Flexibilidade e Adaptabilidade  
        - Proatividade e Foco em Resultados  
        - Análise de Dados  
        - Pensamento Estratégico  
        - Resiliência Profissional
        """)

elif menu == "Certificações":
    st.header("📜 Certificações e Cursos")
    st.markdown("""
    - Gestão de Projetos 1 a 5  
    - LGPD  
    - Fortinet NS1, NS2, NS3  
    - ITIL Foundation  
    - Scrum e Liderança Lean  
    - Python (Básico, Intermediário, Avançado)  
    - Data Science e Inteligência Artificial  
    - Power BI e Crystal Reports  
    - Administração e Planejamento Financeiro
    - Fundamentos de Data Science e Inteligência Artificial, 
    """)

elif menu == "Atividades e Voluntariado":
    st.header("🤝 Atividades e Voluntariado")
    st.markdown("""
    - Desde 2015, responsável pelo **Centro Escoteiro Jaraguá**  
    - Coordenação e instrução de cursos para líderes e voluntários do Estado de SP  
    - Experiência em projetos sociais e modernização de infraestrutura de TI  
    - Implantação de soluções Cisco e PoE em empresas de grande porte
    """)

st.markdown("---")
st.caption("Desenvolvido com ❤️ em Streamlit | © 2025 - Silmar Tolotto")
