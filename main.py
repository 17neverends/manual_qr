from format.mode.digital import DigitalFormatter
from format.mode.alphanumeric import AlphanumericFormatter
from format.mode.bytecode import BytecodeFormatter


decoder = DigitalFormatter
input_data = "12345678"
result = decoder.encode_data(input_data=input_data)
print(result == "000111101101110010001001110")


decoder = AlphanumericFormatter
input_data = "HELLO"
result = decoder.encode_data(input_data=input_data)
print(result == "0110000101101111000110011000")


decoder = BytecodeFormatter
input_data = "Хабр"
result = decoder.encode_data(input_data=input_data)
print(result == "1101000010100101110100001011000011010000101100011101000110000000")
