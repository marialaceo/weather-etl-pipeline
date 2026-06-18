# 🌦️ Pipeline ETL de Dados Climáticos

Projeto de Engenharia de Dados desenvolvido para automatizar a coleta, transformação e armazenamento de dados climáticos utilizando Python, Apache Airflow, PostgreSQL e Docker.

## 📌 Visão Geral

Este projeto simula um fluxo real de Engenharia de Dados por meio de uma pipeline ETL completa:

- **Extract:** coleta dados meteorológicos da API OpenWeather.
- **Transform:** realiza limpeza, padronização e enriquecimento dos dados.
- **Load:** persiste os dados processados em um banco PostgreSQL.
- **Orchestration:** agenda e monitora a execução da pipeline utilizando Apache Airflow.

O objetivo é demonstrar boas práticas de ingestão, transformação e armazenamento de dados em um ambiente próximo ao encontrado em projetos corporativos.

---

## 🏗️ Arquitetura da Solução

```text
OpenWeather API
       │
       ▼
   Extract
       │
       ▼
 JSON Bruto
       │
       ▼
 Transform
 (Pandas)
       │
       ▼
 Arquivo Parquet
       │
       ▼
     Load
(PostgreSQL)
       │
       ▼
 Consultas e Análises
```

---

## 🚀 Tecnologias Utilizadas

### Linguagens e Bibliotecas

- Python 3.12
- Pandas
- Requests
- SQLAlchemy
- python-dotenv

### Banco de Dados

- PostgreSQL

### Orquestração

- Apache Airflow

### Infraestrutura

- Docker
- Docker Compose

### Fonte dos Dados

- OpenWeather API

---

## 📂 Estrutura do Projeto

```text
weather-etl-pipeline/
│
├── dags/
│   └── dag_weather_project.py
│
├── src/
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
│
├── data/
│   ├── weather_data.json
│   └── temp_data.parquet
│
├── config/
│   └── .env
│
├── docker-compose.yaml
│
└── README.md
```

---

## ⚙️ Etapas da Pipeline

### 1. Extração de Dados

A pipeline realiza uma requisição para a API OpenWeather e salva a resposta em formato JSON.

**Entrada:**

```text
API OpenWeather
```

**Saída:**

```text
data/weather_data.json
```

---

### 2. Transformação dos Dados

Nesta etapa são realizadas diversas transformações:

- Normalização de estruturas JSON aninhadas
- Expansão dos campos climáticos
- Renomeação de colunas
- Conversão de timestamps para o fuso horário de São Paulo
- Remoção de colunas desnecessárias
- Padronização dos dados para análise

**Saída:**

```text
data/temp_data.parquet
```

---

### 3. Carga dos Dados

Os dados transformados são carregados no PostgreSQL utilizando SQLAlchemy.

Tabela de destino:

```sql
sp_weather
```

Estratégia de carga:

```python
if_exists='append'
```

Dessa forma, cada execução adiciona novos registros ao histórico climático.

---

## 🔄 Orquestração com Airflow

Toda a execução da pipeline é controlada por uma DAG do Apache Airflow.

### DAG

```text
dag-weather-pipeline-project
```

### Fluxo

```text
Extract
   ↓
Transform
   ↓
Load
```

### Agendamento

```cron
0 */1 * * *
```

A pipeline é executada automaticamente a cada hora.

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` dentro da pasta `config`:

```env
API_KEY=SUA_CHAVE_OPENWEATHER

database=weather_data_project
user=dev01
password=SUA_SENHA
```

---

## 🐳 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/marialaceo/weather-etl-pipeline.git
cd weather-etl-pipeline
```

### 2. Subir o ambiente

```bash
docker compose up -d
```

### 3. Acessar o Airflow

```text
http://localhost:8080
```

Credenciais padrão:

```text
Usuário: airflow
Senha: airflow
```

---

## 📊 Dados Coletados

A pipeline captura informações como:

- Temperatura atual
- Sensação térmica
- Temperatura mínima e máxima
- Umidade do ar
- Pressão atmosférica
- Velocidade do vento
- Direção do vento
- Cobertura de nuvens
- Horário do nascer do sol
- Horário do pôr do sol
- Condição climática
- Descrição do clima

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar conceitos fundamentais de Engenharia de Dados:

- Desenvolvimento de pipelines ETL
- Integração com APIs
- Transformação de dados com Pandas
- Persistência em bancos relacionais
- Orquestração com Apache Airflow
- Containerização com Docker
- Gerenciamento de variáveis de ambiente
- Boas práticas de organização de projetos

---

## 🔮 Próximos Passos

Melhorias planejadas para futuras versões:

- Implementação de testes automatizados
- Validação de qualidade dos dados
- Monitoramento e alertas
- Deploy em ambiente cloud (AWS)
- Integração com Data Warehouse
- Dashboard analítico em Power BI ou Amazon QuickSight
- CI/CD com GitHub Actions

---

## 👩‍💻 Autora

**Luiza Vieira - vbluuiza**

Engenheira de Dados | Professora e Criadora de Conteúdo na @Jornada de Dados | D.E creator na @Nekt | Fundadora e CEO do @Dados por Todos | Youtube

Projeto desenvolvido com foco em aprendizado prático de Engenharia de Dados, simulando uma arquitetura ETL utilizada em ambientes corporativos .
