BARRIER_PHRASES = {
  "high": [
    {
      "category": "Trading History",
      "pattern": "minimum\\s+(1?\\d+)\\s+years?\\s+(?:uninterrupted\\s+)?trading history",
      "threshold": 10,
      "points": 15,
      "description": "Excessive trading history requirement (>10 years)"
    },
    {
      "category": "Insurance",
      "pattern": "professional indemnity insurance of £(\\d+)\\s*million",
      "min_amount": 20,
      "points": 12,
      "description": "High professional indemnity insurance requirement"
    },
    {
      "category": "Insurance",
      "pattern": "public liability insurance of £(\\d+)\\s*million",
      "min_amount": 15,
      "points": 12,
      "description": "High public liability insurance requirement"
    },
    {
      "category": "Turnover",
      "pattern": "turnover.*£(\\d+)\\s*million",
      "min_amount": 50,
      "points": 15,
      "description": "Excessive turnover requirement (>£50M)"
    },
    {
      "category": "Time Constraint",
      "pattern": "no extensions permitted",
      "points": 10,
      "description": "Zero-tolerance timeline"
    },
    {
      "category": "Staff Requirements",
      "pattern": "must employ at least (\\d+) full[- ]time",
      "min_amount": 80,
      "points": 12,
      "description": "Excessive staffing requirements"
    },
    {
      "category": "Geographic/Infrastructure",
      "pattern": "must own.*equipment.*£(\\d+)\\s*million",
      "min_amount": 5,
      "points": 12,
      "description": "High-value equipment ownership requirement"
    },
    {
      "category": "Penalty Clauses",
      "pattern": "liquidated damages.*£(\\d+[,\\d]*)",
      "min_amount": 50000,
      "points": 12,
      "description": "High penalty for delays"
    }
  ],
  "medium": [
    {
      "category": "Trading History",
      "pattern": "minimum\\s+5\\s+years? trading history",
      "points": 7
    },
    {
      "category": "Insurance",
      "pattern": "public liability insurance.*£(5|10)\\s*million",
      "points": 6
    },
    {
      "category": "Turnover",
      "pattern": "minimum annual turnover of £(\\d+)\\s*million",
      "min_amount": 5,
      "max_amount": 20,
      "points": 6
    },
    {
      "category": "Certifications",
      "pattern": "(ISO\\s*9001|ISO\\s*27001|Cyber Essentials Plus)",
      "points": 5,
      "description": "Standard certification requirement"
    },
    {
      "category": "Timeline",
      "pattern": "completion within (\\d+) weeks",
      "max_amount": 12,
      "points": 6
    }
  ],
  "low": [
    {
      "category": "Insurance",
      "pattern": "basic public liability insurance",
      "points": 2
    },
    {
      "category": "Timeline",
      "pattern": "flexible timescales",
      "points": 1
    },
    {
      "category": "Encouraging SME Inclusion",
      "pattern": "we welcome applications from (?:new businesses|SMEs|startups)",
      "points": 1
    }
  ]
}
