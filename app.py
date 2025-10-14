# --- Importar --- #
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from io import BytesIO

# --- Tentativa de importar reportlab --- #
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    REPORTLAB_INSTALLED = True
except ImportError:
    REPORTLAB_INSTALLED = False

# --- Configuração da página --- #
st.set_page_config(
    page_title="Currículo - Silmar Tolotto",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Função para barra de proficiência personalizada --- #
def skill_bar(skill, percent, color="#4CAF50"):
    bar_html = f"""
    <div style="margin-bottom: 10px;">
        <strong>{skill}</strong>
        <div style="background-color: #ddd; border-radius: 10px; height: 22px; position: relative;">
            <div style="width: 0%; background-color: {color}; height: 22px; border-radius: 10px;" id="bar">
                <span style="position: absolute; right: 8px; color: white; font-weight: bold;">{percent}%</span>
            </div>
        </div>
    </div>
    <script>
    var elem = document.currentScript.parentElement.querySelector('#bar');
    var width = 0;
    var id = setInterval(frame, 10);
    function frame() {{
        if (width >= {percent}) {{
            clearInterval(id);
        }} else {{
            width++;
            elem.style.width = width + '%';
        }}
    }}
    </script>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

# --- Função para gerar PDF --- #
def gerar_pdf():
    if not REPORTLAB_INSTALLED:
        st.error("📌 A biblioteca reportlab não está instalada. Instale com 'pip install reportlab'")
        return None
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>Currículo Profissional - Silmar Tolotto</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Dados pessoais
    elements.append(Paragraph("<b>Dados Pessoais</b>", styles["Heading2"]))
    elements.append(Paragraph("📧 silmar.tolotto@gmail.com", styles["Normal"]))
    elements.append(Paragraph("📱 (11) 9 8928-1468", styles["Normal"]))
    elements.append(Paragraph("🎂 09 março de 1969", styles["Normal"]))
    elements.append(Paragraph("🏠 São Paulo, SP", styles["Normal"]))
    elements.append(Paragraph("🔗 LinkedIn: https://www.linkedin.com/in/silmartolottoa227716", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Resumo
    elements.append(Paragraph("<b>Resumo Profissional</b>", styles["Heading2"]))
    elements.append(Paragraph("""
    Gerente de Projetos, Professor e Analista de Infraestrutura de TI,
    organizado e orientado a resultados. Experiência em ambientes corporativos,
    metodologias ágeis, foco em inovação e melhoria contínua.
    """, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Experiência
    elements.append(Paragraph("<b>Experiência Profissional</b>", styles["Heading2"]))
    experiencias = [
        "CONVERSYS IT SOLUTIONS (01/2025 - atual) - Analista de Infraestrutura de TI Pleno",
        "Fundo Social do Estado de SP / Centro Paula Souza (10/2023 - 01/2025) - Professor",
        "9NET TI, TELECOM E SERVIÇOS (07/2022 - 10/2023) - Gerente de Projetos",
        "TFA Tecnologia (10/2020 - 07/2022) - Coordenador de Tecnologia",
        "Sherwin-Williams do Brasil (05/2014 - 08/2019) - Analista de Suporte"
    ]
    for exp in experiencias:
        elements.append(Paragraph(f"- {exp}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Formação
    elements.append(Paragraph("<b>Formação Acadêmica</b>", styles["Heading2"]))
    elements.append(Paragraph("UNINOVE - Universidade Nove de Julho", styles["Normal"]))
    elements.append(Paragraph("Administração de Redes de Computadores e Internet", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Habilidades técnicas
    elements.append(Paragraph("<b>Habilidades Técnicas</b>", styles["Heading2"]))
    habilidades_tecnicas = [
        "Excel Avançado (Dashboards, VBA) - 95%",
        "Análise de Dados e BI - 85%",
        "AutoCAD (2D/3D, Plantas e Diagramas) - 80%",
        "Infraestrutura e Redes - 90%",
        "Python e Automação - 85%"
    ]
    for h in habilidades_tecnicas:
        elements.append(Paragraph(f"- {h}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Habilidades comportamentais
    elements.append(Paragraph("<b>Competências Comportamentais</b>", styles["Heading2"]))
    habilidades_comportamentais = [
        "Liderança e Trabalho em Equipe - 90%",
        "Comunicação Assertiva - 85%",
        "Proatividade e Foco em Resultados - 90%",
        "Pensamento Estratégico - 85%",
        "Resiliência e Adaptabilidade - 95%"
    ]
    for h in habilidades_comportamentais:
        elements.append(Paragraph(f"- {h}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Certificações
    elements.append(Paragraph("<b>Certificações e Cursos</b>", styles["Heading2"]))
    certificacoes = [
        "Gestão de Projetos 1 a 5", "LGPD", "Fortinet NS1, NS2, NS3",
        "ITIL Foundation", "Scrum e Liderança Lean", "Python Avançado",
        "Data Science e Inteligência Artificial", "Power BI e Crystal Reports",
        "Excel Avançado", "AutoCAD 2D e 3D"
    ]
    for c in certificacoes:
        elements.append(Paragraph(f"- {c}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ==============================
# SIDEBAR
# ==============================
st.sidebar.image("Silmar1.png", caption="Silmar Tolotto", use_container_width=True)
st.sidebar.markdown("📧 silmar.tolotto@gmail.com")
st.sidebar.markdown("📱 (11) 9 8928-1468")
st.sidebar.markdown("🎂 09 março de 1969")
st.sidebar.markdown("🏠 São Paulo, SP")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silmartolottoa227716)")

# Botão de PDF na sidebar
st.sidebar.markdown("### 📄 Exportar Currículo")
pdf_buffer = gerar_pdf()
if pdf_buffer:
    st.sidebar.download_button(
        label="⬇️ Baixar em PDF",
        data=pdf_buffer,
        file_name="Curriculo_Silmar_Tolotto.pdf",
        mime="application/pdf"
    )

# Menu lateral interativo
menu = st.sidebar.selectbox(
    "📂 Navegue pelo Currículo",
    ["Resumo", "Formação", "Experiência Profissional", "Habilidades", "Certificações", "Atividades e Voluntariado"]
)

st.markdown("## 💼 Currículo Profissional")
st.markdown("---")

# ==============================
# CONTEÚDO PRINCIPAL
# ==============================
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
    exp_list = [
        ("CONVERSYS IT SOLUTIONS", "01/2025 - atual", "Analista de Infraestrutura de TI Pleno"),
        ("Fundo Social do Estado de SP / Centro Paula Souza", "10/2023 - 01/2025", "Professor"),
        ("9NET TI, TELECOM E SERVIÇOS", "07/2022 - 10/2023", "Gerente de Projetos"),
        ("TFA Tecnologia", "10/2020 - 07/2022", "Coordenador de Tecnologia"),
        ("Sherwin-Williams do Brasil", "05/2014 - 08/2019", "Analista de Suporte")
    ]
    for empresa, periodo, cargo in exp_list:
        st.subheader(f"{empresa} ({periodo})")
        st.markdown(f"- {cargo}")

elif menu == "Habilidades":
    st.header("🧩 Habilidades e Competências")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💻 Técnicas")
        skill_bar("📊 Excel Avançado (Dashboards, VBA)", 95, "#2E8B57")
        skill_bar("📈 Análise de Dados e BI", 85, "#4682B4")
        skill_bar("📐 AutoCAD (2D/3D)", 80, "#DAA520")
        skill_bar("⚙️ Infraestrutura e Redes", 90, "#4B0082")
        skill_bar("🐍 Python e Automação", 85, "#FF4500")
    with col2:
        st.markdown("### 🤝 Comportamentais")
        skill_bar("👥 Liderança e Trabalho em Equipe", 90, "#3CB371")
        skill_bar("🗣️ Comunicação Assertiva", 85, "#4682B4")
        skill_bar("🚀 Proatividade e Foco em Resultados", 90, "#DA70D6")
        skill_bar("🧠 Pensamento Estratégico", 85, "#6A5ACD")
        skill_bar("🧩 Resiliência e Adaptabilidade", 95, "#008B8B")

    st.markdown("---")
    # --- Gráfico de radar ---
    st.subheader("📊 Comparativo de Competências (Radar Chart)")

    labels = np.array(["Excel / BI","AutoCAD","Infraestrutura","Comunicação","Liderança","Resiliência"])
    technical = np.array([95, 80, 90, 0, 0, 0])
    behavioral = np.array([0, 0, 0, 85, 90, 95])
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    technical = np.concatenate((technical, [technical[0]]))
    behavioral = np.concatenate((behavioral, [behavioral[0]]))

    fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
    ax.plot(angles, technical, color="#1E90FF", linewidth=2, label="Técnicas")
    ax.fill(angles, technical, color="#1E90FF", alpha=0.25)
    ax.plot(angles, behavioral, color="#FF69B4", linewidth=2, label="Comportamentais")
    ax.fill(angles, behavioral, color="#FF69B4", alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.legend(loc="upper right", bbox_to_anchor=(1.2,1.1))
    st.pyplot(fig)

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
    - Excel Avançado (Dashboards, Fórmulas, Power Query e VBA)  
    - AutoCAD (2D e 3D, Plantas Técnicas e Layouts Industriais)  
    - Administração e Planejamento Financeiro  
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
