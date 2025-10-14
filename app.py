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
