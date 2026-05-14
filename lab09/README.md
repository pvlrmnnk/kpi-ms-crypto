# Лаб.9 - Advanced Encryption Standard (AES)

Реалізовувати AES самостійно це невдячна праця, тому використовується стандартний модуль cryptography. Обраний режим CTR не потребує робити доповнення як в CBC і перетворює блочний шифр на потоковий.


```
# python3 lab09/lab09.py

Оригінальний текст:  Lorem ipsum dolor sit amet, consectetur adipiscing elit
Ключ:                79f58658e29031f392dad702f4e43a4eabf52ea2eea77f47b09246feca5f0510
Згенерований nonce:  c4a813f90ce8b83fec2d29b7e507b238
Зашифрований текст:  45eec2b231eab97e59662a3124c73128f21dee8df59b2798acbd6d1ddfb20c4b45ad566ad0aa57ac390e640906b507c733721b54d57820
Розшифрований текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit
```