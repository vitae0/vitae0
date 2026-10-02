from datetime import datetime, timezone
from pathlib import Path
import html
import re

# Short quotations with a source note kept beside each entry.
# The pool deliberately avoids startup-motivation filler and dubious internet attributions.
QUOTES = [
    ("The first principle is that you must not fool yourself — and you are the easiest person to fool.", "Richard Feynman", "Caltech commencement address, 1974"),
    ("We can only see a short distance ahead, but we can see plenty there that needs to be done.", "Alan Turing", "Computing Machinery and Intelligence, 1950"),
    ("We must know. We will know.", "David Hilbert", "Königsberg address / epitaph, 1930"),
    ("All things excellent are as difficult as they are rare.", "Baruch Spinoza", "Ethics, Part V"),
    ("The unexamined life is not worth living.", "Socrates", "Plato, Apology 38a"),
    ("If there is no struggle, there is no progress.", "Frederick Douglass", "West India Emancipation speech, 1857"),
    ("He who has a why to live for can bear almost any how.", "Friedrich Nietzsche", "Twilight of the Idols, Maxims and Arrows"),
    ("One must still have chaos in oneself to be able to give birth to a dancing star.", "Friedrich Nietzsche", "Thus Spoke Zarathustra"),
    ("The essence of mathematics lies in its freedom.", "Georg Cantor", "Über unendliche, lineare Punktmannigfaltigkeiten, 1883"),
    ("The Analytical Engine has no pretensions whatever to originate anything.", "Ada Lovelace", "Notes on the Analytical Engine, 1843"),
    ("Ignorance more frequently begets confidence than does knowledge.", "Charles Darwin", "The Descent of Man, 1871"),
    ("I was taught that the way of progress was neither swift nor easy.", "Marie Curie", "Pierre Curie, 1923"),
    ("A man may imagine things that are false, but he can only understand things that are true.", "Isaac Newton", "Unpublished manuscript, c. 1680s"),
    ("Doubt is not a pleasant condition, but certainty is absurd.", "Voltaire", "Letter to Frederick William, Prince of Prussia, 1770"),
    ("Sapere aude! Have courage to use your own understanding.", "Immanuel Kant", "What Is Enlightenment?, 1784"),
    ("Life can only be understood backwards; but it must be lived forwards.", "Søren Kierkegaard", "Journals, 1843"),
    ("Talent hits a target no one else can hit; genius hits a target no one else can see.", "Arthur Schopenhauer", "The World as Will and Representation"),
    ("Attention is the rarest and purest form of generosity.", "Simone Weil", "Letter to Joë Bousquet, 1942"),
    ("Not everything that is faced can be changed; but nothing can be changed until it is faced.", "James Baldwin", "As Much Truth as One Can Bear, 1962"),
    ("Monsters exist, but they are too few in number to be truly dangerous.", "Primo Levi", "The Drowned and the Saved, 1986"),
    ("The line separating good and evil passes not through states, nor between classes, nor between parties, but through every human heart.", "Aleksandr Solzhenitsyn", "The Gulag Archipelago"),
    ("Nothing is so firmly believed as that which we least know.", "Michel de Montaigne", "Essays"),
    ("The greater the difficulty, the more glory in surmounting it.", "Epictetus", "Discourses"),
    ("It is not death that a man should fear, but he should fear never beginning to live.", "Marcus Aurelius", "Meditations"),
    ("No great thing is created suddenly.", "Epictetus", "Discourses"),
    ("There are no facts, only interpretations.", "Friedrich Nietzsche", "Notebooks, 1886–87"),
    ("The important thing is not to stop questioning.", "Albert Einstein", "LIFE magazine interview, 1955"),
    ("In mathematics you don't understand things. You just get used to them.", "John von Neumann", "Attributed in Gary Zukav, The Dancing Wu Li Masters"),
    ("Simplicity is prerequisite for reliability.", "Edsger W. Dijkstra", "EWD498, 1975"),
    ("Testing shows the presence, not the absence of bugs.", "Edsger W. Dijkstra", "NATO Software Engineering conference, 1969"),
    ("The purpose of computing is insight, not numbers.", "Richard Hamming", "Numerical Methods for Scientists and Engineers"),
    ("A language that doesn't affect the way you think about programming is not worth knowing.", "Alan Perlis", "Epigrams on Programming, 1982"),
    ("The most exciting phrase to hear in science is not 'Eureka!' but 'That's funny...'", "Isaac Asimov", "Widely attributed; retained only as a clearly marked attribution"),
]

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

day = datetime.now(timezone.utc).timetuple().tm_yday
quote, author, _source = QUOTES[(day - 1) % len(QUOTES)]

quote_html = html.escape(quote, quote=True)
author_html = html.escape(author, quote=True)

replacement = (
    "<!-- QUOTE_START -->\n"
    f'<p align="center"><i>“{quote_html}”</i><br>\n'
    f'<sub>— {author_html}</sub></p>\n'
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
