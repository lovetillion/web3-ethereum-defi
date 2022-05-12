"""Raw log event data conversion helpers."""
from typing import List

from eth_typing import ChecksumAddress
from web3 import Web3


def decode_data(data: str) -> List[bytes]:
    """Split data of a log to uin256 results"""

    # {'address': '0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f', 'blockHash': '0x359d1dc4f14f9a07cba3ae8416958978ce98f78ad7b8d505925dad9722081f04', 'blockNumber': '0x98b723', 'data': '0x000000000000000000000000b4e16d0168e52d35cacd2c6185b44281ec28c9dc0000000000000000000000000000000000000000000000000000000000000001', 'logIndex': '0x22', 'removed': False, 'topics': ['0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9', '0x000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', '0x000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'], 'transactionHash': '0xd07cbde817318492092cc7a27b3064a69bd893c01cb593d6029683ffd290ab3a', 'transactionIndex': '0x26', 'event': <class 'web3._utils.datatypes.PairCreated'>, 'timestamp': 1588710145}
    b = bytes.fromhex(data[2:])
    entries = []
    for i in range(0, len(b), 32):
        entries.append(b[i: i+32])
    return entries


def convert_uint256_bytes_to_address(bytes32: bytes) -> ChecksumAddress:
    """Convert raw uin256 from log data to addresses.

    .. note ::

        Ethereum address checksum might have a speed penalty for
        high speed operations.
    """
    val = int.from_bytes(bytes32, "big")
    return Web3.toChecksumAddress(hex(val))


def convert_uint256_string_to_address(bytes32: str) -> ChecksumAddress:
    """Convert raw uin256 from log data to addresses.

    .. note ::

        Ethereum address checksum might have a speed penalty for
        high speed operations.
    """
    val = int(bytes32, 16)
    return Web3.toChecksumAddress(hex(val))
