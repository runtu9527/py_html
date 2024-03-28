import asyncio
import time
# async def nested():
#     return 42
# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     nested()
#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".
# asyncio.run(main())


# import asyncio
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({number}), currently i={i}...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#     return f
# async def main():
#     # Schedule three calls *concurrently*:
#     L = await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#     print(L)
# asyncio.run(main())

async def watch_tv(n):
    print('watch_tv time is start %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    await asyncio.sleep(n)
    print('watch_tv time is over %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    return 'watch_tv'

async def eat_food(n):
    print('eat_food time is start %s' %time.strftime('%Y-%m-%d %X',time.localtime()))
    await asyncio.sleep(n)
    print('eat_food time is over %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    return 'eat_food'