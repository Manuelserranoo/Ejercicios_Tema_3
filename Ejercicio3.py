class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        return f"{self.nombre}: Largo - {self.largo}, Tripulación - {self.tripulacion}, Pasajeros - {self.pasajeros}"

def main():
    naves = [
        Nave("Halcón Milenario", 34.75, 4, 6),
        Nave("Estrella de la Muerte", 160.0, 342, 843342),
        Nave("X-Wing", 12.5, 1, 0),
        Nave("AT-AT", 20.0, 5, 40),
        Nave("AT-ST", 8.6, 2, 0),
        Nave("TIE Fighter", 6.4, 1, 0),
        Nave("TIE Interceptor", 9.6, 1, 0),
        Nave("Naboo Royal Starship", 76.0, 8, 10),
        Nave("Slave I", 21.5, 1, 6),
        Nave("Imperial Shuttle", 20.0, 6, 20),
    ]

    # Listado ordenado por nombre ascendente y largo descendente
    naves_ordenadas = sorted(naves, key=lambda nave: (nave.nombre, -nave.largo))
    for nave in naves_ordenadas:
        print(nave)

    # Información del Halcón Milenario y la Estrella de la Muerte
    halcon_milenario = next(nave for nave in naves if nave.nombre == "Halcón Milenario")
    estrella_muerte = next(nave for nave in naves if nave.nombre == "Estrella de la Muerte")
    print(halcon_milenario)
    print(estrella_muerte)

    # Cinco naves con mayor cantidad de pasajeros
    naves_mayor_pasajeros = sorted(naves, key=lambda nave: nave.pasajeros, reverse=True)[:5]
    for nave in naves_mayor_pasajeros:
        print(nave)

    # Nave con mayor cantidad de tripulación
    nave_mayor_tripulacion = max(naves, key=lambda nave: nave.tripulacion)
    print(nave_mayor_tripulacion)

    # Naves que comienzan con AT
    naves_at = [nave for nave in naves if nave.nombre.startswith("AT")]
    for nave in naves_at:
        print(nave)

    # Naves que pueden llevar seis o más pasajeros
    naves_mayor_seis_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
    for nave in naves_mayor_seis_pasajeros:
        print(nave)

    # Información de la nave más pequeña y más grande
    nave_mas_pequena = min(naves, key=lambda nave: nave.largo)
    nave_mas
