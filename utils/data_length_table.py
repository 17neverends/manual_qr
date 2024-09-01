from enums.decoder_enum import Mode

DATA_LENGTH_FIELD_TABLE = {
    Mode.DIGITAL: [10, 12, 14],
    Mode.ALPHANUMERIC: [9, 11, 13],
    Mode.BYTECODE: [8, 16, 16]
}
