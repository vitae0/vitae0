from datetime import datetime, timezone
from pathlib import Path
import re

QUOTES = [
    "Take interesting ideas seriously, not yourself.",
    "Curiosity is a perfectly good reason to start.",
    "If it keeps bothering you, build it.",
    "Make the weird prototype before the sensible presentation.",
    "A good rabbit hole leaves you with a tool.",
    "The fastest way to find the edge is to keep pushing.",
    "Build first, name it later.",
    "If the idea survives contact with reality, keep going.",
    "Learn enough to make the next mistake interesting.",
    "Useful is cool. Strange and useful is better.",
    "Some ideas deserve more than a note in a file.",
    "If the question is good, the detour was probably worth it.",
    "Keep the curiosity. Delete the ceremony.",
    "Serious work does not need serious-looking prose.",
    "Good tools make hard things feel ordinary.",
    "You can be rigorous without being boring.",
    "The best projects usually start slightly unreasonable.",
    "If you want to understand a system, try building one.",
    "Do not confuse polish with depth.",
    "A prototype is a question you can run.",
    "Make it work, then make it make sense.",
    "Build the thing you keep wishing existed.",
    "There is no prize for staying in one field.",
    "Weird ideas are cheap. Following them properly is the hard part.",
    "Keep enough skepticism to break your own favorite idea.",
    "Small tools can have long lives.",
    "Curiosity scales badly, and that is half the fun.",
    "Every abstraction should earn its rent.",
    "If the boring version exists, make the interesting one.",
    "Sometimes the right scope is 'too much.'",
    "Leave the project better than the idea that started it.",
]

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

day = datetime.now(timezone.utc).timetuple().tm_yday
quote = QUOTES[(day - 1) % len(QUOTES)]

replacement = (
    "<!-- QUOTE_START -->\n"
    f"> *“{quote}”*\n"
    "<!-- QUOTE_END -->"
)

updated, count = re.subn(
    r"<!-- QUOTE_START -->.*?<!-- QUOTE_END -->",
    replacement,
    text,
    count=1,
    flags=re.S,
)

if count != 1:
    raise SystemExit("quote markers not found exactly once")

readme.write_text(updated, encoding="utf-8")
