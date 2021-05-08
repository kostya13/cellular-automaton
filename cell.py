"Примитивный клеточный автомат"


WIDTH = 140
LIFE_TIME = 100
DOT = '█'
SPACE = ' '

ID = 30


def make_mapping(map_id):
    def bin2str(num, width):
        return bin(num)[2:].zfill(width)

    keys = (bin2str(i, 3) for i in range(8))
    vals = (int(i) for i in reversed(bin2str(map_id, 8)))
    return dict(zip(keys, vals))


def middle(width):
    line = [0] * width
    mid = len(line) // 2
    line[mid] = 1
    return line


def init(method, width):
    return method(width)


def draw(line):
    printable = (DOT if e else SPACE for e in line)
    print(*printable, sep='')


def iter_state(field):
    f_len = len(field)
    for i in range(f_len):
        left = (i - 1) % f_len
        midlle = i
        right = (i + 1) % f_len
        values = (field[i] for i in (left, midlle, right))
        yield '{}{}{}'.format(*values)


def new_generation(gen_map, field): 
    return [gen_map[state] for state in iter_state(field)]

        
def run():
    gen_map = make_mapping(ID)
    field = init(middle, WIDTH)
    for g in range(LIFE_TIME):
        draw(field)
        field = new_generation(gen_map, field)


if __name__ == '__main__':
    run()