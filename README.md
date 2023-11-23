## Extrator de Dados Abertos

Projeto para extração de dados abertos do Governo Federal, ao qual objetiva tornar o processo de consulta a informação mais fácil e transparente. Atualmente o Governo Federal disponibiliza diversas fontes de informações no site https://dados.gov.br.


Esse projeto inicialmente visa extrair informações como:

- Gestão de Pessoas (Executivo Federal) - Cargos Vagos e Vacâncias;
- Série Histórica de Preços de Combustíveis e de GLP;
-  Indicadores sobre Educação no Campo;

### Fase atual do projeto

Atualmente está sendo trabalhado no processo de extração de dados de informações de cargos vagos e vacâncias no âmbito do Governo Federal.

### Processo para montar o ambiente de teste

1. Inicialmente é necessário clonar o repositório através do comando abaixo:

```bash
git clone https://github.com/marte2050/extrator-dados-abertos
```

2. Após isso precisamos baixar as depedências necessárias para o projeto. Para esse projeto iremos utilizar o poetry para fazer o controle de dependências.

```bash
poetry install
poetry shell
```

3. Após baixar as depedências já estamos aptos a utilizar o sistema. Até o presente momento está disponível a extração de todas as planilhas no que se refere a cargos no âmbito do Governo Federal com base na data de criação. Para baixar esses arquivos pode ser utilizado o comando abaixo:

```bash
cd extrator_dados_abertoscd
scrapy crawl vagas
```