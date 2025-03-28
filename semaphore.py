# #### 4. **Ограничение параллелизма**
# **Задача**: Напиши асинхронный сканер URL,
# у которого не может быть больше `N` одновременных запросов.
# Используй `asyncio.Semaphore`.
# **Цель**: Управление конкуренцией, семафоры в `asyncio`.

import asyncio
import aiohttp


ROOT_URL = 'http://httpbin.org/delay/'
URLS = [ROOT_URL + str(i) for i in range(1, 11)]


async def req(sem: asyncio.Semaphore, url: str, session: aiohttp.ClientSession):
    async with sem, session.get(url) as response:
        res = await response.text()
        print(f'url={url}, resp={res}')


async def main(n: int):
    semaphore = asyncio.Semaphore(n)
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[req(url=i, sem=semaphore, session=session) for i in URLS]
        )


if __name__ == '__main__':
    N = 3
    asyncio.run(main(N))

