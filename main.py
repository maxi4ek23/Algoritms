
def generate_shift_table(pattern):
    shift_table = {}
    for index in range(0, len(pattern)):
        shift_table[pattern[index]] = max(1, len(pattern) - index - 1)
    return shift_table


def boyer_moore(text, pattern):
    bad_char = generate_shift_table(pattern)
    print(bad_char)
    pattern_size = len(pattern)
    text_iter = len(pattern) - 1
    answer = []
    while text_iter <= len(text) - 1:
        pattern_iter = 0
        while pattern_iter < len(pattern) and pattern[len(pattern) - pattern_iter - 1] == text[text_iter - pattern_iter]:
            pattern_iter += 1
        if pattern_iter == len(pattern):
            index = text_iter - len(pattern) + 1
            answer.append(index)
            print('start index', index, 'to', index + pattern_size - 1)
            text_iter += 1
            continue
        else:
            shift = bad_char.get(text[text_iter + pattern_iter], len(pattern))
            skips = shift - pattern_iter
            if skips == 0:
                skips = 1
            text_iter += skips
    return answer, pattern_size


def write_to_file(end_indexes, file_out, pattern_len):
    file = open(file_out, 'w+')
    try:
        for i in end_indexes:
            file.write("Pattern matched at index {} to {}".format(i, i + pattern_len - 1))
            file.write("\n")
    finally:
        file.close()


worst_case_pattern = 'bbbbbbbbbb'
best_case_pattern = 'riteruisdh'
avg_case_pattern = "kamara"
worst_text = open('worst_case.txt').read()
best_text = open('best_case.txt').read()
avg_text = open('avg_case.txt').read()
# indexes, length = boyer_moore(avg_text, avg_case_pattern)
# write_to_file(indexes, 'avg_result.txt', length)




