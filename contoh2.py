import cv2

# Inisialisasi objek VideoCapture dengan indeks kamera (biasanya 0 untuk kamera utama)
cap = cv2.VideoCapture(1)

# Periksa apakah kamera berhasil diakses
if not cap.isOpened():
    print("Kamera tidak dapat diakses")
    exit()

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Periksa apakah frame berhasil dibaca
    if not ret:
        print("Gagal membuka kamera")
        break

    # Tampilkan frame di jendela
    cv2.imshow("Kamera", frame)

    

# Tutup kamera dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
