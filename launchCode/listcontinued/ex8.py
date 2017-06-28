def replace(s, old, new):
    wds = s.split(old)
    glue = new
    new = glue.join(wds)
    return new


print(replace('Mississippi', 'i', 'I'))
