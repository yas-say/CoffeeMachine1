MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = {
    "qtr":0,
    "dim":0,
    "nick":0,
    "penn":0

}


def report():
    for k in resources:
        if k == "coffee":
            print(f"{k.title()}: {resources[k]}g")
        else:
            print(f"{k.title()}: {resources[k]}ml")

    print(f"Money: ${moneyTotal()}")


def isSufficientR(choice):
    flagSuff = True
    for k in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][k] > resources[k]:
            print(f"Insufficient resource: {k}")
            flagSuff = False
    return flagSuff

def moneyTotal():
    totalm = 0
    for k in money:
        if k == "qtr":
            totalm += money[k] * 0.25
        elif k == "dim":
            totalm += money[k] * 0.10
        elif k == "nick":
            totalm += money[k] * 0.05
        elif k == "penn":
            totalm += money[k] * 0.01
    return round(float(totalm), 2)


def moneyprint():
    for k in money:
        print(f"{k}: {money[k]}")

def processMoney(choice):
    print("Please insert coins.")
    qtr = int(input("how many quarters?: "))
    dim = int(input("how many dimes?: "))
    nick = int(input("how many nickles?: "))
    penn = int(input("how many pennies?: "))
    total = round((qtr * 0.25 + dim * 0.10 + nick * 0.05 + penn * 0.01),2)
    # print(total)
    # print(MENU[choice]["cost"])
    # input()
    if total >= MENU[choice]["cost"]:
        diff = round(total - MENU[choice]['cost'],2)
        print(f"Here is ${diff} in change.")
        print("Here is your espresso ☕️.Enjoy!")
        qtrInDiff = round(diff // 0.25,2)
        maxQtr = 0

        if qtrInDiff > qtr+money["qtr"]:
            maxQtr = qtr+money["qtr"]
            diff = round(diff - maxQtr * 0.25,2)
            money["qtr"] = 0
        else:
            maxQtr = qtrInDiff
            money["qtr"] = qtr+money["qtr"]-maxQtr
            diff = round(diff - maxQtr * 0.25,2)

        dimInDiff = round(diff // 0.1,2)
        maxDim = 0

        if dimInDiff > dim+money["dim"]:
            maxDim = dim+money["dim"]
            diff = round(diff - maxDim * 0.10,2)
            money["dim"] = 0
        else:
            maxDim = dimInDiff
            money["dim"] = dim+money["dim"]-maxDim
            diff = round(diff - maxDim * 0.1,2)

        nickInDiff = round(diff // 0.05 , 2)
        maxnick = 0

        if nickInDiff > nick + money["nick"]:
            maxnick = nick + money["nick"]
            diff = round(diff - maxnick * 0.05,2)
            money["nick"] = 0
        else:
            maxnick = nickInDiff
            money["nick"] = nick + money["nick"] - maxnick
            diff = round(diff - maxnick * 0.05,2)


        pennInDiff = round(diff // 0.01,2)
        maxPenn = 0

        if pennInDiff > penn + money["penn"]:
            maxPenn = penn + money["penn"]
            diff = round(diff - maxPenn * 0.01,2)
            money["penn"] = 0
        else:
            maxPenn = pennInDiff
            money["penn"] = penn + money["penn"] - maxPenn
            diff = round(diff - maxPenn * 0.05,2)

        for k in MENU[choice]["ingredients"]:
            resources[k] = resources[k] - MENU[choice]["ingredients"][k]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False




loop = True
while loop:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): "
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user == "off":
        loop = False
    # TODO 3. Print report.
    elif user == "report":
        report()
    elif user == "money":
        moneyprint()
    elif user in ["espresso", "latte", "cappuccino"]:
        # TODO 4. Check resources sufficient?
        if isSufficientR(user):
            # TODO 5. Process coins.
            # TODO 6. Check transaction successful?
            # TODO 7. Make Coffee.
            processMoney(user)
    else:
        print("Wrong choice")



