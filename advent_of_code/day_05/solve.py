from aocd import get_data
from aocd import submit
import numpy as np
import math


def get_rules(data):
    rules = []
    for line in data.splitlines():
        rules.append(list(map(int, line.split("|"))))
    return rules


def get_sequences(data):
    sequences = []
    for sequence in data.splitlines():
        sequences.append(list(map(int, sequence.split(","))))
    return sequences


def get_rules_sequence(data):
    rules, sequences = data.split("\n\n")
    rules = get_rules(rules)
    sequences = get_sequences(sequences)
    return rules, sequences


def check_rules(data):
    rules, sequences = get_rules_sequence(data)
    correct_sequences = []
    for sequence in sequences:
        for rule in rules:
            valid = True
            sequence_array = np.array(sequence)
            first_position = np.where(sequence_array == rule[0])[0]
            second_position = np.where(sequence_array == rule[1])[0]
            if (
                first_position.size > 0
                and second_position.size > 0
                and first_position[0] > second_position[0]
            ):
                valid = False
                break
        if valid:
            correct_sequences.append(sequence)

    return correct_sequences


def apply_rules(data):
    rules, sequences = get_rules_sequence(data)
    set1 = set(tuple(sublist) for sublist in sequences)
    set2 = set(tuple(sublist) for sublist in check_rules(data))
    incorrect_sequences = list(set1 - set2)
    changes_made = True
    while changes_made:
        changes_made = False
        for i, sequence in enumerate(incorrect_sequences):
            sequence_array = np.array(sequence)
            for rule in rules:
                first_pos = np.where(sequence_array == rule[0])[0]
                second_pos = np.where(sequence_array == rule[1])[0]

                if (
                    first_pos.size > 0
                    and second_pos.size > 0
                    and first_pos[0] > second_pos[0]
                ):
                    sequence_array[first_pos], sequence_array[second_pos] = (
                        sequence_array[second_pos],
                        sequence_array[first_pos],
                    )
                    incorrect_sequences[i] = sequence_array
                    changes_made = True
                    break
    return incorrect_sequences


def sum_middles(sequences):
    total = 0
    for sequence in sequences:
        total += sequence[math.trunc(len(sequence) / 2)]
    return total


if __name__ == "__main__":
    data = get_data(day=5, year=2024)
    # Part a
    correct_sequences = check_rules(data)
    total = sum_middles(correct_sequences)
    submit(total, part="a", day=5, year=2024)

    # Part b
    correct_sequences = apply_rules(data)
    total = sum_middles(correct_sequences)
    print(total)
    submit(total, part="b", day=5, year=2024)
