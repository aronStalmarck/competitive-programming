braille = {
    "*.....": "1", 
    "*.*...": "2", 
    "**....": "3", 
    "**.*..": "4",
    "*..*..": "5",
    "***...": "6",
    "****..": "7",
    "*.**..": "8",
    ".**...": "9",
    ".***..": "0"
}

back = {d: b for b, d in braille.items()}

def read_num():
    sz = int(input())

    digits = ["" for _ in range(sz)]
    for _ in range(3):
        for i, row in enumerate(input().split()):
            digits[i] += row
    return int("".join([braille[d] for d in digits]))

def print_as_braille(x):
    x = str(x)
    digits = [back[d] for d in x]
    for i in range(0, 6, 2):
        print(" ".join([d[i:i+2] for d in digits]))

print_as_braille(read_num() + read_num())
