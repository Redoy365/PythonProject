if __name__ == '__main__':

    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    def solve(meal_cost, tip_percent, tax_percent):

        tip = meal_cost and (meal_cost/100)*tip_percent
        tax = tax_percent and (tax_percent/100)*meal_cost
        total_cost = meal_cost+tip+tax
        print(round(total_cost))

    solve(meal_cost, tip_percent, tax_percent)