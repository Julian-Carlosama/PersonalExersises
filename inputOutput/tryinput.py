#!/usr/bin/env python3

print("Type integers, each followed by Enter; o just Enter to finist")

total = 0
count = 0

while True:
    line = input("Please add a number integer: ")
    if line:
        try:
            number = int(line)
        except (ValueError):
            print("Hay errores")
            continue
        total += number
        count += 1
    else:
        break
    if count:
        print("Count = ", count, "Total = ", total, "mean = ", total / count)
