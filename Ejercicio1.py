def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        return 1
    else:
        movimientos = torre_hanoi(n-1, origen, auxiliar, destino)
        movimientos += 1
        movimientos += torre_hanoi(n-1, auxiliar, destino, origen)
        return movimientos

def main():
    n = 74
    origen = "A"
    destino = "C"
    auxiliar = "B"

    movimientos = torre_hanoi(n, origen, destino, auxiliar)

    print("El número total de movimientos necesarios es:", movimientos)

if __name__ == '__main__':
    main()

