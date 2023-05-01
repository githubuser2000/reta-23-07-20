def filter_pairs(pairs):
    # Eine Funktion, die eine Menge von geordneten Paaren filtert
    result = set()  # Eine leere Menge für das Ergebnis
    for pair in pairs:  # Für jedes Paar in der Eingabemenge
        x, y = pair  # Zerlege das Paar in x und y
        if (
            x % 13 != 0 and y % 14 != 0 and x % 14 != 0 and y % 13 != 0
        ):  # Wenn x nicht durch 13 und y nicht durch 14 teilbar ist
            result.add(pair)  # Füge das Paar zum Ergebnis hinzu
    return result  # Gib das Ergebnis zurück

antiheiler=({(13*n+1,14*n+1) for n in range(9)} | {(13*n-1,14*n-1) for n in range(9)} | {(13*n+1,14*n-1) for n in range(9)} | {(13*n-1,14*n+1) for n in range(9)}) - {(13,element) for row in (range(9),[14]) for element in row} - {(-1,-1), (1,1), (-1, 1), (1,-1)}

antiheiler = list(filter_pairs(antiheiler))
antiheiler.sort()
print(antiheiler)
