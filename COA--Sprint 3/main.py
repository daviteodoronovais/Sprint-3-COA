from machine import Pin
from time import sleep

led_verde = Pin(1, Pin.OUT)
led_amarelo = Pin(5, Pin.OUT)
led_vermelho = Pin(9, Pin.OUT)

def desligar_leds():
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)

def verificar_recarga(geracao, consumo):
    disponivel = geracao - consumo

    desligar_leds()

    if disponivel >= 1000:
        estado = "RECARGA AUTORIZADA"
        led_verde.value(1)

    elif disponivel > 0:
        estado = "RECARGA REDUZIDA"
        led_amarelo.value(1)

    else:
        estado = "RECARGA BLOQUEADA"
        led_vermelho.value(1)

    print("==============================")
    print("GERACAO:", geracao, "W")
    print("CONSUMO:", consumo, "W")
    print("DISPONIVEL:", disponivel, "W")
    print("STATUS:", estado)

    print("Decimal:", geracao)
    print("Binario:", bin(geracao)[2:])
    print("Hexadecimal:", hex(geracao)[2:].upper())

    print("==============================")
    print()

# Situação 1
verificar_recarga(4000, 1500)
sleep(3)

# Situação 2
verificar_recarga(1800, 1500)
sleep(3)

# Situação 3
verificar_recarga(1000, 1800)