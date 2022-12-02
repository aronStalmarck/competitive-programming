seq = input()
n = len(seq)

strs = []

def make_strs(s, i):
    if i < 0:
        strs.append(s)
        return
    if seq[i] == "0":
        make_strs(s + [str(int(seq[i-1] + seq[i]))], i - 2)
    else:
        make_strs(s + [seq[i]], i - 1)
    if i < n - 1 and seq[i] in ("1", "2"):
        make_strs(s[:-1] + [str(int(seq[i] + seq[i+1]))], i - 2)

make_strs([], n-1)

strs = set([tuple(reversed(s)) for s in strs])

print(len(strs))