from .data import lorem_text
from typing import Literal

hash_table: list[None | tuple[str, int]] = [None] * 349
c = 31

options = ["linear", "quadratic", "hash2"]


def linear_hash(k: str, M=349, i: int = 0):
    sum = i
    for n in range(len(k)):
        sum += ord(k[n]) * c**n
    return sum % M


def quadratic_hash(k: str, M=349, i: int = 0):
    sum = i**2
    for n in range(len(k)):
        sum += ord(k[n]) * c**n
    return sum % M


def hash2(k: str):
    sum = 0
    for letter in k:
        sum += ord(letter)
    return 277 - (sum % 277)


def double_hash(k: str, M=349, i: int = 0):
    sum = i * hash2(k)
    for n in range(len(k)):
        sum += ord(k[n]) * c**n
    return sum % M


def insert(
    k: str, option: Literal["linear", "quadratic", "hash2"] = "linear", i: int = 0
):
    match option:
        case "linear":
            hash_function = linear_hash
        case "quadratic":
            hash_function = quadratic_hash
        case "hash2":
            hash_function = double_hash
        case _:
            raise Exception("Invalid type")

    index = hash_function(k=k, M=349, i=i)
    index_value = hash_table[index]
    if index_value == None:
        hash_table[index] = (k, 1)
        return i
    if index_value[0] == k.lower():
        hash_table[index] = (k, index_value[1] + 1)
        return i

    return insert(k, option, i + 1)


for item in hash_table:
    print(item)

print(f"Tamanho da tabela: {len(hash_table)}")

print("----------- Selecione o método de tratamento de colisão -----------")
print("1 - Linear")
print("2 - Quadrática")
print("3 - Dispersão dupla")
choice = int(input())

if choice > 3:
    raise Exception("Invalid value")

moves = 0
for word in lorem_text:
    moves += insert(k=word.lower(), option=options[choice - 1])  # type: ignore

for item in hash_table:
    print(item)

print(f"Tamanho da tabela: {len(hash_table)}")
print(f"Procuras: {moves}")
