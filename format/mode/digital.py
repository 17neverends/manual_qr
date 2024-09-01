from ..data_formatter import DataFormatter


class DigitalFormatter(DataFormatter):
    @staticmethod
    def encode_data(input_data: str) -> str:
        bit_sequence = "0001"

        for i in range(0, len(input_data), 3):
            group = input_data[i:i+3]
            bit_sequence += f"{int(group):0{(len(group) * 3) + 1}b}"

        return bit_sequence
