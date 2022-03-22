def tablica (n, m):
  ret = []
  nice_list = [(lambda x: str(x%10))(x) for x in list(range(0,n*m+1))]
  start, end = 0, m

  for _ in range(n):
    ret.append(" ".join(nice_list[start:end]))
    start, end = end, end+m

  return "\n".join(ret)

print(tablica(5,20))