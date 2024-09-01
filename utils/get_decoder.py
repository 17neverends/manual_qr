from enums.decoder_enum import Mode
from format.mode.digital import DigitalFormatter
from format.mode.alphanumeric import AlphanumericFormatter
from format.mode.bytecode import BytecodeFormatter


def get_decoder(mode):
    decoder_map = {
        Mode.DIGITAL: DigitalFormatter,
        Mode.ALPHANUMERIC: AlphanumericFormatter,
        Mode.BYTECODE: BytecodeFormatter
    }
    if mode in decoder_map:
        return decoder_map[mode]
    else:
        raise ValueError("Unknown mode")
