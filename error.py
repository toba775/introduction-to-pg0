errors = {"400" : "Bad Request", "401" : "Unauthorized", "402" : "Payment Required", "403" : "Forbidden", "404" : "Page Not Found"}

num = input("choose a number between 400 and 404")
if num in errors:
    print(errors[num])
else:
    print("Invalid number")