# funcao de preprocessing, onde vamos truncar as colunas, retirar os dados
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definição das regras do sistema 

rules = [
    'Ruim', 'Alto', 'Pouco Integrado', 'Ajuste Alto',
    'Ruim', 'Alto', 'Moderadamente Integrado', 'Ajuste Alto',
    'Ruim', 'Alto', 'Altamente Integrado', 'Ajuste Médio',
    'Ruim', 'Médio', 'Pouco Integrado', 'Ajuste Alto',
    'Ruim', 'Médio', 'Moderadamente Integrado', 'Ajuste Médio',
    'Ruim', 'Médio', 'Altamente Integrado', 'Ajuste Médio',
    'Ruim', 'Baixo', 'Pouco Integrado', 'Ajuste Médio',
    'Ruim', 'Baixo', 'Moderadamente Integrado', 'Ajuste Médio',
    'Ruim', 'Baixo', 'Altamente Integrado', 'Ajuste Baixo',
    'Aceitável', 'Alto', 'Pouco Integrado', 'Ajuste Alto',
    'Aceitável', 'Alto', 'Moderadamente Integrado', 'Ajuste Médio',
    'Aceitável', 'Alto', 'Altamente Integrado', 'Ajuste Médio',
    'Aceitável', 'Médio', 'Pouco Integrado', 'Ajuste Médio',
    'Aceitável', 'Médio', 'Moderadamente Integrado', 'Ajuste Médio',    
    'Aceitável', 'Médio', 'Altamente Integrado', 'Ajuste Baixo',
    'Aceitável', 'Baixo', 'Pouco Integrado', 'Ajuste Médio',
    'Aceitável', 'Baixo', 'Moderadamente Integrado', 'Ajuste Baixo',
    'Aceitável', 'Baixo', 'Altamente Integrado', 'Ajuste Baixo',
    'Excelente', 'Alto', 'Pouco Integrado', 'Ajuste Médio',
    'Excelente', 'Alto', 'Moderadamente Integrado', 'Ajuste Médio',
    'Excelente', 'Alto', 'Altamente Integrado', 'Ajuste Baixo',
    'Excelente', 'Médio', 'Pouco Integrado', 'Ajuste Médio',
    'Excelente', 'Médio', 'Moderadamente Integrado', 'Ajuste Baixo',
    'Excelente', 'Médio', 'Altamente Integrado', 'Ajuste Baixo',
    'Excelente', 'Baixo', 'Pouco Integrado', 'Ajuste Baixo',
    'Excelente', 'Baixo', 'Moderadamente Integrado', 'Ajuste Baixo',
    'Excelente', 'Baixo', 'Altamente Integrado', 'Ajuste Baixo'
]


# Definições, implementações e funções para o sistema de inferência fuzzy

def triangular(x, a, b, c):
    if x < a:
        return 0
    elif a <= x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    else:
        return 0

def fuzzificacao(caso):
    pertinencia_calculada = {
        'Industry_Feedback_Score': {
            'Ruim': triangular(caso['Industry_Feedback_Score'], 0, 0, 35),
            'Aceitável': triangular(caso['Industry_Feedback_Score'], 25, 50, 75),
            'Excelente': triangular(caso['Industry_Feedback_Score'], 70, 100, 100)
        },
        'Skill_Gap_Index': {
            'Baixo': triangular(caso['Skill_Gap_Index'], 0, 0, 0.3),
            'Médio': triangular(caso['Skill_Gap_Index'], 0.2, 0.5, 0.8),
            'Alto': triangular(caso['Skill_Gap_Index'], 0.7, 1, 1)
        },
        'Technology_Integration_Level': {
            'Pouco Integrado': triangular(caso['Technology_Integration_Level'], 0, 0, 25),
            'Moderadamente Integrado': triangular(caso['Technology_Integration_Level'], 20, 50, 80),
            'Altamente Integrado': triangular(caso['Technology_Integration_Level'], 75, 100, 100)
        }
    }
    return pertinencia_calculada

def grau_de_ativacao_dos_antecedentes_de_todas_as_regras(pertinencia_calculada): 
    conjunto_w = []
    for i in range(0, len(rules), 4):
        industry_feedback_score = pertinencia_calculada['Industry_Feedback_Score'][rules[i]]
        skill_gap_index = pertinencia_calculada['Skill_Gap_Index'][rules[i+1]]
        technology_integration_level = pertinencia_calculada['Technology_Integration_Level'][rules[i+2]]
        adjustment = rules[i+3]

        w = min(industry_feedback_score, skill_gap_index, technology_integration_level)

        conjunto_w.append((w, adjustment)) # conjunto de w

    return conjunto_w

def saida_de_cada_uma_das_regras(conjunto_w, universo_saida):
    conjunto_y = []
     
    for w, label in conjunto_w:
        y = np.zeros_like(universo_saida)

        if w > 0: 
            for i in range(len(universo_saida)):
                x = universo_saida[i]

                if label == 'Ajuste Alto':
                    b = triangular(x, 30, 50, 50)
                elif label == 'Ajuste Médio':
                    b = triangular(x, 10, 25, 40)
                elif label == 'Ajuste Baixo':
                    b = triangular(x, 0, 0, 20)

                y[i] = min(w, b)

        conjunto_y.append(y)

    return conjunto_y

def saida_fuzzificada(conjunto_y, universo_saida):
    Y = np.zeros_like(universo_saida)

    for i in range(len(universo_saida)):
        maximo = 0
        for y in conjunto_y:
            maximo = max(maximo, y[i])
        Y[i] = maximo
    return Y

def defuzzificacao(y_agregado, universo_saida):
    numerator = 0
    denominator = 0
    for i in range(len(y_agregado)):
        numerator += y_agregado[i] * universo_saida[i]
        denominator += y_agregado[i]

    if denominator == 0:
        return 0

    return numerator / denominator
