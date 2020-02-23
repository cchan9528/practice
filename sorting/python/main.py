import os, importlib, random, sys, termcolor

MIN = 1
MAX = 10
LEN = 10
INTSORTS = ['counting', 'radix', 'bucket']
FOCUS = [] # Should be the filename without .py

def main(verbose = False):
    print('\n--------------------------------------------------')
    print('  Running sorting algorithms in sibling files...')
    print('--------------------------------------------------')
    og = None
    randinput  = [
        random.randint(MIN, MAX) for _ in range(random.randint(0, LEN))
    ]
    algorithms = [ os.path.splitext(_)[0] for _ in os.listdir() if '__' not in _
                    and 'main' not in _
                    and 'requirements' not in _]
    record = { 'PASS' : [], 'FAIL' : [], 'SKIP' : []}
    for algorithm in algorithms:
        if len(FOCUS) > 0 and algorithm not in FOCUS:
            continue
        try:
            mysorted = importlib.import_module(algorithm).main
            expect   = sorted(randinput)
            actual   = None
            if algorithm == 'counting':
                actual = mysorted(randinput, MIN, MAX)
            elif algorithm == 'radix':
                og = randinput
                randinput = [
                    random.randint(100, 999)
                        for _ in range(random.randint(0, 10))
                ]
                expect = sorted(randinput)
                actual = mysorted(randinput, base = 10)
            else:
                actual = mysorted(randinput)
            if mysorted.__doc__:
                print('%s' % mysorted.__doc__)
            else:
                print('    %s.py: ' % (str(algorithm)))

            print('\n\tImplementation: ', end='')
            if actual == expect:
                termcolor.cprint(' P A S S ', 'white', 'on_green')
                record['PASS'].append(algorithm)
            else:
                termcolor.cprint(' F A I L ', 'white', 'on_red')
                record['FAIL'].append(algorithm)
            print('\t\tinput: %s' % str(randinput))
            mysorted([_ for _ in randinput], verbose = verbose)
            randinput = og or randinput
            print('\t\tactual: %s' % str(actual))
            print('\t\texpect: %s' % str(expect))
            print()
        except AttributeError as e:
            print('\n    %s.py: ' % (str(algorithm)))
            termcolor.cprint('\n\t S K I P ', 'white', 'on_yellow')
            print('\t%s\n' % str(e))
            record['SKIP'].append(algorithm)
            pass

    print('\n--------------------------------------------------')
    print('            PASS-FAIL-SKIP: %s-%s-%s'
            % (
                str(len(record['PASS'])),
                str(len(record['FAIL'])),
                str(len(record['SKIP']))
            )
    )
    print('                PASS: %s ' % str(record['PASS']))
    print('                FAIL: %s ' % str(record['FAIL']))
    print('                SKIP: %s ' % str(record['SKIP']))
    print('--------------------------------------------------\n')
if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '-v':
        main(verbose = True)
    else:
        main()
