#Percobaan 3 : Membalikan Kata/Kalimat (Stack)

def reverse_sentence(sentence) :
    stack = []
    reversed_sentence = ""

    for word in sentence.split():
        stack.append(word)
    while len(stack)>0:
        reverse_sentence += stack.pop() + ""
    return reversed_sentence.strip()

sentence = "Selamat pagi,bagaimana kabarnya hari ini ?"
print(reverse_sentence(sentence))