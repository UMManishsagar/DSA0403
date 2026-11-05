
import re
from collections import Counter

# Dataset input (taken from the given dataset)
data = [
    """tv future in the hands of viewers with home theatre systems
    plasma high-definition tvs and digital video recorders.
    people watch tv in different ways with new technologies.
    broadband connections allow people to watch programmes
    whenever they want.""",

    """worldcom boss left books alone former worldcom boss
    bernie ebbers was accused of overseeing a fraud.
    the phone company collapsed in 2002.
    prosecutors claim that losses were hidden to protect shares.""",

    """tigers wary of farrell gamble leicester say they will
    not be rushed into making a bid for andy farrell.
    the rugby league captain may switch codes.
    he has persistent knee problems.""",

    """yeading face newcastle in fa cup.
    newcastle united face a trip to ryman premier league.
    arsenal were drawn at home to stoke.
    chelsea will play against scunthorpe.""",

    """ocean s twelve raids box office.
    the crime sequel starring george clooney and brad pitt
    has gone straight to number one in the us box office chart.
    the sequel follows master criminals across europe."""
]

# Combine all records
text = " ".join(data)

# Convert to lowercase
text = text.lower()

# Extract words
words = re.findall(r'\b[a-z]+\b', text)

# Calculate frequency
frequency = Counter(words)

# Display word frequency
print("WORD FREQUENCY DISTRIBUTION")
print("--------------------------------")

for word, count in frequency.most_common(20):
    print(word, ":", count)

print("\nTotal number of words:", len(words))
print("Total unique words:", len(frequency))
