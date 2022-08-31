from collections import deque


def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)


if __name__ == '__main__':
    with open('file1.txt') as f:
        for line, prev_lines in search(f, 'python', 3):
            print(prev_lines)
            print(line)
            print('-'*15)
