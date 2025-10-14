import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==============================
# 🎨 CONFIGURAÇÃO BÁSICA
# ==============================
st.set_page_config(page_title="Currículo Interativo", page_icon="💼", layout="wide")

# ==============================
# 🧑‍💻 CABEÇALHO
# ==============================
st.title("💼 Currículo Interativo - Silmar Tolotto")
st.markdown("---")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
with col2:
    st.markdown("""
    **👤 Nome:** Silmar Tolotto  
    **📍 Localização:** Brasil  
    **📧 E-mail:** silmar.tolotto@email.com  
    **🔗 LinkedIn:** [linkedin.com/in/silmartolotto](https://linkedin.com)  
    **💻 GitHub:** [github.com/silmartolotto](https://github.com)
    """)

st.markdown("---")

# ==============================
# 🧠 SEÇÃO DE HABILIDADES
# ==============================
st.header("🧠 Habilidades Técnicas")

skills = {
    "Python": 95,
    "PHP": 85,
    "MySQL": 90,
    "Linux": 80,
    "Docker": 75,
    "Zabbix": 88,
    "Streamlit": 92
}

for skill, level in skills.items():
    st.write(f"**{skill}** ({level}%)")
    st.progress(level / 100)

st.markdown("---")

# ==============================
# 💬 HABILIDADES COMPORTAMENTAIS
# ==============================
st.header("💬 Competências Comportamentais")

soft_skills = {
    "Comunicação": 90,
    "Trabalho em equipe": 85,
    "Resolução de problemas": 95,
    "Liderança": 80,
    "Adaptabilidade": 88
}

for skill, level in soft_skills.items():
    st.write(f"**{skill}** ({level}%)")
    st.progress(level / 100)

st.markdown("---")

# ==============================
# 📊 GRÁFICO DE RADAR (Técnicas x Comportamentais)
# ==============================
st.header("📊 Comparativo: Técnicas vs Comportamentais")

# Unifica habilidades (média das duas listas)
labels = list(skills.keys() | soft_skills.keys())
labels = list(set(list(skills.keys()) + list(soft_skills.keys())))

# Ajusta tamanhos iguais
tamanho = max(len(skills), len(soft_skills))
tech_values = list(skills.values()) + [0]*(tamanho - len(skills))
soft_values = list(soft_skills.values()) + [0]*(tamanho - len(soft_skills))

angles = np.linspace(0, 2*np.pi, tamanho, endpoint=False).tolist()
tech_values += tech_values[:1]
soft_values += soft_values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.plot(angles, tech_values, color='blue', linewidth=2, label='Técnicas')
ax.fill(angles, tech_values, color='blue', alpha=0.25)

ax.plot(angles, soft_values, color='green', linewidth=2, label='Comportamentais')
ax.fill(angles, soft_values, color='green', alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(list(skills.keys()))
ax.set_yticklabels([])
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

st.pyplot(fig)

st.markdown("---")

# ==============================
# 🏆 EXPERIÊNCIA PROFISSIONAL
# ==============================
st.header("🏆 Experiência Profissional")

st.subheader("🔹 Analista de Sistemas - Empresa X (2020 - Atual)")
st.write("""
- Implementação e manutenção de sistemas de monitoramento com **Zabbix**.  
- Desenvolvimento de **chatbots de Service Desk** integrados a **Telegram e Gmail**.  
- Criação de dashboards interativos com **Python, Streamlit e MariaDB**.
""")

st.subheader("🔹 Desenvolvedor PHP - Empresa Y (2017 - 2020)")
st.write("""
- Criação de sistemas internos de cadastro e relatórios com **PHP e Bootstrap**.  
- Integração com APIs e controle de acesso por departamentos.
""")

st.markdown("---")

# ==============================
# 🎓 FORMAÇÃO
# ==============================
st.header("🎓 Formação Acadêmica")
st.write("""
**Engenharia de Software - Universidade Federal XYZ**  
(Concluído em 2018)
""")

st.markdown("---")

# ==============================
# 📫 CONTATO
# ==============================
st.header("📫 Contato")
st.write("Sinta-se à vontade para entrar em contato via e-mail ou LinkedIn para colaborações e oportunidades!")

st.success("📧 silmar.tolotto@email.com")
st.info("🔗 [LinkedIn](https://linkedin.com/in/silmartolotto)")

