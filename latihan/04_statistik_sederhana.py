
def statistik_sederhana(data):
    nilai_minimum = min(data)
    nilai_maksimum = max(data)
    rata_rata = sum(data) / len(data)

    return nilai_minimum, nilai_maksimum, rata_rata


data = [70, 80, 65, 90, 75]

minimum, maksimum, rata_rata = statistik_sederhana(data)

print("Data:", data)
print("Nilai minimum:", minimum)
print("Nilai maksimum:", maksimum)
print("Rata-rata:", rata_rata)
