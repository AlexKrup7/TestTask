def zipper(upper: list, lower: list) -> dict:
    for _ in range(len(upper) - len(lower)):
        lower.append(None)

    zip_dict = {}
    for key, val in zip(upper, lower):
        zip_dict.setdefault(key, val)
    return zip_dict


if __name__ == '__main__':
    print(zipper(['A', 'B', 'C', 'D', 'E'], ['a', 'b', 'c', 'd', 'e', 'f']))
    print(zipper(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                 ['a', 'b', 'c', 'd', 'e', 'f']))
