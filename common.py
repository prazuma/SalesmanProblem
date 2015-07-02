def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_solution(solution):
    return 'index\n' + '\n'.join(map(str, solution))


def print_solution(solution):
    print(format_solution(solution))


def write_solution(solution):
    n = len(solution)
    num_cities = [5, 8, 16, 64, 128, 512, 2048]
    file_name = "solution_yours_" + str(num_cities.index(n)) + ".csv"
    file = open(file_name, "w")
    file.write(format_solution(solution))
    file.close()
