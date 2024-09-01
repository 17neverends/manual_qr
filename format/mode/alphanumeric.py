from ..data_formatter import DataFormatter
from utils.char_map import get_char_value


class AlphanumericFormatter(DataFormatter):
    @staticmethod
    def encode_data(input_data: str) -> str:
        bit_sequence = ""

        for i in range(0, len(input_data), 2):
            group = input_data[i:i+2]
            padded_group = group.ljust(2)

            values = [get_char_value(char) for char in padded_group]

            if -1 in values:
                raise ValueError(f"Unknown char in input data at index {i}")

            combined_value = values[0] * 45 + values[1] if len(group) == 2 else values[0]
            bit_sequence += f"{combined_value:011b}" if len(group) == 2 else f"{combined_value:06b}"

        return bit_sequence
