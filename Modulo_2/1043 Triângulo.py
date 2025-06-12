def main():
    A, B, C = map(float, input().split())

    if A < B + C and B < A + C and C < A + B:
        perimetro = A + B + C
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((A + B) * C) / 2
        print(f"Area = {area:.1f}")

if __name__ == "__main__":
    main()
