dict1 = {"apple": 45, "avocado": 10, "banana": 30, "cashew": 5}

print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

print({k: v for k, v in sorted(dict1.items(), key=lambda x: x[1])})
