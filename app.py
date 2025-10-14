# --- Importar --- #
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# --- Tentar importar reportlab --- #
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
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

# --- Função para gerar PDF --- #
def gerar_pdf():
    if not REPORTLAB_INSTALLED:
        st.error("📌 A biblioteca reportlab não está instalada. Execute: pip install reportlab")
        return None

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph("Currículo Profissional - Silmar Tolotto", styles['Title']))
    elements.append(Spacer(1, 12))

    # Dados pessoais
    elements.append(Paragraph("📧 silmar.tolotto@gmail.com", styles['Normal']))
    elements.append(Paragraph("📱 (11) 9 8928-1468", styles['Normal']))
    elements.append(Paragraph("🎂 09 março de 1969", styles['Normal']))
    elements.append(Paragraph("🏠 São Paulo, SP", styles['Normal']))
    elements.append(Paragraph("🔗 LinkedIn: https://www.linkedin.com/in/silmartolottoa227716", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Resumo
    elements.append(Paragraph("<b>Resumo Profissional</b>", styles['Heading2']))
    elements.append(Paragraph(
        "Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados. "
        "Sólida experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis. "
        "Profissional com forte espírito de equipe e foco em inovação e melhoria contínua.",
        styles['Normal']
    ))
    elements.append(Spacer(1, 12))

    # Experiência
    elements.append(Paragraph("<b>Experiência Profissional</b>", styles['Heading2']))
    experiencias = [
        "CONVERSYS IT SOLUTIONS (01/2025 - atual) - Analista de Infraestrutura de TI Pleno",
        "Fundo Social do Estado de SP / Centro Paula Souza (10/2023 - 01/2025) - Professor",
        "9NET TI, TELECOM E SERVIÇOS (07/2022 - 10/2023) - Gerente de Projetos",
        "TFA Tecnologia (10/2020 - 07/2022) - Coordenador de Tecnologia",
        "Sherwin-Williams do Brasil (05/2014 - 08/2019) - Analista de Suporte"
    ]
    for exp in experiencias:
        elements.append(Paragraph(f"- {exp}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Formação
    elements.append(Paragraph("<b>Formação Acadêmica</b>", styles['Heading2']))
    elements.append(Paragraph("UNINOVE - Universidade Nove de Julho", styles['Normal']))
    elements.append(Paragraph("Administração de Redes de Computadores e Internet", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Habilidades técnicas
    elements.append(Paragraph("<b>Habilidades Técnicas</b>", styles['Heading2']))
    habilidades_tecnicas = [
        "Excel Avançado (Dashboards, VBA) - 95%",
        "Análise de Dados e BI - 85%",
        "AutoCAD (2D/3D) - 80%",
        "Infraestrutura e Redes - 90%",
        "Python e Automação - 85%"
    ]
    for h in habilidades_tecnicas:
        elements.append(Paragraph(f"- {h}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Habilidades comportamentais
    elements.append(Paragraph("<b>Competências Comportamentais</b>", styles['Heading2']))
    habilidades_comportamentais = [
        "Liderança e Trabalho em Equipe - 90%",
        "Comunicação Assertiva - 85%",
        "Proatividade e Foco em Resultados - 90%",
        "Pensamento Estratégico - 85%",
        "Resiliência e Adaptabilidade - 95%"
    ]
    for h in habilidades_comportamentais:
        elements.append(Paragraph(f"- {h}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Certificações
    elements.append(Paragraph("<b>Certificações e Cursos</b>", styles['Heading2']))
    certificacoes = [
        "Gestão de Projetos 1 a 5", "LGPD", "Fortinet NS1, NS2, NS3",
        "ITIL Foundation", "Scrum e Liderança Lean", "Python Avançado",
        "Data Science e Inteligência Artificial", "Power BI e Crystal Reports",
        "Excel Avançado", "AutoCAD 2D e 3D"
    ]
    for c in certificacoes:
        elements.append(Paragraph(f"- {c}", styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ==========================
# SIDEBAR
# ==========================
st.sidebar.image("Silmar1.png", caption="Silmar Tolotto", use_container_width=True)
st.sidebar.markdown("📧 silmar.tolotto@gmail.com")
st.sidebar.markdown("📱 (11) 9 8928-1468")
st.sidebar.markdown("🎂 09 março de 1969")
st.sidebar.markdown("🏠 São Paulo, SP")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silmartolottoa227716)")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 Exportar Currículo")
pdf_buffer = gerar_pdf()
if pdf_buffer:
    st.sidebar.download_button(
        label="⬇️ Baixar em PDF",
        data=pdf_buffer,
        file_name="Curriculo_Silmar_Tolotto.pdf",
        mime="application/pdf"
    )

# ==========================
# CONTEÚDO PRINCIPAL
# ==========================
st.markdown("## 💼 Currículo Profissional")
st.markdown("---")
st.header("👋🏻 Resumo Profissional")
st.markdown("""
Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados.  
Sólida experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis.  
Profissional com forte espírito de equipe e foco em inovação e melhoria contínua.
""")

st.caption("Desenvolvido com ❤️ em Streamlit | © 2025 - Silmar Tolotto")
