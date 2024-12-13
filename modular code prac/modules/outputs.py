def final(results):
    with open("calculations.txt", "a") as f:
              for line in results:
                  print(line)
                  f.write(line)
