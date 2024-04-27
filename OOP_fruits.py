fruits=list(('banana','apple','cherry','peach','watermelon','melon','blueberry'))
print(sorted(fruits))
for fruit in fruits:
    if(fruit.startswith('b')):
        print(fruit)
    else:
        continue