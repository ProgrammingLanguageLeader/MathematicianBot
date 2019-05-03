import asyncio
import requests


async def fetch(url, params=None, timeout=2.5):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(
        None,
        requests.get,
        url,
        params
    )
    try:
        response = await asyncio.wait_for(future, timeout)
        print(f'{url} answered with {response.status_code} status code')
        return response
    except asyncio.TimeoutError:
        print(f'{url} answer timeout!')


async def main():
    await asyncio.gather(
        fetch('https://vk.com'),
        fetch('https://google.com'),
        fetch('https://yandex.ru'),
        fetch('https://heroku.com'),
        fetch('https://github.com'),
    )
    print('End')


if __name__ == '__main__':
    asyncio.run(main())
