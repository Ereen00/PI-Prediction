import math

def generate_digit_sequence(n, filename="complex_digit_sequence.txt"):
    with open(filename, "w") as file:
        for i in range(1, n+1):  # i = 0 için logaritmik terimden kaçınmak için 1'den başlıyoruz
            # Karmaşık fonksiyon:
            digit = (math.sin(i) * i**3 + math.log(i + 1) + math.exp(i % 10) + i**2 + 5 * i) % 10
            digit = int(abs(digit))  # Negatif değerler olmaması için mutlak değer ve tam sayıya çevirme
            file.write(f"{digit}")
    print(f"Dataset '{filename}' created with {n} complex digits.")

# Kullanım
n = 10000000  # Üretilecek rakam sayısı
generate_digit_sequence(n)
