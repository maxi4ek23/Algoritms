
def get_info_from_file():
    file = open('input.txt')
    line = file.read()
    print(line)
    workers = line.split('\n')[0].split(' ')[0]
    print('Number of workers:', workers)
    beers = line.split('\n')[0].split(' ')[1]
    print('Number of types of beer:', beers)
    answers = line.split('\n')[1].split(' ')
    print('Answers to question "Do u like this types of beer?" Y-Yes or N-No?', answers)
    return workers, beers, answers


def get_one_love_beer(result_of_function, array_of_answers) -> list:
    for all_worker_answers in array_of_answers:
        counter = 0
        for answer in all_worker_answers:
            if answer == 'Y':
                counter += 1
        if counter == 1:
            index_of_current_worker_answers = array_of_answers.index(all_worker_answers)
            print(array_of_answers[index_of_current_worker_answers].index("Y") + 1)
            result_of_function.append(array_of_answers[index_of_current_worker_answers].index('Y') + 1)
            print(result_of_function)
    return result_of_function


def find_all_favourite_beers(answers, workers, beers):
    first_format_data = []
    second_format_data = []
    for i in range(int(workers)):
        helper_array = []
        for j in range(int(beers)):
            if answers[i][j] == "Y":
                helper_array.append((j + 1))
                second_format_data.append(j + 1)
        first_format_data.append(helper_array.copy())
        helper_array.clear()
    print('First format:', first_format_data)
    print('Second format:', second_format_data)
    return first_format_data, second_format_data


def find_if_arrays_have_same_values(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result


# Create new array which include values from first array and get them from second array
def create_union_array(arr1, arr2):
    arr3 = []
    for k in arr2:
        if k in arr1:
            arr3.append(k)
    print(arr3)
    return arr3


def create_eventual_list_of_beers(result_of_function, first_format_data, second_format_data):
    for x in first_format_data:
        if find_if_arrays_have_same_values(result_of_function, x):
            continue
        else:
            union_array = create_union_array(x, second_format_data)
            res = max(set(union_array), key=union_array.count)
            result_of_function.append(res)
    return result_of_function


def get_optimal_amount_of_beers(result_of_function):
    print(len(result_of_function))
    f = open('output.txt', 'x')
    f.write(str(len(result_of_function)))


if __name__ == '__main__':
    results = []

    number_of_workers, number_of_beers, yes_no_elements = get_info_from_file()

    get_one_love_beer(results, yes_no_elements)

    array_of_lovely_beers, lovely_beers_according_to_workers = \
        find_all_favourite_beers(yes_no_elements, number_of_workers, number_of_beers)

    create_eventual_list_of_beers(results, array_of_lovely_beers, lovely_beers_according_to_workers)

    get_optimal_amount_of_beers(results)
