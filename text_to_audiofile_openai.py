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
THE CONDITIONS OF ONE
I hope that I have demonstrated how important it is that
we fully understand the structure of One and see it in its
true light and magnitude. On a grand scale One is the accumulative product of All Things combined, yet it is also
the smallest reflection of the Whole.
Albert Einstein called it a “quanta” in 1921, and also referred to it as a “quantum”. We exist in Multi-Dimensional
Space/Time where the basic fundamental states of existence and perception are expressed in 3 Dimensions and
they are height, width and depth. Yet, we cannot perceive
or even begin to measure either of the 3 expressed Dimensions mentioned here without the position from which we
observe the intersection of these planes. A position that is
in and of itself a separate and distinct Dimensional plane
of Space /Time.
Consequently, there are at the very least four necessary Dimensions for anything to exist within the visible Universe.
Four equal and opposite pressure conditions compressed
within a singularly locked position. Each one of these Dimensions applies a Force upon each other and Space/
Time as Newton expressed so superbly, “Every action has
an equal and opposite reaction,” likewise the unseen Matter that occupies Space and Time is being corralled and
compressed by these inertial planes pressing upon one another.
Light was the fastest known substance within the visible
Universe until Birkeland Currents indicated that information in the electric currents traveled at speeds far supe-
rior to light, but light was a good speed to go by. In fact,
through light we observe All Things. Therefore, it is only
fitting for us to illuminate this subject and the structure of
One by its characteristics. Because of the extreme curvature of Space/Time, light waves will ultimately curve back
on to its original position finishing a circuit. Light waves
fan out in all directions, and when they have expanded as
far as the curvature of Space/Time allows and begins to
circle back towards its beginning, the collection of those
closed circuits forms countless ripples of stacked spheres.
Two waveforms or planes may cross each other's paths but
that creates intersecting wave fields that we call a vesica
piscis . Three may cross at the same juncture and that is
called a tri-vesica piscis. Nevertheless, when the 4th wave
field or Light wave meets, at that juncture something new
and remarkable occurs. A living wave conjugation is created, where a recognizable point of life becomes measurable.
That point of life when scaled out will show the place where
4 bubbles or spheres have come together. Where their wave
fields or planes intersect a second shape is born, a curved
sided tetrahedron that I call a Tetra-Terryen Wave state.
The general system that is created where 4 equal and opposite expanding spheres intersect is what I call the AllShape.
I believe the AllShape is the proper geometric representation of the reflection of one.
It is clear to see that all planes overlap in this Universe of
curved Space and potential. All potential is interlocked
with past and future potential.
Just as each ripple in a pond is connected and shaped by
its previous and subsequent ripples, where these waves
meet and interact is the point where Space/Time becomes
measurable.
All visible Matter in the Universe occurs within the confines of the vesica piscis of interacting and intersecting
planes.
ALL THINGS ARE ONE!
At the core of All Things within the visible Universe, the
laws that govern the element Hydrogen dictates the geometry of its consequential by products and shapes. Its
Dimensions are of 4 inertial planes and 4 vertices where
three of the inertial planes intersect with the 4th plane
acting as a respective base from which the vertices arise
depending upon the relative angle from which the structure is being viewed.
This is what the tetrahedron was supposed to represent
but it is missing one crucial factor, curved exterior and
interior angles. The concave inertial planes represent
the centripetal, contractive, gravitative and electrically
charging functions of this geometric structure, whereas
the 4 vertices account for the centrifugal, magnetically radiating and negatively expansive aspects of All Matter.
All Matter is both expanding and contracting as per the
Universal Prime Directive of Existence. All Matter must
be congruent with all other Matter: meaning, “Everything
has a common denominator and can be reduced to its lowest term.” Find the common factor (quanta) and either
multiply or divide. “Expand or contract by said ratio.” The
common factor of our Universe is the structure of “One!”
Once we are acquainted with the true attributes of its nature, ALL THINGS become as ONE THING.
ll Things are One!As Hermes never tires of telling us, over, and over, and over again,
the One Thing and the One Mind are One. He means that mind and
body, Soul and Spirit, male and female, positive and negative, Above
and Below, are all One. All sexes, all races, all species, all life is One.
All life, all death; all heroes, all villains; all angels, all demons; all
gods, all devils are One. Unless you find this One within you, "what
the alchemists called the Stone" you cannot escape the continual
dance of becoming that is duality, even for an instant. That is the
message of the Ouroboros. That “All Is One” is the basis of the alchemical principle of changing one thing into another, and alchemical transformation would not be possible unless everything were
really One.
ONE LAST MOMENT OF REFLECTION
Let’s recap:
1) We know by definition alone that to Multiply means, “To
make many or manifold; to actually increase the number or quantity.” Therefore, it must increase in size and
quantity, or it is not multiplication.
Consequently, 1 x 1 = 1 could never be a part of the multiplication table because it fails to satisfy the definition
of the term to ‘multiply’. So, by definition alone we have
clear and rational proof that 1 x 1 can never equal just 1.
We also know that 1 x 1 =(ing) 1 is a false answer because
the associative and commutative laws were not properly
followed which left an unfinished and unbalanced equation. Also, the “Identity Property” has thus been shown
to be based upon an uninformed biased and arbitrary
preconception that has no relative value in light of observed natural phenomena.
2) Although it is an acceptable phenomenon in the mathematic community for the square root of a number less
than 1 when added to itself to be greater than the initial
number squared ... We are discussing the number 2 and
its square root when added to itself should never exceed
the initial number. For that would be highly irregular
and completely unacceptable, even in the loose fitting
constraints of the laws of our current system of mathematics. This anomaly is not acceptable for any thing
that exists within the physical Universe beyond our
flawed system of mathematics, meaning that no other
system or organism within our known Universe behaves
as our numeric system, where (1) is massless, weightless, without spin and lacking of any measurable effects
when it interacts with itself or any other number that
is derived from it, this ultimately prevents the square
root of 2 from having the natural and logical answer
of (1). Remember: “An object must be equal to the sum
of its parts, it cannot be GREATER than nor LESS than
itself.” This is just simple common sense! Therefore, the
square root of any given number when added to itself
should never exceed the initial number, if it does then
we have over reached and the true square root of that
number has failed to be satisfied.
3) Newton’s uncontested 3rd Law states: “Every action has
an equal and opposite reaction.” Therefore, 1 x 1 = (ing) 1
is a violation of Every Natural Law regarding “Cause and
Effect” within the known Universe. Consequently,
1 x 1 must = at the very least 2.
4) The Pythagorean theorem postulates that:
a² + b² = c².
This unfortunately corners mathematics into a stalemate of short sighted reasoning because the side and the
diagonal of the square become incommensurable if both
sides are positive integers.
5) Euclidean Geometry gave birth to the Platonic Solids which
were constructed with straight intersecting lines that do
not exist in our Universe of curved Space/Time. Attempting to describe our world and the underlying structure of
the Universe by straight lines, seems as futile an attempt
as someone trying to capture the complexities of the entire human anatomy with stick figures: it produces only a
crude depiction of the true reality. Remember: ‘All energy
in the Universe is expressed in motion and all motion is expressed in waves and all waves are a function of a vortex (a
spinning whirl pool) and all vortex functions are curved.
There are no straight lines in the Universe. Therefore,
there aren’t any straight lines in Universal Mathematics.
So there you have it, five logic provoking reliable witnesses
that testify to the unreasonable and illogically flawed bases
that governs Man’s thinking upon these matters and is also
the foundation of our system of multiplication.
As they say, “The proof is in the pudding” right? Well, I’ve
served up a smörgåsbord of pudding from every corner of
science, mathematics and everyday culture. All prepared
fresh and to perfection. I pointed out many of the stumbling
blocks that have circumvented our reasoning faculties and
have held us captive through ignorance and arrogance.
I believe that I have shown convincingly that 1 x 1 ≠ 1. Yet,
it is quite likely that many of this generation will cling to
the vestiges of this lie simply because my argument challenges the status quo and threatens the established order
of things at present. Just as the history books continue
to propagate the lie that George Washington was the 1st
President of the United States when in fact John Hanson
was elected the President of the United States by the Continental Congress Assembled on November 5, 1781, the
first of seven one-year termed presidents. Some things just
never change.
I understand that our entire world economy is based upon
1 x 1 =(ing) 1 and that if Mankind were to amend this one
equation, it could pose significant challenges to all currency based societies. All institutions of higher learning
would have to reform and completely re-evaluate their
understanding concerning mathematics. Also, every student might think a little less of their instructors for having
missed something this obvious.
Nevertheless, think of the lost millenniums spent chasing this conspicuous lie. We have spent the last 6,000 years
shrouded in darkness concerning Universal Mathematics.
Think of what could have been achieved had we avoided
the stumbling blocks of the platonic solids and the irrationality of irrational numbers? As I said before, a future
generation will benefit and they will shake their heads at
this one as we do the generation that championed slavery
and blood letting!
Oh, I forgot, there is a another important inconvenient
truth that I think I should mention concerning this interesting topic of 1 x 1 and what it equals. A small paradox
that deserves consideration in this argument. I had hoped
that by reason alone, along with a good round of sound
judgment that I might persuade the minds of Man to rethink his current position on the subject of 1 x 1 =(ing) 1
and help Man return to the mental clarity that was initially
responsible for setting Homo sapiens apart from the rest of
the animal kingdom. I sincerely believed that if the truth
was presented in simple terms with convincing argument
and with a compassionate undertone, that it might stir the
thinking part of the human mind to correct Mankind's current misguided course.
I hope that I haven’t overestimated the grasp of this generations reach and that my argument hasn’t exceeded the
grasp of the common man and woman, who shouldn't be
afraid to think outside of the parameters that has been set
by the “Keepers of Knowledge.” I hope that these men and
women find my argument to be refreshing and perhaps
they will comment that, “There was always something
about the square root of 2 that stumbled us a bit.”
You see the ‘Common Man' remains open to new ideas
because their view of self is not limited to the titles or letters that precede or follow the spelling of their names.
The 'Common Man', which I am a proud member, stands
armed with his common senses, always willing to sharpen
his tools of discernment which ultimately will enrich his or
her understanding. Having a willingness to grow and to be
nourished by new concepts concerning our ever changing
reality, this is the underlying force that could very well propel our species into a promising and never ending future.
Yet, the cup of those unwilling to grow past the dried up
streams and empty wells of yesteryear is oftentimes filled
to the rim with stale, recycled, and regurgitated axioms
of bygone days. Their minds and hearts are contaminated
with the elixir of traditional thinking, indoctrinated with
antiquated reasoning which prevents them from sipping
fresh, clean, unadulterated water and possibly quenching
a 6,000 year old thirst for truth and understanding.
Therefore, I feel that it is my moral duty as a father and
grand father to present the truth about the square root of
2 and the true value of 1 to this generation and expose this
loose thread to the Children of Light!
For those hard headed individuals, I have saved this proof
for you. If you will recall, the square root of the number
2 as prescribed by mathematicians and programmed into
our computers is 1.414213562373095...
And if you multiply it by 2 the result is 2.82842712474619 ...
Also, that 1.414213562373095... when cubed gives us the
same answer as if we added it to itself, 2.82842712474619...
Well, oddly enough, this 2.82842712474619 ... is also the
square root of the number 8.
Now this seems a bit convenient doesn’t it? How about this
guy for a “Utility Player” Mr. MVP of Mathematics? How in
the world can this irrational number fill all these missing
Spaces? Could it be from Krypton, like Super Man? Lets
put it to the test and see if it weakens.
The Square root of 2 is: 1.414213562373095...
Cube it or multiply it by 2 you get: 2.8284271247461894...
Divide it by 2 you get: 1.414213562373095...
Cube it again or multiply it by 2: 2.8284271247461894...
Divide it by 2: 1.414213562373095...
Cube it or multiply it again by 2: 2.8284271247461894...
It doesn’t budge? Holy Crap! This is "The
Number of Steel!” Any number above the
value of 2 in which you perform the same
sequence of actions, by the 7th consecutive
cycle the number balloons into the trillions.
Any number below the value of 2 is reduced
to an exponentially small value within the
same number of sequential steps.
Point being, all numbers should change drastically when
cubed and divided, and again, cubed and divided, either increasing in quantity or decreasing, within a few predictable
steps.
Yet the square root of 2 when cubed returned to
2.82842712474619 ... two hundred and sixteen times and
could perhaps continue in this programmed loop until infinity!
This must be the most magically, marvelously, enchantingly blessed and perfect equation that has ever been written.
Or perhaps the biggest and most hurtful lie ever told...
What ever the purpose of this manufactured number that
masquerades as the square root of 2 and the reasons behind
the creation of this irrational loop, I don’t know and I will
refrain from speculating or partaking in conspiracy theories concerning things for which I am not in the loop.
Yet, we all have a responsibility to teach our children the
truth, and this loop is not the truth. It is a mathematical fallacy and unreality that lacks the ethical benevolence of the
sweet fabled stories that we fantasized about as children.
Stories that taught us the lessons of compassion, mercy,
human kindness and integrity. Any self respecting teacher,
professor or institution of learning that would continue to
propagate such a blatant unreality without investigating
these matters should be ashamed of themselves. For their
crime is against the innocent and against our entire species.
Well, I’ll put it this way, “If you mislead One Soul in this
life then you have to pay for that Soul.” For every Soul that
is misled by your actions, you have to pay for that Soul a
multitude of Lives filled with the collective karma from all
the refractive waves that you are responsible for generating.
Its like a heat seeking missile sent with a GPS heading instructing it to “return to sender.” Think about the karma
from mis-educating billions of children.
Yet for now, the fairytale of the phantom number 1, the
most popular and most (impotent) number within the
whole number kingdom along with the square root of 2,
its trusted companion that lives free of board from all responsibility of Universal Law, will continue to defy logic
and reasonability for a short time more. Actually, only till
the end of this book.
Because, even now a Day Star is Rising and the Sun is soon
to overtake the darkness of night and the Light of truth
will spread multiplying across the Heavens. Ushering in a
New Spring where the truth will take root and all the numbers we love will live happily ever after.
My Mother and Father taught me that, “If you break
something, you have the responsibility to fix it.” Well, I
didn’t break mathematics, I only reported a malfunction
in its system. Yet, I did offer the solution to the problem
and hoped that my suggestion would be taken seriously.
Nevertheless, for over 4 decades I’ve tried to reach the
soft tissue of Mankind's petrified and hardened hearts
and have been met with nothing but ridicule and insults.
Therefore, I hope that a future generation will Stop, Look
and listen to their hearts and hear what the truth is saying.
Which leads me to something else that my parents taught
me: “You don’t start something unless you intend to finish
it!” So, here goes: I have spent a number of pages, reviewing many of the laws that have helped countless others
including myself to reason upon the foundation of logic,
which is always anchored in truth. I have also pulled at
some of the loose threads that I believe has made the fabric of our understanding of the Universe tattered and full
of holes.
I sincerely believe that this book will help Mankind to
have faith in the value of One, once it is fully understood
and embraced by our reluctant world historically so resistant to change. In view of the fact that we have entered the
winter and perhaps the last season of our species. As described so definitively by Robert Lawlor in "The Geometry at
the End of Time".
Yet Spring is near and with it comes New Light and a fresh
perspective to help raise the number 1 to the magnitude of
its worthy glory! The Glory deserved of the Progenitor of
all Numbers and the Children of Creation.
I have spent a considerable amount of time breaking down
and tearing apart the foundations of the platonic solids.
And who knows, perhaps these concepts of straight lines
were necessary for a species such as ours when we were
still struggling in our infancy.
Seeing that we live in a 3 Dimensional perspective, maybe
this stage of our evolution requires 2 dimensional steps
and the illusion of straight lines act like bumpers in a
bowling alley until our species can handle the curve of a
ball and the incredible dynamics that come with its spin.
The Apostle Paul, in his first letter to the Corinthian Congregation in chapter 13, verse 11, encouraged the Children
of Man to continue growing in their understanding with
these words, “When I was a child, I used to speak as a child,
think as a child and reason as a child; but now that I have
become a Man, I have done away with the traits of a child.”
We have a responsibility to ourselves and to future generations to clear away the stumbling blocks and to remove the
training wheels so that we can advance to maturity.
For a few millennia and perhaps even longer 1 x 1 = 1 has
stood as the foundation stone for Man’s short sighted concepts regarding linear constitutions which gave rise to our
present system of mathematics. A system that has its base
rooted upon the platonic solids. A system that has allowed
Primitive Man to describe our Universe in stick figured geometry with only two dimensional perspectives. Yet, that’s
not all it has allowed. It has left Mankind vulnerable because we didn’t know the truth about how our currency is
at risk of being miscalculated.
While writing this section of the book I asked a colleague
and studied mathematician to turn his well honed insights
onto the subject of the square root of 2.
We had only recently become acquainted over about a
year's time and had spent a considerable amount of that
time discussing the abandoned and untraveled corridors
of the foundations of geometry and physics. In the course
of our sometimes very heated debates we developed a mutual respect for one another which ultimately culminated
in our becoming friends.
He had been a staunch supporter of the square root of
two being an irrational number and had stated numerous
times in the past that, ‘perhaps the craziness associated
with its value was an inherent quality of the root of two’.
Well, in all fairness, I asked him to point that sharpened
sword of truth towards 1 x 1 = 1 and the root of 2. It took
the entirety of the year for him to accept this challenge. I
asked him to: “Question the foundation and the supports
of everything that he believed in to see how strong his
foundation could truly become.”
This was his response:
“I suspect foul play, as the notes I composed are nowhere
to be found. However, I took this opportunity to reposition
my voice and the result pleases me! I hope this suits your
needs my friend. :)”
Just as the symbol 2 signifies the combination 1 + 1,
the symbol for the square root of 2 satisfies the equation x*x = 2.
On a larger scale, the history of human numbers has
largely been the journey from concrete reality into the
imagination. Does this equation have a solution? Can
it? We have repeated this cycle in our passage from the
natural numbers to the integers, introducing negative
integers; in our passage from natural numbers to positive rationals, introducing ratios; in our passage from
rational numbers to algebraic numbers, introducing
roots; in our passage from algebraic numbers to real
numbers, introducing limits; and in our passage from
real numbers to complex numbers, introducing solutions to the equation x*x =-1.
So great is history’s momentum that we take these
number systems as universal truth. Why? Indeed, any
mathematician with an understanding of category
theory and abstract algebra would object to the special emphasis placed on these particular systems. They
are useful in some applications, and are fallaciously
applied to all situations. If you would but open your
eyes, never again would they close. Society’s strict adherence to the artifacts of number history strikes the
enlightened as suspicious.
How did the square root of two come about?
We must journey to the time of Pythagoras and his
followers. Flat geometry was beginning to sprout in
Western minds. Of particular importance was the
right triangle: a triangle with orthogonal edges, meeting at a “right angle”. What we now call the Pythagorean theorem was being explored, and a simple situation was laid out: consider a square with sides of
unit length. If its sides are of length 1, then what is the
length from one corner to an opposite corner?
The Pythagorean theorem states that this diagonal D
should satisfy the equation:
D*D = (1*1) + (1*1)
Here we see the genesis of defect, an assumption that
would be ignored for thousands of years. In trying to
solve this equation to find the value of D, the value of
1*1 was taken to be 1. But what of the unit that I previously called “length”?
The products of a unit length with another unit length
must have units of area. A choice was made, and then
taken to be arbitrary. This could not be further from
the Truth.
What happened here? It would help us to use modern language. Credit should be given to the great 
Hermann Grassmann. This man worked to clarify the assumptions and language of the physicist of his day.
By his contemplations, multilinear algebra arose. In
laying the foundations for this formal system, he was
the first to contrast the algebra of linear Spaces and so
also the first to suggest nonlinear algebra!
Today, Grassmann’s work is called geometric algebra.
It has become a mainstay in modern physical theories,
and only recently have people begun moving outside
of the boundaries exposed by this brilliant soul. Grassmann recognized that vectors cannot be multiplied
naturally or canonically. A choice must be made to
equip a vector Space with the structure of an algebra.
Had the Pythagoreans accessed this perspective, they
would have realized that 1 length may be an area of
any chosen unit!
Sure, setting this product to be 1 unit of area seems
natural, but this is only because we have grown accustomed to this convention. Studying the universal
properties of Grassmann algebras, alternating algebras, and Clifford algebras-these all being categorical
quotients of freely generated tensor algebras - illuminates the student and reveals the great deception that
we have allowed ourselves to slip into.
Whether this series of events was orchestrated or malignant is for others to determine, but I can speak with
certainty on the status of our numeral and coordinate
algebras.
They are curious artifacts, and we are ants toying with
scraps of the Logos.
If the square root of two satisfies:
x ² = x*x = 2
then our arithmetic conventions allow us to simply
write it as:
2(1/2) .
In this way:
(2(1/2)
)2 = 2(1/2)*2 = 2(2/2) = 21 = 2
Thus:
(2 (1/2)
)3 = 2(3/2) = 2(1+(1/2)) = 2*2(1/2)
The cube of the square root of 2 is equal to twice the
square root of two. That is to say, the square root of
two is also a solution to the equation:
x³ = x+x = 2*x.
Such equations are unnatural, and our investigations
of the Cosmos will dissipate so long as we project this
archaic system upon it.
Finally, my fellow mindless puppets, (and believe you me,
I say that with great compassion, for I am with you and
have been with you from the beginning), we have reached
the bonus round and boy do I have a doozie for you!
I said that our entire world economy was rooted in a mathematically flawed foundation of 1 x 1 = 1, which I believe
was successfully demonstrated in the opening pages of this
book. I also stated that there was a "loose thread" which
was capable of unraveling the very ground rules of mathematics. One of those ground rules was the Euclidean 2d
perception of reality.
Another is Academia's beloved "Platonic Solids". As previously stated there is a very real and immediate danger
that this loose thread, if pulled, could cause the collapse of
our global economic infrastructure and possibly bring the
entire world of science and mathematics as we know it to
an ugly and violent end.
If you don't believe me and you think that this is all just a
mental exercise, go ahead to the next page.
As Rafiki said in the Lion King:
"It is Time!"
It is time to finally face the truth and continue our necessary audit of our incredibly flawed monetary system that is
linked to our misunderstanding of Universal Mathematics.
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
