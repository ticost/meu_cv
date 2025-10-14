# --- Importar --- #
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO
import tempfile
import os
from datetime import datetime

# Verificar se fpdf está disponível
try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False
    st.sidebar.error("❌ Biblioteca FPDF não instalada. O PDF será gerado em formato texto.")

# --- Configuração da página --- #
st.set_page_config(
    page_title="Currículo - Silmar Tolotto",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Função para gerar PDF --- #
def generate_pdf():
    if not FPDF_AVAILABLE:
        # Fallback: criar um arquivo de texto com o currículo
        content = """CURRICULUM VITAE - SILMAR TOLOTTO

INFORMAÇÕES PESSOAIS:
E-mail: silmar.tolotto@gmail.com
Celular: (11) 9 8928-1468
Endereço: Rua Cajati, 345 Freguesia do Ó - CEP 02729-040 São Paulo - SP
Nascimento: 09 de março de 1969
LinkedIn: https://www.linkedin.com/in/silmartolottoa227716

RESUMO PROFISSIONAL:
Gerente de Projetos, Professor e Analista de Infraestrutura de TI, organizado e orientado a resultados. 
Sólida experiência em gestão de ambientes corporativos e aplicação de metodologias ágeis. 
Profissional com forte espírito de equipe e foco em inovação e melhoria contínua.

FORMAÇÃO ACADÊMICA:
UNINOVE - Universidade Nove de Julho
Administração de Redes de Computadores e Internet

EXPERIÊNCIA PROFISSIONAL:
CONVERSYS IT SOLUTIONS (01/2025 - atual)
- Analista de Infraestrutura de TI Pleno
- Gestão de ambientes corporativos complexos com foco em desempenho e segurança
- Especialista em servidores, redes, virtualização e automação

Fundo Social do Estado de SP / Centro Paula Souza (10/2023 - 01/2025)
- Professor nas áreas de Administração, Empreendedorismo e Informática

9NET TI, TELECOM E SERVIÇOS (07/2022 - 10/2023)
- Gerente de Projetos: gestão técnica e operacional de infraestrutura de TI
- Projetos: CIA Matarazzo, ALUBAR, BP Bunge
- Aplicação de metodologias ágeis, governança e KPIs

TFA Tecnologia (10/2020 - 07/2022)
- Coordenador de Tecnologia
- Gestão de equipe com Scrum e Kanban
- Desenvolvimento de ERP para inventário de TI

Sherwin-Williams do Brasil (05/2014 - 08/2019)
- Analista de Suporte
- Implantação de PABX IP Cisco, rede Wi-Fi e linhas móveis
- Gestão de contas operadoras e atualização de equipamentos de TI

HABILIDADES E COMPETÊNCIAS:
COMPETÊNCIAS TÉCNICAS:
- Excel Avançado (Dashboards, VBA) - 95%
- Análise de Dados e BI - 85%
- AutoCAD (2D/3D, Plantas e Diagramas) - 80%
- Infraestrutura e Redes - 90%
- Python e Automação - 85%

COMPETÊNCIAS COMPORTAMENTAIS:
- Liderança e Trabalho em Equipe - 90%
- Comunicação Assertiva - 85%
- Proatividade e Foco em Resultados - 90%
- Pensamento Estratégico - 85%
- Resiliência e Adaptabilidade - 95%

CERTIFICAÇÕES E CURSOS:
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

ATIVIDADES E VOLUNTARIADO:
Desde 2015, responsável pelo Centro Escoteiro Jaraguá.
Coordenação e instrução de cursos para líderes e voluntários do Estado de SP.
Experiência em projetos sociais e modernização de infraestrutura de TI.
Implantação de soluções Cisco e PoE em empresas de grande porte.

_________________________________________

São Paulo, 14 de outubro de 2025

Desenvolvido com Streamlit | © 2025 - Silmar Tolotto"""
        
        # Criar arquivo temporário
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8')
        temp_file.write(content)
        temp_file.close()
        
        return temp_file.name
    
    # Se FPDF estiver disponível, usar a versão original com gráficos
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
    pdf.cell(200, 5, txt="Endereco: Rua Cajati, 345 Freguesia do O - Sao Paulo - SP", ln=True)
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
        plt.close(fig)  # Fechar a figura explicitamente
        
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
    
    # --- Data, Local e Assinatura com Imagem --- #
    pdf.ln(15)
    
    # Espaço para a imagem da assinatura
    try:
        # Tentar carregar a imagem da assinatura
        # Nome do arquivo: "assinatura.png" ou "assinatura.jpg"
        assinatura_files = ["assinatura.png", "assinatura.jpg", "assinatura.jpeg", "signature.png"]
        assinatura_encontrada = False
        
        for assinatura_file in assinatura_files:
            try:
                # Adicionar imagem da assinatura (largura 60mm, altura automática)
                pdf.image(assinatura_file, x=20, y=pdf.get_y(), w=60)
                assinatura_encontrada = True
                pdf.ln(25)  # Espaço após a assinatura
                break
            except:
                continue
        
        if not assinatura_encontrada:
            # Se não encontrar imagem da assinatura, usar linha
            pdf.cell(0, 5, txt="_" * 50, ln=True)
            pdf.ln(10)
            
    except Exception as e:
        # Em caso de erro, usar linha padrão
        pdf.cell(0, 5, txt="_" * 50, ln=True)
        pdf.ln(10)
    
    # Nome
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, txt="", ln=True)
    
    # Data e local (atualizada automaticamente)
    data_atual = datetime.now().strftime("%d de %B de %Y")
    # Converter para português
    meses_pt = {
        'January': 'janeiro', 'February': 'fevereiro', 'March': 'março',
        'April': 'abril', 'May': 'maio', 'June': 'junho',
        'July': 'julho', 'August': 'agosto', 'September': 'setembro',
        'October': 'outubro', 'November': 'novembro', 'December': 'dezembro'
    }
    
    for eng, pt in meses_pt.items():
        data_atual = data_atual.replace(eng, pt)
    
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, txt=f"São Paulo, {data_atual}", ln=True)
    
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

# Informações de contato
st.sidebar.markdown("**📧 E-mail:** silmar.tolotto@gmail.com")
st.sidebar.markdown("**📱 Celular:** (11) 9 8928-1468")
st.sidebar.markdown("**🎂 Aniversário:** 09 março de 1969")
st.sidebar.markdown("**🏠 Endereço:** Rua Cajati, 345 Freguesia do Ó - CEP 02729-040  São Paulo - SP")
st.sidebar.markdown("**🔗 LinkedIn:** [silmartolottoa227716](https://www.linkedin.com/in/silmartolottoa227716)")

# --- Botão para gerar PDF --- #
st.sidebar.markdown("---")
if st.sidebar.button("📄 Gerar PDF Completo", use_container_width=True):
    with st.spinner("Gerando arquivo..."):
        file_path = generate_pdf()
        
        with open(file_path, "rb") as f:
            file_bytes = f.read()
        
        # Determinar o tipo de arquivo e extensão
        if file_path.endswith('.pdf'):
            mime_type = "application/pdf"
            file_extension = "pdf"
            download_name = "Curriculo_Silmar_Tolotto.pdf"
            success_message = "✅ PDF gerado com sucesso!"
        else:
            mime_type = "text/plain"
            file_extension = "txt"
            download_name = "Curriculo_Silmar_Tolotto.txt"
            success_message = "📄 Arquivo de texto gerado (PDF não disponível)"
        
        # Criar link de download
        b64 = base64.b64encode(file_bytes).decode()
        href = f'<a href="data:{mime_type};base64,{b64}" download="{download_name}">⬇️ Clique aqui para baixar o {file_extension.upper()}</a>'
        
        st.sidebar.success(success_message)
        st.sidebar.markdown(href, unsafe_allow_html=True)
        
        # Limpar arquivo temporário
        os.unlink(file_path)

# --- Layout principal com foto à direita --- #
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("# 📄 Curriculum Vitae")
    st.markdown("## Silmar Tolotto")
    st.markdown("---")

with col2:
    try:
        st.image(
            "Silmar1.png",
            caption="Silmar Tolotto",
            width=150
        )
    except:
        st.info("📷 Foto não carregada")

# --- Resto do código permanece igual --- #
# ... (função skill_bar e seções do currículo)
