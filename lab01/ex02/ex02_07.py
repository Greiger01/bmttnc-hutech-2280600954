print("nhap van ban (Nhap 'end'de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'end':
        break
    lines.append(line)
print("\nCac dong da nhap sau khi in hoa:")
for line in lines:
    print(line.upper())
    