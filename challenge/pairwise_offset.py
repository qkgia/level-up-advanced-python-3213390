

def pairwise_offset(sequence, fillvalue='*', offset=0):
    result = []
    for i in range(len(sequence) + offset):
        second_i = (i - offset)

        if second_i < 0:
            second_value = fillvalue
        else:
            second_value = sequence[i - offset]

        if i >= len(sequence):
            first_value = fillvalue
        else:
            first_value = sequence[i]

        pair = tuple([first_value, second_value])

        result.append(pair)

    return result
