import random
import bisect

class Ant(object):

    def __init__(self, initial_city, fields, alpha, beta):
        self.initial_city = initial_city
        self.fields = fields
        self.alpha = alpha
        self.beta = beta
        self.before_run()

    def before_run(self):
        self.next_city = -1
        self.current_city = self.initial_city
        self.path_len = 0.0
        self.path = []

    def run(self):
        self.before_run()
        available_cities = range(len(self.fields['cities']))
        available_cities.pop(self.initial_city)

        while available_cities:
            self.next_city = self.select_next_city(available_cities)
            self.path.append(self.current_city)
            self.path_len += distance(self.fields[self.current_city], self.fields[self.next_city])
            self.current_city = self.next_city
            available_cities.remove(self.next_city)

        self.path_len += distance(self.fields[current_city], self.fields[initial_city])
        self.path.append(self.current_city)

        return self.path

    def get_path_value(self, current_city, to_city):
        pheromone = self.fields['pheromone'][current_city][to_city]
        distance = distance(self.fields[current_city], self.fields[next_city])
        return pheromone**self.alpha * ((1.0 / distance)**self.beta)

    def cdf(self, weight):
        total = sum(weight)
        cdf_vals = []
        cumulation = 0
        for w in weight:
            cumulation += w
            cdf_vals.append(cumulation / total)
        return cdf_vals

    def select_next_city(self, cities):
        weight = []
        for to in cities:
            weight.append(self.get_path_value(self.current_city, to))
        cdf_vals = self.cdf(weight)
        return cities[bisect.bisect(cdf_vals, random.random())]
