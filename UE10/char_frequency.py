import matplotlib.pyplot as plt

def read_text(path):
    with open(path, "r") as f:
        return f.read()

def char_counts(text):
    d = {}
    for ch in text:
        d[ch] = d.get(ch, 0) + 1
    return list(d.keys()), list(d.values())

def safe_label(ch):
    if ch.isprintable() and not ch.isspace():
        return ch
    return ch.encode("unicode_escape").decode()

def plot_char_freq(chars, freqs, figsize=(12, 6)):
    plt.figure(figsize=figsize)
    x = range(len(chars))
    plt.bar(x, freqs)
    labels = [safe_label(ch) for ch in chars]
    plt.xticks(x, labels, rotation=90, fontsize=8)
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Character frequencies")
    plt.tight_layout()
    plt.show()

text = read_text("data/data.txt")
chars, freqs = char_counts(text)
print(f"Unique characters: {len(chars)}")
plot_char_freq(chars, freqs)