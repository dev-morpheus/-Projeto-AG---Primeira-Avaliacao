# 📚 Projeto AG - Primeira Avaliação

![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Linguagem Principal](https://img.shields.io/badge/Linguagem-Substituir_Aqui-blue?style=for-the-badge)

## 🎯 Sobre o Projeto

Este repositório contém a entrega da Primeira Avaliação da disciplina de FUNDAMENTOS EM INTELIGÊNCIA ARTIFICIAL. O objetivo principal do projeto é demonstrar de forma prática os conceitos de Algoritmos Genéticos na prática.

## Objetivos

* **[Objetivo 1]:** Implementar 2 algoritmos genéticos para otimização de 2 problemas selecionados do artigo apresentado em sala conforme os slides.
* **[Objetivo 2]:** A entrega deve ser EM PDF contendo a tabela comparativa dos algostimos selecionados e a descrição sucinta dos AGs implementados. 

## 🛠️ Tecnologias Utilizadas

* **[Linguagem]** (Python)
* **[Biblioteca/Framework 1]** (NumPy / Time)

## Descrição dos AGs implementados

**[População]:** Geração de população com 100 indivíduos.
**[Fitness]:** 100 
**[Crossover]:** Aritmético com taxa de 90%, utilizando α=0.8 para dar preferência à carga genética do pai mais apto (Elitismo Local). 
**[Mutação]:** Mutação Gaussiana com Decaimento Linear. Em vez de substituição aleatória, foi adicionado um ruído cuja amplitude (escala) diminui conforme as gerações avançam. Isso permitiu que o Algoritmo Genético escapasse de mínimos locais no início e fizesse um ajuste de precisão no final da busca. 
**[Seleção]:** Torneio binário, para escolha dos pais. 
**[Critérios de Parada]:** 
* Estabilidade de 20 sequenciais; 
* Atinja o ótimo; 
* 1000 gerações;

Representação real direta das funções de Bohachevsky 1 e 2. Sendo o ótimo global 0 
na origem. 
