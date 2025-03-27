# #### 3. **Асинхронная очередь**
# **Задача**: Используя `asyncio.Queue`, реализуй продюсера,
# который кладёт в очередь числа от 1 до 10 с небольшой задержкой,
# и несколько консюмеров, которые читают из очереди и печатают числа.
# **Цель**: Понять модель продюсер–консюмер, работу с очередями в асинхронном контексте.
import asyncio
from asyncio import Queue


async def producer(queue: Queue):
    for i in range(1, 11):
        print(f'put {i}')
        await queue.put(i)
        await asyncio.sleep(0.1)
    await queue.put(None)
    await queue.put(None)


async def consumer(i: int, queue: Queue):
    while True:
        res = await queue.get()
        await asyncio.sleep(0.2)
        if res is None:
            break
        print(f'consumer {i}: res = {res}')


async def main():
    queue = Queue()

    await asyncio.gather(
        producer(queue),
        consumer(1, queue),
        consumer(2, queue),
    )

if __name__ == '__main__':
    asyncio.run(main())
