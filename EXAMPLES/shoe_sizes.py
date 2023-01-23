#
BARLEYCORN = 1 / 3.0
CM_TO_INCH = 2.54
MENS_START_SIZE = 12
WOMENS_START_SIZE = 10.5

LINE_FORMAT = '{:6.1f} {:8.2f} {:8.2f}'
HEADER_FORMAT = '{:>6s} {:>8s} {:^8s}'
HEADINGS = ['Size', 'Inches', 'CM']

SIZE_RANGE = []
for i in range(6, 14):
    SIZE_RANGE.extend([i, i + .5])

def main():
    for heading, flag in [("MEN'S", True), ("WOMEN'S", False)]:
        print(heading)
        print((HEADER_FORMAT.format(*HEADINGS)))  # format expects individual arguments for each placeholder; the asterisk unpacks HEADINGS into individual strings
        for size in SIZE_RANGE:
            lengths = get_length(size, flag)
            print(LINE_FORMAT.format(size, *lengths))

        print()

def get_length(size, mens=True):
    start_size = MENS_START_SIZE if mens else WOMENS_START_SIZE

    inches = start_size - ((start_size - size) * BARLEYCORN)
    cm = inches * CM_TO_INCH
    return inches, cm

if __name__ == '__main__':
    main()
