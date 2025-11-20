def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input("Introduce un número: "))

    if primo(n):
        print("El número es primo.")
    else:
        print("El número no es primo.")


main()