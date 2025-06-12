def main():
    valores = list(map(int, input().split()))
    
    ordenados = sorted(valores)

    for v in ordenados:
        print(v)

    print()

    for v in valores:
        print(v)

if __name__ == "__main__":
    main()
