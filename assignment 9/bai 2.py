def find_keyword_lines(filename, keyword):
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                result.append(i)
    return result