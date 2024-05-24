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
RELATIVE FACTORING
AND USEFUL INSIGHTS IN
DEDUCTIVE REASONING
"When the ancients considered the process of mathematical
multiplication, their mode of calculation had a direct relationship with natural life processes as well as metaphysical
ones. Schwaller de Lubicz called this mode the "principle of
the crossing" (we continue to symbolize multiplication with
the sign of the crossing: x)."
"This crossing was not a sterile, mental, numerical manipulation but a symbol for the process by which things enter
into corporeal existence. All birth into nature requires a
crossing of opposites. It can be the crossing of vertical and
horizontal lines, which give birth to the square, the first
measurable surface; or male and female, giving birth to
a new individual; or warp and weft, creating a fabric; or
light, and darkness, giving birth to tangible forms; or matter and spirit, giving birth to life itself."
"Thus the vital linking up of the mental abstraction of calculation with its counterpart in natural phenomena gave
the ancient mathematician a living and philosophic basis
for his science."
Insight
The ability to look into a situation
beyond the obvious and discern the outcome.
The number One is the very first quantity of any measurable Space. The lowest cardinal number, because half of
two is one. Also, it encompasses all of the total potential
energy within the entirety of what we call visible Matter. In
astrophysics, this is expressed in the notion of the “singularity”, where everything is compressed and represented
within the quantity of the number One. (singular)
Now, there are many within the scientific community that
would say, “You cannot equate numerical values to physical occurrences.” This is what Dr. Neil Degrasse Tyson told
me. They assert that, “The use of mathematics is more of
a tool for measurement and not the measurement itself.”
The ancients and nature disagree wholeheartedly! The assertation is that the term “Singularity” is not a literal term
but more of a concept and cannot be viewed as a quantity.
To be perfectly honest, the entire notion of a Singularity
where all Matter collapses upon itself, and all the laws of
physics breaks down is inconsistent with natural phenomena, and lives more in the 
realm of science-fiction than reality.
Yet, many within the field of astrophysics firmly ascribe to
this imaginative mathematical impossibility. What is this
thing called One and how can it or the concept of it be
shrouded in so much mystery and controversy?
The number One actually has the same foundational and
patriarchal relationship with all other numbers that are
descended from it, just as the element Hydrogen has with
all other elements that occur after it, it just so happens to
be the most abundant element within the known Universe.
In view of this relationship let’s compare our number sequence to the periodic table and the elements that make
it up.
THE PERIODIC TABLE OF ELEMENTS
In our number system, all the numbers have something
in common. Every number following the number One is a
product of the number One.
If we were to use our human bodies as an example, we
would see that the human body is a collection of trillions
of cells. Some of the cells look very similar, yet there are
different cells for every different part of our being. In the
simplest terms and most convenient definition, a cell is the
smallest component of an organism. It is self contained
within a membrane and in every multi-celled organism, a
number of cells work in conjunction for the benefit of the
overall organism.
The smallest component of a cell for the purpose of this
discussion, we’ll say is an atom. As each cell has a nucleus and an outer membrane, so does each theoretical atom
have a nucleus and something that functions like an outer
membrane. Let’s take a closer look at some of the inner
structures that make up an atom.
Atoms are the basic units of a chemical element. They are
believed to be composed of three basic particles: protons,
electrons and neutrons. Neutrons and protons are theoretically heavier than electrons and live within the center
of the atom, an area that is commonly referred to as the
nucleus. Every single element within the visible Universe
has a common ancestry with the element Hydrogen, which
is the first visible element within this Universe followed by
a series of subsequent elements that all share a commonality with this first child of the visible atomic world.
When I was a child the Periodic Table of Elements had just
over ninety two elements. Now a days, the periodic table
extends into more than a hundred and twenty elements.
Some of these elements can only be produced in a lab and
have a life expectancy of thousandths of a second. Some
of you may be asking, “What is the Periodic Table of Elements?”
The periodic table of elements refers to a series of motion and pressure conditions that occurs with regularity
or with a degree of predictability and the effects that they
have on Space and Time. Take ice for instance, it regularly occurs with some predictability in the winter or in geographic locations that are closer to the poles. 
Meteorologist can often predict with a certain degree of accuracy
in their weather forecast when and where icy conditions
will present themselves. That is what the periodic table of
elements does, it predicts and charts the atomic structure
of elements based upon certain conditions. This could be
based upon the number of theoretical protons, neutrons,
electrons and so forth that it supposedly posses.
Let’s stick with the analogy of ice for a moment. Say for
instance that you wanted to create ice? Do you have to
provide water in order for ice to appear. Not necessarily,
because on most occasions if you create the conditions of a
cold enough environment, the ice occurs as a result.
The moisture within the molecules of air collect together
and freeze and 'voila', ice is served. Therefore, if you provide the conditions that occur at the surface of the Sun
relative to the heat, pressure and it’s angular momentum
(thats just a fancy word for ‘its spin’) the element Hydrogen occurs. Hydrogen (in the simplest light as told by
modem science) is believed to have 1 proton and Helium
being the second known occurring atomic structure within this table is composed of 2 protons at its nucleus, per
modern science. Lithium the 3rd visible atomic structure
in the table is reported to have three protons. Beryllium
has 4 protons and every subsequent element follows this
pattern all the way down the periodic table until the very
last known element.
The protons that make up the Hydrogen atom can be gathered into an unstable configuration as is the case with the
radioactive elements of Uranium which has 92 protons and
Plutonium with 94 protons. These protons are always followed by an entourage of theoretical neutrons and elec-
trons. They can collect together under a more comfortable
setting as in the case of the element Carbon which is believed to have only 6 protons. It is generally taught that Carbon has only six neatly arranged protons, with six neutrons
wrapped in six perfectly organized electrons. The element
Nitrogen has 7 of each of these so-called sub-atomic particles, while the element Oxygen has 8 of each. Are you
starting to get the picture?
With this perspective in mind, lets consider the planet
Mercury and its relative pressure and motion conditions
being situated so close to our star. It is under the greatest
pressures of any planet within our solar system.
Here we have a giant ball of Iron for the most part, where
each Iron atom is the accumulated sum of theoretically 26
protons carrying 26 neutrons along with 26 electrons as
they tour the solar system in their collective orbits around
our Sun. Twenty-six protons compressed into a very small
amount of Space wound so tightly that we think of it as a
different substance from its base element Hydrogen. Under significantly lower pressure conditions, somewhere
between 141.6 million miles and 483.8 million miles away
from the Sun and just south of Mars and north of Jupiter,
the first visible element Hydrogen is freed from its confinement of greater pressures near the Sun in the case of
Mercury. Its supposed single electron can occupy a much
wider orbit and exists as a free standing Hydrogen atom.
Under these low pressure conditions the element isn’t
forced to transmute into a (seemingly) different element.
Transmutation from Hydrogen to Iron is the direct result
of complex motion conditions believed to be caused by
26 protons, neutrons and electrons jousting for position
within a very small and confined Space.
Consider what happens to Hydrogen in the case of our gas
giants like Jupiter at 483.8 million miles from the Sun and
Saturn at 888.2 million even Neptune at 2.795 billion and
Uranus at 1.787 billion miles from the Sun. Under the limited influence of lower pressures from the Sun in a more
vacuous environment, Hydrogen atoms expand and become more tenuous in their configurations.
Abounding in it’s endless supply of what to the naked eye
appears to be empty Space, but we know that there is no
empty Space in Space. Nevertheless, under these conditions Hydrogen which makes up most of these planets upper atmosphere can remain in its most comfortable state,
a mono (single atom) or in a diatomic (2 atom) configuration. Yet, deeper into the planet the extreme pressures
from the weight of the atmosphere force Hydrogen atoms
to change from a gaseous state into a liquid state and eventually form into a metallic state called metallic Hydrogen.
Just as Carbon can transform from a gas state as methane,
into a liquid state as oil, from there to a solid state as coal
and into a more compressed state as a diamond.
Likewise, all the elements adjust to their individual pressure and motion conditions. But do not be misled, for all of
the planets and everything that exists within the Sun’s heliosphere from Mercury to the theoretical Oort cloud that
borders our solar system, they are all direct descendants of
the Hydrogen atom. Every single thing that we see in our
Universe from the most distant star to the nearest moon
owes its existence to the pressure and motion conditions
responsible for Hydrogen. Everything visible, no matter
how complex is composed of the atomic sub-structure
of Hydrogen atoms existing under different motion and
pressure conditions.
If the Universe followed Man’s rules concerning multiplication, Hydrogen times Hydrogen would only equal
Hydrogen. Then, diatomic Hydrogen would never come
into being which is a precursor for water. According to
academia’s present believe concerning nuclear fusion, it
takes 4 Hydrogen atoms to make 1 Helium atom. Again
an unsustainable process.
If nuclear fusion was responsible for the distribution of
Matter throughout the visible Universe no other element
would ever come into existence because Helium and its
initial isotopes are very stable and monatomic in nature,
so the Universe would quickly run out of building materials necessary to form the rest of the elements found
within the periodic table. This ‘catch 22’ is the result of
Man’s mathematics being rooted in the
“IDENTITY PROPERTY.”
A misleading imaginative construct that negates all observed Universal phenomena. Just another one of those
inconvenient truths that I am sure deserves some reflection but we have to keep pushing ahead. There’s still so
much more to see on this journey towards the truth concerning the square root of Two and the value of One.
Based upon the laws of the “IDENTITY PROPERTY” how
does diatomic Hydrogen come into existence? Diatomic
Hydrogen is a condition that Hydrogen is most observed
in and it is not the result of them being added together.
Modern science states that:
(H x H = H2 = Diatomic Hydrogen)
If, (H) x (H) = H2 then 1 x 1 = 12. This is called a covalent
bond, the sharing of electron pairs between atoms. They
multiply their forces against each other with every polarization causing their effects to multiply indefinitely.
Likewise, with the number One every other number within the number system is the number One under different
motion and pressure conditions. Lower pressures allow the
number One to stand alone or in diatomic pairs where it is
most comfortable. However under higher pressure conditions the number One can coalesce into the trillions. The
point is, that like Hydrogen and its subsequent elements,
every element made from the Hydrogen atom follows the same rules of conduct as Hydrogen 
and are likewise predictable based upon Hydrogens particular mass, weight,
charge and its spin. Each element that is descended from
Hydrogen must also follow the laws that govern Hydrogen
concerning the relative Space that it occupies and its
PRF or Prime Resonant Frequency.
These attributes account for its consistent oscillations, it’s
polarizing swing from positive to negative charges and its
predictability as to when it shall occur and with what frequency. That is why it is called ‘’The PERIODIC table of
elements.”
Yet, the subsequent numbers that follow the number One
all seem to be based on a phantom number because the
number 1 will not interact with itself in multiplication and
it will not interact with any other number for that matter
based upon the current rules and understanding of multiplication in mathematics.
Let us take a closer look at this pathetic circumstance
of "1 x 1 =(ing) 1". It is easy to see
why Harry Nilsson wrote an ode
to the number One in, “One is the
loneliest number that you’ll ever
do!” Can you not feel the loneliness of this number? It can’t even
affect itself. Which means it must
be void of weight, have no mass,
nor measurable motion, no color, nor taste, not even a
slight heat signature or any other characteristics of measurable dimension what so ever! And yet, every other
number is based upon its constitution or lack thereof.
How can this be? The logical conclusion is... “It cannot
be!”
In the process of writing this book I was asked by Brian
Grazier, “How does any of this effect me? Why should I
care whether 1 x 1 = 1 or 2? Is this just a mental exercise?”
Well, let’s look at it in terms of everyday mathematics, our
money.
“Does page 161 look like this is just a mental exercise? ( “I
didn’t think so either!)”
Trust me, we’ll get back to this. Let us address this important topic one page at a time. But I’m quite sure you can
clearly see that this question concerns EVERYONE.
ELEMENTARY LAWS CONCERNING THE USE OF GRAMMAR
I ask that you please take a moment and consider this line
of reasoning, if you will.
If multiplication is truly rooted in addition as common
sense informs us then the 1st rule of addition must be the
first rule of multiplication and that first rule should always
be applied. The 1st rule of addition simply put is to ADD!
Like the old saying, “When in doubt, see rule #1.”
Then in all reasonableness, how can 1 x 1 = 1? The way it
has been explained to us is that we are seeing (1) only one
time. Well, we have a term for that don’t we? It is called,
“ONCE” and is defined as a (noun) and means: “A single
occasion, one time only.” So why is it phrased as a plural
interaction if we are seeing (1) only one time?
In long form writing it is expressed as follows “One time(s)
One.” Do you see the (s)(s)? If we are only seeing one number once, then why is there a need to add the (s) to the
multiplicative indicator?
The (s) indicates that it is plural, meaning “more than
one.” Why go through the superfluous act of including another (1) if we are only seeing a single, lone number? 
I understand, it is hard to admit that you’ve been misled about
something as important as this but for the sake of putting
this question to bed once and for all lets be thorough.
What were some of the other excuses that we were told in
order to justify 1 x 1 = 1 ?
I am sure that we’ve all heard the same explanation when
we asked this question, “How can 1 x 1 = just 1? My second
grade teacher told our class that, “We should imagine that
you are looking at the number 1 in the mirror.”
Okay:
How do we see an object in a mirror? Well, a mirror reflects Light waves, right? What exactly is this thing called
Light? Light is an effect of electromagnetic radiation that
falls within a particular portion of the electro/magnetic
spectrum. The term (Light) usually refers to visible Light,
which is visible to the orbital organ called the eye and is
responsible for the sensation of sight.
Without all the mumbo jumbo, Light is an illuminate substance that allows us to see. According to modern science
and by most estimates, humans can see about 0.0035% of
the electro/magnetic spectrum. That’s less than one percent of the known Light spectrum, which includes radio
waves, x-rays, gamma rays, infrared, ultraviolet, microwaves ... , the list goes on and on.
Human Beings see only a tiny fraction of the electromagnetic Light spectrum. This means that, if Humanity took a
Universal eye exam, as a species we would be considered
blind! We would not be allowed to operate a cosmic vehicle and would also need the assistance of a guide as it were
to accomplish anything that depended upon vision. Yet,
we judge most of our world and experiences by what we
see or in Light of this information, what we truly fail to see.
Consequently, how much can we trust our view of our
world and of the Universe as a whole based upon this limited vision? Also, how can we have complete confidence
in many of the conclusions that have been derived from
results based upon our limited tools of perception?
All Visible things are composed of the properties of Light!
Therefore Light is the source from which life springs and
should be revered as such. This is what the equation E = MC²
is ultimately illustrating, that Energy equals Mass times the
velocity of Light squared.
All Things are Light, Everything just happens to be Light
existing under different motion and pressure conditions.
In other words, depending upon the speed by which Light
travels through a particular medium (The rate by which it
reproduces itself) along with the density and conditions
of that medium it is traveling within, these are the factors
that determine its relative nature and the temporary manifestation in which you experience its 
materializing properties through Crystallization.
This occurs because Light waves exert enormous pressures
waves upon Everything it encounters which ultimately
freeze and crystallize into every form of visible Matter depending upon 
the pressure and motion conditions of that system.
The Light of 4 gyroscopic waves interweaves those forms
into the predictable patterns of Polarized Pressures of
Light. Water can be experienced as a solid when the pressure is low and it is under a limiting motion condition
which creates a cold enough environment for water to exist in the form of ice. Under warmer conditions between
32 degrees Fahrenheit and 212 degrees Fahrenheit it is
represented in a liquid state. From 213 degrees Fahrenheit
and higher it appears as a gas or vapor. Nevertheless, it is
still two atoms of Hydrogen and one atom of Oxygen, just
under different motion and pressure conditions. Likewise,
Light is effected by its particular environment and affects
its particular environment in concert.
What may be more shocking to the reader is this fact,
“Living things must consume living things”. Therefore,
it is reasonable to conclude that since so many organisms
feed directly from Light, then perhaps Light itself is also
Alive! Just something for you to reflect upon.
I think that I’ve given a sufficient enough picture of (Light)
for us to continue our conversation regarding 1*1=x and
how Light interacts with a mirror. In order for us to see the
number One in front of a mirror we need to employ the
use of Light. Well, how does Light interact with a mirror?
If we were to place a candle in front of a mirror and used
a Light sensor, the measurement of Light observed will be
more than the Light produced by one candle. It does not
measure as only one Light source we actually observe multiple sources. A Light meter will show almost twice the in-
tensity of Light. Any reduction if any, in the measurement
of the Light's intensity is due primarily to the position of
the Light meter from the mirror and the fact that no man
made mirror is ever 100 percent reflective. A spectrometer will show two separate spectra that fan out in multiple
rainbows.
Again, if we are discussing Light and the unquestionable
constant of the speed of light, a measurement that we are
told is unchanging. Light is believed to travel faster than
most things within our 3-D Universe. Due to the seemingly instantaneous transference of information across the
electrified Universe as observed in Birkeland Currents, we
know that electricity is not limited to the speed of Light, it
is much faster. Yet, Light a radiative product of a magnetic
interaction isn’t doing so bad coming in a close second. Remember, Radiant Light moves in the opposite direction of
Electricity and Light’s centrifugal expansion is at a higher
ratio than the centripetal contraction of Electricity, which
leaves behind the effects of gravity, as a by product!
Now, if Light reflected in a mirror, proves that a mirror
creates two separate effects then we are informed once
more by this natural phenomena that
One times One equals
More than just One.
ets hear what sound
has to say on the
Matter.
SOUND AND ITS WAVE DYNAMICS
Let’s add Sound into the equation.
Pythagoras has been quoted as saying, “A rock is nothing
but frozen music.” Therefore, a rock is compressed sound
waves that have mass, weight and dimension.
If we say aloud, One times One we have created two separate and distinct wave forms.
Two separate individual frequencies that will travel from
one end of our Universe to the other and will touch Everything in between and will not come to rest until it has
registered its frequency in Every Structure within the seen
and unseen Universe. This is the nature of Everything in
our Universe being connected to Everything else.
When one atom polarizes, Every other atom in the Universe must not only register its change but must likewise,
adjust to its particular charge, spin and the relative mass
of the new pressure condition. It may take hundreds of
trillions of years for All the atoms within our Universe to
equalize to the new pressure arrangement.
Picture in your minds a pebble being dropped into a lake.
Regardless of the size of the lake or the size of the pebble
that disturbs its surface, the pressure waves that are created
will fan out in all directions until they eventually reach the
shore, at which point the pressure waves will begin their
journey back towards the center of the initial disturbance.
Even if the ripples are invisible to the naked eye their journey is still the same. 
If two pebbles are dropped into the Lake they will produce two separate pressure waves that
will behave the same as the initial wave traveling to the
edge of the lake and back to the center again.
Well, in the case of sound waves, the ‘Lake’ is the fabric
of Space and the pebbles are our voices. Frequency never
stops until it has registered its vibratory information into
All Things in existence.
Its wave lengths and amplitude may become so low that it
is imperceptible to the human ear or by any other means
of Man’s measuring devices but it will continue its journey
until time indefinite. Continually displacing Every atom
in its wake until it reaches the edge of our atmosphere at
which point it interacts with our electromagnetic field,
pressing against it and likewise affecting all systems that
our electromagnetic field is connected to.
How do we know this?
Listening to the radio waves that make up the background
noise of the visible Universe, the so-called “white noise”.
A very respected member of the scientific community
disagreed with me on this point, his remarks were, and I
quote:
“FYI: Sound cannot travel across a vacuum of Space. Ra-
dio waves, in spite of their name, have nothing to do with
sound.” (Dr. Neil deGrasse Tyson)
What he failed to recognize is that the so called vacuum
of Space is not a vacuum at all. It is filled with the most
wonderful vibrating pre-atomic geometry that I will be introducing to Mankind at the end of this book.
Nevertheless, common sense should inform the reader
that Electricity/Gravity winds All Things together tightly,
so tightly that there is No Thing that stands by itself alone.
All Things touch All Other Things. Consequently, when
One Thing vibrates All Other Things touching it vibrates.
Hence, sound does travel through Space, it reproduces itself by means of converting its energy into another waveform.
The facts are that sound waves convert into pressure
waves which interact with the electro/magnetic pressure
waves of the Earth and that of our Sun and that of the Cosmic radiation flowing into our solar system.
Therefore, Every thought, word or motion that we make
is conducted to Every Other atom within our Universe. For
All Things are truly One!
Something that should not be forgotten is the undisputed
fact that in the process of even saying “1 x 1” the sound
waves that are formed have a butterfly effect upon Everything they encounter and Everything they encounter shall
be forever changed.
Just to be clear, I think that it is important for me to inform the reader that sound is Light waves slowed down. If
you wanted to see the color of any particular sound? All
you have to do is continue doubling the frequency of the
sound until it resonates within the visible Light spectrum.
Like Einstein said, “Everything is Relative.” He wasn’t simply speaking about relative positions to some event. It can
actually be applied in this way, “All Things are directly related to All Other Things!”
It is all relative to the length of the wave, the shorter the
wave the higher the frequency. If the frequency is high
enough it reveals itself as Light/Life. The longer the wave,
the lower the frequency and low frequencies produce the
sensations that we experience as audible sound.
I cannot blame Dr. Neil deGrasse Tyson, the Astrophysicists who made the comment that “Sound waves don’t
travel through the vacuum of Space,” because his line of
thinking is a common mistake made by modern scientist
as a result of being misled by their limited vision.
They are often fooled by this misconception because you
cannot see the things that make up the so called ‘vacuum
of Space’ does not mean that there is an actual vacuum, a
Space with nothing in it.
For example, if we used a Geiger counter in whatever respected room we find ourselves at the present moment,
the sensor would register the ambient radiation with and
audible “click.” This would signify the amount of radioactive particles/waves that occupy the Space and the Geiger
counter would click, a little. Yet, if we turned one on just
outside of the Earth’s atmosphere, the clicker would go
crazy!
That’s because all of that so-called empty Space, that “vacuum” that Dr. 
Tyson spoke of is actually filled with countless sub-atomic radiating particles streaming from our
Sun, surfing the solar wind at speeds so fast that its effects
can traverse 93,000,000 miles in 6 minutes depending
upon the magnitude of the Coronal Mass Ejection (CME).
That solar wind is filled with highly charged magnetic particles 
that travel from our galaxy to other galaxies and are
converted into electricity through the pressure conditions
of plasma tendrils called Birkeland Currents.
Something that should not be overlooked is the fact that
the Earths atmosphere is 78% Nitrogen, 21% Oxygen,
0.9% argon, and 0.03% Carbon dioxide with very small
percentages of other elements, so even though the air we
breath may appear to be clear and empty, nothing could
be farther from the truth. All Space is filled with Matter
there is no vacuum. The Matter is either visible or invisible
but it is there.
Since sound and Light are but longer or shorter wave
forms of the same wave field then the effects of sound does
“travel across the so-called vacuum of Space” by the same
vehicle that the energy from Light waves travel.
It is estimated that we can listen to sound waves that began as explosions with such intensity and consistency that
they register in the form of radio waves from the furthest
parts of our early Universe. Sound waves that have been
traveling across the Universe for billions of years.
Therefore, it is reasonable to conclude that by simply uttering, “1 x 1” we create two separate and distinct wave
forms that will still be vibrating billions of years from today.
Consequently, regarding sound waves and vibration:
1 x 1 = 2
ELECTRO-MAGNETIC WAVE INTERACTIONS
Then again, it could be argued that,
“We are only thinking or imagining 1 x 1.”
If so, let us now consider how thoughts are formed in the
mind and lets examine the hidden processes by which our
brains do this thing called "thinking".
As information is funneled into the brain through various
receptors located on the human body and are analyzed as
thoughts, they are re-born as newly formatted electrical
impulses. These impulses are different from the state by
which they entered your sensory organs, because now they
have been transmuted by your brain's narcissistic editorial
process. It interprets All Things according to its own image.
Thoughts are generated inside a neuron (as told by modern science) as an electrical impulse (a frequency) that
travels along the axion where it encounters a neural transmission fluid after which it is converted into electro/
chemical energy.
Afterwards, it is carried through that fluid on a wave in its
chemical state until it reaches the dendrites of a neighboring neuron where it converts again into electrical energy.
Within this process of electrical energy being converted
into chemical energy and back again into electrical energy
a measurable wave field is generated and with each conversion that wave field intensifies.
The simple act of thinking or imagining “1 x 1” creates a
large enough impulse that it can be measured through
EEG’s (Electroencephalograms).
EEGs are measurements of voltage fluctuations from electric wave motions within the neurons of the brain.
Brainwave frequency is measured in hertz in the same
manner that musical tones are measured. Therefore, if
you think “1 x 1” you have created two separate wave forms
(two separate songs) of continually converting energy that
travels from the brain, through the skull, and out into the
Universe where it can be interpreted by simple electronic
measuring and monitoring devices.
Those 2 thoughts about the multiplication of those 2 numbers creates 2 separate wave fields that will transfer their
wave amplitude upon Everything in existence until Time
Indefinite.
Therefore, even the act of thinking, “1 x 1” creates at least
2 equal and opposite consequences. Each of them will have
both a positive charge and a negative discharge which in
turn will have at the very least two separate and distinct
consequences that will double into:
4 and then 8,
16, 32, 64, etc.
Do you see my point?
Everything is affected by Everything else! There aren’t any
isolated states of being where Anything exists within a vacuum without the consequence of Multi-Dimensional chain
reactions. Likewise, even the act of thinking 1 x 1, the consequences equal at least 2.
ESTABLISHED LAWS OF THERMODYNAMICS
If we were to take into consideration Newtons third law of
motion, which states: “For every action there is an equal
and opposite reaction.”
For if 1 x 1 ever equaled just 1 then two forces or substances will have interacted without any reaction. 
Therefore, either Newton’s Third Law is fundamentally flawed,
or 1 x 1 must equal at the very least 2!
I’d like for you to take particular interest in Newton’s
idea’s concerning Mass and its attraction to other objects
of Mass.
Within these concepts rest another obvious proof of 1 x 1
= 2 in Nature. Gravity which directly correlates to the Mass
of an object (as taught by modern science) is represented
through values in our current number system.
Examine for instance the tedious process of collecting
data and the arduous task of processing that data. Do
you recall how the human mind collects bits of information from multiple forms of stimuli? It is initially routed
from the sensory organ to the thalamus where it is converted into electrical impulses. Those impulses are then
converted into chemical structures that represent the
data. Remember that a chemical is composed of elements
and each element has a particular mass and mass is determined through a consideration of force. In Newtonian
terms F=ma.
Nevertheless; if, “1 (mass) x 1 (mass)= only 1 (mass)”, then
there wouldn’t be any such thing as the electrical effects
that have been labeled as gravity to initially accumulate
the Matter into a MASS. In fact, it would create the opposite effect of gravity for every mass would effectively repel
every other mass. Our entire Universe would never come
into fruition.
Therefore, in order for there to be the affect of gravity:
“1 x 1” must = (equal) at least 2.
PURE LOGIC AND TRUTH
Let’s approach this problem from another logical perspective. 
By making the numbers 1 x 1 = 1 we reduce the number [1] to a lesser value than[0] zero.
Because zero [0] is the only digit (number) that when
multiplied by itself the sum could remain the same because the number doesn’t really exist, it is a placeholder
that holds no value.
The number [1] is valueless if it does not affect itself or
even a [0] zero Space for that matter. For if you multiply “1
x 0” it equals [0], which in itself is a direct violation of the
laws concerning the “Conservation of Energy.” The law
states that, “Energy cannot be created or destroyed,” ... ‘lt
can only be transferred or transformed into another state’.
This is what we have observed in natural phenomena. This
is reality! So, how can SOMETHING times NOTHING
equal NOTHING? How can SOMETHING just disappear
because it encountered a NON THING?
The very notion of this impossible scenario suggest that
if one was to travel too far down a plane, at some point
that individual will encounter the end of that plane and
enter into a Non-Space. A Non Space, a place where the
laws of the Universe cease to exist as per the Idenity Property (lol). Anything foolish enough to venture past that
point will themselves fall into an abyss or a place of NonSpace. Because that is exactly what [0] is, an empty Space.
This line of reasoning is undoubtedly a hold over from the
days of ignorance when primitive Man believed that the
world was flat and that if one went to far past that forbidden edge they would fall into the Nothing World, a place
where nothing exist. A dangerous consequence of having
the World’s Mathematics, Sciences and Economy based
upon
SUPERSTITION AND FALSE AXIOMS!
Again, we have a conspicuous example of mathematics violating the very laws of physics that it vehemently claims
to uphold and swears, ‘through mathematics the beauty of
the natural world is expressed in all of its equations.’
Every wave must follow the wave that proceeds it, unless
that wave is acted upon by another wave. This is a law made
by Nature.
Here’s my point, if every number that follows the number
[1] is a product of the number [1], then shouldn’t those
subsequent numbers which are nothing more than a collection of many [1]'s behave like the number [1]? Since the
number [1] is in fact their progenitor, their patriarch, the
object of their reflection and the very foundation and nature of their entire being, should not those reproductions
of the number [1] be susceptible to the weaknesses and
strengths of the number [1]?
Again, how can the descendants of the number [1] or even
a mass of congregated [1]s have a different constitution
than their base?
When any number interacts with (0) it behaves like its
phantom patriarch the number 1, meaning it completely
disappears, another impossibility.
All of these inconsistencies expose our lack of understanding upon the subject because our “understanding”
at present is apparently based upon a number of no real
measurable value. The only THING that can interact
with NON-THING and become a NON-THING is a NONTHING!
Nevertheless, the multiplication table corrects itself after
falsely stating that one times any number equals itself.
It immediately recognizes its folly and completely changes
its tune when it reaches the numbers (2) and greater.
Let us examine this conundrum from another angle. Lets
approach it in reverse ...
If we were to ask the question:
“What is the square root of 4?”
The answer is 2.
If you multiply 2 x 2 it equals 4. Also, if we add 2 + 2 it
equals 4, it doesn’t equal more or less than 4.
Pretty simple, right? And it should be that simple because
remember “When in doubt, see rule number 1 “.
We were taught in elementary mathematics that in order
to check our answers when using multiplication it is sometimes necessary to “add our results and see if the results
are balanced.”
Well, let’s find the RECOMMENDED VALUE of the square
root of the number 2.
In other words, what number times itself (as suggested by
the mathematic community) equals the number 2?
If you have a calculator handy it will help in this process.
The computer represents the square root of the number 2
as:
...
A brilliant mathematician named NJ Wildberger raised
an interesting argument regarding this ( ... ) that occurs at
the end of the last number presented.
If I may, I shall paraphrase his insightful observation. He
said; “(Is this a correct answer? (referring to the irrational
number sequence above that ends with the ( ... ))
Does it give you the square root of 2? No, It gives an
approximation of what academia would like for you to believe the square root of 2 is. But in all truth, no mathema-
tician has ever given the solution to the root of 2.
That is what the "..." represents at the end of the last number in the computer’s ‘irrational’ program. It means that if
you wished, you could extend the decimal out to the 100th
digit or you can shorten the decimal chain and put the (
... ) right after the 1.414 and the answer would still be a
flawed assumption.
It doesn’t matter where you put it, because it is and will
always be an assumption. It’s simply not true and yet it
is presented as absolute truth. That approximation only
predicts a flat, 2 Dimensional non-existent unreality. A
straight lined approximation of a 3 Dimensional curved
Universe that is filled with tangible curved Multi-Dimensional pre-atomic existing geometry 
that has never before been revealed. It is over saturated with intersecting
spheres of pulsating and polarizing systems of energy.
For the sake of rigor and accuracy, let’s calculate this number to the 15th decimal. Let us add it to itself ...
Well, thats odd, because adding the square root of 4 (the
number 2) to itself, equals the number 4.
Yet, when you add the ‘suggested’ value of the square
root of 2 to itself the sum of those numbers added together are more than the initial number squared.
The sum of these numbers is 2.828427124746190...
The resulting number is so high that it could be rounded
off to the number 3.
How can something like that ever make any logical sense?
‘It is important to note that it has been an accepted
anomaly for this kind of phenomena to occur with every
number less than 1’. This is what Neil DeGrassi Tyson said
to me regarding this conundrum.
For example:
the square root of 0.64 = 0.8
(a number larger than the original).
0.64² = 0.4096
(a number smaller than the original).
and of course 0.8 + 0.8 = 1.6 NDTyson
From a logical standpoint this looks more like, proof of
failure rather than proof of success. Look at how convoluted these results are. 
Try to imagine the desperate circumstances necessary for this kind of hypothesis with such
flawed results to be deemed acceptable in pure mathematics. Especially, considering the fact that the results are in
direct violation of any observable natural phenomena and
call for the laws governing Conservation of Energy to be
suspended in order for any of these functions to occur.
Lets not forget that all of this takes place in the imaginary
world called Euclidean Space, the flat non-existent world
of 2-D, where everything is make-believe.
Nevertheless, for argument sake Dr. Tyson, we are not discussing the square root of the numerical values between 0
and 0.9999 ... (a value less than 1)
We are examining the square root of the number 2 which
does not fall within the margins of this so called excepted
anomaly.
If we remember one of the primary things that we learned
from our earlier lessons in mathematics is ‘That an object
or Number must be equal to the sum of it’s parts it cannot
be greater than it or less than it.’
Therefore, common sense alone informs us that
1.414213562373095 ... cannot be the square root of 2. It’s no
only an irrational number it is borderline delusional.
If a psychiatrist were to give a clinical diagnosis for this
number and this ‘identity crisis’ that it is suffering from it
would be diagnosed with a Schizo-Associative disorder with
acute hallucinations and delusions of grandeur if it believes
for one moment that it could have ever been the root of 2!
Because the sum of those numbers added together becomes
greater than the initial number squared. It is as absurd as
the thought of one of Cinderella’s step sisters breaking the
bones in her foot to try and force her oversized paw to fit
into that delicate glass slipper made for a Princess. No matter how badly she wanted to be Cinderella, and regardless
of how desperately her mother wanted it for her, it simply
wasn’t reality.
When I was 14 years of age and was struggling to grasp a
concept in class. My teacher, Mr. William Tisdale gave me
an acronym that I believe is perfect for this topic of conversation. He used the phrase: “K.I.S.S!” Which means,
“KEEP. IT. SIMPLE. STUPID!” It made me laugh at myself
to reflect on how complicated I was making things.
In like manner I believe that modern mathematicians have
completely complicated a simply reality.
Consider this line of reasoning:
The square root of the number 4 is 2.
2 x 2 = 4 (not a fraction less) and
2 + 2 = 4 (not a digit more)
Did you notice, in these simple steps that the final sum of
both mathematical processes from either using multiplication or addition, the resulting number is greater than
the initial number? In fact it doubled. All of these effects
occur billions of times per second, within each and every
act of expansion and contraction in the observable Universe and have been 
studied and documented as observable phenomena in Nature.
If we consider the Fibonacci Sequence of
1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
which follows the Multi Dimensional expansion ratio of Everything in the Universe. Be it Light waves, sound waves,
waves upon the ocean, the growing of leaves on a branch,
our DNA chain, any and all things made of Hydrogen atoms, they all expand and contract in like manner.
This sequence is as old as Time itself as even Time follows
this pattern where the sum of the two proceeding numbers equals the next number in the sequence.
That’s funny, even Time expands and contracts! You’ll also
notice that the very first action in this Universal sequence
is to double itself and that doubling occurs within the primary steps of a system which is manifested in the relative
value of the number [1]. It should be crystal clear by now
that Everything, even number sequences follow the underlying rules regarding expansion and contraction that 
Everything else within the Universe follows.
All except Man’s rules regarding mathematics and his approach to multiplication. 
Man’s laws are completely contrary to the laws that Every other system within this Universe follows.
Not to be forgotten is the Doubling Sequence, of 1,2,4,8,7,5
{just a friendly note to the reader}
The Pythagoreans believed that there was no greater number
than the number 9. Therefore, if they encountered the number 16, which is the next number in the doubling sequence
following the number 8, they would add 1 + 6 which as you
know equals 7, then they would double the 7 equalling 14.
Next, they would add 1 + 4 equalling 5 and the process would
continue. Interestingly enough, this process even works backwards in the divisible direction.
The Doubling Sequence which accurately predicts periodic expansion and contraction of Multi-Dimensional Space
was famously used by Nikola Tesla in all of his work. Pointbeing, the first Action of every Interaction is to double itself.
Let’s consider the insight gained by the law of fractals also
known as the Mandelbrot set. Wikipedia gives this definition: “A fractal is a natural phenomenon or a mathematical set that exhibits a repeating pattern that displays itself
at every scale. It is often referred to as an expanding symmetry or an evolving symmetry."
Fractals differ from other geometric structures because of
the way in which they scale. DOUBLING the edge lengths
of a polygon multiplies its area by four, which is TWO (the
ratio of the new to the old side length) raised to the power
of TWO (the dimension of the Space the polygon resides
in).
Likewise, if the radius of a sphere is DOUBLED, its volume
scales by eight, which is TWO (the ratio of the new to the
old radius) to the power of three (the dimension that the
sphere resides in).
Notice the continued running theme in Nature’s law of
doubling in its initial steps. Consequently, if Everything
within our Universe employs this process of doubling,
shouldn’t the mathematical operations that describe these
natural processes follow suit?
The square root of 4 is 2. The number 2 goes into the
number 4 twice. Because 4 is divided by two twice. Well, 2
is divided by 1 twice. The number 4 follows the number 2
and must take its lead from that number and the number 2
must follow the rules established by the number 1.
The true Universal value of the square root of the number
2 is 1.
Unfortunately, there are many out there that have built
their “pain body” personas and their entire academic careers upon the false and forced dogma that 1 x 1 = 1. Also
they have insisted that the square root of 2 is an irrational
number and will fight tooth and nail to remain in its doctrine. In view of this unfortunate reality, I offer two short
examples of irrefutable evidence that requires only reasoning and a limited amount of discernment.
If you input into a calculator the number 2 and ask for
its square root the calculator will give you this answer:
[1.414213562373095 ... ]If you multiply that number by itself using the computer
or the calculator it will give the programmed number of
[2] as its answer. Yet, if you multiply the computer calculated value of the root of two by itself by hand the answer
is very different...
1.414213562373095... x 1.414213562373095... =
1.999999999999999861967979879025...
Which in no way shape or form is equal to the number 2!
For with the constant expansion of Everything within the
Universe and with each step of the Doubling Sequence,
this 1.999999999999999861967979879025... trails further
and further behind the trajectory of the real number 2 as
it expands and follows the Fibonacci Sequence in its never ending journey towards the edge of our Universe and
back! Trust me this is just the tip of iceberg regarding the
the mathematical fallacies of the square root of two. Stay
tuned.
Although this number may be sufficient for approximations here on Earth and may even work for travel to and
from the near Earth planets within our solar system. Yet,
if our species is going to advance enough for interstellar
and intergalactic travel this kind of approximation would
result in a traveler being millions of light years off course.
Therefore, it behooves Mankind to make the necessary
adjustments now regarding how we calculate the square
root of 2 which happens to be a value that is incorporated quite frequently in quantum mechanics, especially in
the Higgs dynamic and mass terms, which is part of the
Standard Model Lagrangian. The CERN collider whose
primary purpose (on paper) is to identify and isolate the
illusive Higgs boson and other theorized sub atomic particles, relies upon the true square root of 2 for its purpose to
be realized and cost over 13.25 billion dollars to build and
1 billion dollars a year to run. It would be such a waste of
time and resources for all of that to be based upon a false
approximation.
(The Higgs boson is a theorized elementary particle in the
Standard Model of particle physics. It is the quantum excitation of the Higgs field, a fundamental field of crucial im-
portance to particle physics theory, first suspected to exist
in the 1960s.)
Accuracy is very important especially when we are dealing
with the very nature of one of the founding fathers of our
number system. The closest (even) number to the number
2 is the number 4...
And the square root of that number is 2.
A very simple number.
A rational number.
Also, 2 x 2 = 4 without stretching or rounding it off. In
truth, the Square root of 2 has never been given by academia because:
1.999999999999999861967979879025
Is “CLOSE, BUT NO CIGAR!”
We must be the most naive and gullible of intelligent species in the history of the Universe. 
I can understand Primitive Man accepting this standard practice of multiplication
before the invention of decimals, but not a technologically
savvy and advanced group of Homo sapiens such as ourselves capitulating to something this blatantly ridiculous
and inaccurate.
Our current practices of multiplication was actually inherited from the ancient Greeks, who stole/borrowed it
from the early Mesopotamians, who developed this system
some 4,000 years ago. Lets take a moment to consider what
the average day was like for the Babylonians and examine
some of their other means of handling minor and complex issues. For the sake of comparison, in the hopes that
we may reason on the idea of how many other practices of
that ancient clan in Mesopotamia did the ancient Greeks
also borrow and implement into our modern world.
A BRIEF HISTORY OF BABYLONIAN LOGIC AND A
GLIMPSE INTO THEIR DAILY LIVES
Babylonians weren’t that tall on average, they were more
wide and girth in nature. It has been reported that they
called themselves “The Dark Haired People” because they
had darker eyes than their neighbors, darker hair and
darker skin. Most of the clothing they wore was made from
animal by products. Therefore, they had a certain pungent
smell to foreigners, primarily because the region was quite
warm and rather dry and woolen garments retained heat.
As a result, perfumes, incense, fragrances, and oils were
very common articles of trade that were imported and
manufactured by the inhabitants of that ancient city.
The historical city of Babylon was located where Iraq stands
today, a land also known as Mesopotamia which may give
the reader a better visual perspective of the climate and
the difficulties that one might encounter being forced to
scratch out an existence in such an arid and inhospitable
environment.
The entire population had a responsibility to contribute
to the prosperity and welfare of the city. They lived under a socialistic form of government, they did not trade
in currency but incorporated a system of bartering. Exchanging food or livestock, wool, tools, jewelry and whatnots. In return for their dedication and sacrifices the
government made sure that everyone had food, clothing,
and suitable housing. It seems as though they had a very
successful socialist society for quite some time.
The family structure was more traditional in nature than
that practiced by most modern day families. Arranged
marriages, stay at home moms, father worked while boys
were schooled and girls remained home with their mothers learning the art of “home making”.
BABYLONIAN MEDICINE
Babylonian medicine was governed by the:
“Code of Hammurabi”, Dated 1800 BCE.
The code carried with it some rather harsh penalties for
medical and surgical therapeutic failure.
There is no clear indication that the physician actually
understood anything related to the real nature of the ailment they may have encountered except in the more obvious cases or even the true function of the organs affected. Among the long list of available remedies, a few like
oil for stiff limbs, or milk for stomach troubles, salt peter
and crushed ostrich shell for kidney stones may have been
beneficial, but some of the remedies employed seem to be
entirely valueless. This may even have been realized at that
time as indicated by the seeming indifference with which
the physician moved through a long list of medications,
shifting from one to another for the same disease.
Therefore, while these tablets have revealed a wide range
of observed diseases and an extensive list of herbs and
minerals in the physician’s pharmacopoeia, there was not
a systematic fund of knowledge of the human body and
neither was there any rational consideration of disease.
The causes of disease and the application of remedies, as
conceived by the physician, were so intertwined with belief
in supernatural forces, that a rational understanding of
the organs and functions of the human body was not likely or even possible. It is evident that primitive folk medicine, with All of its superstitions completely dominated
the medical teaching of the ancient Mesopotamians just
as such superstitions suffused their general outlook on the
Natural World.
Ancient Babylonian knowledge of anatomy, physiology,
and pathology was therefore extremely limited and under these circumstances, the contributions of Babylonian
medicine to later medical science cannot be said to have
been important. There is little to no evidence of its cultural crossover into other civilizations except, perhaps
that of India. Our own knowledge of Babylonian attainments is limited by the fact that not a single Babylonian
tablet on surgery has survived long enough for modern
science to reference. We cannot however, doubt the existence of such treatments being employed in early Babylonia, especially in view of the legally recognized and
regulated position of the surgeon in Babylonian society
of the 20th century B.C.E.
MATHEMATICS
The Babylonian system of mathematics was sexagesimal,
or based in a numerical system rooted in the number 60.
Among the Babylonians mathematical accomplishments
were the determination of the square root of 2 incorrectly
to seven places. The Babylonians where also credited with
the invention of 2-Dimensional geometry, better known
as Euclidean Geometry. So, here we have one of the culprits for the idea of irrational number systems and for the
confusion related to the existence of straight lines. They
both have their roots in a culture that is synonymous with
(Babble) “confusion.” Now it becomes a little more clear:
as to how and why the Greek Euclid came up with Euclidean Geometry: he borrowed it from the Babylonians who
also borrowed many of their concepts regarding mathematics and geometry from the Egyptians.
CALENDAR
The ancient Babylonians used a calendar with alternating
29 and 30 day months. This system required the addition
of an extra month three times every eight years, and as a
further adjustment, the king would periodically order the
insertion of an additional extra month into the calendar.
Interestingly enough, this is where the idea that a circle has
360 degrees comes from since they believed there were 12
months in a year and the average month had 30 days in it.
Thus, 12 x 30 = 360
Yet we now know that there aren’t just 360 days in a year
and likewise, there aren’t only 360 degrees in a circle.
Armed with this knowledge it would be foolish to believe
that the irrational value given for π by academia is a correct value based upon this dreadfully faulty foundation and
false approximation. This value could never have come
close to the true number of degrees refracted in a circle.
As can be seen by the Babylonian calendar system, they
were a civilization that was quite used to making adjustments to mathematical quantities as needed by the circumstance. In academia they call this “fudging.” There
were no absolute truths in their approach to numbers or
the measurement of Space and the things that occupied it.
A process still employed by modern mathematics and science today. I guess the fruit doesn’t fall far from the tree.
ASTRONOMY
Among the sciences, astronomy and astrology occupied a
conspicuous place in Babylonian society. The zodiac was a
Babylonian tool, perhaps borrowed from the Zoroastrians
of great antiquity, foretelling eclipses of the Sun and moon.
Observatories were attached to the temples and reports
were regularly sent by astronomers to the king. The stars
were numbered and named from an earlier date and we
possess now tables of lunar longitudes and observations of
the phases of Venus. Great attention was naturally paid to
the calendar, and we find a week of seven days with a five day
work week. We haven’t even begun to mention the animal
sacrifices to their many gods, nor their cruel and unusual
treatment of criminals and captives which included decapitating prisoners and playing ‘kick ball’ with their severed
heads.
Needles to say, the modern world had the good sense to
recognize that most of the practices and methods employed
in the daily life of early Mesopotamia would not be useful
in today’s technologically advanced and purportedly more
evolved world. Yet, we have made the mistake of adopting
a faulty system of mathematics from an extinct civilization.
The question still remains, why hasn’t anyone over the
last four thousand years, and I am talking about some of
the most gifted, thinking, men and women who have ever
walked the planet, ever questioned the inconsistencies related to the square root of 2 and the true value of 1? It
seems incomprehensible to imagine that these inconsistencies have escaped the notice of such an amazing group
of Intellectual Geniuses. Individuals who have been venerated by Man for hundreds upon hundreds of generations
because of the many contributions they have made to the
world of science as a result of their mental prowess. A power so strong that they have held a remarkable influence
over Man’s thinking for over 4 millennia.
Yet, not one of these 'cerebral giants' bothered to question
the blatant and apparent impossibilities concerning
1 x 1 = 1
and
the Square Root of 2 being 1.414213562373095...
How sad for Mankind. We are not only Cosmically blind,
but severely mentally challenged as well.
Unfortunately, here is another one of those inconvenient
truths concerning the square root of two that deserves the
immediate attention of the mathematic community!
THE SYSTEM AIN'T BROKE, ITS FIXED!
Finally, I believe it is important that we drive the point
home that there is a deliberate untruth woven throughout the fabric of our mathematics and is embedded within
the programs that run our calculators, computers and our
smart phones.
If you were to input the number 2 into your calculator
and ask for its square root, you will receive the answer that
we’ve mentioned numerous times before:
If you square that number (x2) the calculator will tell you
the answer is 2.
But if you add that number to itself or multiply it by 2 the
result is:
1.414213562373095...
+ 1.414213562373095...
2.828427124746190...
Surprisingly, if you cube this result of the Square root of 2:
(1.414213562373095...)³
According to the calculator you’ll get:
NOW WAIT A MINUTE! THATS THE SAME ANSWER
THAT YOU GET BY ADDING THE NUMBER TO
ITSELF!
1.414213562373095...
+ 1.414213562373095...
2.828427124746190...
How is it possible for a number whether rational or irrational to have the same exact value when being added to
itself or being multiplied by two as it does when that number is cubed? The only other number in like manner is 0
because it is a Non-Number.
Can this be a mistake?
The truth is 1 x 1 = 2
And 1 x 1 = (ing) 1 isn’t multiplication, it’s a fabrication
which is also known as a mathematical fallacy.
OBSERVATION FROM WITHIN
“Irrationality in the field of mathematics is a major problem within the subject. Our approach to irrationality
doesn’t work. Most senior mathematicians are aware of
this at some level but they would rather not address the
issue and acknowledge it. Many junior mathematicians
and most students are blissfully unaware of the problems.
Nevertheless, the problems are serious, they are deep and
they effect many things. They weaken mathematics and
they make it much less beautiful than it ought to be.”
NJ Wildberger
In other words, they choose to ignore the 800 pound gorilla in the room!
Truth is absolute. It doesn’t waiver or meander through
the meadows of Time. Truth is dependable, reliable and
consistent, it is trustworthy and always right! It holds the
line under all circumstance and the rule of Universal law
and established order is built upon its foundation.
We have seen the end result of blindly following the established standards set out by the practitioners of this
convoluted logic in the examples from our programmed
calculators regarding the root of 2. Where the square root
of a given number times 2 becomes greater than the initial
number squared and that same square root of a number
when cubed becomes equal to the same value as when it
was multiplied by 2.
First of all, who are the people that dictate and set the prerequisites for how the Natural Universe should be counted
and how it multiplies itself? Who are the individuals responsible for the ‘Identity Element’ which could very well
turn out to be the single greatest stumbling block ever
placed before Man’s already precarious path, next to the
institution of false religion?
Shouldn’t Nature and the natural events that occur within the Universe dictate the rules of engagement regarding
our understanding of its functions? Shouldn’t the observable Universe have the final word on how we measure its
systems and account for its weights and balances?
Irrationality in numbers occurs in many places in our established system of mathematics. Nevertheless, the most
famous and well known examples are the ratio between
the circumference of a circle and its diameter, π, and the
square root of 2. Where the Pythagorean theorem postulates that:
a² + b² = c²
This unfortunately corners mathematics into a stalemate
of reasoning because the side and the diagonal of a square
become incommensurable. Each instance of irrationality
surfaces when a straight line is used to define or merge
with curved Space.
The term “Irrational” means to be without the faculty of
reason, deprived of reason, without or deprived of normal
mental clarity or sound judgment!
For 4,000 years Mankind has approached the concept of
defining our Universe with these “irrational” arguments
coupled with his attempt at measuring it’s working functions with impossible and impractical tools.
These misconceptions have prevented Man from properly
viewing the orderliness and the working dynamics of this
wonderfully creating Universe. Because of assigning properties to the structure of the Universe that do not exist,
our approach to mathematics has led our sciences into an
intellectual and technological quagmire.
A quicksand as it were, of misguided concepts that we
have built our entire understanding of the visible Universe
upon.
The entire concept of the platonic solids and straight lines
are themselves incommensurable with the visible Universe
and are non-sustainable structures in logic and in practice.
For if our Universe were constructed of these rigid linear
bodies Everything in it would collapse upon itself! Our
Universe is a living and breathing entity that expands and
contracts with every polarization in regular and predictable cycles.
Unfortunately, the Pythagorean theorem, Euclid’s
Assumption, the axiom that
there is no rational number
a/b satisfying [(a/b) squared]
and the very nature of Euclidean geometry fails to satisfy
the needs of the fields of mathematics and the physical sciences because it does not allow for either contraction or
expansion of the Universe at any scale.
Go ahead, don't be scared,
touch 'em, if you want to see where they
come from:It all began I believe, with the invention of the platonic
solids, whatever these structures were called when used
by the Egyptians, Assyrians or the Babylonians before the
Greeks is not important. What is important is that they
were followed by Archimedes’ truncated solids, then came
Kepler’s pentagonal solids. All of these are beautiful works
of art that share a limited symmetry consistent with Man’s
designs. Our modern day buildings and the cities of old
were all built upon these non-sustainable geometric structures along with all of the wonders of the ancient world. I
use the term ‘invention’ because that is exactly what they
are, ‘Inventions from the minds of Men.’ It is of no consequence that these relics of the past have been venerated
by Mankind as a “discovery” of Universal shapes, but in all
truth, not one thing in the Natural Universe reflects their
static design.
The Pythagorean theorem which is one of the most important theorems in mathematics is rooted in this unre-
ality. The theorem that there is no rational number a/b
satisfying (a/b) squared is also rooted in this philosophy.
Platonic solids were born on paper and the math that describes them dies when it leaves the margins of that paper.
Deuces are wild in two dimensional Space and anything
can happen in the land of linear giants and flat horizons.
Yet in Universal Mathematics, Space begins in
curved 3 dimensional wave conjugations and is
reasonably understood. Therefore, all of Creation, espe-
cially thinking Man, can enjoy and find supreme delight in
its Super-Symmetry.
With all of that being said, if it can be proven that there
are no straight lines in the visible Universe, then all theorems and postulates based upon these imaginary and
philosophical lines would have to be abandoned and the
door would be open for the introduction of a new line of
reasoning, something that is not considered to be:
IRRATIONAL
or
“deprived of mental clarity
and sound judgment.”
(Right?)
Let us ask a few questions then, “Where does a straight
line come from anyway?” Are there any straight lines
in Space? Are there any objects whose trajectory is on a
straight linear path? The answer to the last two questions
is, NO! There has never been, nor shall there ever be a
straight line in this curved Universe.
Regarding the origin of straight lines, the concept of a
straight line was invented in the minds of Primitive Man
before his ability to comprehend the curvature of Space-Time. It is an illusion fabricated by man’s limited sense of
sight and propagated by the, [WE PEOPLE] the “trustees
of knowledge and higher learning.” Do not forget that
Homo sapiens can sense only a tiny fraction of the total
“light” spectrum.Therefore, Academia's stumbling about and their false
predictions regarding Space and Time is understood. The
same show of compassion that one would have along with
a certain level of sympathy for a society of children, relative infants on a cosmic scale, born blind, attempting to
build a model of the Universe.
I personally do not blame modern nor ancient academia
for attempting to make sense of their world. As a result,
we have gained some ideas about structure, design and
an awareness of the need for there to be an underlying
symmetry of structure that dictates the geometry of All
Things physical.
Nevertheless, the geometry that they’ve invented, the platonic solids, fail to truly grasp nor does 
it define the undercurrent of super symmetry that exists in All Things. They
only define static structures which only exists within the
confines of academia’s mind. They are incommensurable
with the curved functions that govern All Matter.
Unfortunately, our present system of mathematics is based
upon linear projections that exist only in two dimensional
Space. A Space that does not exist. A Space that is imaginary. A Space that was initially invited as a temporary
“mental exercise.” In order for mathematics to correctly
represent the physical Universe we must think and calculate it’s proportions in Multi-Dimensional curved Space/
Time.
I challenge anyone to show me a true straight line in
this curved Universe! It has been theorized in calculus that a significantly short line segment in a curved
Space can be shown to be indistinguishable from a
straight line. [Not to be forgotten is the fact that calculus is a child of Euclidean geometry which is based
upon 2-D imaginary and non-existent Space. Therefore,
‘calculus’ doesn’t carry any (pardon the pun) weight in 3D
Space/Time] Yet, that theoretical straight line would be
infinitesimally small, so small that it would be impossible
to see even if we could experience 100% of the total Light
spectrum. Also, the illusion of that theoretical straight
line would disappear immediately following any projection from its segmented point. In view of the fact that all
things in this Universe is in constant motion it makes the
true creation of a straight line not only improbable but an
impossibility to say the least. The Creator of the Universe
could not make a straight line, that’s why
ALL SPACE IS CURVED!
Yet, Man in his ignorance introduced the impossible notion of a straight line into the field of mathematics and it
has proven to be his proverbial Achilles' heel till this very
day!
Let’s tug on this loose thread for just a bit and see what
unravels.
If it can be proven that there are no straight lines in the
Universe, what would happen to all structures and theorems that are based upon these presumed straight lines?
If there are no straight lines, how does a polygon come to
exist? And if there are no polygons that create polyhedrons
with straight lines, how does a platonic solid ever come to
be? And if there aren’t any straight lines, how does a triangle come to be? And if there aren’t any true triangles, how
does an isosceles triangle come to be? And if there aren’t
any isosceles triangles, how does a right angle come to be?
And if there are no right angles? Then how does the Pythagorean theorem ever come to exist? And if there is no
such thing as the Pythagorean theorem? Then there never
comes into existence the ratio of the side of a square to the
diagonal of a square because there aren’t any such things
as squares either. Also, if there aren’t any such things as
triangle’s? Then the irrational number for π doesn’t exist
either.
“Newton’s first law of physics which states that a moving body
left to itself moves on forever in a straight line with a uniform
velocity, is not in conformity with the laws of motion. In this
Universe of varying pressures, all masses floating ‘in Space’ constantly move in the direction of their changing potentials. This
direction is always spiral. All motion being spiral, all direction
being curved, and all pressure planes being conic sections, electric action cannot proceed directly north from south in a straight
line, but must progress toward north in a spiral direction.”
As told by Walter Russell, in his book “The Universal One.”
Published in 1926.
‘All energy in the Universe is expressed in motion and all
motion is expressed in waves and all waves are a function
of a vortex and all vortex functions are curved.’ There are
no straight lines in the Universe. Therefore, there aren’t
any straight lines in Universal Mathematics.
When will Mankind say enough is enough and begin again
with a new math that is built upon truth and a conscious
society who desires a more evolved understanding of life
and of All Living Things? A true and reliable new math
that will usher in a new understanding of this remarkable
Universe.
I believe that it is clear that two dimensional perspectives
and conjecture about irrationality concerning Multi-Dimensional Matters will forever be incommensurable and
shall always produce dissonant values within the field of
mathematics. Remember, “There are no straight lines!”
Therefore, all axioms based upon the Platonic solids and
linear reasonings are flawed and are a mathematical fallacy.
Also, the formulas in use today do not account for the constant simultaneous contraction and expansion of our 
Universe and of everything within it. Therefore, most of them
are flawed because they are rooted in a false understanding and a misconception regarding Universal phenomena.
There is a dire need for a better understanding about the
Conditions of Matter that correctly represent our curved
Universe and its curved Universal ratios.
Man must abandon his misguided beliefs in the imaginary straight lines first and foremost, then his mind shall
be free to realize that the shortest distance between two
points is that of a curved condition.
Nevertheless, in order for Man to comprehend two separate things, 
I believe we must first understand the meaning and the true value of One. Yet, 
before we can recognize the value of One we must first discern the conditions
under which ONE comes to exist.
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
