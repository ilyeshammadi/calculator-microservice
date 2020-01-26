from schema import Use, Schema, And

add = Schema({
    "a": And(Use(float), lambda val: float(val)),
    "b": Use(float, lambda val: float(val))
})
