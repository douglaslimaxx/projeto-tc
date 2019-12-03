# Projeto TC

Interface de linha de comando (CLI) para simular autômatos finitos e principais algoritmos existente sobre autômatos. O projeto foi feito em python 2.7.

## Funcionamento

Escolha o arquivo que você quer executar 

Rode o comando no terminal:

verificador
```zsh
python src/verificador.py <automato> <entrada>
```

conversor
```zsh
python src/conversor.py <automato> 
```

operações
```zsh
python src/<operacao>.py <automato> <automato>
```

obs: se a operação for a estrela ou complemento o CLI só leva um automato.

Onde `<entrada>` é uma palavra qualquer usando o alfabeto {0, 1}. Essa entrada por enquanto não é utilizada e `data/exemplo.txt` é o caminho para o arquivo que contém o autômato.

## Diretórios do projeto

A pasta `src/` tem todo o código referente ao projeto.

Em `src/classes` estão todas as classes utilizadas como modelo.
