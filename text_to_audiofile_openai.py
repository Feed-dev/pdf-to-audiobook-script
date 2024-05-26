import os
import shutil

from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with the API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Configurable chunk size
CHUNK_SIZE = 4096

# Function to split text into chunks
def split_text(text, chunk_size=CHUNK_SIZE):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Example text for demonstration
text = """
THE TERRYEN WAVE FIELDS
The illusion of our visible Universe is constructed of regenerated successive waves of predictable phase conjugations.
Linked in recursive ‘action and reactionary’ moments.
Caught in a chain of unending events that culminate in
a symmetrical lattice work of self propagating structures.
Where each action, moment or quanta of existence is represented by an expanding sphere.
The concentration of these spheres leaves a recorded message of each and every action and reaction that has ever
occurred or shall ever occur. Every wave is predictable and
quantifiable. There are no unknowns in this Universe of
recorded history. It all comes from the physical manifestation of the life force which was recognized by the ancients
and is represented geometrically using the symbol called
“The Flower of Life”.
Everything that we experience is the result of ‘Effects’, the
‘Cause’ has remained shrouded in mystery since
the beginning of Man’s existence and until now
there has never come to be a truly satisfying answer for ‘Cause’. Allow me to introduce you to the
“CAUSE” of all visible action and reaction. We have always
had the freedom to examine the ‘Effects’ without the pitfalls of speculation because we are effects. All the things
around us are Effects. The enigma associated with the
Flower of Life pattern that has eluded Mankind for thousands of years is finally unraveled in the Wave Conjugations I am presenting in this book.
The Super Symmetry that rules our Universe is predictable, reliable and beautiful. The concentric lines of force
become the very fabric of the Universe. Made up of two
forces alone, ELECTRICITY and MAGNETISM.
They are two different sides of the same coin, two separate reactions from a single “CAUSATIVE” action within a
diverse system.
On one hand you have centripetal spin, like the tight spin
of a gold medal ice skater spinning in a north eastern direction that drives the contractive, gravitative force of Nature.
Rising from the flat surface of the ice, her leg extends
out like a flag suspended from a flag pole. She pulls her
leg in closer and her spin increases until she reaches such
rotational speeds that it looks as if she is almost entirely
transparent.
This is spin with such force that Space raps around her as
she bundles Time and Dimension seamlessly. Rising slowly from the southern inertial plane towards the northern
apex of a vortex, and the closer to the apex, the center of
the spin, the faster the spin.
That is the case with Electricity, it always seeks a higher pressure zone, with a faster and tighter spin. Whereas
Magnetism, has a completely different appetite. Magnetism, contrary to what most of Mankind has been taught,
seeks a lower pressure condition. Its prime directive is to
expand out, radiate, rarefy and disperse that which has
been collected together into a Mass.
Just think about it, a magnifying glass does what? Makes
things appear larger. To magnify something, you increase
the amount of Space that it occupies. Well, that is exactly
the work of Radiation/Magnetism.
If you take a closer look at the Earth's poles, you will see
where Electricity is funneled into and through the planet.
What happens to the concentrated Electricity at the core
of the planet? As the Electricity spins into a state of higher
pressures, so high a pressure zone that it has to discharge,
that discharge is Magnetism.
It explodes from the equator of our planet at tremendous speeds. Being accelerated by the continuous engine
of electrical contraction taking place at the poles, that is
soon jettisoned from the equator, heating and expanding
all Matter in its wake. This is also true of our Sun that contracts electricity at its poles from the Interstellar Plasma
Currents converting that Electricity into Magnetism at its
equator, which creates the solar wind that drives our entire solar system.
All things expand and contract simultaneously.
What would the math look like that describes this kind of
geometry? Might this be the geometry of the center of a
bubble?
The Pythagoreans explored this line of thought for quite
some time and through deep meditative, concentrative
and focused efforts, along with vigorous experimentation
and tireless application they managed to uncover some
simple and obvious truths about how our Universe operates as a whole. 
They began describing many of its underlying functions and dynamics through sympathetic harmonious vibratory mechanics and basic geometry.
Centuries after Pythagoras’ death, followers of the sect
would ultimately succumb to the pressures of the general
populous and acquiesced to the standards and practices of
the prevailing culture. The dominant elite of this culture
promoted the use of irrationality in their number systems
and are single handedly responsible for the many inconsistencies and misunderstandings found in use within physics
and mathematics today.
This surrender of their common sense is solely responsible for the mis-education of countless generations of truth
seekers and curious minds over the last two millennia.
Nevertheless, the early Pythagoreans held the thought
that the Dodecahedron was the greatest of all the platonic
solids. For some reason they felt it was the physical manifestation of Spirit into Form. 
An invocation of the Creator’s Divine Symmetry and Beauty manifested in the material world.
The Dodecahedron was considered to be so sacred, that
according to reports, if someone from the ‘brotherhood’
mentioned the word “Dodecahedron” outside of their secret meetings, they would be killed on the spot.
I have discovered this structure in its purist form. It is the
scaffolding and backbone of the Allshape. A structure that
encapsulates all of the principals that were sacred to the
Pythagoreans.
In fact, it is the structure where All numbers meet and
become of equal value. (It is the detailed geometric manifestation of the cubed root of one!)
THE LYNCHPIN
THE COMMON FACTOR OF ALL THINGS
If Mankind knew how to multiply this simple equation
correctly (x * x = 2), the Universe would be completely
understood in all of its Multi-Dimensional beauty and for
all of its super symmetrical complexities.
Touch The Image Below
To see the Lynchpin Bonding Behaviors.
In two dimensional analysis, it is a confluence of the
The AllShape: the general structure of Matter in the Universe.
Four equal and opposite curved intersecting planes creating an interior and exterior Space.
Rayleigh–Plesset equation coupled with the Trilling Equation and Henry’s Law. Look them up when you get the time,
but they all fail to describe true curved Space/Time. Nevertheless, in 3 Dimensional Space/Time the model of the
Universe can be expressed in this single geometric equation!
1 ³ = |π|
when one is given its necessary complement of 3 Dimensions allowing it to expand and contract within.
This is the neutral condition of all visible Matter. It is the
reservoir of all zero point energy and the center of a bubble. It predicts the periodic distribution of the elements
of Matter. In Physics, a quantum or quanta is the smallest
measurable phenomenon of any Matter involved in an interaction. 
The Lynchpin is the Lowest Common Denominator of All Matter either seen or unseen.
When 4 Gyroscopic vortices meet at an equatorial common frame and bond their apices, the north points to
maximum pressures. The four vortices share a central axis
rotating in opposing directions. The subsequent structure
of combined forces is called a Torus.
The Lynchpin is the internal dimensions of a torus, a dynamo that converts and 
recycles all energy by reconditioning it through the effects of motion and pressure. 
Either centripetally in a charging, gravitative state at its concaved
centers or centrifugally, in a radiating, expanding state,
discharging where three of its 4 planes meet at a single
vortex. The Lynchpin is the Universal wave conjugator for
all things Matter. It is the true currency of the Universal
flow because it is “the Common Factor” of All Things.
The Lynchpin is the measurable constitution of a quantum or quanta, the smallest reflection of One and ultimately the collected potential of All Things, which equals the Multi-Verse!
Each Lynchpin is created as a series of stacked events occurring consecutively under consistent pressure and motion conditions. It is the product of pressure walls made
from 4 Dimensions of relentless waves of continuous, converting energy moving from high to low potential within
each system.
Each stacked AllShape is a small visible portion of a ripple
of converting energy. Either wrapped into a tight vortex
at the northern poles of the wave or being dispersed evenly along the southern equatorial plane of the wave. All of
these dynamics take place between 4 equal and opposite
gyroscopic forces, moving at various speeds within the
spectrum of Light. Dividing itself into 3 initial dimensions
and ultimately expressing those dimensions in twelve concentric circle’s of 5th’s.
UNIVERSAL MATHEMATICS
All Things are moving in this Universe of motion, for if One
Thing was to be still All Things connected to it would have
to be still. There would be no breathing of anything inside
the Universe because all things would be dead. There isn’t
one motionless thing within our Universe. That is what
the straight line has attempted to represent, the idea of an
unmoving and unchanging planar existence. An unreality,
for All Dimension is formed in Motion and All Motion is
oscillatory and every oscillation is a function of frequency
and all frequency is periodic and periodic oscillations are
rhythmic vibrations and all rhythmic vibrations are music
and Music is Symmetry. As Pythagoras once stated, “Rock
is nothing but frozen music!”
It is my sincere hope that this will aide Mankind in our
journey towards a more conscious understanding of the
Super Symmetry that underlines All Creation will ultimately lead to our obtaining a symbiotic co-existence with
our Universe, along with a better appreciation of its Infinite Beauty.
THE FLOWER OF LIFE AND
THE GARDEN OF EDEN
This is where it gets meta-physical or even heretical. It
would be negligent on my part not to mention the possible
connection of this work to the very first occurrence of a
“Flower” or “Tree of life.” in recorded literature. That, as a
necessary consequence would produce “Fruit” that would
either contain some key components of life’s essence or
provide seeds in some form that would create a foundation
for the continued preservation of Life. Or it could provide
the key to the geometric conditions that would make all
life possible and generate the motion and pressure conditions that would make it possible for Creation itself to be
realized.
My experience in working with this Flower and meditating upon this figurative Tree has led me to believe that the
knowledge of the Flower of Life and its properties are the
seeds that are planted in fertile soil or the hearts of Man.
If conditions are ripe, then these seeds will grow and allow
those cultivating these precious seeds to become Wise and
All Knowing concerning the secrets that are hidden within
its majestic and glorious petals.
In the Judean, Christian, and Islamic sacred texts we are
introduced to one of the most adored and cherished stories that could chronicle Mankind’s desired history. In the
Judeo/Christian version taken from the first book of the
Bible named Genesis, we are first exposed to what many
around the world consider to be Mankind’s first human
parents.
The story recounts the creation of the Heavens and the
Earth along with the creation of all plant and animal life
upon this planet. In the beginning of the 3rd chapter we
are introduced to the concept of ‘original sin’ by our fore
parents Adam and Eve and the story of them being ejected from the lush paradise that was once their home. As
they are forced into a barren world where they will have to
struggle in order to gain the very bare necessities of life.
In chapter 3, verse 24, of that same book, we are introduced to the two Angelic creatures called Cherubim with
4 wings who were placed in front of the entrance of the
romanticized epic Garden of Eden in order that they may
block the way to the “Tree of Life”. That no Man may come
and take from its fruit and actually live to Time Indefinite.
What is most interesting to note, is the fact that the “Flower of Life” is often referred to in its initial stages as the
“Tree of Life”. What is also remarkable, are the comparable
factors involved in the “Flaming Blade of Sword” that was
spinning continuously. This fiery sword spinning would
create the overlapping circles that cause the illusion of the
appearance of the “Flower of Life” and the mention of the
sword being on fire or “Flaming” as it were, I don’t think
that it was in reference to them being "flaming". ((lol))
I believe, in all seriousness, that it was in reference to the
appearance of the ‘Flower’ producing a powerful and ever
brightening light.
Now all of these things can be interpreted to mean a million and one different 
things depending upon the inclination of the reader. Nevertheless, not one of the Children
of Mankind that has come before me in recorded history
has ever opened the Flower and pulled from it the “Fruit”
that is Life Giving.
Because of these Terryen Wave Fields future generations
will be able to conquer the mediocrity of thought that has
permeated the ever dull minds of Mankind for the last ten
thousand years. Along with the truth about the value of
the number 1 and how it should be calculated.
Therefore, future generations will with ease be able to
overcome the hurdles of disease and death and be transformed into truly conscious and very powerful beings.
It all depends upon one anagram:
“L.I.F.E.”
The "L" stands for the word "Life"
The "E" stands for the word "Ever-Lasting"
Yet, there are two little letters that stand between those
two promises, the word:
“IF”
Life Everlasting "IF" we learn from the lessons of the past
and abandon the antiquated and dead works of the past.
"""

# Split the extracted text into chunks
chunks = split_text(text)

# Print the number of chunks
print(f"Total chunks: {len(chunks)}")

# Directory to store individual chunk audio files
chunk_audio_dir = "chunk_audio"
os.makedirs(chunk_audio_dir, exist_ok=True)

# Synthesize audio for each chunk and save them as individual files
for j, chunk in enumerate(chunks):
    print(f"Synthesizing audio for chunk {j+1}/{len(chunks)}...")
    chunk_audio_path = os.path.join(chunk_audio_dir, f"chunk_{j+1}.mp3")
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="onyx",
        input=chunk,
        response_format="mp3"
    )
    response.stream_to_file(chunk_audio_path)

# Combine the audio files
combined_audio = AudioSegment.empty()
for j in range(len(chunks)):
    chunk_audio_path = os.path.join(chunk_audio_dir, f"chunk_{j+1}.mp3")
    audio_segment = AudioSegment.from_file(chunk_audio_path, format="mp3")
    combined_audio += audio_segment

# Save the combined audio to an MP3 file
output_path = "combined_output_text_audio.mp3"
combined_audio.export(output_path, format="mp3")
print(f"{output_path} saved successfully.")

# Clean up the directory with chunk audio files
shutil.rmtree(chunk_audio_dir)
