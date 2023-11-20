# задание 1



import asyncio
#
# async def Plus(a, b):
#     print('складывание началось')
#     await asyncio.sleep(5)
#     print('Результат суммы', a+b)
#     return a + b
#
# async def kvadrat(a):
#     print('квадратирование началось')
#     await asyncio.sleep(2)
#     print('Резултат квадратирования', a**2)
#     return a**2
#
# async def main():
#     task1=asyncio.create_task(Plus(4, 4))
#     task2 = asyncio.create_task(kvadrat(4))
#
#     await asyncio.gather(task1, task2)
#
# asyncio.run(main())




# задание 2

# async def handle_phone_calls():
#     while True:
#         print('Handling phone calls')
#         await asyncio.sleep(1)
#
# async def handle_visitors():
#     while True:
#         print('Handling visitors')
#         await asyncio.sleep(2)
#
# async def book_tickets():
#     while True:
#         print('Booking tickets')
#         await asyncio.sleep(3)
#
# async def control_schedules():
#     while True:
#         print('Controlling schedules')
#         await asyncio.sleep(4)
#
# async def fill_documents():
#     while True:
#         print('Filling documents')
#         await asyncio.sleep(0.5)
#
# loop = asyncio.get_event_loop()
#
# tasks = [
#     loop.create_task(handle_phone_calls()),
#     loop.create_task(handle_visitors()),
#     loop.create_task(book_tickets()),
#     loop.create_task(control_schedules()),
#     loop.create_task(fill_documents())
# ]
#
# try:
#     loop.run_until_complete(asyncio.wait(tasks))
# except KeyboardInterrupt:
#     pass
# finally:
#     loop.close()