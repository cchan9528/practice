import os, importlib, random, sys, termcolor

def main(verbose = False):
    print('\n--------------------------------------------------')
    print('  Running sorting algorithms in sibling files...')
    print('--------------------------------------------------')
    randinput  = [random.randint(-10, 10) for _ in range(10)]
    algorithms = [ os.path.splitext(_)[0] for _ in os.listdir() if '__' not in _
                    and  'main' not in _]
    for algorithm in algorithms:
        try:
            mysorted = importlib.import_module(algorithm).main
            expect   = sorted(randinput)
            actual   = mysorted(randinput)
            if mysorted.__doc__:
                print('%s' % mysorted.__doc__)
            else:
                print('    %s.py: ' % (str(algorithm)))

            print('\n\tImplementation: ', end='')
            if actual == expect:
                termcolor.cprint('PASS', 'green')
            else:
                termcolor.cprint('FAIL', 'red')
            print('\t\texpect: %s' % str(expect))
            mysorted(randinput, verbose = verbose)
            print('\t\tactual: %s' % str(actual))
            print()
        except AttributeError as e:
            print('\n    %s.py: ' % (str(algorithm)))
            termcolor.cprint('\n\tSKIPPED', 'yellow')
            print('\t%s\n' % str(e))
            pass


    print('\n--------------------------------------------------\n')
if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '-v':
        main(verbose = True)
    else:
        main()
