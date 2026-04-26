import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fuzzy import triangular

def grafico_pertinencia():
    universo_industry_feedback_score = np.linspace(0, 100, 500)
    universo_skill_gap_index = np.linspace(0, 1, 500)
    universo_technology_integration_level = np.linspace(0, 100, 500)

    plt.figure(figsize=(15, 10))

    # Gráfico para Industry Feedback Score
    plt.subplot(3, 1, 1)
    plt.plot(universo_industry_feedback_score, [triangular(x, 0, 0, 35) for x in universo_industry_feedback_score], label='Ruim')
    plt.plot(universo_industry_feedback_score, [triangular(x, 25, 50, 75) for x in universo_industry_feedback_score], label='Aceitável')
    plt.plot(universo_industry_feedback_score, [triangular(x, 70, 100, 100) for x in universo_industry_feedback_score], label='Excelente')
    plt.title('Variável Linguística: Industry Feedback Score')
    plt.ylabel('Grau de Pertinência')
    plt.ylim(0, 1.1)
    plt.legend()

    # Gráfico para Skill Gap Index
    plt.subplot(3, 1, 2)
    plt.plot(universo_skill_gap_index, [triangular(x, 0, 0, 0.3) for x in universo_skill_gap_index], label='Baixo')
    plt.plot(universo_skill_gap_index, [triangular(x, 0.3, 0.6, 0.9) for x in universo_skill_gap_index], label='Médio')
    plt.plot(universo_skill_gap_index, [triangular(x, 0.9, 1, 1) for x in universo_skill_gap_index], label='Alto')
    plt.title('Variável Linguística: Skill Gap Index')
    plt.ylabel('Grau de Pertinência')
    plt.ylim(0, 1.1)
    plt.legend()

    # Gráfico para Technology Integration Level
    plt.subplot(3, 1, 3)
    plt.plot(universo_technology_integration_level, [triangular(x, 0, 0, 25) for x in universo_technology_integration_level], label='Pouco Integrado')
    plt.plot(universo_technology_integration_level, [triangular(x, 20, 50, 80) for x in universo_technology_integration_level], label='Moderadamente Integrado')
    plt.plot(universo_technology_integration_level, [triangular(x, 75, 100, 100) for x in universo_technology_integration_level], label='Altamente Integrado')
    plt.title('Variável Linguística: Technology Integration Level')
    plt.xlabel('Nível de Integração Tecnológica')
    plt.ylabel('Grau de Pertinência')
    plt.ylim(0, 1.1)
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'data/pertinencia.png')

def grafico_saida_agregada(universo_saida, y_agregado, caso_idx):
    plt.figure(figsize=(10, 5))
    plt.plot(universo_saida, [triangular(x, 30, 50, 50) for x in universo_saida], label='Ajuste Alto', linestyle='--')
    plt.plot(universo_saida, [triangular(x, 10, 25, 40) for x in universo_saida], label='Ajuste Médio', linestyle='--')
    plt.plot(universo_saida, [triangular(x, 0, 0, 20) for x in universo_saida], label='Ajuste Baixo', linestyle='--')
    plt.plot(universo_saida, y_agregado, color='blue')
    plt.fill_between(universo_saida, 0, y_agregado, color='blue', alpha=0.3, label='Área de Agregação')
    plt.title(f'Gráfico de Saída Agregada - Caso {caso_idx}')
    plt.xlabel('Ajuste Recomendado')
    plt.ylabel('Grau de Pertinência')
    plt.ylim(0, 1.1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'data/saida_agregada_caso_{caso_idx}.png')
