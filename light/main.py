DISPLAY = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def light(n: int):
    result = 1
    for i in list(str(n)):
        result *= DISPLAY[int(i)]
    
    return result

def main():
    log = {123456}
    last = 123456

    while True:
        last = light(last)
        if last in log:
            break

        log.add(last)
    
    print(len(log))


if __name__ == "__main__":
    main()
