name_file = input("File name: ").strip().lower()

if name_file.endswith(".gif"):
    print("image/gif")
elif name_file.endswith(".jpg"):
    print("image/jpeg")
elif name_file.endswith(".jpeg"):
    print("image/jpeg")
elif name_file.endswith(".png"):
    print("image/png")
elif name_file.endswith(".pdf"):
    print("application/pdf")
elif name_file.endswith(".txt"):
    print("text/plain")
elif name_file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
