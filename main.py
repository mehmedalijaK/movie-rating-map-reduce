import json
from functools import reduce


def load_data(file_path):
    with open(file_path) as my_file:
        return json.load(my_file)


def map_data(user_rating_list):
    return map(lambda value: (value['movie_id'], value['rating'], 1), user_rating_list)


def shuffle_data(movie_rating_list):
    return sorted(movie_rating_list, key=lambda x: x[0])


def reduce_sum(acc, x):
    if acc and acc[-1][0] == x[0]:
        acc[-1] = (acc[-1][0], acc[-1][1] + x[1], acc[-1][2] + 1)
    else:
        acc.append(x)
    return acc


def reduce_data(shuffled_list):
    return reduce(reduce_sum, shuffled_list, [])


def reduce_average(final_data):
    return map(lambda x: ("movie_id " + str(x[0]), round(x[1] / x[2], 2)), final_data)


if __name__ == '__main__':
    data = load_data('sample_data/user_reviews.json')
    mapped_data = map_data(data)
    shuffled_data = shuffle_data(mapped_data)
    reduced_data = reduce_data(shuffled_data)
    average_result = reduce_average(reduced_data)
    print(list(average_result))
