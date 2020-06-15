def run():
    var1 = int(input("Put a number..."))
    var2 = int(input("Put a number..."))
    var3 = input("Put a sign...")
    if (var3 == "+"):
        print(var1 + var2)
    if var3 == "-":
        print(var1 - var2)
    if var3 == "/":
        ans = (var1 / var2)
        ans = round(ans, 2)
        print(ans)
    if var3 == "*":
        dan = (var1 * var2)
        print(dan)
run()
finish = input("Press n to finish")
if finish == "n":
    quit()
else:
    run()
    

