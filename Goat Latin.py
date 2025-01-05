class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(sentence)):
            if sentence[i][0].lower() in vowels:
                sentence[i] += 'ma' + 'a'*(i+1)
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + 'ma' + 'a'*(i+1)
        return ' '.join(sentence)