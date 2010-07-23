def check_digit_10(isbn):
    assert len(isbn) == 9
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        w = i + 1
        sum += w * c
    r = sum % 11
    if r == 10:
        return 'X'
    else:
        return str(r)

def check_digit_13(isbn):
    assert len(isbn) == 12
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2: w = 3
        else: w = 1
        sum += w * c
    r = 10 - (sum % 10)
    if r == 10:
        return '0'
    else:
        return str(r)

def isbn_13_to_isbn_10(isbn_13):
    isbn_13 = isbn_13.replace('-', '')
    try:
        assert len(isbn_13) == 13 and isbn_13.isdigit()
        assert isbn_13.startswith('978')
        assert check_digit_13(isbn_13[:-1]) == isbn_13[-1]
    except AssersionError:
        return
    return isbn_13[3:-1] + check_digit_10(isbn_13[3:-1])