from pathlib import Path

base_path = Path(__file__).parent
with open(base_path / "input.txt", "r") as f:
    content = f.read()


def check_marker(content, offset, size=4):
    part = content[offset:offset+size]
    return len(set(part)) == size


def start_of(content, size):
    for index in range(len(content)-size):
        if check_marker(content, index, size):
            return index + size
    return -1


def start_of_packet(content):
    return start_of(content, 4)


def start_of_message(content):
    return start_of(content, 14)


def test_examples():
    contents = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ]

    for content in contents:
        print(f"start-of-packet (after marker): {start_of_packet(content)}")
        print(f"start-of-message (after marker): {start_of_message(content)}")

# test_examples()
print(f"start-of-packet (after marker): {start_of_packet(content)}")
print(f"start-of-message (after marker): {start_of_message(content)}")
