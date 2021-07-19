from vector import Vector

def cosin(vec1, vec2):
    cos = vec1.cos(vec2, mode='extern_call')
    return round(cos, 9)
