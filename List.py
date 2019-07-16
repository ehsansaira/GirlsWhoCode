thingsinmybag = ["chapstick", "hand lotion", "headphones" "pens", "purse"]
print(len(thingsinmybag))
print(thingsinmybag[3])
print("chapstick" in thingsinmybag)
for item in thingsinmybag:
    print(item)
for num in range(len(thingsinmybag)):
    print(thingsinmybag[num])
thingsinmybag.append("markers")
print(thingsinmybag)
thingsinmybag.extend("chapstick")
print(thingsinmybag)
