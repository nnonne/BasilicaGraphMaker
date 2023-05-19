# a = (b, id)
# b = (0 1)(a, id)
def state_id(w):
    return w, state_id

def a(w):
    return ("0", b) if w == "0" else ("1", state_id)

def b(w):
    return ("1", a) if w == "0" else ("0", state_id)

def go(w):
    out_a = ""
    out_b = ""
    q0 = a
    for letter in w:
        ans, q1 = q0(letter)
        out_a += ans
        q0 = q1

    q0 = b
    for letter in w:
        ans, q1 = q0(letter)
        out_b += ans
        q0 = q1
    return out_a, out_b
