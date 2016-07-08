# play_break.py - play with using try/raise to simulate breaks


class FirstLevelBreak(Exception): pass


class SecondLevelBreak(Exception): pass


class ThirdLevelBreak(Exception): pass


class test_exp_break:
    """
    Test using exceptions to simulate breaks
    """

    @classmethod
    def try_it_out(self, x_limit: int, y_limit: str, z_limit: str):
        x = 0
        y = ''
        z = ''
        try:
            for x in range(1, 10):

                try:
                    for y in 'abcde':

                        try:
                            for z in ('old', 'new', 'borrowed', 'blue'):
                                print(x, y, z)
                                if x == x_limit:
                                    raise FirstLevelBreak
                                elif y == y_limit:
                                    raise SecondLevelBreak
                                elif z == z_limit:
                                    raise ThirdLevelBreak
                                else:
                                    pass
                        except ThirdLevelBreak as z_exp:
                            print('Stopped at z = {} (third level)'.format(z))

                            return

                except SecondLevelBreak as y_exp:
                    print('Stopped at y = {} (second level)'.format(y))
                    return

        except FirstLevelBreak as x_exp:
            print('Stopped at x = {} (first level)'.format(x))
            return


if __name__ == '__main__':
    teb = test_exp_break()
    print("Calling with (11, 'f', 'old')")
    test_exp_break.try_it_out(11, 'f', 'old')

    print("\nCalling with (11, 'b', 'green')")
    test_exp_break.try_it_out(11, 'b', 'green')

    print("\nCalling with (2, 'f', 'green')")
    test_exp_break.try_it_out(2, 'f', 'green')

    print('\nDone')


