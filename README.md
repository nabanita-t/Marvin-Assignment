#### Getting Started

Project Setup [Installation Steps]

Install virtual environment

```

pip install virtualenv

```

create and activate the virtual env

```

python3 -m venv "venv_name"

source venv/bin/activate

```

Install requirements 

```
pip install -r requirements.txt
```

Migrate 

```

python manage.py migrate

```

Run Server

```

python manage.py runserver

```

```

API Contract for Wikipedia Word Frequency API 

url : http://localhost:8000/wiki/word-frequency-analysis/?topic=south korea&n=3
request type : GET
resposne : 
{
    "success": true,
    "code": 200,
    "data": {
        "Topic": "south korea",
        "Top Words": [
            [
                "the",
                1040
            ],
            [
                "of",
                505
            ],
            [
                "and",
                476
            ]
        ]
    }
}

```


```

API Contract for Wikipedia Word Frequency API 

url : http://localhost:8000/wiki/search-history/
request type : GET
resposne : 
{
    "success": true,
    "code": 200,
    "data": [
        {
            "topic": "south korea",
            "top_words": {
                "Topic": "south korea",
                "Top Words": [
                    [
                        "the",
                        1040
                    ],
                    [
                        "of",
                        505
                    ],
                    [
                        "and",
                        476
                    ]
                ]
            },
            "timestamp": "2024-03-16T14:31:55.432287Z"
        },
        {
            "topic": "Hospital Playlist Korean Drama",
            "top_words": {
                "Topic": "Hospital Playlist Korean Drama",
                "Top Words": [
                    [
                        "the",
                        95
                    ],
                    [
                        "of",
                        67
                    ],
                    [
                        "as",
                        62
                    ],
                    [
                        "and",
                        57
                    ],
                    [
                        "in",
                        39
                    ],
                    [
                        "to",
                        32
                    ],
                    [
                        "on",
                        24
                    ],
                    [
                        "a",
                        23
                    ],
                    [
                        "lee",
                        23
                    ],
                    [
                        "his",
                        20
                    ],
                    [
                        "hospital",
                        18
                    ],
                    [
                        "kim",
                        18
                    ]
                ]
            },
            "timestamp": "2024-03-16T13:04:42.542479Z"
        },
        {
            "topic": "Django Admin",
            "top_words": {
                "Topic": "Django Admin",
                "Top Words": [
                    [
                        "the",
                        53
                    ],
                    [
                        "and",
                        38
                    ],
                    [
                        "in",
                        35
                    ],
                    [
                        "a",
                        31
                    ],
                    [
                        "to",
                        29
                    ],
                    [
                        "of",
                        28
                    ],
                    [
                        "django",
                        27
                    ],
                    [
                        "for",
                        20
                    ]
                ]
            },
            "timestamp": "2024-03-16T13:03:14.581801Z"
        },
        {
            "topic": "towel",
            "top_words": {
                "Topic": "towel",
                "Top Words": [
                    [
                        "the",
                        77
                    ],
                    [
                        "tower",
                        44
                    ],
                    [
                        "of",
                        37
                    ],
                    [
                        "a",
                        33
                    ],
                    [
                        "to",
                        31
                    ],
                    [
                        "in",
                        28
                    ],
                    [
                        "towers",
                        25
                    ],
                    [
                        "and",
                        23
                    ]
                ]
            },
            "timestamp": "2024-03-16T12:53:29.772079Z"
        },
        {
            "topic": "lilies",
            "top_words": {
                "Topic": "lilies",
                "Top Words": [
                    [
                        "the",
                        205
                    ],
                    [
                        "lilium",
                        134
                    ],
                    [
                        "of",
                        111
                    ],
                    [
                        "and",
                        107
                    ],
                    [
                        "in",
                        86
                    ],
                    [
                        "are",
                        80
                    ],
                    [
                        "to",
                        59
                    ],
                    [
                        "as",
                        45
                    ]
                ]
            },
            "timestamp": "2024-03-16T12:43:45.273823Z"
        },
        {
            "topic": "apple",
            "top_words": {
                "Topic": "apple",
                "Top Words": [
                    [
                        "the",
                        79
                    ],
                    [
                        "in",
                        55
                    ],
                    [
                        "a",
                        49
                    ],
                    [
                        "of",
                        48
                    ],
                    [
                        "is",
                        36
                    ],
                    [
                        "function",
                        28
                    ],
                    [
                        "apply",
                        27
                    ],
                    [
                        "and",
                        26
                    ],
                    [
                        "to",
                        25
                    ],
                    [
                        "as",
                        16
                    ],
                    [
                        "are",
                        15
                    ],
                    [
                        "this",
                        13
                    ],
                    [
                        "list",
                        12
                    ],
                    [
                        "with",
                        12
                    ]
                ]
            },
            "timestamp": "2024-03-16T12:01:34.667957Z"
        },
        {
            "topic": "tubelight",
            "top_words": {
                "Topic": "tubelight",
                "Top Words": [
                    [
                        "the",
                        615
                    ],
                    [
                        "of",
                        316
                    ],
                    [
                        "a",
                        272
                    ],
                    [
                        "to",
                        230
                    ],
                    [
                        "and",
                        208
                    ],
                    [
                        "in",
                        185
                    ]
                ]
            },
            "timestamp": "2024-03-16T12:01:13.923498Z"
        }
    ]
}

```