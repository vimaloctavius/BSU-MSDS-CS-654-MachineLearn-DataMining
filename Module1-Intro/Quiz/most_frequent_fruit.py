data_s = ['Mango', 'Kiwi', 'Mango', 'Apple', 'Kiwi', 'Apple', 'Banana', 'Pineapple', 'Mango', 'Apple', 'Pineapple', 'Kiwi', 'Banana', 'Pineapple', 'Apple', 'Banana', 'Kiwi', 'Kiwi', 'Apple', 'Mango', 'Pineapple', 'Banana', 'Pineapple', 'Apple', 'Apple', 'Apple', 'Mango', 'Pineapple', 'Kiwi', 'Kiwi', 'Pineapple', 'Pineapple', 'Banana', 'Apple', 'Pineapple', 'Kiwi', 'Kiwi', 'Mango', 'Banana', 'Kiwi', 'Pineapple', 'Apple', 'Pineapple', 'Kiwi', 'Apple', 'Apple', 'Banana', 'Pineapple', 'Kiwi', 'Apple', 'Banana', 'Pineapple', 'Kiwi', 'Banana', 'Apple', 'Mango', 'Kiwi', 'Banana', 'Mango', 'Banana', 'Apple', 'Banana', 'Kiwi', 'Banana', 'Banana', 'Mango', 'Apple', 'Apple', 'Mango', 'Apple', 'Pineapple', 'Kiwi', 'Kiwi', 'Banana', 'Banana', 'Apple', 'Pineapple', 'Pineapple', 'Apple', 'Kiwi', 'Mango', 'Kiwi', 'Kiwi', 'Apple', 'Kiwi', 'Pineapple', 'Kiwi', 'Pineapple', 'Banana', 'Kiwi', 'Kiwi', 'Kiwi', 'Apple', 'Apple', 'Pineapple', 'Pineapple', 'Banana', 'Banana', 'Apple', 'Pineapple']

# Count each fruit
for fruit in sorted(set(data_s)):
    print(f"{fruit}: {data_s.count(fruit)}")

# Most frequent
most = max(set(data_s), key=data_s.count)
print(f"\nMost frequent: {most} ({data_s.count(most)} times)")
