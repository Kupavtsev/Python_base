import threading
import asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    loop = asyncio.get_running_loop()
    # print('loop: ', loop)
    # print('user threads: ', threading.active_count())
    
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # both awaited, but you would get a Value!
    # await asyncio.gather(
    #     loop.create_task(fetch_data()),
    #     loop.create_task(print_numbers()))
    # What a difference with LOOP ?
    # await asyncio.gather(
    #     fetch_data(), print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())

# Future: place holder for the value
# that will exist in the future

# 2
# async def main():
#     print('oleg')
#     task = asyncio.create_task(second())
#     # await task
#     await asyncio.sleep(0.5)
#     print('finished')

# async def second():
#     print('text')
#     await asyncio.sleep(1)

# asyncio.run(main())

# 1
# async def main():
#     print('oleg')
#     await second()
#     print('while waiting...')

# async def second():
#     print('second')
#     await asyncio.sleep(1)

# asyncio.run(main())