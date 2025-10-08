import streamlit as st

# --- Configuração da página --- #
st.set_page_config(
    page_title="Currículo - Silmar Tolotto",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Função auxiliar para cards --- #
def card(title, icon, content, background="#FFFFFF"):
    st.markdown(
        f"""
        <div style="
            background-color: {background};
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        ">
        <h4 style="margin-bottom:5px">{icon} {title}</h4>
        <p style="margin-top:5px">{content}</p>
        </div>
        """, unsafe_allow_html=True
    )

# --- Sidebar com foto e menu --- #
st.sidebar.image(
    r"C:/Users/SilmarTolotto/OneDrive - Conversys/Documentos/Pessoal/Silmar1.png",
    caption="Silmar Tolotto",
    use_container_width=True
)
st.sidebar.markdown("📧 silmar.tolotto@gmail.com")
st.sidebar.markdown("📱 (11) 9 8928-1468")
st.sidebar.markdown("🎂 09/03/1969")
st.sidebar.markdown("🏠 São Paulo, SP")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silmartolottoa227716)")

menu = st.sidebar.radio(
    "📂 Seções do Currículo",
    ["Resumo", "Formação", "Experiência", "Habilidades", "Certificações", "Atividades/Voluntariado"]
)

# --- Conteúdo Dinâmico --- #
st.markdown("## 💼 Currículo Profissional")
st.markdown("---")

if menu == "Resumo":
    card(
        "Resumo Profissional",
        "👋🏻",
        """Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados.  
        Experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis.  
        Foco em inovação, melhoria contínua e entrega de soluções estratégicas."""
    )

elif menu == "Formação":
    card(
        "Graduação",
        "🎓",
        """**UNINOVE - Universidade Nove de Julho**  
        *Administração de Redes de Computadores e Internet*"""
    )

elif menu == "Experiência":
    card(
        "CONVERSYS IT SOLUTIONS",
        "🏢",
        "01/2025 - atual\nAnalista de Infraestrutura de TI Pleno\nGestão de ambientes corporativos complexos com foco em desempenho, segurança e continuidade."
    )
    card(
        "Fundo Social do Estado de SP / Centro Paula Souza",
        "🏫",
        "10/2023 - 01/2025\nProfessor ministrando aulas em Administração, Empreendedorismo e Informática."
    )
    card(
        "9NET TI, TELECOM E SERVIÇOS",
        "💻",
        "07/2022 - 10/2023\nGerente de Projetos em infraestrutura de TI e Cybersecurity.\nProjetos: CIA Matarazzo, ALUBAR, BP Bunge."
    )
    card(
        "TFA Tecnologia",
        "🖥️",
        "10/2020 - 07/2022\nCoordenador de Tecnologia, gestão de equipe com Scrum/Kanban e desenvolvimento de ERP."
    )
    card(
        "Sherwin-Williams do Brasil",
        "🔧",
        "05/2014 - 08/2019\nAnalista de Suporte, implantação de PABX IP Cisco, rede Wi-Fi, linhas móveis e atualização de equipamentos."
    )

elif menu == "Habilidades":
    col1, col2 = st.columns(2)
    with col1:
        card(
            "Competências Técnicas",
            "🧩",
            """- Gestão de Projetos\n- Liderança e Trabalho em Equipe\n- Comunicação Assertiva\n- Resolução de Problemas\n- Organização"""
        )
    with col2:
        card(
            "Competências Adicionais",
            "💡",
            """- Flexibilidade e Adaptabilidade\n- Proatividade e Foco em Resultados\n- Análise de Dados\n- Pensamento Estratégico\n- Resiliência Profissional"""
        )

elif menu == "Certificações":
    card(
        "Certificações e Cursos",
        "📜",
        """- Gestão de Projetos 1 a 5\n- LGPD\n- Fortinet NS1/NS2/NS3\n- ITIL Foundation\n- Scrum e Liderança Lean\n- Python (Básico a Avançado)\n- Data Science e Inteligência Artificial\n- Power BI e Crystal Reports"""
    )

elif menu == "Atividades/Voluntariado":
    card(
        "Voluntariado e Projetos",
        "🤝",
        """Desde 2015, responsável pelo Centro Escoteiro Jaraguá, coordenando cursos e líderes.  
        Experiência em projetos sociais, modernização de infraestrutura de TI e implantação de soluções Cisco e PoE."""
    )

st.markdown("---")
st.caption("Desenvolvido com ❤️ em Streamlit | © 2025 - Silmar Tolotto")
