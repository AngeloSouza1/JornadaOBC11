def sequencia_dos_anciaos(n, a, b):
    """
    Retorna o n-ésimo número da sequência dos anciãos começando com a dupla (a, b).

    Args:
        n (int): Posição desejada na sequência.
        a (int): Primeiro número da sequência.
        b (int): Segundo número da sequência.

    Returns:
        int: O n-ésimo número da sequência.
    """
    if n == 1:
        return a
    elif n == 2:
        return b

    # Inicializando a sequência com os dois primeiros números
    sequencia = [a, b]

    # Gerando a sequência até a posição n
    for i in range(2, n):
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)

    return sequencia[-1]
