def isAlienSorted(words, order):

    if len(words) < 2:
        return True

    d = {c: i for i, c in enumerate(order)}
    d["#"] = -1

    for i in range(1, len(words)):

        word1 = words[i - 1]
        word2 = words[i]

        l1 = len(word1)
        l2 = len(word2)

        if l1 > l2:
            word2 += "#" * (l1 - l2)
        else:
            word1 += "#" * (l2 - l1)

        for j in range(len(word1)):
            if d[word1[j]] > d[word2[j]]:
                return False

    return True


# by https://leetcode.com/problems/verifying-an-alien-dictionary/solutions/1149916/python-short-solution-explained
def isAlienSorted2(words, order):
    ord_d = {l: i for i, l in enumerate(order)}

    for w1, w2 in zip(words, words[1:]):
        for i, j in zip(w1, w2):
            if i != j:
                if ord_d[i] > ord_d[j]:
                    return False
                break
        if w1.startswith(w2) and w1 != w2:
            return False

    return True


print(isAlienSorted2(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
