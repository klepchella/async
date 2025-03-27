# #### 2. **Сравнение синхронного и асинхронного исполнения**
# **Задача**: Реализуй функцию, которая делает запросы к списку URL (например, на `httpbin.org/delay/1`)
# сначала синхронно через `requests`, а потом асинхронно через `aiohttp`.
# Замерь время выполнения.
# **Цель**: Увидеть выигрыш по времени при параллельной обработке IO.


from datetime import datetime

import aiohttp
import requests
import asyncio

ROOT_URL = 'http://httpbin.org/delay/'
URLS = [ROOT_URL + str(i) for i in range(1, 10)]


def sync_request():
    for i in URLS:
        requests.get(i)


async def async_request(session: aiohttp.ClientSession, url: str) -> None:
    async with session.get(url) as resp:
        assert resp is not None


async def main():
    print('start')
    start_time_1 = datetime.now()
    sync_request()
    print('First: --- %s seconds ---' % (datetime.now() - start_time_1))

    start_time_2 = datetime.now()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[asyncio.create_task(async_request(session, i)) for i in URLS]
        )
    print('Second: --- %s seconds ---' % (datetime.now() - start_time_2))


if __name__ == '__main__':
    asyncio.run(main())
