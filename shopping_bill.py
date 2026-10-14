
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100

    return total - discount


a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
finalAmount = calculateDiscountedBill(a, b, c, d, e)

print(f"Electronics with GST: {electronics:.2f}")
print(f"Fashion with GST: {fashion:.2f}")
print(f"Food with GST: {food:.2f}")
print(f"Total after GST: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final payable amount: {finalAmount:.2f}")
