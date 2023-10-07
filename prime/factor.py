def factor(n: int):
    if n == 1:
        return [1]

    result = []
    div = 2
    while div * div <= n:
        if n % div == 0:
            result.append(div)
            n, _ = divmod(n, div)
        
        else:
            div += 1

    if n != 1:
        result.append(n)
    
    return result

if __name__ == '__main__':
    print(' x '.join([ str(i) for i in factor(123456789)]))
