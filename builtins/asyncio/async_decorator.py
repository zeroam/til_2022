import asyncio

loop = asyncio.get_event_loop()

@asyncio.coroutine
def hello1():
    print("hello1")
    yield from asyncio.sleep(3)
    print("world1")


async def hello2():
    print("hello2")
    await asyncio.sleep(3)
    print("world2")


async def main():
    await asyncio.gather(hello1(), hello2())


if __name__ == "__main__":
    loop.run_until_complete(main())
