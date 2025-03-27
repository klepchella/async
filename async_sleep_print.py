
import asyncio

#### 1. **Асинхронная задержка**
# **Задача**: Напиши функцию `async_sleep_print(msg, delay)`,
# которая печатает сообщение `msg` после задержки в `delay` секунд.
# Затем запусти три таких функции с разными сообщениями и задержками параллельно.

# **Цель**: Понять, как работают `async def` и `await asyncio.sleep`.


async def async_sleep_print(msg: str, delay: float) -> None:
    await asyncio.sleep(delay)
    print(msg)


async def main():
    await asyncio.gather(
        asyncio.create_task(async_sleep_print('first', 2)),
        asyncio.create_task(async_sleep_print('second', 1)),
        asyncio.create_task(async_sleep_print('third', 10)),
        asyncio.create_task(async_sleep_print('fourth', 3))
    )


if __name__ == "__main__":
    asyncio.run(main())
