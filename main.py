import numpy
from collections import defaultdict


def get_info_from_file():
    file = open('input.txt')
    lines = [line.rstrip() for line in file]
    print(lines)
    array_of_line = [list(i) for i in lines[1:]]
    print(input)
    width = int(lines[0].split(' ')[0])
    print(width)
    return array_of_line, width


def delete_not_finish_elements(array):
    transposed_array = numpy.transpose(array)
    print(transposed_array[-1:])
    for not_finish_elements in transposed_array[-1:]:
        not_finish_elements[1:-1] = ""
    print(transposed_array)
    return transposed_array


def find_unique_values(array):
    unique_values_array = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            unique_values_array.append((array[i][j]))
    unique_values = list(dict.fromkeys(unique_values_array))
    return unique_values


def find_result(matrix, width, unique_values):
    current_route = defaultdict(list)
    previous_route = defaultdict(list)

    for unique_value in unique_values:
        for b in range(width):
            current_route[unique_value].append(0 * width)
            previous_route[unique_value].append(0 * width)
    print(current_route)
    print(previous_route)

    for i, i_value in enumerate(matrix):
        for j, j_value in enumerate(i_value):
            if not j_value:
                continue
            current_route[j_value][i] += 1

            if i > 0 and j_value != matrix[i - 1][j]:
                previous_route[j_value][i] += 1
                previous_element_in_row = matrix[i - 1][j]
                current_route[j_value][i] *= current_route[previous_element_in_row][i - 1]

        if i == 0:
            continue
        for element in set(i_value):
            print(sum((current_route[element])[:i]))
            if element and sum((current_route[element])[:i]) != 0:
                current_route[element][i] *= sum((current_route[element])[:i])
                current_route[element][i] += previous_route[element][i]
    return current_route


def write_result(routes):
    number_paths = numpy.sum([value[-1] for value in routes.values()])
    print(number_paths)
    f = open('output.txt', 'x')
    f.write(str(number_paths))


if __name__ == "__main__":
    row_array, width = get_info_from_file()

    edited_row_array = delete_not_finish_elements(row_array)

    unique = find_unique_values(edited_row_array)

    paths = dist_for_element(edited_row_array, width, unique)

    write_result(paths)
