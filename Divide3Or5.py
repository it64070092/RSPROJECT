"""Divide3Or5"""
def main():
    """Divide3Or5"""
    inputs = abs(int(input()))
    count = 0
    for i in range(1, inputs+1):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    print(count)
main()
