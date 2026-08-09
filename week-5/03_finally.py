# finally always runs - whether or not there was an error.
# Perfect for cleanup like closing a file.

try:
    file = open("report.txt", "w", encoding="utf-8")
    file.write("Revenue: 100000")
    print("Wrote the report.")
except OSError:
    print("Could not write the file.")
finally:
    file.close()
    print("File closed (finally always runs).")
