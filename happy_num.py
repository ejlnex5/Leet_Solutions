# def isHappy(n: int) -> bool:
#     conv_number = []
#     while True:
#         n_str = str(n)
#         n_str_arr = n_str.split()
#         for num in n_str_arr:
#             conv_number.append(int(num))
#         for m in conv_number:
#             n = n + m*m
#         if n == 1:
#             return True
#         else:
#             conv_number.clear()
            
x = int(19)

def test_funk(n: int):
    while True:
        n_str_arr = []
        n_str = str(n)
        n = 0
        print(type(n_str))
        n_str_arr = list(n_str)
        print(n_str_arr)
        for num in n_str_arr:
            n += int(num)**2
        print(n)
        if n == 1:
            print(n)
            break
    
    #return type(n_str) == str

test_funk(x)