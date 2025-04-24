# 📊 Pipeline de Extração de Dados - Brasileirão Série A

Este pipeline tem como objetivo extrair semanalmente os dados dos times da Série A do Campeonato Brasileiro e gerar um arquivo CSV organizado com todas as movimentações e informações relevantes de cada time.

## ⚙️ Tecnologias Utilizadas

- [Requests](https://pypi.org/project/requests/)
- [Pandas](https://pandas.pydata.org/)
- [API Football-Data.org](https://www.football-data.org/)

> ℹ️ **Observação:** A versão utilizada da API é gratuita. Para obter dados atualizados com maior frequência, é necessário realizar uma assinatura no site da [Football-Data.org](https://www.football-data.org/).

## 🧩 Estrutura do Projeto

O pipeline é dividido em dois scripts principais:

### 1. `extraction.py`

- Realiza a extração completa dos dados da Série A do Brasileirão.
- Os dados são salvos em formato `.json` dentro de um diretório nomeado com a data da extração.

### 2. `transform.py`

- Filtra informações irrelevantes.
- Constrói um `DataFrame` e gera o arquivo final em formato `.csv`.

## 🔐 Configuração da API Key

Para que o pipeline funcione corretamente, é necessário criar um arquivo `.env` chamado `credentials` no diretório onde estão os scripts, contendo a seguinte variável:


## 📅 Frequência de Atualização

- Este pipeline foi projetado para ser executado **semanalmente**.

## 📂 Exemplo de Saída

- `/BSA/2025-04-24-teams.json`
- `/BSA/2025-04-24-teams.csv`

## ✅ Status

✔️ Projeto funcional em desenvolvimento. Ambos scripts estão funcionando.  
🚧 Melhorias futuras: agendamento com Airflow, suporte a outros campeonatos e visualização via dashboards. Também será adicionado uma seção para carregamentos de dados em serviços de Cloud. Provavelmente Amazon Web Services

---

### 🔗 Contato

Criado por [Matheus Volodka](https://github.com/matheusvolodka) – contribuições e sugestões são bem-vindas!

[LinkedIn](https://www.linkedin.com/in/matheusvolodka/)

