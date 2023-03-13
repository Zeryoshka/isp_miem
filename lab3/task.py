import re

def main():
    line = input()
    k = int(input())
    
    line = re.sub(r'[0-9]', '', line)
    line = re.sub(r'(\+{2})|(\*{3})', '?', line)
    print('fixed line:', line)
    
    def is_k_reverso(word):
        return len(word) >= k and word[:k] == word[:k][::-1]
    
    print(' '.join(sorted(filter(is_k_reverso, line.split(' ')), key=len)))


if __name__ == '__main__':
    main()