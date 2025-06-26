# ⚖️ Classificador Jurídico v1 — Sistema Inteligente de Classificação de Documentos Jurídicos

## 🧠 Visão Geral

O **Classificador Jurídico v1** é um módulo de inteligência artificial simbólica e baseada em padrões heurísticos que analisa documentos jurídicos e os classifica automaticamente por tipo, subtipo e escore de confiança.

Este sistema foi desenvolvido como parte de uma arquitetura modular de automação jurídica com foco em explicabilidade, integração e aplicabilidade comercial.

---

## 🚀 Funcionalidades

- 🗂️ Identificação do tipo de documento (Contrato, Petição, Edital, Sentença, etc)
- 🧩 Classificação por subtipo (ex: “Petição Inicial”, “Contestação”)
- 🎯 Cálculo de escore de confiança com base em múltiplos padrões
- 📖 Justificativa simbólica da decisão (transparência legal)
- ⚙️ Código limpo, modular e pronto para integração
- 🧪 Testes funcionais incluídos (`teste_classificador.py`)

---

## 📁 Estrutura do Projeto

📁 classificador_juridico_v1/
├── classificador.py              ← Núcleo do classificador
├── teste_classificador.py        ← Script de teste funcional
├── contrato_amostra.txt          ← Documento de teste (exemplo real)
├── Classificador Jurídico v1.pdf ← Relatório técnico da arquitetura

---

## 🛠️ Como usar

1. Instale os requisitos:
pip install -r requirements.txt

2. Execute o classificador com um exemplo:
python teste_classificador.py

3. Saída esperada:
🧠 Tipo detectado: CONTRATO
📂 Subtipo: Contrato de Prestação de Serviços
📊 Confiança: 91%
🧾 Racional: ['objeto', 'cláusula', 'prestação', 'serviços']

---

## 🧠 Estratégia de Classificação

O sistema utiliza uma lógica híbrida entre:

- 🔎 Expressões regulares por padrão jurídico
- 📊 Score heurístico simbólico
- 🧠 Justificativa de decisão (explicabilidade)

Diferente de classificadores baseados apenas em LLMs ou ML, este modelo é:

- 💡 Explicável por design
- ⚡ Leve e rápido
- 🔒 Ideal para ambientes offline ou com restrições de compliance

---

## 🔗 Aplicações

- Triagem de documentos jurídicos em escritórios
- Classificação automatizada de arquivos em massa
- Sistemas de RPA jurídica
- Pré-processamento para motores de IA (ex: CrewAI, LangChain)

---

## 📄 Licença

Distribuído sob a Licença MIT. Veja `LICENSE` para detalhes.

---

## 📬 Contato

Desenvolvido por **Kauan Lunghin**  
📫 Contato comercial: [klunghin@gmail.com]

---

## ⭐️ Contribua ou acompanhe

Este projeto faz parte de um sistema maior de **IA Jurídica Modular**.  
Siga, contribua ou entre em contato para fazer parte das próximas versões.
