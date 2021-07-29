print("\nCaffeine Machine")
tea,coffee={"\nTea":{"1.Lemon_Tea":["1.Tea_Small 20 rs","2.Tea_Medium 30 rs","3.Tea_Large 40 rs"],"2.Milk_Tea":["1.Tea_Small 20 rs","2.Tea_Medium 30 rs","3.Tea_Large 40 rs"]}},{'Coffee':{"1.Cold_Coffee":["1.Coffee_Small 40 rs", "2.Coffee_Medium 60 rs", "3.Coffee_Large 80 rs"],"2.Hot_Coffee":["1.Coffee_Small 40 rs","2.Coffee_Medium 60 rs","3.Coffee_Large 80 rs"]}}
for i,z in zip(tea.values(),coffee.values()):
    print("1.Tea","\n2.Coffee")
    us =int(input("\nWhat do you want to drink?\nFor Tea press 1 or for Coffee press 2 :"))
    if us==1 or us==2:
        print(f"\n{list(i.keys())[0]}\n{list(i.keys())[1]}") if us == 1 else print(f"\n{list(z.keys())[0]}\n{list(z.keys())[1]}")
        user = int(input("\nEnter your choice:"))
        if user == 1 or user==2:
            for k,x in zip(i.values(),z.values()):
                print(f"\n{k[0]}\n{k[1]}\n{k[2]}") if us==1 else print(f"\n{x[0]}\n{x[1]}\n{x[2]}")
                s=int(input("\nEnter your size :"))
                if s==1:
                    print("\nYou Have To Pay 20 rs") if us==1 else print("\nYou Have To Pay 40 rs")  
                    break    
                elif s==2:
                    print("\nYou Have To Pay 30 rs") if us==1 else print("\nYou Have To Pay 60 rs")
                    break
                elif s==3:
                    print("\nYou Have To Pay 40 rs") if us==1 else print("\nYou Have To Pay 80 rs") 
                    break
                else:
                    print("\nOnly 3 options are there.")
                    break
            else: print("\nOnly 2 options are there.")
    else: print("\nOnly 2 options are there.")