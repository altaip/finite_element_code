import numpy as np
from operator import itemgetter, attrgetter


class Nelder:
    def __init__(self, function, tol, *variables):
        o_list = []  # Objective constants
        self.tol = tol
        self.function = function
        for arg in variables:
            o_list.append(arg)
        self.function_iter = np.size(o_list)
        self.o_list = o_list

    def min(self):
        # Guess random start
        guess_vec = np.size(self.o_list)
        guess_vec1 = np.random.random_sample((14,1))
        guess_vec2 = np.random.random((14,1))
        guess_vec3 = np.random.random((14,1))
        func_guess_1 = np.append(guess_vec1,self.function(guess_vec1))
        func_guess_2 = np.append(guess_vec2,self.function(guess_vec2))
        func_guess_3 = np.append(guess_vec3,self.function(guess_vec3))
        func_guess = sorted([func_guess_1, func_guess_2, func_guess_3], key=itemgetter(-1))
        best_of_three = func_guess[0][: len(func_guess[0]) - 1]
        second_best_of_three = func_guess[1][: len(func_guess[1]) - 1]
        worst_of_three = func_guess[2][: len(func_guess[2]) - 1]

        while self.function(best_of_three) - self.function(worst_of_three):
            midpoint = (best_of_three + second_best_of_three) / 2.0
            reflected_point = 2.0 * midpoint - worst_of_three
            midpoint2 = (best_of_three + worst_of_three) / 2.0
            reflected_point2 = 2.0 * midpoint2 - second_best_of_three
            midpoint3 = (second_best_of_three + worst_of_three) / 2.0
            reflected_point3 = 2.0 * midpoint3 - best_of_three

            if self.function(reflected_point) < self.function(worst_of_three):
                expanded_point = 2.0 * reflected_point - midpoint
                a = reflected_point
                while self.function(expanded_point) < self.function(reflected_point):
                    reflected_point = expanded_point
                    a = expanded_point
                    expanded_point = 2.0 * reflected_point - midpoint
                worst_of_three = a
                if self.function(worst_of_three) < self.function(best_of_three):
                    b = best_of_three
                    c = second_best_of_three
                    best_of_three = worst_of_three
                    second_best_of_three = b
                    worst_of_three = c
                elif self.function(second_best_of_three) > self.function(worst_of_three) > self.function(best_of_three):
                    c = second_best_of_three
                    second_best_of_three = worst_of_three
                    worst_of_three = c
                else:
                    continue

            elif self.function(reflected_point2) < self.function(second_best_of_three):
                expanded_point = 2.0 * reflected_point2 - midpoint2
                a = reflected_point2
                while self.function(expanded_point) < self.function(reflected_point2):
                    reflected_point2 = expanded_point
                    a = expanded_point
                    expanded_point = 2.0 * reflected_point2 - midpoint2
                second_best_of_three = a
                if self.function(second_best_of_three) < self.function(best_of_three):
                    b = best_of_three
                    best_of_three = second_best_of_three
                    second_best_of_three = b

            elif self.function(reflected_point3) < self.function(best_of_three):
                expanded_point = 2.0 * reflected_point3 - midpoint3
                while self.function(expanded_point) < self.function(reflected_point3):
                    reflected_point3 = expanded_point
                    expanded_point = 2.0 * reflected_point3 - midpoint3

            else:
                # SHRINK
                worst_of_three = best_of_three + 0.5 * (worst_of_three - best_of_three)
                second_best_of_three = best_of_three + 0.5 * (second_best_of_three - worst_of_three)
        self.o_list.append(best_of_three)
        return self.o_list