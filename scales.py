from random import randint

class MentalMathGame(object):
    def __init__(self):
        self.points = 0
        self.tries = 0


    def create_problem(self, differ_by_power_10=True):
        found_valid_problem = False

        while not found_valid_problem:
            first_int, first_scale = randint(1, 9), randint(1, 9)

            if differ_by_power_10:
                second_int, second_scale = first_int, randint(1, first_scale)
            else:
                second_int, second_scale = randint(1, first_int), randint(1, first_scale)

            numerator = first_int * 10**first_scale
            denominator = second_int * 10**second_scale

            if self.check_problem(numerator, denominator):
                found_valid_problem = True


        return numerator, denominator, numerator / float(denominator)

    def check_problem(self, numerator, denominator):
        return numerator != denominator and numerator >= denominator

    def ask_question(self):
        num, denom, ans = self.create_problem()

        guess = raw_input(">> %s / %s: " % ("{:,d}".format(num), "{:,d}".format(denom)))

        self.tries += 1

        if float(guess) == float(ans):
            print("Nice work!")
            self.points += 1
            print("%s points, %s tries; %s percent accuracy." % (self.points, self.tries,
                                                                 "{:.1f}%".format(self.points/float(self.tries)*100)))
        else:
            print("Whoops! The correct answer was: %s." % "{:,d}".format(int(ans)))

    def loop(self):
        while True:
            self.ask_question()

if __name__ == "__main__":

    mmg = MentalMathGame()
    mmg.loop()
