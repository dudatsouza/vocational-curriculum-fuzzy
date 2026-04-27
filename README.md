<h1 align='center'>
  Sistema Fuzzy Linguístico - Análise de Currículos Profissionais
</h1>

<div align='center'>
 
[![Python][Python-badge]][Python-url]
[![IDE][vscode-badge]][vscode-url]
[![macOS][macos-badge]][macos-url]


<b>
  Maria Eduarda Teixeira Souza
</b>

Inteligência Computacional - Prof. Alisson Marques<br>
Engenharia de Computação <br>
CEFET-MG Campus V <br>
2026/1


</div>

## 📚 Visão Geral
Este trabalho é fruto de uma atividade proposta pelo professor Alisson Marques para a disciplina de Inteligência Computacional. Nela foi desenvolvido um sistema de inferência fuzzy do tipo **Mamdani**, contendo 3 variáveis de entrada, cada uma com 3 funções de pertinência e 1 variável de saída. O sistema comtempla todas as estapas fundamentais de um sistema fuzzy baseado em regras: definição ds variáveis  linguísticas, fuzzificação, inferência, agrefação e defuzzificação. 

O problema escolhido para ser resolvido pelo sistema fuzzy foi a análise de currículos profissionais com objetivo de identificar se aquele currículo que está sendo analisado precisa ser adaptado ou não para uma determinada vaga de emprego. A base de dados utilizada foi o arquivo csv **vocational_curriculum_dataset.csv**, fruto de uma pesquisa realizada no Kaggle, que pode ser encontrado aqui: [Kaggle](https://www.kaggle.com/datasets/ziya07/vocational-curriculum-adaptability-dataset). Dentre as 11 colunas que esse arquivo csv possui, apenas as colunas "Industry_Feedback_Score", "Skill_Gap_Index", "Technology_Integration_Level" e "Recommended_Curriculum_Adjustment_ %" foram utilizadas. Sendo as 3 primeiras variáveis de entrada e a última a variável de saída. Porém os três casos de testes foram definidos manualmente, pois a base não possuia dados suficientes para gerar casos extremos e intermediários.

O ´Industry Feedback Score´ representa a média das notas de feedback dadas por indústrias para currículos de alunos de cursos vocacionais ao longo do tempo, tendo seu valor variando de 0 a 100. Já o ´Skill Gap Index´ representa o índice de lacuna de habilidades, que indica o quão atualizadas estão as habilidades ensinadas no currículo em relação às habilidades exigidas pelo mercado de trabalho, seu valor variando de 0 a 1. Por fim, o ´Technology Integration Level´ representa o nível de integração de tecnologia no currículo, tendo seu valor variando de 0 a 100. Para a variável de saída, "Recommended_Curriculum_Adjustment_%", que representa o percentual de ajuste recomendado para o currículo, seu valor variando de 0 a 50.




<details> 
  <summary>
    <b style='font-size: 20px'> 📂 Estrutura do Diretório  </b>
  </summary> 

---

A seguir está a estrutura geral do diretório referente a atividade:

```
├── data
│   ├── pertinencia.png
│   ├── saida_agregada_caso_1.png
│   ├── saida_agregada_caso_2.png
│   ├── saida_agregada_caso_3.png
│   └── vocational_curriculum_dataset.csv
├── README.md
├── requirements.txt
├── documentacao.pdf
└── src
    ├── fuzzy.py
    ├── main.py
    └── plotagem.py
```

</details>

<br>


<details> 
  <summary>
    <b style='font-size: 20px'> 🚀 Execução e Compilação  </b>
  </summary> 

---



### 📥 Clonando o repositório

Primeiro, clone o repositório do projeto:

```bash
git clone https://github.com/dudatsouza/vocational-curriculum-fuzzy.git
cd vocational-curriculum-fuzzy
```

## 🧩 Instalação do Python e bibliotecas necessárias

O projeto utiliza o **Python 3.10+**.
Siga as instruções de acordo com o seu sistema operacional.


1. Garanta que o python esteja instalado na máquina, se não tiver basta rodar o comando abaixo:

### 🔹 **Windows**
```powershell
winget install Python.Python.3.13
```

### 🔹 **Linux (Debian / Ubuntu)**
```powershell
sudo apt install python3.10
```

### 🔹 **macOS**

```powershell
brew install python@3.10
```


2. Instale as bibliotecas necessárias, através do arquivo requirements.txt:

```powershell
pip install -r requirements.txt
```

### ⚠️ Atenção: Instalação com venv
Em algumas situações, principalmente com macOS, o comando acima pode não funcionar corretamente, sendo necessário criar um ambiente virtual e instalar as bibliotecas necessárias, seguindo os passos abaixo. Caso já tenha um ambiente virtual, pode pular para o passo 3:

1. Crie um ambiente virtual:
```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:
```bash
source .venv/bin/activate
```
  
3. Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```



## 🛠️ Compilação e Execução

O processo de compilação e execução é o para todos os sistemas operacionais é feito utilizando o python:

```bash
python3 src/main.py
```

O programa irá executar, analisando três casos de teste pré-definidos e gerando gráficos de pertinência e saída agregada para cada caso.

</details>

<br>

<details> 
  <summary>
    <b style='font-size: 20px'> 📚 Referências Bibliográficas  </b>
  </summary> 

---


1. Ziya. Vocational Curriculum Adaptability Dataset. Kaggle, 2025. Disponível em: https://www.kaggle.com/datasets/ziya07/vocational-curriculum-adaptability-dataset. Acesso em: 26 abr. 2026.

2. SILVA, Alisson Marques da. Inteligência Computacional: Introdução à Lógica Fuzzy. Notas de aula, CEFET-MG Divinópolis, 2023.

3. SILVA, Alisson Marques da. Inteligência Computacional: Conjuntos Fuzzy. Notas de aula, CEFET-MG Divinópolis, 2023.

4. SILVA, Alisson Marques da. Inteligência Computacional: Operações e Relações Fuzzy. Notas de aula, CEFET-MG Divinópolis, 2023.

5. SILVA, Alisson Marques da. Inteligência Computacional: Sistemas de Inferência Fuzzy. Notas de aula, CEFET-MG Divinópolis, 2023.
</details>

<br>


## 📩 Contato

Trabalho desenvolvido pelos seguintes alunos:

<div align="center">

**Maria Eduarda Teixeira Souza**  
*Graduando - 7º Período de Engenharia de Computação @ CEFET-MG*  

[![INSTA](https://img.shields.io/badge/-000?style=flat&logo=instagram&logoColor=red)](https://www.instagram.com/dudat_18)
[![DISCORD](https://img.shields.io/badge/-000?style=flat&logo=discord)](https://discord.com/invite/dudat_18)
[![GMAIL](https://img.shields.io/badge/-000?style=flat&logo=gmail)](dudateixeirasouza@gmail.com)
[![LINKEDIN](https://img.shields.io/badge/In-000?style=flat&logo=linkedin)](https://www.linkedin.com/in/dudatsouza)
[![TELEGRAM](https://img.shields.io/badge/-000?style=flat&logo=telegram&logoColor=blue)](https://t.me/dudat_18)
[![X](https://img.shields.io/badge/-000?style=flat&logo=x)](https://x.com/dudat_18)

</div>



[gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[linkedin-badge]: https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white
[telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white

[linkedin-arthur]: https://www.linkedin.com/in/arthur-s-m/
[gmail-joao]: mailto:joaoteles0505@gmail.com

[gmail-duda]: mailto:dudateixeirasouza@gmail.com
[telegram-duda]: https://t.me/dudat_18
[linkedin-duda]: https://www.linkedin.com/in/dudatsouza/


[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[vscode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[vscode-url]: https://code.visualstudio.com/

[make-badge]: https://img.shields.io/badge/_-MAKEFILE-427819.svg?style=for-the-badge
[make-url]: https://www.gnu.org/software/make/manual/make.html

[linux-badge]: https://img.shields.io/badge/Linux-E34F26?logo=linux&logoColor=black&style=for-the-badge
[Linux-url]: https://www.kernel.org/

[windows-badge]: https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white
[Windows-url]:  https://www.microsoft.com/windows

[macos-badge]: https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white
[macos-url]: https://www.apple.com/macos/
