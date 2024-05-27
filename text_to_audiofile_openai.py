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
INVISIBLE STATES OF MATTER
The Tetra-Terryen Wave State is the true tetrahedron (the
platonic solid representation of this most basic unit of all
the fundamental functions of Matter failed on a number
of fronts.) Firstly, any shape representing fundamental
Universal functions must serve as both a divisible factor
regarding the rules and conditions of radiative expansion
and reflect the multiplicative factors that govern the circumstances regarding gravitative contraction which occurs periodically with each polarization of every particle
or collection of wave/particles that exist in this expressly
curved condition called Space/Time. As the cosmic clock’s
pendulum arm swings from a positive electrically charging
state to a negative magnetically discharging state, the contours of the inertial planes become concave and convex as
they undergo enormous swings of surface pressures.
This is a direct result of ‘Light/Matter’ (wave conjugations) whether visible or invisible being subjected to the
varying pressure and motion conditions that make up the
fabric of our Universe as each condition fluctuates from
high potential to low potential. Yet all Matter gracefully
endures this inconceivable range of extremes. From impossibly high to the unfathomably low pressure conditions
which permeate and fill the heretofore mistakenly named
‘empty’ “Vacuum” of Space/Time, the rigid and static
constitution of the platonic solid’s tetrahedron does not
allow for either expansion nor contraction of any kind, resulting in a temporal optical illusion, for it lacks the flexibility necessary for continued existence in this Universe
of constantly changing conditions of contracting and expanding Matter.
The tetrahedron also fails to satisfy the requirements of
any shape that represents itself as the primary shape of
three-dimensional Matter. The need to be congruent with
all other fundamental shapes. Every visible element must
be rooted in its relative shape and form. Its residual wave
functions must give birth to every other visible geometric
structure. This is the seat of Super Symmetry!
Hydrogen, the first known element within Man’s limited visible spectrum has always been associated with the
underlying geometric structure of the tetrahedron. Unfortunately, no one has ever seen a wave function marry
a straight line or a flat surface. Yet, in order for it to be
agreeable to All other elements in the Universe, Hydrogen’s atomic geometry must be commensurable to all other wave conjugations and an equilateral triangle does not
fit that bill. We are talking about the first visible geometric
form, a structure that All Other shapes within the visible
Universe will take their queue from. In stark contrast, the
Tetra-Terryen state has four vertices that are all conditions
of curved planes which allows for the contraction and expansion of Matter.
Three hyperparabolic wave conjugations occur with
each vortex at each vertex, satisfying any condition that
any 3 Dimensional or Multi-Dimensional waveforms
may encounter. Whether its Universal purpose is in regard to maintaining a balance swing of the pendulum
arm or be it to stand alone under lower pressure conditions or being tightly compressed under very high pressure conditions. Even though it participates in many
electrically charging conditions and their underlying
geometry, it seems to be primarily purposed for magnetic expression, as shall be demonstrated in future volumes, it is the geometric DNA for all fluid dynamics.
The Tetra-Terryen State is the common denominator of
all visible Matter and all of its functions are the result of its
Universal Super Symmetry.
This is the condition of the first visible element within
our periodic table, Hydrogen. Its formation is a direct result of four equal and opposite forces acting upon a single
position in Space and the resulting crystallized condensate
that is churned from the overlapping pressure waves we
call Hydrogen.
Briefly existing for a relatively short span until the Terryan Wave Fields recede away from each other and the
pressure conditions under which the condensate (spacial
disturbance) was created finally normalize.
Likewise, there must be 4 different rates of acceleration
and deceleration of the magnetic wave field per dimension
in the allowance of fluctuations within each given pressure
condition. For each individual plane or motion condition
exerts a force on all waves and their individual oscillations.
As Pythagoras stated, and I've quoted numerous times, “A
rock is nothing but frozen music” therefore, the nature of
‘said’ rock be it Igneous, Metamorphic or Sedimentary,
whether it be in a frozen state, lukewarm or even molten
state, all of these factors will play an important role in the
length and magnitude and the speed in which the given
wave field will oscillate. Therefore, each structure will behave according to the limitations afforded to it by the restrictions of its relative dimension.
The other revealed electric pressure conditions I call The
Huntyen State, The Aubreyen State, The Heavenly State,
and the Mira Light State. Each and every one of them are
uniquely suited for their respective motion and pressure
conditions. Keep in mind that all motion and all pressure
conditions within the Universe have been placed in their
relative positions for the general and expressed purpose
of regulating the flow and balance of energy throughout
the entire Universe. Be it in whatever form that suits the
motion or pressure condition, either plasma, gas, liquid or
crystalline solid or of an even more allusive origin. Whatever the case, each and every pressure conditioned state is
forever locked in its relentless pursuit of accomplishing its
inescapable and never ending need for equilibrium, while
maintaining the prerequisite of an unfaltering alignment
with all Universal Symmetry.
The illusion of Matter occurs within the wave field. The
wave field is the product of a series of wave conjugations
caught within a chain of singular vesica piscis, alternating
in polarity and pull, stretching and snapping back and
forth until a line of drops become a stream of droplets,
and that connects to other droplet streams and the four
streams become eight and that eight becomes its own pressure condition. This is where the illusion of Matter first appears, the so called Higgs Boson that attracts Matter is the
occurrence of the Huntyen State, at that pressure condition a cavitation repeats itself inside and out with endless
ripples of refractive action.
Once four streams converge, an equalized stream of preconditioned wave conjugations emerges. Having a balanced charge to potentially compliment either magnetic
or electric conditions, it becomes an all weathered friend.
Nevertheless, the entirety of Creation is completely hinged
upon these two fundamental geometries, the Huntyen
combined with different configurations and arrangements
of Tetra-Terryens creates every condition of Matter that
has ever been observed or shall ever be experienced.
The duality of the wave/particle field has been a sore spot
in the minds of physicist for quite a number of years. Does
Light behave as a wave or a particle, or can it be both? That
has been the question of the ages and finally some truly
needed Light is being shed upon the subject. When I was
a boy, the uncertainty regarding the particle/wave duality was pretty much established and accepted. ‘We simply
didn’t know the answer’ and it was all right, not to know. I
mean there where many mysteries that eluded the minds
of great men and women through out the annals of time.
So, the idea of not knowing the nature of one of the most
basic systems within the quantum field, how waves and
particles interact wasn’t a slight to one’s ego. Yet, this is the
“Electric Age,” an age of Enlightenment and Understanding. Therefore, it is unforgivable for academia to remain in
the dark concerning these basic fundamentals regarding
reality. Each one of these individual states of Matter behave as a particle individually and collectively they behave
as a wave. But make no mistake of it, they are all converging waves. Intersecting and overlapping, expanding and
contracting, oscillating and integrating from the beginning of Creation, until time indefinite.
For those wondering at what scale do these Terryen Wave
Fields occur, the 4 quadrants of the Lynchpin, the place
where 4 curved planes intersect is the birth place of these
5 primary Wave conjugations. These occur within the scaffolding of the Lynchpin as a result of the fluctuating inner
dynamics of the Lynchpin itself and the Lynchpin exists at
the fractal scale, THE SOURCE! These wave conjugations
redefines the notion of ‘Quanta’. Which redefines our understanding of the Plank scale for these wave conjugations
occur at a scale much smaller than Plank. Therefore, the
second and third generational wave conjugations like the
Mira State and the Contracting and Expanding Crystalline states occur at a scale and magnitude much smaller
than the sub atomic scale. These occur within the Invisible
Matter scale because until now they have been impossible
to detect let alone to be completely modeled out in All of
their Glorious Geometry. What I find most surprising is
that the key to these wave conjugations have always been
right within the grasp of Man’s hands, if they’d only dissected the Flower of Life and assembled the pieces in curved
3 Dimensional Space instead of the unreal non-existent
place called 2d. They would have discovered the underlying geometry that is the source of All visible Matter. 
If they had only maintained the simple principal of balance
in their thinking? 1 x 1 would have always equaled a composite number called two. The value of One would have
always been understood and likewise our species would be
millions of years more advanced than we currently are.
This Book is a treatise on the wondrous truths that exist in Multi-Dimensional Universal Geometry. Therefore,
I have tried to keep the conversation as poignant and as
brief as possible and have only included the AllShape, the
Lynchpin, plus 5 primary wave conjugations along with 3
secondary conjugations that expands into an infinite array
of geometric symmetry. With the blessings of the Collective Consciousness there will be many more books to come
with fascinating details that will allow you to peer deeper
into our Multi-Dimensional Electro/Magnetic Universe.
I hope that I have shed a little light upon the subject of
Energy and Matter, and have helped in the search for a
Grand Unified Understanding of Universal Phenomena.
What I am sure of is the fact that I have been privileged
with the blessing of defining the In-Between Spaces, and
contributing to the conversation regarding the true nature of Space/Time, thanks to our Great Mother and Father who loves the curious soul and cherishes the Children
Of Light.
A
NEW
BEGINNING
For the last 6,000 years the Children of Man has wondered
through the darkened corridors of ignorance in want of
heart, in dire need of discernment, along with a desperate need to understand how our Universe truly works and
what is our specific role as a species in its grand evolution.
We’ve meandered in and out of countless philosophies,
enumerable religions and a never ending stream of political idealisms in search of the one true path towards a
sustainable and prosperous existence. Yet, time and time
again we have been forced to sing dirges of sorrow instead
of celebratory anthems of congratulations and conquest.
And again, here we stand, faced with the possibility of extinction due to our inability to responsibly utilize our resources in a sustainable manner, another failed attempt at
being truly successful Human Beings. (Hue of Man)
“Had we both world enough and time,” Cried Andrew
Marvell at some frustrated point in his life cycle during the
later half of the seventeenth century, possibly lamenting a
loss of gaining a potential mate. In like manner, the Children of Man have cried out in sheer desperation for a lamp
for our feet and a light for our road way into the future.
I believe that the illumination that we have so anxiously
pursued comes from understanding that the purpose of
All Created Things in this Universe is to bring BALANCE
to the two seemingly opposing forces that makes up the
foundation of All Existence seen and unseen, Universally
called, “Electricity and Magnetism.” Equilibrium is a necessity if our world is to survive.
Nevertheless, humanity is a fledgling development in Creation. Finding equilibrium with All Other Living Things
in this Universe is essential if we are to survive as a species.
We must first learn to live in balance with All Things or we
will be crushed out of existence by the collective weight
and purpose of All things. Whatever is out of balance will
be either brought into balance through the process of rarefication followed by reconstitution.
Just as the number One is the accumulated sum of All
Things combined and consequently the most important
number of All and from it All other Created things exist.
Then it follows that All the numbers that are derived from
the number One have a share in All of its attributes but in
different ratios. Likewise, All Creating Things in existence
share the same relative rights in this Creating Universe. All
Matter is Alive! All Matter breaths, grows, loves, mates, reproduces, peeks in their relative life cycle and slowly begin
their decay until All that was gathered into One through
positive electrically charging, centripetal gravitative spin
may be dispersed into the Many, through negative magnetic, centrifugally discharging radiation. All this happens
only to be re-gathered together and again re-dispersed until time indefinite. This is the Universal example of breathing in and breathing out, positive inhalation and negative
exhalation.
The soul purpose of this book is to provide the Children
of Man with a taste of what consciousness can offer in
hopes that they may become The Children of Light, “Enlightened Ones.” Whatever the material may be from
which you are reading this book, in Man’s present state
of fleeting moments of consciousness he views that Matter as dead. Yet, if you peer deeply into its texture with an
electron microscope or even deeper and more clearly with
your consciousness, you will see that each and every corpuscle that makes up its structure is still polarizing from
positive to negative.
Every atom inhales with a positive charge and exhales with
negative discharge. Everything is Alive, Aware and Consciously sharing the same feelings and desires as that of
Man, within their own unique Temporal Dimensions and
Relative Way. Yet, we refuse to recognize and respect their
Universal given rights, for that would force Man to drastically change our ego driven perceptions regarding our
Universal neighbors and require a more responsible and
respectful view towards Co-Existence.
Everything that we take shall be taken from us and Everything that we give shall be given back to us in exponential ratios. The insight revealed in this book was gained
through lifetimes full of deep reflection upon existence itself. Along with a profound appreciation for all Creating
Things. As well as having a deep respect for the Sanctity of
Life that is in All Things and animates All Created Things.
There is so much more that the Universe desires to share
with the Children of Man. Nevertheless, Man must first,
“Come in to the Light,” as the saying goes and come to fully appreciate and comprehend the meaning of One! After
this is accomplished, all the secrets of Living Matter and
the Knowledge that can be gained from living in Harmony
with Nature will be revealed, but first “Baby Steps!”
Let us start at the beginning ... 1 x 1 = 2 and 1 x 2 = ?
Since we have been misled on this and so many other issues
concerning our universe then there seems to be another
unanswered question:
What is the true age of the
Universe?
Here's a hint:
It is much,
Much, Much Older
Than you've been led
To Believe.
A Note of Encouragement
Dear World,
This book is presented to you as a gift. In the hope
that the truth will set you free! Just as the Sun gifts its
rays of Light, This book is an offering of Life,
A New Beginning!
"And the spirit and the bride keep on saying, “Come!”
and let anyone hearing say, “Come!” and let anyone
thirsting come; let anyone who wishes take life’s water
free." ...Revelation 22:17
EPILOGUE
As life would have it, All questions have answers and seeing
that ALL THINGS are cyclic, All answers would naturally
loop back to an initial question. I say this out of respect for
Absolute Truth. If you were to consider the thought that
One is the accumulation of All Things then, the truth reveals itself in the most ironic ways. One times One equals
ALL Things because ALL THINGS are the result of
1 x 1 = x.
Therefore, philosophically and literally One times One
would first equal Two and ultimately One times One equals
ALL THINGS which equals One.
Nevertheless, as a species we have not evolved enough
to recognize the value of One. Therefore, how could we
ever fully appreciate the value of ALL THINGS? I believe
that we have to understand the consequences of ACTION
and REACTION before we can begin to understand the
Universal constant of Oneness. So, there is a deeper and
a more complete system of Mathematics that awaits Mankind if we can survive long enough to gain the Consciousness necessary for us to be a sustainable species and be
considered a permanent member of the Universal Family.
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
