# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):

    segments.sort(key=lambda x:x[1])
    result = [segments[0][1]]
    prev = segments[0][1]
    for i in range(1, len(segments)):

        if (segments[i][0] > prev):
            result.append(segments[i][1])
            prev = result[-1]

    return result


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
