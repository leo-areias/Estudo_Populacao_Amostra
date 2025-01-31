# **Estudo de População, Amostragem e Viés**

## 📌 **Descrição**
Este estudo explora conceitos fundamentais de estatística, incluindo **população, amostragem e viés**, utilizando **Python** para simular diferentes métodos de amostragem e analisar seus impactos na precisão dos dados.

## 🔍 **Objetivo**
- Gerar **amostras aleatórias** e **amostras estratificadas** a partir de uma população pré-definida.
- Comparar os métodos e identificar possíveis **viéses estatísticos**.
- Demonstrar como a **escolha da amostragem** pode afetar a representatividade dos dados.

---

## 📊 **Metodologia**
1. **Definição da População**  
   - A população é representada por uma lista de valores numéricos variando de **0.0 a 10.0**.
  
2. **Amostragem Aleatória Simples**  
   - Seleciona uma amostra de **50% da população** de maneira completamente **aleatória**.

3. **Amostragem Estratificada**  
   - Divide a população em **dois grupos**:
     - **1 a 5** (valores menores ou iguais a 5.0).
     - **5.1 a 10** (valores maiores que 5.0).
   - Dentro de cada grupo, uma amostragem aleatória é aplicada, garantindo uma **representação proporcional**.

4. **Cálculo do Viés**  
   - Compara a **média da população** com a **média da amostra** para avaliar se há **desvio significativo**.

---

## ⚙️ **Execução do Código**
O código implementa as seguintes funções:

- **`amostra_aleatoria(populacao)`**  
  -> Retorna uma amostra aleatória de **50%** da população.

- **`amostra_estratificada(populacao)`**  
  -> Divide a população em **dois estratos** e seleciona uma amostra proporcional de cada um.

- **`verifica_vies(populacao, amostra)`**  
  -> Calcula e retorna o **viés estatístico**, comparando a média da amostra com a média da população.

---

## 📈 **Resultados**
O código imprime os seguintes resultados:
1. **Amostra Aleatória Selecionada**
2. **Amostra Estratificada Selecionada**
3. **Cálculo do Viés**
   - O viés indica **se a amostra representa bem a população** ou se há distorções nos dados coletados.

---

## 🔥 **Principais Aprendizados**
✅ **Amostragem Aleatória** pode levar a uma distribuição não homogênea da amostra, resultando em viés.  
✅ **Amostragem Estratificada** melhora a representatividade dos dados, reduzindo o viés quando há grupos distintos na população.  
✅ A comparação entre **médias da população e da amostra** é essencial para avaliar a precisão estatística.  

---

## 🚀 **Possíveis Melhorias**
- Implementar **tamanhos de amostra variáveis** para observar mudanças no viés.
- Testar diferentes **estratégias de estratificação** (ex.: mais de dois grupos).
- Aplicar **métodos estatísticos mais avançados** para medir a variabilidade das amostras.

---

📝 **Conclusão:** Este estudo reforça a importância da escolha correta da técnica de amostragem e como um método inadequado pode gerar um viés significativo nos resultados.
