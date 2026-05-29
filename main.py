import os
import time

from Crypto.Cipher import AES


class X917Generator:
    def __init__(self, key=None, seed=None):
        if key is None:
            self.key = os.urandom(32)
        else:
            self.key = key
            
        self.block_size = AES.block_size
        
        if seed is None:
            self.V = os.urandom(self.block_size)
        else:
            if len(seed) != self.block_size:
                raise ValueError(f"Seed должен быть длиной {self.block_size} байт")
            self.V = seed

        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def _get_datetime_vector(self):
        t = int(time.time() * 1e9)
        dt_bytes = t.to_bytes(self.block_size, byteorder='big')
        return dt_bytes

    def _xor_bytes(self, a, b):
        return bytes(x ^ y for x, y in zip(a, b, strict=True))

    def get_random_bytes(self, num_bytes):
        result = b''
        
        iterations = (num_bytes + self.block_size - 1) // self.block_size

        for _ in range(iterations):
            DT = self._get_datetime_vector()
            
            I = self.cipher.encrypt(DT)
            
            temp = self._xor_bytes(I, self.V)
            R = self.cipher.encrypt(temp)
            
            temp_v = self._xor_bytes(I, R)
            self.V = self.cipher.encrypt(temp_v)
            
            result += R

        return result[:num_bytes]

if __name__ == "__main__":
    gen = X917Generator()

    print("--- Генерация 16 байт (один блок) ---")
    random_block = gen.get_random_bytes(16)
    print(f"Hex: {random_block.hex()}")
    
    print("\n--- Генерация 32 байт (два блока) ---")
    random_data = gen.get_random_bytes(32)
    print(f"Hex: {random_data.hex()}")