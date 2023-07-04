def p_to_v(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])


def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


p1, p2, p3 = [list(map(int, input().split())) for _ in range(3)]
v1 = p_to_v(p1, p2)
v2 = p_to_v(p2, p3)

print(cross(v1, v2) // abs(cross(v1, v2)) if cross(v1, v2) else 0)
