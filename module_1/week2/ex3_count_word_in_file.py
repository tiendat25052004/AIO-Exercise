def count_word(filename):
    with open(filename, "r") as file:
        words = file.read().split()
        res = {}
        for word in words:
            if word in res:
                res[word] += 1
            else:
                res[word] = 1
    return res


filename = "D:\AIO\AIO-Exercise\module_1\week2\P1_data.txt"
print(count_word(filename))
