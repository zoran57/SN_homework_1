
with open("data.csv", "r") as data_file:

    content = data_file.read().splitlines()

    for line in content:
        line_data = line.split(",")
        print(line_data)

    print("{0} is {1} years old and {2}".format(line_data[0], line_data[1], line_data[2], ))

    print(f"{line_data[0]} is {line_data[1]} years old and {line_data[2]}")

with open("data.csv", "r") as data_file:

    content = data_file.read().splitlines()

    for line in content:
        line_data = line.split(",")
        print("%s is  %s and %s" % (line_data[0], line_data[1], line_data[2]))
