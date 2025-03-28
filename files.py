# **Задача**: Реализуй асинхронную загрузку нескольких файлов
# (или картинок, можно из `https://picsum.photos`) и сохрани их локально.
# **Цель**: Работа с `aiohttp` и асинхронными файловыми операциями (через `aiofiles`).
import asyncio
import aiofiles
import aiohttp
import uuid


url = 'http://picsum.photos/300/200'


async def download(url: str, session: aiohttp.ClientSession):
    response = await session.get(url)
    filename = str(uuid.uuid4())
    async with aiofiles.open('./images/' + filename + '.jpg', 'wb') as file:
        image = await response.read()
        print(f'image={image}')
        await file.write(image)
    print('file downloaded: ' + filename)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download(url, session) for _ in range(10)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
