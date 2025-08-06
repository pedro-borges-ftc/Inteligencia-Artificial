<style>
body {
  background-color: #121212;
  color: #FFFFFF;
  font-family: Consolas, monospace;
}
h1, h2 {
  color: #39FF14;
}
code {
  background-color: #1e1e1e;
  padding: 4px;
  border-radius: 4px;
  color: #00ffff;
}
</style>

# Guia Rápido – Introdução à Inteligência Artificial

## 🤖 O que é Inteligência Artificial?

É o campo da ciência da computação que desenvolve sistemas capazes de simular comportamentos inteligentes humanos, como:
- Tomada de decisão
- Reconhecimento de padrões
- Aprendizado com dados
- Resolução de problemas

---

## 📜 Origem da IA

- O termo "Inteligência Artificial" foi criado em **1956**, na conferência de **Dartmouth**, por **John McCarthy**.
- Na época, o objetivo era criar programas que pudessem "pensar".

---

## 🧠 Categorizações da IA

1. **IA Fraca (ou Estreita)**  
   - Focada em tarefas específicas  
   - Exemplos: assistentes virtuais, filtros de spam, algoritmos de recomendação

2. **IA Forte (ou Geral)**  
   - Capaz de realizar qualquer tarefa cognitiva humana  
   - Ainda é hipotética

3. **IA Superinteligente**  
   - Superaria a inteligência humana em todas as áreas  
   - Discussão teórica e ética

---

## 📊 A importância da análise de dados

- A IA moderna depende de **grandes volumes de dados**
- Com **estatística e programação**, é possível:
  - Extrair padrões
  - Treinar algoritmos
  - Avaliar desempenho
- Python é a linguagem mais usada por oferecer bibliotecas como `pandas`, `numpy`, `scikit-learn` e `matplotlib`

---

## 🧪 Exemplo com Python:

```python
from sklearn.datasets import load_iris
import pandas as pd

# Carrega o dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Mostra estatísticas básicas
print(df.describe())
