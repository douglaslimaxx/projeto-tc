# Projeto TC

Interface de linha de comando (CLI) para simular autômatos finitos e principais algoritmos existente sobre autômatos.

## Instalação

Este projeto é feito utilizando [Python 3](https://www.python.org/), você precisa tê-lo [instalado](https://www.python.org/downloads/) na sua máquina.

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
