"""  14. Electricity Bill Calculator (Tiered Slabs) Q14
Calculate the electricity bill based on progressive graduated tariff slabs:
Consumption Slab Rate per Unit
First 100 units (0 – 100) ₹2 per unit
Next 100 units (101 – 200) ₹3 per unit
Units consumed above 200 ₹5 per unit
Slab Trace for 250 Units:
• First 100 units × ₹2 = ₹200
• Next 100 units × ₹3 = ₹300
• Remaining 50 units × ₹5 = ₹250
Total Bill: 200 + 300 + 250 = ₹750 (Sample Output: 750) """



a = int(input())

b = 0

if a <= 100:
    b = a * 2
elif a <= 200:
    b = (100 * 2) + ((a - 100) * 3)
else:
    b = (100 * 2) + (100 * 3) + ((a - 200) * 5)

print(b)