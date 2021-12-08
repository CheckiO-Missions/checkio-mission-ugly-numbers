"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [4],
            "answer": 4,
            "explanation": "4th Ugly number is..."
        },
        {
            "input": [6],
            "answer": 6,
            "explanation": "6th Ugly number is..."
        },
        {
            "input": [11],
            "answer": 15,
            "explanation": "11th Ugly number is..."
        },
        {
            "input": [1],
            "answer": 1,
            "explanation": "1st Ugly number is..."
        },
        {
            "input": [29],
            "answer": 75,
            "explanation": "Result is below 100..."
        },
        {
            "input": [84],
            "answer": 960,
            "explanation": "Result is below 1000..."
        },
        {
            "input": [171],
            "answer": 9216,
            "explanation": "Over nine thousands!"
        },
        {
            "input": [313],
            "answer": 100000,
            "explanation": "Jackpot!"
        },
        {
            "input": [593],
            "answer": 2332800,
            "explanation": "It's getting harder..."
        },
        {
            "input": [899],
            "answer": 26214400,
            "explanation": "Too slow?.. It's not the end..."
        }
    ],
    "Extra": [
        {
            "input": [978],
            "answer": 44789760,
            "explanation": "When are you turn the wron way?"
        },
        {
            "input": [1173],
            "answer": 150000000,
            "explanation": "150 billions!"
        },
        {
            "input": [1398],
            "answer": 512000000,
            "explanation": "150 billions!"
        },
        {
            "input": [1407],
            "answer": 536870912,
            "explanation": "2 ** 29"
        },
        {
            "input": [1500],
            "answer": 859963392,
            "explanation": "Final test!"
        }
    ]
}
