# --- Importar --- #
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import base64
from io import BytesIO
import tempfile
import os

# --- Configuração da página --- #
st.set_page_config(
    page_title="Currículo - Silmar Tolotto",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Função para gerar PDF --- #
def generate_pdf():
    # Criar PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Configurar fonte reduzida
    pdf.set_font("Arial", size=8)
    
    # Título principal
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Curriculum Vitae", ln=True, align='C')
    pdf.ln(3)

    # Tentar adicionar a foto no lado direito
    try:
        pdf.image("Silmar1.png", x=150, y=20, w=35)
    except:
        st.sidebar.warning("Foto não encontrada. PDF gerado sem foto.")
    
    # Informações pessoais
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Silmar Tolotto", ln=True)
    pdf.set_font("Arial", size=9)
    pdf.cell(200, 5, txt="E-mail: silmar.tolotto@gmail.com", ln=True)
    pdf.cell(200, 5, txt="Celular: (11) 9 8928-1468", ln=True)
    pdf.cell(200, 5, txt="Endereço: Rua Cajati, 345 Freguesia do Ó - CEP 02729-040  São Paulo - SP", ln=True)
    pdf.cell(200, 5, txt="Nascimento: 09 marco de 1969", ln=True)
    pdf.cell(200, 5, txt="LinkedIn: https://www.linkedin.com/in/silmartolottoa227716", ln=True)
    pdf.ln(5)
    
    # Resumo Profissional
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(200, 8, txt="Resumo Profissional", ln=True)
    pdf.set_font("Arial", size=8)
    pdf.multi_cell(0, 4, txt="Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados. Solida experiencia em gestao de ambientes corporativos e aplicacao de metodologias ageis. Profissional com forte espirito de equipe e foco em inovacao e melhoria continua.")
    pdf.ln(3)
    
    # Formação Acadêmica
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(200, 8, txt="Formacao Academica", ln=True)
    pdf.set_font("Arial", size=8)
    pdf.multi_cell(0, 4, txt="UNINOVE - Universidade Nove de Julho | Administracao de Redes de Computadores e Internet")
    pdf.ln(3)
    
    # Experiência Profissional
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(200, 8, txt="Experiencia Profissional", ln=True)
    pdf.set_font("Arial", size=8)
    
    experiencias = [
        "CONVERSYS IT SOLUTIONS (01/2025 - atual)\n- Analista de Infraestrutura de TI Pleno\n- Gestao de ambientes corporativos complexos\n- Especialista em servidores, redes, virtualizacao\n",
        "Fundo Social SP / Centro Paula Souza (10/2023 - 01/2025)\n- Professor: Administracao, Empreendedorismo, Informatica\n",
        "9NET TI, TELECOM (07/2022 - 10/2023)\n- Gerente de Projetos de infraestrutura de TI\n- Projetos: CIA Matarazzo, ALUBAR, BP Bunge\n- Metodologias ageis, governanca e KPIs\n",
        "TFA Tecnologia (10/2020 - 07/2022)\n- Coordenador de Tecnologia\n- Gestao de equipe com Scrum e Kanban\n- Desenvolvimento de ERP para inventario de TI\n",
        "Sherwin-Williams (05/2014 - 08/2019)\n- Analista de Suporte\n- Implantacao de PABX IP Cisco, rede Wi-Fi\n- Gestao de contas operadoras e equipamentos\n"
    ]
    
    for exp in experiencias:
        pdf.multi_cell(0, 4, txt=exp)
        pdf.ln(1)
    
    # Verificar se precisa de nova página
    if pdf.get_y() > 200:
        pdf.add_page()
        pdf.set_font("Arial", size=8)
    
    # Habilidades
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(200, 8, txt="Habilidades e Competencias", ln=True)
    pdf.set_font("Arial", size=8)
    
    habilidades_tecnicas = "TECNICAS: Excel(95%), Analise BI(85%), AutoCAD(80%), Infraestrutura(90%), Python(85%)"
    habilidades_comportamentais = "COMPORTAMENTAIS: Lideranca(90%), Comunicacao(85%), Proatividade(90%), Pensamento Estrategico(85%), Resiliencia(95%)"
    
    pdf.multi_cell(0, 4, txt=habilidades_tecnicas)
    pdf.multi_cell(0, 4, txt=habilidades_comportamentais)
    pdf.ln(5)
    
    # --- Gerar e adicionar gráfico de radar --- #
    chart_temp_file = None
    try:
        # Criar gráfico de radar compacto
        labels = ["Excel/BI", "AutoCAD", "Infra", "Comun.", "Lider.", "Resil."]
        technical = [95, 80, 90, 0, 0, 0]
        behavioral = [0, 0, 0, 85, 90, 95]

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]
        technical += [technical[0]]
        behavioral += [behavioral[0]]

        fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
        ax.plot(angles, technical, color="#1E90FF", linewidth=1.5, label="Tecnicas")
        ax.fill(angles, technical, color="#1E90FF", alpha=0.25)
        ax.plot(angles, behavioral, color="#FF69B4", linewidth=1.5, label="Comportamentais")
        ax.fill(angles, behavioral, color="#FF69B4", alpha=0.25)

        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=8)
        ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=7)
        
        # Salvar gráfico como imagem temporária
        chart_temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        plt.savefig(chart_temp_file.name, dpi=100, bbox_inches='tight')
        plt.close(fig)  # FECHAR A FIGURA EXPLICITAMENTE
        
        # Adicionar gráfico ao PDF
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(200, 8, txt="Grafico de Competencias", ln=True)
        pdf.image(chart_temp_file.name, x=50, y=pdf.get_y() + 2, w=100)
        pdf.ln(55)
        
    except Exception as e:
        # Em caso de erro, apenas continue sem o gráfico
        pdf.multi_cell(0, 4, txt="Grafico de competencias indisponivel")
    
    finally:
        # Limpar arquivo temporário se existir
        if chart_temp_file and os.path.exists(chart_temp_file.name):
            try:
                os.unlink(chart_temp_file.name)
            except:
                # Se não conseguir excluir, ignore silenciosamente
                pass
    
    # Verificar posição para continuar na mesma página ou ir para próxima
    if pdf.get_y() > 180:
        pdf.add_page()
        pdf.set_font("Arial", size=8)
    else:
        pdf.ln(5)
    
    # Certificações
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(200, 8, txt="Certificacoes e Cursos", ln=True)
    pdf.set_font("Arial", size=8)
    
    certificacoes = [
        "Gestao de Projetos 1-5, LGPD, Fortinet NS1-NS3, ITIL Foundation",
        "Scrum, Lideranca Lean, Python, Data Science, Inteligencia Artificial",
        "Power BI, Crystal Reports, Excel Avancado, AutoCAD, Administracao Financeira"
    ]
    
    for cert in certificacoes:
        pdf.multi_cell(0, 4, txt=cert)
    
    pdf.ln(3)
    
    # Atividades e Voluntariado
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(200, 8, txt="Atividades e Voluntariado", ln=True)
    pdf.set_font("Arial", size=8)
    pdf.multi_cell(0, 4, txt="Desde 2015: Centro Escoteiro Jaragua. Coordenacao de cursos para voluntarios do Estado de SP. Experiencia em projetos sociais e modernizacao de infraestrutura de TI. Implantacao de solucoes Cisco e PoE.")
    
    # Salvar PDF temporariamente
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    
    return temp_file.name

# --- Menu lateral interativo --- #
menu = st.sidebar.selectbox(
    "📂 Navegue pelo Currículo",
    ["Resumo", "Formação", "Experiência Profissional", "Habilidades", "Certificações", "Atividades e Voluntariado"]
)

# --- Informações pessoais na sidebar --- #
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Informações Pessoais")

# Foto na sidebar
st.sidebar.image(
    "Silmar1.png",
    caption="Silmar Tolotto",
    use_container_width=True
)

# Informações de contato
st.sidebar.markdown("**📧 E-mail:** silmar.tolotto@gmail.com")
st.sidebar.markdown("**📱 Celular:** (11) 9 8928-1468")
st.sidebar.markdown("**🎂 Aniversário:** 09 março de 1969")
st.sidebar.markdown("**🏠 Endereço:** Rua Cajati, 345 Freguesia do Ó - CEP 02729-040  São Paulo - SP")
st.sidebar.markdown("**🔗 LinkedIn:** [silmartolottoa227716](https://www.linkedin.com/in/silmartolottoa227716)")

# --- Botão para gerar PDF --- #
st.sidebar.markdown("---")
if st.sidebar.button("📄 Gerar PDF Completo", use_container_width=True):
    with st.spinner("Gerando PDF..."):
        pdf_path = generate_pdf()
        
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        
        # Criar link de download
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Curriculo_Silmar_Tolotto.pdf">⬇️ Clique aqui para baixar o PDF</a>'
        st.sidebar.markdown(href, unsafe_allow_html=True)
        
        # Limpar arquivo temporário
        os.unlink(pdf_path)

# --- Layout principal --- #
st.markdown("# 📄 Curriculum Vitae")
st.markdown("## Silmar Tolotto")
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

# --- Seções --- #
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
    st.header("🧩 Habilidades e Competências")
    st.markdown("Abaixo estão as principais competências técnicas e comportamentais, com níveis de proficiência:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💻 Competências Técnicas")
        skill_bar("📊 Excel Avançado (Dashboards, VBA)", 95, "#2E8B57")
        skill_bar("📈 Análise de Dados e BI", 85, "#4682B4")
        skill_bar("📐 AutoCAD (2D/3D, Plantas e Diagramas)", 80, "#DAA520")
        skill_bar("⚙️ Infraestrutura e Redes", 90, "#4B0082")
        skill_bar("🐍 Python e Automação", 85, "#FF4500")

    with col2:
        st.markdown("### 🤝 Competências Comportamentais")
        skill_bar("👥 Liderança e Trabalho em Equipe", 90, "#3CB371")
        skill_bar("🗣️ Comunicação Assertiva", 85, "#4682B4")
        skill_bar("🚀 Proatividade e Foco em Resultados", 90, "#DA70D6")
        skill_bar("🧠 Pensamento Estratégico", 85, "#6A5ACD")
        skill_bar("🧩 Resiliência e Adaptabilidade", 95, "#008B8B")

    st.markdown("---")

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
    ax.set_xticks(angles[:-1])                 # ← usar apenas os ângulos originais
    ax.set_xticklabels(labels, fontsize=10)    # ← sem duplicar labels
    ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
    st.pyplot(fig)

elif menu == "Certificações":
    st.header("📜 Certificações e Cursos")
    st.markdown("""
    - 🎯 Gestão de Projetos 1 a 5  
    - 🧩 LGPD  
    - 🔒 Fortinet NS1, NS2, NS3  
    - 🧠 ITIL Foundation  
    - ⚡ Scrum e Liderança Lean  
    - 🐍 Python (Básico, Intermediário, Avançado)  
    - 🤖 Data Science e Inteligência Artificial  
    - 📊 Power BI e Crystal Reports  
    - 🧮 Excel Avançado (Dashboards, Fórmulas, Power Query e VBA)  
    - 📐 AutoCAD (2D e 3D, Plantas Técnicas e Layouts Industriais)  
    - 💰 Administração e Planejamento Financeiro  
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
