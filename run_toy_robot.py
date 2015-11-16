import toys
import sys

def main():
    """
    Call ToyRobot class functions from input.txt
    """
    toy_robot = toys.ToyRobot()
    filename = 'input.txt'
    try:
        with open(filename) as f:
            lines = f.readlines()
    except IOError:
        print "%s not found. Exiting" % filename
        sys.exit()

    lines = [line.rstrip() for line in lines]
    for line in lines:
        try:
            print line
            line = line.rstrip().split(' ')
            try:
                command, args = line[0].lower(), line[1].split(',')
                output = getattr(toy_robot, command)(*args)
            except IndexError:
                command = line[0].lower()
                output = getattr(toy_robot, command)()
            if output:
                print output

        except TypeError:
            print "Invalid command syntax"

if __name__ == '__main__':
    main()
