col_data: dict[str, list[float]] = { "high": [77,84,78,79,65,67,74,61,55,61], "low": [67,51,64,45,43,53,56,37,34,42], "rain": [.3,.2,.4,.8,0,.2,.4,.5,.1,.1] }

def less_than(col, threshold):
    result = []
    for item in col:
        if item < threshold:
            result.append(True)
        else:
            result.append(False)

    return result

def masked(col, mask):
    result = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])

    return result

def not_mask(mask: list[bool]) -> list[bool]:
  result: list[bool] = []
  for item in mask:
    result.append(not item)
  return result

mask_a: list[bool] = less_than(col_data["high"], 80)
mask_b: list[bool] = not_mask(mask_a)

values: list[float] = masked(col_data["low"], mask_b)
print(values)
print(mask_a)
print(mask_b)