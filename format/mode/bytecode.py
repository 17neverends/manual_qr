from ..data_formatter import DataFormatter


class BytecodeFormatter(DataFormatter):
    @staticmethod
    def encode_data(input_data: str) -> str:
        byte_sequence = input_data.encode('utf-8')
        bit_sequence = ''.join(f'{byte:08b}' for byte in byte_sequence)
        return bit_sequence
