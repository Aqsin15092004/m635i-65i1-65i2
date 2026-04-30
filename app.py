# app.py - Demo Python Tətbiqi

def toplayin(a, b):
    """İki ədədi topla"""
    return a + b

def vurun(a, b):
    """İki ədədi vur"""
    return a * b

def faktorial(n):
    """n-in faktorialını hesabla"""
    if n < 0:
        raise ValueError("Mənfi ədədin faktorialı yoxdur!")
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

if __name__ == "__main__":
    print(f"5 + 3 = {toplayin(5, 3)}")
    print(f"4 x 6 = {vurun(4, 6)}")
    print(f"5! = {faktorial(5)}")
