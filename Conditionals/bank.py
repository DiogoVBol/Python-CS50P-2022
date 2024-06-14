question = input("Greeting: ").lower().strip()

if question.startswith("hello"):
    print("$0")
elif question.startswith("h"):
    print("$20")
else:
    print("$100")
