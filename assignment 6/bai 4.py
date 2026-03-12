def word_frequency(text):
    words = text.split()
    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top5 = dict(sorted_words[:5])

    total_words = len(words)
    top_sum = sum(top5.values())

    proportion = top_sum / total_words * 100

    print("Top 5:", top5)
    print("Total words:", total_words)
    print("Proportion:", round(proportion,2), "%")


text = input("Enter text: ")
word_frequency(text)