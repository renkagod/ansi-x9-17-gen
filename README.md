# ANSI X9.17 PRNG (AES)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Генератор псевдослучайных байт по схеме **ANSI X9.17** (вариант с **AES-256** в режиме ECB). Вектор даты/времени берётся из наносекундного таймстампа; внутреннее состояние `V` обновляется после каждого блока.

> Только для учёбы и экспериментов. Для криптографически стойких задач используйте `secrets` / OS CSPRNG.

## Особенности

- Реализация ANSI X9.17 с AES-256 (ECB)
- Вектор даты/времени из наносекундного таймстампа
- CLI и импорт как модуль (`X917Generator`)

## Быстрый старт

```bash
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

## Лицензия

[MIT](LICENSE) — Copyright (c) 2026 [renkagod](https://github.com/renkagod).
