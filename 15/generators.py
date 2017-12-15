#!/usr/bin/python3

FACTOR_A = 16807
FACTOR_B = 48271
SCALING = 2147483647


def compare_generators(gen_a, gen_b):
    bin_a = bin(gen_a)[2:].zfill(32)[-16:]
    bin_b = bin(gen_b)[2:].zfill(32)[-16:]
    return bin_a == bin_b


def first_part():
    gen_a = 591
    gen_b = 393
    matches = 0
    for i in range(40000000):
        gen_a = (gen_a * FACTOR_A) % SCALING
        gen_b = (gen_b * FACTOR_B) % SCALING
        matches += 1 if compare_generators(gen_a, gen_b) else 0
    return matches


def second_part():
    pairs = 0
    matches = 0
    gen_a = 591
    gen_b = 393
    while pairs < 5000000:
        while not gen_a % 4 == 0:
            gen_a = (gen_a * FACTOR_A) % SCALING
        while not gen_b % 8 == 0:
            gen_b = (gen_b * FACTOR_B) % SCALING
        matches += 1 if compare_generators(gen_a, gen_b) else 0
        pairs += 1
        gen_a = (gen_a * FACTOR_A) % SCALING
        gen_b = (gen_b * FACTOR_B) % SCALING
    return matches


print("Part I:  %d" % first_part())
print("Part II: %d" % second_part())
