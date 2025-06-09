# Corrida de Processos — Simulador de Escalonamento de CPU
Este projeto é um minijogo interativo com interface gráfica que simula uma corrida entre processos usando políticas reais de escalonamento de CPU. O objetivo é visualizar de maneira divertida como os algoritmos FIFO e Round Robin funcionam.

## Objetivo
Cada processo é representado por uma barra de progresso que avança conforme o tempo de CPU. A política de escalonamento determina a ordem e a forma como os processos "correm". O processo que terminar primeiro é o vencedor da corrida!

## Conceitos aplicados
Escalonamento de CPU

FIFO (First In, First Out)

Round Robin com quantum

Concorrência com threading

Atualização em tempo real da interface com Tkinter

## Como executar
### Requisitos
Python 3.6 ou superior

Biblioteca padrão (tkinter, threading, random, time)

## Executar o programa
Clone este repositório ou baixe o arquivo .py.

Execute no terminal com:

bash
Copiar
Editar
python corrida_processos.py
## Como funciona
Ao abrir o programa, escolha uma política de escalonamento: FIFO ou Round Robin.

Clique em "iniciar Corrida".

De 3 a 5 processos serão gerados com tempos de CPU aleatórios.

As barras de progresso representam o avanço de cada processo.

O processo que terminar primeiro é declarado vencedor.

## Algoritmos implementados
### FIFO (First In, First Out)
Os processos são executados um por vez, na ordem em que chegam.

Um processo só começa após o anterior terminar.

### Round Robin
Cada processo recebe um tempo de CPU fixo (quantum).

Os processos se revezam até que todos terminem.

## Extras e diversão
Os nomes dos processos são aleatórios (ex: 🐢 Tartaruga, 🐇 Coelho, 🚀 Foguete, 🏎️ Fórmula 1, 🦥 Bicho-Preguiça).

A interface mostra a corrida de forma visual e clara.

Um alerta aparece ao final para indicar o vencedor da corrida!

## Estrutura do código
Processo: classe que representa cada processo com nome, tempo total e progresso.

CorridaDeProcessosApp: classe principal da interface gráfica.

### Funções:

fifo(): executa os processos em ordem.

round_robin(): alterna entre processos com quantum.

atualizar_barras(): atualiza a interface em tempo real.

## Arquivos
corrida_processos.py — Código-fonte do jogo

README.md — Instruções de uso e explicação

## Autor
Luis Arthur Vasconcellos Marciao

## Uso de IA
Usado IA apenas para a parte dos nomes dos processos (ex: 🐢 Tartaruga, 🐇 Coelho, 🚀 Foguete, 🏎️ Fórmula 1, 🦥 Bicho-Preguiça).

