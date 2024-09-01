from utils.version_category import get_version_category
from utils.get_decoder import get_decoder
from enums.decoder_enum import Mode
from utils.bits_table import MAX_BITS_TABLE
from utils.data_length_table import DATA_LENGTH_FIELD_TABLE


class QRCode:
    def __init__(self, level, input_data, mode):
        self.level = level
        self.input_data = input_data
        self.mode = Mode[mode.upper()]
        self.decoder = get_decoder(self.mode)
        self.data_bits = self.decoder.encode_data(input_data=input_data)
        self.version = self._choose_version()
        self.encoded_data = self._add_service_fields()

    def _choose_version(self):
        data_length = len(self.data_bits)
        for version, max_bits in enumerate(MAX_BITS_TABLE[self.level],
                                           start=1):
            if data_length <= max_bits:
                return version
        raise ValueError("Data too large to encode in any QR code version")

    def _add_service_fields(self):
        version = get_version_category(self.version)
        mode_bits = self._get_mode_bits()
        data_length_bits_len = DATA_LENGTH_FIELD_TABLE[self.mode][version]
        data_length_bits = f"{len(self.input_data):0{data_length_bits_len}b}"

        result_bits = [mode_bits, data_length_bits, self.data_bits]
        return ''.join(result_bits)

    def _get_mode_bits(self):
        return {
            Mode.DIGITAL: '0001',
            Mode.ALPHANUMERIC: '0010',
            Mode.BYTECODE: '0100'
        }[self.mode]

    def _pad_bits(self):
        padded_data = [self.encoded_data]

        padding_needed = len(self.encoded_data) % 8
        if padding_needed != 0:
            padded_data.append('0' * (8 - padding_needed))

        max_bits = MAX_BITS_TABLE[self.level][self.version - 1]

        while len(''.join(padded_data)) < max_bits:
            padded_data.append('11101100')
            if len(''.join(padded_data)) < max_bits:
                padded_data.append('00010001')

        return ''.join(padded_data)[:max_bits]

    def encode(self):
        return self._pad_bits()


# Тестирование
qr = QRCode(level='M', input_data="12345678", mode='digital')
encoded_data = qr.encode()
print(encoded_data)

qr = QRCode(level='M', input_data="HELLO", mode='alphanumeric')
encoded_data = qr.encode()
print(encoded_data)

qr = QRCode(level='M', input_data="Хабр", mode='bytecode')
encoded_data = qr.encode()
print(encoded_data)
