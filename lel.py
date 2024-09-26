def multiple_each_val_by_idx(number) -> str:
    idx = 0
    lelly = ""
    num_str = str(number)

    while idx < len(num_str):
        tim = int(num_str[idx])
        lelly += str(tim * idx)
        idx += 1
    return lelly


print(multiple_each_val_by_idx(10784))
