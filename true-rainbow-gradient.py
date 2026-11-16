codes = ["0, 0, 0"]

for r in range(1, 256):
    for g in range(256):
        for b in range(256):
            codes.append("{},{},{}".format(r, g, b))

    print("{} / 255".format(r))

code = " ".join(codes)

print("done:")
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(code)
