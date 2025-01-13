try:
    file = open("example.txt", "r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed, cleanging up resources.")
    file.close() if 'file' in locals() and not file.closed else None