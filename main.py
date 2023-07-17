# def math ():
#     vvod_1 =int(input("vvedite chislo: "))
#     table = input(f"""
#     1: +
#     2: -
#     3: *
#     4: /
#     5: %
#     """)
#     vvod_2 =int(input("vvedite 2 chislo: "))

#     if table == "1":
#         print(vvod_1+ vvod_2)
#     if table =="2":
#         print(vvod_1-vvod_2)
#     if table == "3":
#         print(vvod_1*vvod_2)



# math()


# is_year_leap = int(input("vvod: "))
# if is_year_leap % 4 == 0 and (is_year_leap % 100 !=0 or is_year_leap % 400 == 0):
#     print (True)
# else:
#     print(False)



# def is_leap(year):
#     "year -> 1 if leap year, else 0."
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# is_leap()



def square():
    kvadrat = int(input("vvod: "))
    perimetr_kv = kvadrat * 4 
    ploshad_kv = kvadrat * kvadrat
    # diagonal_kv = 
    print(perimetr_kv, ploshad_kv)

square()
    