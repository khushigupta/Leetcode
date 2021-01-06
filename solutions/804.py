from collections import defaultdict


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letters = list('abcdefghijklmnopqrstuvwxyz')
        letter_to_morse = dict()
        for i, l in enumerate(letters):
            letter_to_morse[l] = morse_code[i]

        unique_dict = defaultdict(int)
        for word in words:
            word_letters = list(word)
            morse_string = ''.join([letter_to_morse[l] for l in word_letters])
            unique_dict[morse_string] += 1
        return len(unique_dict.keys())




