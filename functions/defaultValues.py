def defaultValue(prog_language, rating, in_use="No"):
    result = f" Language {prog_language} is holding {rating} star rating and using in company {in_use}"
    return result


print(defaultValue(prog_language="python", rating=5))
print(defaultValue(rating=4, prog_language="Java", in_use="YES"))
print(defaultValue("c", 5))
