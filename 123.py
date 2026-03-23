produkt1={"name":"1-sigaret", "price":200, "count":20}
produkt2={"name":"2-сигарета", "price":100, "count":10}
produkt3={"name":"3-некурилы", "price":50, "count":5}
товары=(produkt1 ,produkt2 ,produkt3)
a=int(input("возраст"))
if a<18:
    print("нет")
if a>=18:
    print("добро пожаловать в табачку")
    print(f"tovari {товары}")
    poisk=input("что хочешь?")
    print(f"вот {товары[int(poisk)-1]}")
