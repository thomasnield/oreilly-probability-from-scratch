from urllib.request import urlopen

# Retrieve golden retriever weights
weights = [float(w) for w in urlopen("https://bit.ly/3cXuufY") \
    .read().decode('utf-8').split("\n") if w]

for w in weights: 
    print(w)

