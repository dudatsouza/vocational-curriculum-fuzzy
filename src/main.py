import pandas as pd
import numpy as np
from fuzzy import fuzzificacao, grau_de_ativacao_dos_antecedentes_de_todas_as_regras, saida_de_cada_uma_das_regras, saida_fuzzificada, defuzzificacao
from plotagem import grafico_pertinencia, grafico_saida_agregada

# Preprocessamento dos dados
def preprocessamento(df, n_cases):
    df = df[['Industry_Feedback_Score', 'Skill_Gap_Index', 'Technology_Integration_Level', 'Recommended_Curriculum_Adjustment_%']]

    # df = df.sample(n=n_cases, random_state=42)

    # selecionar 3 casos específicos para garantir diversidade
    caso_1 = [10, 0.95, 5, 45]
    caso_2 = [50, 0.5, 50, 25]
    caso_3 = [95, 0.1, 95, 5]
    df = pd.DataFrame([caso_1, caso_2, caso_3], columns=['Industry_Feedback_Score', 'Skill_Gap_Index', 'Technology_Integration_Level', 'Recommended_Curriculum_Adjustment_%'])

    return df

def main():
    n_casos = 3
    print("----- ATIVIDADE - SISTEMA FUZZY LINGUÍSTICO ------")
    print(f"Será processado e analisado {n_casos} casos aleatórios do dataset de avaliação de currículos vocacionais, utilizando um sistema fuzzy para fazer a recomendação de ajuste curriculares com base em variáveis de entrada como Industry Feedback Score, Skill Gap Index e Technology Integration Level.\n")

    print("\n------------------------------\n")

    df = pd.read_csv('data/vocational_curriculum_dataset.csv')
    df = preprocessamento(df, n_casos)
    print("Dados pré-processados:")
    print(df)

    print("\n------------------------------\n")

    grafico_pertinencia()
    
    print("Processando os casos selecionados e gerando gráficos de saída agregada para cada caso...")
    for index, row in df.iterrows():
        print(f"Processamento do caso {index + 1}:")
        print(f"{row}\n")
        pertinencia_calculada = fuzzificacao(row)

        conjunto_w = grau_de_ativacao_dos_antecedentes_de_todas_as_regras(pertinencia_calculada)

        universo_saida = np.linspace(0, 50, 500)

        conjunto_y = saida_de_cada_uma_das_regras(conjunto_w, universo_saida)

        y_agregado = saida_fuzzificada(conjunto_y, universo_saida)

        ajuste_recomendado = defuzzificacao(y_agregado, universo_saida)
        
        print(f"-> Ajuste Recomendado para o caso {index + 1}: {ajuste_recomendado:.2f}")

        grafico_saida_agregada(universo_saida, y_agregado, index + 1)

        print("\n------------------------------\n")
    
    print("Processamento concluído. Para ver tudo, suba um pouco os dados do terminal pois pode ter muita informação. Os gráficos de pertinência e saída agregada foram salvos na pasta './data'.")

if __name__ == "__main__":    
    main()