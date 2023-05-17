def returnDictionary(prog_language, rating, in_use=""):
    result = {}
    if in_use:
        result = {"language": prog_language, "star_rating": rating, "using": in_use}
    else:
        result = {"language": prog_language, "star_rating": rating}
    return result


response = returnDictionary("python", 5, True)
print(response["language"])
