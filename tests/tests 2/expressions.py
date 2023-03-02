tests = [
    {
        "expressions": [
            "abandon",
            "ability",
            "able",
            "above",
            "abroad",
            "accomplish",
            "a*z",
        ],
        "regex_true": [
            ["abandon"],
            ["ability"],
            ["able"],
            ["above"],
            ["abroad"],
            ["accomplish"],
            ["z"],
            ["a", "z"],
            ["a", "a", "a", "z"],
        ],
        "regex_false": [
            ["adjust"],
            ["adjustment"],
            ["administration"],
            ["administrator"],
            ["admire"],
            ["a", ""],
            ["a", "g"],
            ["a", "a", "z", "g"],
        ],
    },
    {
        "expressions": [
            "a",
            "b*",
            "c",
        ],
        "regex_true": [
            ["a", "b", "c"],
            ["a", "b", "b", "c"],
        ],
        "regex_false": [
            ["a", "c", "b"],
            ["b", "a", "c"],
            ["b", "c", "a"],
            ["c", "a", "b"],
            ["c", "b", "a"],
        ],
    },
    {
        "expressions": [
            "car.car",
            "a.b.c.z*",
            "career",
        ],
        "regex_true": [
            ["car", "car"],
            ["career"],
            ["a", "b", "c", "z"],
        ],
        "regex_false": [
            ["car"],
            ["a", "b", "z"],
            ["a", "b", "c", ""],
            ["car.", "car"],
        ],
    },
]
