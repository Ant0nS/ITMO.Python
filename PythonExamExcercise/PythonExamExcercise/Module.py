import datetime
import pandas as pd
import json

print("""
        Hello!
        ______
        """)
while input!=0:
    print("""
            Navigation menu:

            1. Add item
            2. Show all items
            3. Show for date 
            4. Show by category
            5. Show by min -> max
            6. Delete 
            0. Exit
        """)
    try:
        num = int(input("What would you like to do? Please input a number according to Navigation menu: "))
        if num ==0:
            print("""
        ________
        Goodbye!
        """)
            break

        if num == 1:

            cat = input("---> Category: ")
            prod = input("---> Item: ")
            price = input("---> Price: ")
            date = input("---> Date in format 'DD.MM.YYYY': ")
            try:
                with open('table.json') as t:
                    table_data = json.load(t)
                df = pd.DataFrame(data = table_data)
                print("---->")
                ser = pd.Series({"Category": cat, "Product": prod, "Cost": int(price), "Date": date})
                dfUpd = df.append(ser, ignore_index=True)
                print(dfUpd)
                dfUpd.to_json('table.json')
                print("---> Item was sussecfully added to table!")
            except Exception as e:
                print("---> No data found!")
        if num == 2:
            print("---> 2")
            try:
                with open('table.json') as t:
                    table_data = json.load(t)
                df = pd.DataFrame(data=table_data)
                print(df)
            except:
                print("---> No data found!")

        if num == 3:
            print("---> 3")
            try:
                with open('table.json') as t:
                    table_data = json.load(t)
                df = pd.DataFrame(table_data)
                date = input("---> Choose the date in format 'DD.MM.YYYY': ")
                df_show = df[df["Date"] == date]
                print(df_show)
            except:
                print("---> No data found!")

        if num == 4:
            print("---> 4")
            try:
                with open('table.json') as t:
                    table_data = json.load(t)
                df = pd.DataFrame(table_data)
                print(df['Category'])
                category = input("Choose the category: ")
                df_show = df[df["Category"] == category]
                print(df_show)
            except:
                print("---> No data found!")
        if num == 5:
            print("---> 5")
            try:
                with open('table.json') as t:
                    table_data = json.load(t)
                df = pd.DataFrame(table_data)
                print(df.sort_values('Cost'))
            except:
                print("---> No data found!")
        if num == 6:
            print("---> 6")
            try:
                with open('table.json') as t:
                    table_data = json.load(t)
                df = pd.DataFrame(data=table_data)
                print("--->")
                print(df)
                index = input("---> Choose the item for delition by index nubmer:")
                dfUpd = df.drop([index])
                dfUpd.to_json('table.json')
                print("---> Item was sussecfully deleted!")
                print(dfUpd)
            except:
                print("---> No data found!")
        if num>6:
            print("---> No option found! Please enter the number in range 0...6 !")

    except (TypeError, ValueError):
        print("---> Type Error! Please input an integer!")

