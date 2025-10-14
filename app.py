# --- Importar --- #
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pdfkit
import base64
from io import BytesIO

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
st.sidebar.image("Silmar1.png", caption="Silmar Tolotto", use_container_width=True)
st.sidebar.markdown("📧 silmar.tolotto@gmail.com")
st.sidebar.markdown("📱 (11) 9 8928-1468")
st.sidebar.markdown("🎂 09 março de 1969")
st.sidebar.markdown("🏠 São Paulo, SP")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silmartolottoa227716)")

st.markdown("## 💼 Currículo Profissional")
st.markdown("---")

# --- Função para barra de proficiência personalizada --- #
def skill_bar(skill, percent, color="#4CAF50"):
    bar_html = f"""
    <div style="margin-bottom: 10px;">
        <strong>{skill}</strong>
        <div style="background-color: #ddd; border-radius: 10px; height: 22px; position: relative;">
            <div style="width: {percent}%; background-color: {color}; height: 22px; border-radius: 10px;">
                <span style="position: absolute; right: 8px; color: white; font-weight: bold;">{percent}%</span>
            </div>
        </div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

# --- Função para gerar gráfico de radar como imagem base64 --- #
def radar_chart_base64():
    labels = np.array([
        "Excel / BI", 
        "AutoCAD", 
        "Infraestrutura", 
        "Comunicação", 
        "Liderança", 
        "Resiliência"
    ])
    technical = np.array([95, 80, 90, 0, 0, 0])
    behavioral = np.array([0, 0, 0, 85, 90, 95])
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
    
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

# --- Conteúdo das seções --- #
content_html = ""

if menu == "Resumo":
    st.header("👋🏻 Resumo Profissional")
    st.markdown("""
    Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados.  
    Sólida experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis.  
    Profissional com forte espírito de equipe e foco em inovação e melhoria contínua.
    """)
    content_html += "<h2>Resumo Profissional</h2><p>Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados. Sólida experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis. Profissional com forte espírito de equipe e foco em inovação e melhoria contínua.</p>"

elif menu == "Formação":
    st.header("🎓 Formação Acadêmica")
    st.markdown("**UNINOVE - Universidade Nove de Julho**  \n📘 *Administração de Redes de Computadores e Internet*")
    content_html += "<h2>Formação Acadêmica</h2><p>UNINOVE - Universidade Nove de Julho<br>Administração de Redes de Computadores e Internet</p>"

elif menu == "Habilidades":
    st.header("🧩 Habilidades e Competências")
    st.markdown("Abaixo estão as principais competências técnicas e comportamentais, com níveis de proficiência:")

    col1, col2 = st.columns(2)
    skills_html = "<h2>Habilidades e Competências</h2><table>"
    
    with col1:
        st.markdown("### 💻 Competências Técnicas")
        skill_bar("📊 Excel Avançado (Dashboards, VBA)", 95, "#2E8B57")
        skill_bar("📈 Análise de Dados e BI", 85, "#4682B4")
        skill_bar("📐 AutoCAD (2D/3D, Plantas e Diagramas)", 80, "#DAA520")
        skill_bar("⚙️ Infraestrutura e Redes", 90, "#4B0082")
        skill_bar("🐍 Python e Automação", 85, "#FF4500")
        skills_html += "<tr><td>Excel Avançado (Dashboards, VBA) - 95%</td></tr>"
        skills_html += "<tr><td>Análise de Dados e BI - 85%</td></tr>"
        skills_html += "<tr><td>AutoCAD (2D/3D) - 80%</td></tr>"
        skills_html += "<tr><td>Infraestrutura e Redes - 90%</td></tr>"
        skills_html += "<tr><td>Python e Automação - 85%</td></tr>"

    with col2:
        st.markdown("### 🤝 Competências Comportamentais")
        skill_bar("👥 Liderança e Trabalho em Equipe", 90, "#3CB371")
        skill_bar("🗣️ Comunicação Assertiva", 85, "#4682B4")
        skill_bar("🚀 Proatividade e Foco em Resultados", 90, "#DA70D6")
        skill_bar("🧠 Pensamento Estratégico", 85, "#6A5ACD")
        skill_bar("🧩 Resiliência e Adaptabilidade", 95, "#008B8B")
        skills_html += "<tr><td>Liderança e Trabalho em Equipe - 90%</td></tr>"
        skills_html += "<tr><td>Comunicação Assertiva - 85%</td></tr>"
        skills_html += "<tr><td>Proatividade e Foco em Resultados - 90%</td></tr>"
        skills_html += "<tr><td>Pensamento Estratégico - 85%</td></tr>"
        skills_html += "<tr><td>Resiliência e Adaptabilidade - 95%</td></tr>"

    skills_html += "</table>"
    content_html += skills_html

    st.markdown("---")
    st.subheader("📊 Comparativo de Competências (Radar Chart)")
    img_base64 = radar_chart_base64()
    st.image(f"data:image/png;base64,{img_base64}")
    content_html += f'<h3>Gráfico de Radar</h3><img src="data:image/png;base64,{img_base64}"/>'

# --- Botão para gerar PDF --- #
if st.button("📄 Exportar PDF"):
    pdf_html = f"""
    <html>
    <head>
    <meta charset="utf-8">
    <title>Currículo - Silmar Tolotto</title>
    </head>
    <body>
    <h1>Silmar Tolotto</h1>
    <p>📧 silmar.tolotto@gmail.com</p>
    <p>📱 (11) 9 8928-1468</p>
    {content_html}
    </body>
    </html>
    """
    pdfkit.from_string(pdf_html, "Curriculo_Silmar.pdf")
    st.success("✅ PDF gerado com sucesso! Confira o arquivo Curriculo_Silmar.pdf na pasta do projeto.")
