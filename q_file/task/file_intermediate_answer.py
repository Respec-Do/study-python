with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()
    temp = []
    for character in content:
        if 'a' <= character <= 'z':
            temp.append(character)
        else:
            temp.append(" ")

    content = "".join(temp)

    words = [
        word
        for word in content.split()
        if len(word) > 1
    ]

    result = {}
    for word in words:
        if result.get(word) is not None:
            result[word] += 1
        else:
            result[word] = 1


    result = {
        word : result[word]
        for word in result
        if result[word] >= 100
    }

    sorted_key = sorted(result, key=result.get, reverse=True)
    for key in sorted_key:
        print(key, result[key])