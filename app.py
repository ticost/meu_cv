# --- Importações --- #
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

# ==========================
# FUNÇÃO PARA GERAR PDF
# ==========================
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

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ==========================
# BARRA LATERAL
# ==========================
st.sidebar.image("Silmar1.png", caption="Silmar Tolotto", use_container_width=True)
st.sidebar.markdown("📧 silmar.tolotto@gmail.com")
st.sidebar.markdown("📱 (11) 9 8928-1468")
st.sidebar.markdown("🎂 09 março de 1969")
st.sidebar.markdown("🏠 São Paulo, SP")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silmartolottoa227716)")

# Botão de download PDF logo abaixo do LinkedIn
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

# --- Gráfico de radar --- #
st.subheader("📊 Comparativo de Competências (Radar Chart)")

labels = np.array([
    "Excel / BI", 
    "AutoCAD", 
    "Infraestrutura", 
    "Comunicação", 
    "Liderança", 
    "Resiliência"
])
technical = np.array([95, 80, 90, 0, 0, 0])   # técnicas
behavioral = np.array([0, 0, 0, 85, 90, 95])  # comportamentais

# Fechar o gráfico adicionando o primeiro ponto no final
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

technical = np.concatenate((technical, [technical[0]]))
behavioral = np.concatenate((behavioral, [behavioral[0]]))

fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
ax.plot(angles, technical, color="#1E90FF", linewidth=2, label="Técnicas")
ax.fill(angles, technical, color="#1E90FF", alpha=0.25)
ax.plot(angles, behavioral, color="#FF69B4", linewidth=2, label="Comportamentais")
ax.fill(angles, behavioral, color="#FF69B4", alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
st.pyplot(fig)

st.caption("Desenvolvido com ❤️ em Streamlit | © 2025 - Silmar Tolotto")
