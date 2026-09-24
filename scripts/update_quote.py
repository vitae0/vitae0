from datetime import datetime, timezone
from pathlib import Path
import html
import re

# Short, sourceable quotations. Keep the source note here so attribution can be audited later.
QUOTES = [
    ("The best way to predict the future is to invent it.", "Alan Kay", "Xerox PARC, c. 1971"),
    ("What I cannot create, I do not understand.", "Richard Feynman", "final Caltech office blackboard, 1988"),
    ("We can only see a short distance ahead, but we can see plenty there that needs to be done.", "Alan Turing", "Computing Machinery and Intelligence, 1950"),
    ("Any sufficiently advanced technology is indistinguishable from magic.", "Arthur C. Clarke", "Profiles of the Future"),
    ("Simplicity is prerequisite for reliability.", "Edsger W. Dijkstra", "EWD498, 1975"),
    ("Testing shows the presence, not the absence of bugs.", "Edsger W. Dijkstra", "NATO Software Engineering conference, 1969"),
    ("The purpose of computing is insight, not numbers.", "Richard Hamming", "Numerical Methods for Scientists and Engineers"),
    ("A language that doesn't affect the way you think about programming is not worth knowing.", "Alan Perlis", "Epigrams on Programming, 1982"),
    ("Plan to throw one away; you will, anyhow.", "Fred Brooks", "The Mythical Man-Month"),
    ("Not everything that is faced can be changed; but nothing can be changed until it is faced.", "James Baldwin", "As Much Truth As One Can Bear, 1962"),
    ("We are all in the gutter, but some of us are looking at the stars.", "Oscar Wilde", "Lady Windermere's Fan, 1892"),
    ("It is better to fail in originality than to succeed in imitation.", "Herman Melville", "Hawthorne and His Mosses, 1850"),
    ("One must imagine Sisyphus happy.", "Albert Camus", "The Myth of Sisyphus"),
    ("We are what we pretend to be, so we must be careful about what we pretend to be.", "Kurt Vonnegut", "Mother Night, 1966 introduction"),
    ("Ever tried. Ever failed. No matter. Try again. Fail again. Fail better.", "Samuel Beckett", "Worstward Ho, 1983"),
    ("If you find a book you really want to read but it hasn't been written yet, then you must write it.", "Toni Morrison", "Ohio Arts Council talk, 1981"),
    ("Go and make interesting mistakes, make amazing mistakes, make glorious and fantastic mistakes.", "Neil Gaiman", "University of the Arts commencement, 2012"),
    ("Even bad coffee is better than no coffee at all.", "David Lynch", "Catching the Big Fish"),
    ("Absorb what is useful, discard what is not, add what is uniquely your own.", "Bruce Lee", "Bruce Lee writings / estate"),
    ("The unexamined life is not worth living.", "Socrates", "Plato, Apology 38a"),
    ("What stands in the way becomes the way.", "Marcus Aurelius", "Meditations 5.20, trans. Gregory Hays"),
    ("If you have built castles in the air, your work need not be lost; that is where they should be.", "Henry David Thoreau", "Walden"),
    ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs", "Stanford commencement, 2005"),
    ("The only way of discovering the limits of the possible is to venture a little way past them into the impossible.", "Arthur C. Clarke", "Profiles of the Future"),
    ("People who are really serious about software should make their own hardware.", "Alan Kay", "Creative Think seminar, 1982"),
    ("It is better to do the right problem the wrong way than the wrong problem the right way.", "Richard Hamming", "quoted in Mathematical Maxims and Minims"),
    ("Simplicity does not precede complexity, but follows it.", "Alan Perlis", "Epigrams on Programming, 1982"),
    ("This is only a foretaste of what is to come and only the shadow of what is going to be.", "Alan Turing", "The Times interview, 1949"),
]

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

day = datetime.now(timezone.utc).timetuple().tm_yday
quote, author, _source = QUOTES[(day - 1) % len(QUOTES)]

quote_html = html.escape(quote, quote=True)
author_html = html.escape(author, quote=True)

replacement = (
    "<!-- QUOTE_START -->\n"
    f'<h2 align="center"><i>“{quote_html}”</i></h2>\n'
    f'<p align="center"><sub>— {author_html}</sub></p>\n'
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
