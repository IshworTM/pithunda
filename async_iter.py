import asyncio

async def my_async_iterator():
    for i in range(69):
        yield i

    # Obtain an asynchronous iterator
    async_iter = aiter(my_async_iterator())

    # Get the next element from the asynchronous iterator
    next_element = await anext(async_iter, None)
    print(next_element)
print(my_async_iterator)