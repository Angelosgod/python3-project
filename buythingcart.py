# Author:anliyong
product_list= [
    ('Iphonex',7800),
    ('MacPro',9800),
    ('Bike',800),
    ('Iwatch',10600),
    ('coffee',30),
]

Shoping_list=[]
Salary =input("输入你的预算：")
if Salary.isdigit():
    Salary = int(Salary)
    for index ,iterm in enumerate(product_list) :
        print(index,iterm)
    user_choice=input("你想买啥?")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice<len(product_list)and user_choice>=0:
            p_item=product_list[user_choice]
            Shoping_list.append(product_list)
            if p_item[1] <=Salary:
                Shoping_list.append(p_item)
                Salary-=p_item[1]
                print("添加%s到你的购物车，你的余额\33[31;1m%s\033[0m"%(p_item,Salary))
            else:print("033[41;1m你的余额只剩[%s]了买不了了"%Salary)
        else:print("产品%s 并不存在"%user_choice)

    elif user_choice=='q':
        print('-----购物清单------')
        for p in Shoping_list:
            print(p)
        print("你的额是：",Salary)
        exit()



    else:print("请输入数字！")


else:
    print("错误的输入！")