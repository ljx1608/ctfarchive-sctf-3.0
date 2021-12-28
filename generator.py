import json
import re

r = re.compile(r"[^a-zA-Z0-9-]")

challengesj = open("challenges.json")
challenges = json.load(challengesj)
with open("README.md", "a") as f:
    f.write("\n")

    for cat in challenges:
        f.write(f"[{cat.upper()}](#{cat})\n\n")
        for challenge in challenges[cat]:
            id = r.sub("", challenge["name"].replace(" ", "-")).lower()
            f.write(f"- [{challenge['name']}](#{id})\n")
        f.write("\n")

    f.write("---\n\n")

    for cat in challenges:
        f.write(f"## {cat.upper()}\n\n")
        for challenge in challenges[cat]:
            f.write(f"### {challenge['name']}\n\n")
            f.write(f"Points: {challenge['points']}\n")
            f.write(f"Solves: {challenge['solves']}\n")
            f.write(f"Author: {challenge['author']}\n")
            f.write("\n")
            f.write(f"Flag: {challenge['flag']}\n\n")
            f.write("#### Description\n\n")
            description = "> " + challenge["description"].replace("\n", "\n> ")
            f.write(f"{description}\n\n")
            for i, hint in enumerate(challenge["hints"]):
                f.write(f"Hint {i+1}: {hint}\n\n")
challengesj.close()
