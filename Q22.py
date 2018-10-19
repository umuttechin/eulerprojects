from string import ascii_uppercase
def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))

if __name__ == "__main__":
    names = sorted(open("name.txt").read().split(","))
    print(sum(ix*score(ax) for ix, ax in enumerate(names,1)))
