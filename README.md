# ChargeGrid – Controle Inteligente de Sessão de Recarga

Projeto desenvolvido para a Sprint 3 de Organização e Arquitetura de Computadores.

O projeto utiliza um **Raspberry Pi Pico** com **MicroPython** para simular o controle inteligente de uma sessão de recarga, considerando a geração e o consumo de energia da residência.

## Funcionamento

O sistema calcula:

**Energia disponível = Geração - Consumo**

A partir do resultado, o sistema define o estado da recarga:

- 🟢 **Verde:** Recarga autorizada
- 🟡 **Amarelo:** Recarga reduzida
- 🔴 **Vermelho:** Recarga bloqueada

O programa também apresenta os valores de geração em **decimal, binário e hexadecimal** no terminal.

## Tecnologias

- Raspberry Pi Pico
- MicroPython
- Wokwi
- LEDs
- Simulação de dados de energia

## Simulação no Wokwi

🔗 **[Acessar projeto no Wokwi](https://wokwi.com/projects/475360710572423169)**

## Objetivo

Demonstrar, de forma prática, a relação entre **entrada de dados, processamento, armazenamento e saída**, aplicando conceitos de Organização e Arquitetura de Computadores.
