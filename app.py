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
Profissional com mais de 20 anos de experiência em coordenação de infraestrutura de TI e gestão de projetos, liderando equipes técnicas e implementando soluções tecnológicas para otimizar ambientes corporativos complexos. Atuo com foco em alta disponibilidade, segurança da informação, automação e eficiência operacional. Possuo ampla vivência em planejamento estratégico de infraestrutura, administração de servidores, redes, virtualização e governança de processos. Conduziu projetos de modernização de data centers, atualização de equipamentos e redesenho de processos em empresas nacionais e internacionais. Reconhecido pela liderança colaborativa, gestão de riscos e custos, inovação contínua e experiência docente voltada ao desenvolvimento de equipes e disseminação de conhecimento técnico.
FORMAÇÃO ACADÊMICA:
UNINOVE - Universidade Nove de Julho
Administração de Redes de Computadores e Internet

EXPERIÊNCIA PROFISSIONAL:
CONVERSYS IT SOLUTIONS (01/2025 - atual)
•
Responsável pela administração e otimização de ambientes corporativos complexos, garantindo alto desempenho, disponibilidade e segurança das operações de TI.
•
Atuo no gerenciamento de servidores, redes, soluções de virtualização e automação de processos, com foco em eficiência, estabilidade e inovação tecnológica.

Fundo Social do Estado de SP / Centro Paula Souza (10/2023 - 01/2025)
• Professor nas áreas de Administração, Empreendedorismo e Informática
• Atuação no desenvolvimento e condução de aulas voltadas às áreas de Administração, Empreendedorismo e Informática, com foco em promover o aprendizado prático e o pensamento crítico dos alunos.
• Responsável pela elaboração de planos de ensino, aplicação de metodologias ativas e acompanhamento do desempenho estudantil, incentivando o desenvolvimento de competências técnicas e comportamentais voltadas ao mercado de trabalho.

9NET TI, TELECOM E SERVIÇOS (07/2022 - 10/2023)
• Gestão completa da entrega de projetos, abrangendo cronograma, custos, escopo e integração entre equipes;
• Gerenciamento de recursos e definição de métricas de performance;
• Comunicação e governança de projetos, assegurando alinhamento entre áreas e partes interessadas;
• Criação e aplicação de padrões, metodologias e processos para melhoria contínua;
• Análise de riscos, elaboração de planos de mitigação e monitoramento de desempenho;
• Desenvolvimento de relatórios executivos e indicadores de performance (KPIs).
• Principais Projetos e Resultados:
• CIA Matarazzo: Gerenciamento de um complexo composto por shoppings, dois hotéis (SORO e ROSEWOOD) e coworking (AYA). Coordenei equipes multidisciplinares para implantações de plantas CAD, softwares, equipamentos e processos operacionais.
• Alubar: Condução de projeto internacional em Memphis (EUA), além da gestão de firewalls corporativos em localidades como Casa Rosada, Becancour, São Paulo, Coita, Miami, Barcarena e Montenegro.
• BP Bunge: Liderança no refresh de software e equipamentos, garantindo modernização e continuidade operacional com mínimo impacto nos negócios.

TFA Tecnologia (10/2020 - 07/2022)
• Era responsável pela administração e infraestrutura de redes corporativas, abrangendo ambientes WAN, LAN e WLAN, além de servidores virtuais e físicos.
• Atuava no planejamento, implementação e monitoramento de soluções tecnológicas para garantir segurança, estabilidade e performance dos sistemas. Realizava o desenho e implantação de projetos de otimização de
rede e topologias;
• Configuração e análise de regras de firewall e políticas de segurança;
• Administração de servidores Hyper-V, VMware e Senha Segura;
• Gestão de antivírus corporativo, câmeras de monitoramento e suporte técnico (Help Desk);
• Gerenciamento de contratos de software e licenciamento;
• Administração de Windows Server 2008/2012 R2, políticas de backup e armazenamento;
• Gerenciamento do Microsoft 365 e Exchange Online;
• Conhecimento em bancos de dados MySQL e SQL Server;
• Desenvolvimento de sistemas internos e sites utilizando PHP, HTML, CSS e MySQL.

Sherwin-Williams do Brasil (05/2014 - 08/2019)
• Atuei como analista na Sherwin-Williams entre 2013 e 2016, período em que fui promovido ao cargo de coordenador.
• Era responsável pela organização e otimização dos recursos de telefonia móvel e fixa da empresa, com foco em controle de custos, eficiência operacional e padronização de processos.
• Criação de sistema de gestão e relatórios para monitoramento e controle dos gastos com telefonia;
• Redução significativa de custos, diminuindo em um terço as despesas com telefonia móvel;
• Implantação de dispositivos iOS (iPhone e iPad) para diretoria, gerências, coordenadores e equipe comercial;
• Desenvolvimento e aplicação de política corporativa de uso de telefonia móvel e fixa;
• Gerenciamento de equipamentos, manutenção, controle de linhas e acompanhamento de contratos.

Analista de telecomunicações - Anhanguera Educacional
jan/2012 a mar/2013
• Realizava a reestruturação e padronização da infraestrutura de comunicação em 54 unidades da empresa.
• Era responsável pelo planejamento, implantação e manutenção de sistemas de telefonia e cabeamento estruturado, garantindo alta disponibilidade e eficiência operacional.
• Realizava a coordenação de projetos de telefonia móvel e fixa em múltiplas unidades;
• Reestruturação da infraestrutura de rede e cabeamento estruturado;
• Suporte técnico e gestão de contratos de telefonia corporativa;
• Colaboração com equipes multidisciplinares para otimização de processos e redução de custos.

Coordenador de TI - Alpha Cons. Com. Serv. De Telecomunicações LTDA
mar/1998 a jan/2012
• Atuei como analista na Alpha entre 1998 e dezembro de 2000. Após esse período, assumi o cargo de coordenador.
• Participação em projetos com clientes corporativos como Banco Alfa e Banco ING, acompanhando todas as etapas de implantação;
• Desenvolvimento de soluções VOIP, integrando centrais telefônicas de forma eficiente e inovadora.
• Monitoramento de bases de dados para controle e atualização do inventário corporativo;
• Ministração de treinamentos presenciais e capacitação de equipes técnicas;
• Responsável pela obtenção de licenças, certificados e autorizações junto a órgãos reguladores;
• Supervisão de equipe composta por cinco colaboradores, promovendo alinhamento e produtividade;
• Criação de manual de procedimentos e avaliação das necessidades de capacitação, resultando em padronização e melhoria contínua dos processos internos.

INFORMAÇÕES ADICIONAIS
• Fluência Fundamentos da inteligência Artificial - Senac São Paulo, 2025.
• Microsoft Power BI para Data Science - Data Science Academy,2025.
• Fundamentos de Data Science e Inteligência Artificial - Data Science Academy, 2025.
• AI-900 Fundamentos de IA no Azure- Fundação Bradesco, 2025.
• Python Advanced Module, 32- Faculdade de Tecnologia de São Paulo - FATEC-SP-2025.
• SOLUÇÕES DE IA NO GITHUB- Fundação Bradesco, 2025.
• Gestão estratégica de TI- ITIL- Fundação Bradesco, 2017.
• Gestão de Projetos- Fundação Bradesco, 2016.
• Modelagem de dados-- Fundação Bradesco, 2016.
• Inglês Básico.

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
Silmar Tolotto
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

# --- Seções do Menu --- #
if menu == "Resumo":
    st.header("👋🏻 Resumo Profissional")
    st.markdown("""
    **Gerente de Projetos, Professor e Analista de Infraestrutura de TI**, organizado e orientado a resultados.  
    
    **Sólida experiência** em gestão de ambientes corporativos e aplicação de metodologias ágeis.  
    
    **Profissional** Profissional com mais de 20 anos de experiência em coordenação de infraestrutura de TI e gestão de projetos, liderando equipes técnicas e implementando soluções tecnológicas para otimizar ambientes corporativos complexos. Atuo com foco em alta disponibilidade, segurança da informação, automação e eficiência operacional. Possuo ampla vivência em planejamento estratégico de infraestrutura, administração de servidores, redes, virtualização e governança de processos. Conduziu projetos de modernização de data centers, atualização de equipamentos e redesenho de processos em empresas nacionais e internacionais. Reconhecido pela liderança colaborativa, gestão de riscos e custos, inovação contínua e experiência docente voltada ao desenvolvimento de equipes e disseminação de conhecimento técnico..
    
    ### 🎯 Objetivo
    Atuar em posições de liderança e gestão de projetos de TI, contribuindo com minha experiência 
    em infraestrutura, metodologias ágeis e desenvolvimento de equipes de alta performance.
    """)

elif menu == "Formação":
    st.header("🎓 Formação Acadêmica")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        **UNINOVE - Universidade Nove de Julho**  
        📘 *Administração de Redes de Computadores e Internet*
        
        - **Período:** 1998 - 2002
        - **Área de Estudo:** Redes de computadores, infraestrutura de TI, segurança da informação
        - **Projeto Final:** Implementação de rede segura para pequenas empresas
        """)
    
    with col2:
        st.markdown("""
        ### 📚 Cursos Complementares
        - Gestão de Projetos
        - Scrum Master
        - LGPD
        - ITIL Foundation
        """)

elif menu == "Experiência Profissional":
    st.header("💼 Experiência Profissional")

    with st.expander("CONVERSYS IT SOLUTIONS (01/2025 - atual)", expanded=True):
        st.markdown("""
        **Cargo:** Analista de Infraestrutura de TI Pleno
        
        **Principais Responsabilidades:**
        - Responsável pela administração e otimização de ambientes corporativos complexos, garantindo alto desempenho, disponibilidade e segurança das operações de TI.
        • Atuo no gerenciamento de servidores, redes, soluções de virtualização e automação de processos, com foco em eficiência, estabilidade e inovação tecnológica.
        
        **Tecnologias:** VMware, Cisco, Azure, PowerShell, Python
        """)

    with st.expander("Fundo Social do Estado de SP / Centro Paula Souza (10/2023 - 01/2025)"):
        st.markdown("""
        **Cargo:** Professor
        
        **Áreas de Atuação:**
        • Professor nas áreas de Administração, Empreendedorismo e Informática
        • Atuação no desenvolvimento e condução de aulas voltadas às áreas de Administração, Empreendedorismo e Informática, com foco em promover o aprendizado prático e o pensamento crítico dos alunos.
        • Responsável pela elaboração de planos de ensino, aplicação de metodologias ativas e acompanhamento do desempenho estudantil, incentivando o desenvolvimento de competências técnicas e comportamentais voltadas ao mercado de trabalho.
        
        **Atividades:** Desenvolvimento de material didático, ministração de aulas práticas e teóricas
        """)

    with st.expander("9NET TI, TELECOM E SERVIÇOS (07/2022 - 10/2023)"):
        st.markdown("""
        **Cargo:** Gerente de Projetos
        
        • Gestão completa da entrega de projetos, abrangendo cronograma, custos, escopo e integração entre equipes;
        • Gerenciamento de recursos e definição de métricas de performance;
        • Comunicação e governança de projetos, assegurando alinhamento entre áreas e partes interessadas;
        • Criação e aplicação de padrões, metodologias e processos para melhoria contínua;
        • Análise de riscos, elaboração de planos de mitigação e monitoramento de desempenho;
        • Desenvolvimento de relatórios executivos e indicadores de performance (KPIs).
        • Principais Projetos e Resultados:
        • CIA Matarazzo: Gerenciamento de um complexo composto por shoppings, dois hotéis (SORO e ROSEWOOD) e coworking (AYA). Coordenei equipes multidisciplinares para implantações de plantas CAD, softwares, equipamentos e processos operacionais.
        • Alubar: Condução de projeto internacional em Memphis (EUA), além da gestão de firewalls corporativos em localidades como Casa Rosada, Becancour, São Paulo, Coita, Miami, Barcarena e Montenegro.
        • BP Bunge: Liderança no refresh de software e equipamentos, garantindo modernização e continuidade operacional com mínimo impacto nos negócios.
        """)

    with st.expander("TFA Tecnologia (10/2020 - 07/2022)"):
        st.markdown("""
        **Cargo:** Coordenador de Tecnologia
        
        **Principais Conquistas:**
        • Era responsável pela administração e infraestrutura de redes corporativas, abrangendo ambientes WAN, LAN e WLAN, além de servidores virtuais e físicos.
        • Atuava no planejamento, implementação e monitoramento de soluções tecnológicas para garantir segurança, estabilidade e performance dos sistemas. Realizava o desenho e implantação de projetos de otimização de
rede e topologias;
        • Configuração e análise de regras de firewall e políticas de segurança;
        • Administração de servidores Hyper-V, VMware e Senha Segura;
        • Gestão de antivírus corporativo, câmeras de monitoramento e suporte técnico (Help Desk);
        • Gerenciamento de contratos de software e licenciamento;
        • Administração de Windows Server 2008/2012 R2, políticas de backup e armazenamento;
        • Gerenciamento do Microsoft 365 e Exchange Online;
        • Conhecimento em bancos de dados MySQL e SQL Server;
        • Desenvolvimento de sistemas internos e sites utilizando PHP, HTML, CSS e MySQL.
        """)

    with st.expander("Sherwin-Williams do Brasil (05/2014 - 08/2019)"):
        st.markdown("""
        **Cargo:** Analista de Suporte
        
        **Principais Atividades:**
        • Atuei como analista na Sherwin-Williams entre 2013 e 2016, período em que fui promovido ao cargo de coordenador.
        • Era responsável pela organização e otimização dos recursos de telefonia móvel e fixa da empresa, com foco em controle de custos, eficiência operacional e padronização de processos.
        • Criação de sistema de gestão e relatórios para monitoramento e controle dos gastos com telefonia;
        • Redução significativa de custos, diminuindo em um terço as despesas com telefonia móvel;
        • Implantação de dispositivos iOS (iPhone e iPad) para diretoria, gerências, coordenadores e equipe comercial;
        • Desenvolvimento e aplicação de política corporativa de uso de telefonia móvel e fixa;
        • Gerenciamento de equipamentos, manutenção, controle de linhas e acompanhamento de contratos.
        """)
    with st.expander("Anhanguera Educacional 01/2014 - 03/2019)"):
        st.markdown("""
        **Cargo:** Analista de telecomunicações
        
        **Principais Atividades:**
        • Realizava a reestruturação e padronização da infraestrutura de comunicação em 54 unidades da empresa.
        • Era responsável pelo planejamento, implantação e manutenção de sistemas de telefonia e cabeamento estruturado, garantindo alta disponibilidade e eficiência operacional.
        • Realizava a coordenação de projetos de telefonia móvel e fixa em múltiplas unidades;
        • Reestruturação da infraestrutura de rede e cabeamento estruturado;
        • Suporte técnico e gestão de contratos de telefonia corporativa;
        • Colaboração com equipes multidisciplinares para otimização de processos e redução de custos.
        """)

    with st.expander("Alpha Cons. Com. Serv. De Telecomunicações LTDA 03/1998 - 01/2012)"):
        st.markdown("""
        **Cargo:** Analista de telecomunicações
        
        **Principais Atividades:**
        • Atuei como analista na Alpha entre 1998 e dezembro de 2000. Após esse período, assumi o cargo de coordenador.
        • Participação em projetos com clientes corporativos como Banco Alfa e Banco ING, acompanhando todas as etapas de implantação;
        • Desenvolvimento de soluções VOIP, integrando centrais telefônicas de forma eficiente e inovadora.
        • Monitoramento de bases de dados para controle e atualização do inventário corporativo;
        • Ministração de treinamentos presenciais e capacitação de equipes técnicas;
        • Responsável pela obtenção de licenças, certificados e autorizações junto a órgãos reguladores;
        • Supervisão de equipe composta por cinco colaboradores, promovendo alinhamento e produtividade;
        • Criação de manual de procedimentos e avaliação das necessidades de capacitação, resultando em padronização e melhoria contínua dos processos internos.
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Gestão e Metodologias
        - **Gestão de Projetos 1 a 5** - PMI
        - **Scrum Master** - Scrum Alliance
        - **Liderança Lean** - Lean Institute
        - **ITIL Foundation** - AXELOS
        
        ### 🔒 Segurança e LGPD
        - **LGPD** - EXIN
        - **Fortinet NS1, NS2, NS3** - Fortinet
        - **Cybersecurity Fundamentals** - ISC²
        """)
    
    with col2:
        st.markdown("""
        ### 💻 Tecnologia e Desenvolvimento
        - **Python** (Básico, Intermediário, Avançado) - Alura
        - **Data Science e IA** - Data Science Academy
        - **Power BI e Crystal Reports** - Microsoft
        - **Excel Avançado** (Dashboards, Power Query, VBA) - Udemy
        
        ### 🛠️ Ferramentas Especializadas
        - **AutoCAD** (2D e 3D) - Autodesk
        - **Administração Financeira** - FGV
        - **Cloud Computing** - AWS Academy
        """)

elif menu == "Atividades e Voluntariado":
    st.header("🤝 Atividades e Voluntariado")
    
    st.markdown("""
    ### 🏕️ Centro Escoteiro Jaraguá
    **Desde 2015** - *Responsável e Coordenador*
    
    **Principais Atividades:**
    - Coordenação de atividades escoteiras para jovens
    - Instrução de cursos para líderes e voluntários do Estado de SP
    - Organização de acampamentos e eventos comunitários
    - Desenvolvimento de programas educacionais
    
    ### 🔧 Projetos Sociais de TI
    **Experiência** em modernização de infraestrutura de TI para instituições sem fins lucrativos
    
    **Principais Realizações:**
    - Implantação de soluções Cisco e PoE em empresas de grande porte
    - Modernização de laboratórios de informática em escolas públicas
    - Capacitação de jovens em tecnologia
    - Implementação de redes Wi-Fi comunitárias
    
    ### 🎖️ Reconhecimentos
    - **Medalha do Mérito Escoteiro** - 2018
    - **Voluntário Destaque** - Secretaria de Educação do Estado de SP - 2020
    - **Certificado de Agradecimento** - Prefeitura de São Paulo - 2022
    """)

st.markdown("---")
st.caption("Desenvolvido com ❤️ em Streamlit | © 2025 - Silmar Tolotto")
