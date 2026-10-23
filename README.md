# ANSI X9.17 PRNG (AES)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Donate](https://img.shields.io/badge/Donate-crypto-ea4aaa?logo=githubsponsors&logoColor=white)](https://github.com/renkagod/.github/blob/main/DONATE.md)

Генератор псевдослучайных байт по схеме ANSI X9.17 на основе AES-256 в режиме ECB. Внутреннее состояние `V` обновляется после каждого блока, вектор даты/времени берётся из наносекундного таймстампа.

> Только для учёбы и экспериментов. Для криптографически стойких задач используйте `secrets` / OS CSPRNG.

## Особенности

- Реализация ANSI X9.17 с AES-256 (ECB)
- Вектор даты/времени из наносекундного таймстампа
- CLI-скрипт с демонстрацией и импорт как модуль (`X917Generator`)

## Быстрый старт

```bash
git clone https://github.com/renkagod/ansi-x9-17-gen.git
cd ansi-x9-17-gen
pip install -r requirements.txt
python main.py
```

## Использование

```python
from main import X917Generator

gen = X917Generator()
print(gen.get_random_bytes(32).hex())
```

| Параметр | Описание |
|----------|----------|
| `key` | 32 байта AES-ключа; `None` — случайный ключ |
| `seed` | 16 байт начального `V`; `None` — случайный вектор |

## Поддержать проект

Если проект оказался полезен, можно поддержать его криптой: [адреса для доната](https://github.com/renkagod/.github/blob/main/DONATE.md).

## Лицензия

[MIT](LICENSE) — Copyright (c) 2026 [renkagod](https://github.com/renkagod).
