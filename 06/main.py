from dataclasses import dataclass


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        raw = f.read()
    return raw


def write_file(filename: str, data: str):
    with open(filename, "w") as f:
        f.write(data)


@dataclass
class Signal:
    stream: str
    packet_marker_length: int = 4
    message_marker_length: int = 14

    def chars_until_unique_sequence(self, seq_length: int):
        for index in range(len(self.stream) - seq_length):
            if len(set(self.stream[index:index + seq_length])) == seq_length:
                return index

    def start_of_packet(self) -> int:
        return self.chars_until_unique_sequence(self.packet_marker_length) + self.packet_marker_length

    def start_of_message(self) -> int:
        return self.chars_until_unique_sequence(self.message_marker_length) + self.message_marker_length


def main():
    raw_in = read_file("in.txt")
    signal = Signal(raw_in)
    start_of_packet = signal.start_of_packet()
    write_file("pt1.txt", str(start_of_packet))
    start_of_message = signal.start_of_message()
    write_file("pt2.txt", str(start_of_message))


if __name__ == "__main__":
    main()
