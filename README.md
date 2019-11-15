# Projeto TC

Interface de linha de comando (CLI) para simular autômatos finitos e principais algoritmos existente sobre autômatos.

## Testando o importador de autômato
Rode o comando no terminal:

```bash
python src/index.py data/exemplo.txt <entrada>
```

Onde `<entrada>` é uma palavra qualquer usando o alfabeto {0, 1}. Essa entrada por enquanto não é utilizada.

## Diretórios do projeto

A pasta `project/` tem todo o código referente ao projeto.

Dentro de `project/`, temos a pasta `comands/`, que contém o código todos os comandos e as funções executadas pelos mesmos.

Também dentro de `project/`, temos a pasta `utils/`, que contém funções utilitárias que podem ser reaproveitadas em mais de um contexto.

## Instalação

Este projeto é feito utilizando [Python 3](https://www.python.org/), você precisa tê-lo [instalado](https://www.python.org/downloads/) na sua máquina.

Além disso, o projeto também se utiliza do pacote *Click* ([ver documentação](https://click.palletsprojects.com/en/7.x/)), para facilitar a construção de uma CLI usando Python.

### Configuração do projeto

``` bash
# instalando o pipenv
pip install --user pipenv
```

### Configurando o projeto

``` bash
# clonando o repositório
git clone https://github.com/douglaslimaxx/projeto-tc.git
cd projeto-tc

# instalando as dependências
pipenv install

# rodar programa (será exibida uma tela de HELP, pois nenhum argumento foi dado para a CLI)
pipenv run start
```

Para saber os comandos disponíveis pela CLI, você pode acessar a pasta `project/commands` e olhar os comandos disponíveis, assim como o que recebe de argumentos. Para rodar, basta executar da seguinte maneira:

```bash
# executando o script de inicialização com algum comando sendo executado
pipenv run start [COMANDO]
```
