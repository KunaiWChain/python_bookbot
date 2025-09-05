def get_word_count(filepath):
    num_count = 0
    text = ""
    words = []
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        num_count = len(words)
    result = str(num_count) + " total words"
    return result

def get_letter_count(filepath):
    word_counts = {}
    with open(filepath) as f:
        text = f.read()
        text = text.lower()
    for char in text:
        if char in word_counts:
            word_counts[char] += 1
        else:
            word_counts[char] = 1

    return word_counts


def sort_letter_count(word_counts):
    def sort_on(items):
        return items["amount"]
    
    clean_word_counts = []
    for key, value in word_counts.items():
        key_dict = {'char': key, 'amount': value}
        if key.isalpha():
            clean_word_counts.append(key_dict)
            clean_word_counts.sort(reverse=True, key=sort_on)
    

    return clean_word_counts

