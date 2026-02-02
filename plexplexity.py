def perplexity(sentence, prob):
    words = sentence.lower().split()
    N = len(words)
    log_prob = 0

    for w in words:
        log_prob += math.log(prob.get(w, 1e-6))

    return math.exp(-log_prob / N)
