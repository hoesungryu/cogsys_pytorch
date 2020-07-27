#lec_03 answer
# Q1. 
def volume(r):
    return 4 / 3 * math.pi * r ** 3

def surface_area(r):
    return 4 * math.pi * r ** 2

def density(r, m=0.35):
    return m / volume(r)

print(volume(0.69))
print(surface_area(0.4))
print(density(0.3))
print(density(0.25, m=2.0))


# Q2.
def quadratic(a, b, c):
    x0 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x0, x1

print(quadratic(3.3, 1.7, -9.4))


# Q3. 
def ch_bin(word):
    word = word.strip().replace(' ','').lower()
    word_dict = dict()
    for c in word:
        word_dict[c] = word.count(c)
    return word_dict

for word in words:
    print(("{word:<%d} : "%maxlen).format(word=word),ch_bin(word))