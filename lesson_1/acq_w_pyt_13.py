import re

while True:
    print("input X")
    X = input()
    match = re.fullmatch(r'-?[1-9]+', X)
    if match: break

while True:
    print("input Y")
    Y = input()
    match = re.fullmatch(r'-?[1-9]+', Y)
    if match: break

if int(X) > 0 and int(Y) > 0: print("1")
if int(X) < 0 and int(Y) > 0: print("2")
if int(X) < 0 and int(Y) < 0: print("3")
if int(X) > 0 and int(Y) < 0: print("4")

