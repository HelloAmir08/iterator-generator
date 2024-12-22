class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.n:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return result
        else:
            raise StopIteration


x = Fibonacci(10)
for i in x:
    print(i)

# generator
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n + 1):
#         fib.append(fib[i - 1] + fib[i - 2])
#     yield fib
#
#
# x = fibonacci(10)
# for i in x:
#     print(i)