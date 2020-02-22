import os, importlib, random, sys, termcolor

def main(verbose = False):
    print('\n--------------------------------------------------')
    print('  Running sorting algorithms in sibling files...')
    print('--------------------------------------------------')
    randinput  = [random.randint(-10, 10) for _ in range(random.randint(0, 10))]
    algorithms = [ os.path.splitext(_)[0] for _ in os.listdir() if '__' not in _
                    and 'main' not in _
                    and 'requirements' not in _]
    record = { 'PASS' : 0, 'FAIL' : 0, 'SKIP' : 0}
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
                termcolor.cprint(' P A S S ', 'white', 'on_green')
                record['PASS'] += 1
            else:
                termcolor.cprint(' F A I L ', 'white', 'on_red')
                record['FAIL'] += 1
            print('\t\tinput: %s' % str(randinput))
            mysorted([_ for _ in randinput], verbose = verbose)
            print('\t\tactual: %s' % str(actual))
            print('\t\texpect: %s' % str(expect))
            print()
        except AttributeError as e:
            print('\n    %s.py: ' % (str(algorithm)))
            termcolor.cprint('\n\t S K I P ', 'white', 'on_yellow')
            print('\t%s\n' % str(e))
            record['SKIP'] += 1
            pass

    print('\n--------------------------------------------------')
    print('            PASS-FAIL-SKIP: %s-%s-%s'
            % (str(record['PASS']), str(record['FAIL']), str(record['SKIP'])))
    print('--------------------------------------------------\n')
if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '-v':
        main(verbose = True)
    else:
        main()
