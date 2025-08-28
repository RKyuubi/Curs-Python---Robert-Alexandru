def fibonacci(n):
    if n <= 0:
        return

    a, b = 0, 1 #acestia sunt primii doi termeni ai sirului
    yield a

    if n > 1:
        yield b

    for _ in range(2,n):
        a, b = b, a + b
        yield b

def fibonacci_fara_generator(n):
    if n <= 0:
        return
    elif n == 1:
        return [0]

    primii_termeni = [0,1]

    while len(primii_termeni) < n:
        urmatorul_termen = primii_termeni[-1] + primii_termeni[-2]
        primii_termeni.append(urmatorul_termen)
    return primii_termeni

if __name__ == "__main__":
    n = int(input("Introduceti numarul de termeni ai sirului Fibonacci:"))
    generator = fibonacci(n)
    for termen in generator:
        print(termen, end=" ")

    sir_fibonacci = fibonacci_fara_generator(n)
    print(f"\n{sir_fibonacci}")


