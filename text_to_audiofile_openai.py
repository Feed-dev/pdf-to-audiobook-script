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
A CRASH COURSE
INTO
PARTICLE PHYSICS
AND
QUANTUM MECHANICS
JUST A LIE
So here we are, at the point of no return!
This is the part of our journey that takes the greatest
amount of courage and heart because from this point onward, we are on our own. We have performed a thorough
investigation of the foundations that form the cornerstones upon which our understanding of math and science
are based. We have found the structural integrity lacking,
inherently unstable and ultimately based upon a series of
mathematical fallacies.
We’ve already looked behind the figurative curtain and
can clearly see that the Great and Powerful Wizard of OZ
(the Scientific and Mathematic community) and all of
their false promises of a Real Heart for the Tin Man, A
Real Rational Brain for the Scarecrow, Courage for the
Lion Hearted and the Hope of Getting Home to a place
that we can trust and feel secure in our expectations for a
prosperous and harmonious future. All of these promises
were embodied in the complex theories, theorems, postulates and equations that have been proliferated within the
academic community of Mathematicians and Scientists.
This is where we realize that it was all “JUST A LIE!”
And YOU have witnessed for yourself, the slick tongued,
snake oil selling con man luring you in with arbitrary rules
that create enough of a mental distraction to separate
you from your rational train of thought. But clicking your
heels three times and repeating the mantra “There’s no
place like home” will not get us to the safe and sustainable existence which is essential for our species if we are to
avoid the ever increasing consequences that often follow
the outright arrogance and ignorance of a prideful species
like ourselves that seems hell bent on extinction.
We have finally reached the subject of:
Quantum Mechanics
The process by which all the little bitty things that create
the illusion of the big things come together. I would love
to make my own introduction to this field and share with
you the insights and highlights that I’ve encountered upon
this journey. Nevertheless, I think that it is better to hear it
from one of their own.
He is a giant in the world of Theoretical Physics, he holds
a tenured seat at Cambridge University, he also works very
closely with the talented men and women at the CERN
Large Hadron Collider. And I’m quite sure that he has perhaps more letters after his name than 
that seen by the biggest and brightest of them.
He is Dr. David Tong and I think that some of the excerpts
from the presentation that he gave at Cambridge Hall in
2016 on Quantum Fields provides some of the most outstanding proof for the Terryen Wave Fields that 
I have discovered which form the basis of this New and True Universal Geometry. A Geometry that compliments the Universal
cosmogony and properly illustrates and defines the Nature
of Space-Time and the Forces that are responsible for its
many complexities. This will be presented right after Dr.
Tong’s skillful, brutally honest and most-inadvertent introduction to the “Terryen Wave Fields”!
So, I ask that you forgive me for quoting directly from
Dr. Tong as much as I will be doing for the next few pages. I will try to paraphrase as much as possible so that this
portion of the book is not considered plagiarized and this
work gets held up with a cease and desist letter but I’d hate
for someone to think that I’d stretched his words or took
them out of context. Therefore I am including some full
paragraphs from his lecture in the hope that you will understand from his own words what Quantum Mechanics is
missing and hear word for word what leading physicist are
seeking to accomplish in all of their various experiments
and are desperately hoping to find. I have summarized as
much of his lecture as is humanly possible in the attempt
of maintaining his overall voicing so that the thoughts are
coherent, in order to make sure that there is no confusion
concerning these most important matters as we proceed
to the unveiling of The Geometric TRUTH, one main essential component that Mankind has missed. The need
for Equanimity in all of Nature’s processes!
He started his lecture in a Victorian styled grand lecture
hall. The hall has an almost cathedral like appeal to it.
There are tiers of balconies from which the minds of science have sat and pondered over the subject matters that
were being presented. Pews where some of the greatest
minds in the world of science have gathered together over
the last five centuries and contemplated, meditated and
have stood to debate and have delivered some of the most
astonishing theories and counter arguments and hypotheses ever uttered in recorded history.
Then, very solidly and with full purpose of voice Dr. Tong
begins his lecture. He alludes to the fact that he could
take the audience back 2,500 years and pontificate upon
the ideas of Democrates an ancient Greek Philosopher
who was also known to be a very famous follower of the
Great Pythagoras and his philosophies. He could wow us
to boredom with the tales of Lucretius and the six volumes
he wrote regarding his own ideas about Epicureanism, in a
book titled, “The Nature Of Things.” Which is filled with
many insightful gains regarding the super symmetry that
All Created Things share with multiple correlations to
many of the ideals that the ancient Greeks ascribed.
Instead Dr. Tong chooses to push us into the relevant
present and proceeded to share information about the
test results from the Hadron Collider at CERN (the largest particle accelerator in the world) 
and how disappointed the scientific community was with the data and about
the other experiments conducted in the field of Quantum
Mechanics, in order to give the audience a general view of
the world of Physics as they (scientist) understand it, based
upon observable phenomena.
I applaud Dr. Tong for paying tribute to past innovators
who have made tremendous contributions to our overall
understanding of the complexities of Creation and Existence itself. Especially including men who were not famous
for their letters of accreditation or for the works that typically accompany someone that works in their perspective
fields of Philosophy and Art.
Nevertheless, the Universe saw that these men and women were true scientist at heart and the Universe spoke its
simple truth to them in poetic prose.
He spoke of Michael Faraday and his curiosities with the
fields created by Electricity and Magnetism. This is really
the focal point in the discussion because from these fields
all relatable Matter occurs. I call them Conditioned Matter
Fields, you’d most likely call them elements. He then began
to speak of the Periodic Table and its 120 or so individual
elements that fill its Euclidean attempt at symmetry and
he commented how “Nature itself thinks this is a silly
way to organize nature.” He points out very charmingly
that these elements aren’t fundamental but are made of
even smaller entities called atoms and that these atoms are
made of an electron orbiting a nucleus.
Dr. Tong then began to illustrate how JJ Thompson in
1897, in this very lecture series, in this same room, made
a startling announcement. So preposterous was this notion he was presenting them, that many of his colleagues
gasped at his audacity. He claimed that his test results revealed that something could be smaller than an atom.
After a night of wildly vocalizing a radical idea like this,
an idea that questioned the status quo and foundation of
scientific understanding, an idea so unfathomable that it
took 15 years for him to fully regain his previously esteemed
high standing as a cutting edge scientist in the field of Mechanics and as a rational and respected physicist within
the scientific community.
His reprieve came when Ernest Rutherford his successor
confirmed JJ’s insights. Rutherford discovered that atoms
are made of even smaller entities than just an electron or
collection of electrons orbiting a nucleus.
He discovered that the nucleus of an atom was composed
of smaller particles called protons and neutrons.
Now it took nearly 70 years for the small advancements
made in the fields of theoretical physics, mathematics and
computer processing for the world to catch a glimpse at
the next big revolution that was to occur within this blossoming field of Quantum Mechanics when in the early
1970’s scientist theorized that the proton and the neutron
were made up of smaller entities called an up quark and a
down quark.
To put it simply the proton has two up and one down
quark and the neutron has two down and one up quark. I
could go into length about it and the excitement by which
he presented this grandiose Standard Model of the fundamentals of the Universe and how fortunate we are to have
arrived at this incredible place of understanding, but wait
till you hear his punchline.
The punchline is in the crescendo of this portion of his
lecture, it is epic. If he or the rest of the scientific community at the turn of the century or at any given point would
have briefly taken into consideration the established works
and numerous papers and diagrams concerning vibratory harmonics and sympathetic vibrations from what John
Keeley’s insight underscored, with his superlative understanding of the vibratory 
mechanics we would have avoided this unfortunate conundrum regarding our misunderstandings about the atom. Nevertheless, I believe that
you’d have to hear it directly from the horses mouth to
gain a full appreciation of the desperate quagmire that the
Standard Model and those following the herd of scientist
who abandoned the model of “truth at all cost” and chased
after the false dogma left over from a collapsing system
that was built upon an absurd and unsound foundation.
Therefore, I think that it is best that you hear it in
Dr. Tongs own words:
Here is a link to his video:
Quantum fields the real building blocks of the Universe.
In the interim, I’ll give you a paraphrased overview:
He begins this part by saying, “We have 3 particles of
which everything we know is made". And it’s worth stressing that’s kind of astonishing. It’s true that we really can’t
appreciate how much we actually learn in school. Nevertheless, this entire Universe can be reduced down to just
3 particles that all have a narcissistic nature and keeps reinventing itself in many different variations of its 3 basic
attributes.
He also states that none of these 3 particles which are
made up of an electron and 2 quarks are what the Greeks
or the Victorians had in mind when they were looking for
the fundamentals of Nature but like Democrates believed:
‘There has to be some basic structure, some fractal part of
Nature that is responsible for all visible phenomena.’
Twenty-five centuries ago these same questions were being asked. Dr. Tong said it this way:
“These lego bricks are particles and the particles are the
electron and 2 quarks.”
The confidence in his voice, the flare by which he waved
his hands, gesturing to the assembled audience with a
warm and most inviting tone, a slight and reassuring smile
and then he floors them; “It’s a very nice picture, it’s a very
comforting picture, it’s the picture we teach kids at school,
it’s the picture we even teach our students in undergraduate university.”
“And there’s a problem with it. The problem is
IT’S A LIE.”
(by deception we shall rule)
He goes on to try and underplay the fiendish and duplicitous purpose for deliberately propagating a lie of this
magnitude by saying:
“It’s a white lie, it’s a white lie that we tell our children
because we don’t want to expose them to the different and
horrible truth too early on. It makes it easier to learn if you
believe that these particles are the fundamental building
blocks of the Universe,
BUT IT’S SIMPLY NOT TRUE.”
Ain’t that something! You mean to tell me that from kindergarten to graduate school Its all just BS? Billions of
combined HUMAN lifespans spent studying in the hopes
of evolving our species intellectually and it was all wasted
on “WHITE (Pardon my French) @^&!%^# LIES!”
He tries to seem as transparent as possible by stating that
the most respected theories within the world of physics/
mechanics don’t even hint at the suggestion of a universal
foundation being laid upon the concepts of an electron
and a couple of quarks.
The most trusted theories don’t even present the opportunity for a Universe that relied upon particles purely.
The cutting edge theory suggest that our Universe is
made up of something less tangible and more all encompassing. Something more fluid that happens to “socialize
and propagate the consequences of conjugating (mating)
in harmonic and rhythmic balance.
His words were not as lofty in their scope and resonance
as my own in my attempt at paraphrasing his talk but keep
in mind, I am somewhat of a showman and have a flare for
the dramatics. ((lol))
He continues by calling them “FIELDS” and he reminds
the audience that these fields are EVERYWHERE in the
Universe and that they behave like fluids.
This is particularly interesting because in the early 1860’s
James Clerk Maxwell produced a set of equations that began to summarize the myriad of effects caused by electromagnetic fluid like fields.
At the turn of the century most of the industrialized world
had turned a deaf ear to the whimperings of the Church
and the distaste of stale and fermented religions who’s
rituals were rooted in superstition. The dogma that they
propagated had stifled the growth of knowledge and understanding for millennia.
There was a united front within the scientific community
to root out the spiritual and esoteric. A call for all seriously minded scientist to turn away from alchemical foundations and make them synonymous with superstition and
the occult.
Mind you, alchemy was the life blood of discovery during
the renaissance. Tens of thousands of hours spent secretly
working in the quietude of their cellars, men worked in
near darkness in fear, for being discovered could cost you
your life and possessions. Many of our first discovered elements were uncovered by these very means.
Nevertheless, at the introduction of the Industrial Age
(The Show Me Age) anything that was inexplicable through
modern measuring devices was considered scientific taboo
and those practices or experiments were shunned.
The idea of an Aether or some mysterious fluid like substance that vibrated and traversed the entire Universe
seemed more like a supernatural astro/spiritual/metaphysical description than a purely scientific understanding of the Universe.
Well, to add to the mounting troubles within the field of
Physics, Max Planck came with his ‘Ultraviolet Catastrophe’. He was trying to understand the relationship between
the intensity of a black body like the Sun and the frequency of the light that it emitted. What was the relationship
between heat and the spectrum of light that was observed
from each change in temperature? His results frightened
him and forced him to consider the highly unorthodox usage of Ludwig Boltzmann’s ideas and his almost blasphemous approach to statistical mechanics. He attempted to
explain how the properties of atoms determine the physical
properties of Matter. The annals of time have shown that
Boltzmann’s instincts were correct. There is an equal and
opposite balancing field that reconditions the discharging
light. Negatively discharging heat through a Universal cooling action that eventually accumulates the newly rarefied
Matter.
Max Planck did pick the proper example, because a few
years later a promising young theoretical physicist by the
name of Albert Einstein received his only Nobel prize for
successfully proving the Photo-Electric Effect that Max
Planck predicted in his work as a direct result of ignoring
convention and listening to the little voice of truth that
rang in Boltzmann’s genius.
We often tacitly believe that Albert Einstein received numerous Nobel awards because his theories were so popular.
Most noteworthy, of course, are his theories on General
Relativity and his most famous equation of E=mc². Einstein is credited as being one of the greatest minds of all
time all though he made very few applicable contributions
to the world of Science. He is revered as a god while Boltzmann’s contributions were relinquished to just a footnote
in Max Planck’s biography.
That’s one of the biggest problems in the field of Science
and Mathematics, it goes beyond the fact that its a outrageously clickish. It’s as if they never truly left high school
and the silly games of unconscious children pretending to
be important adults. In truth, they are just afraid to explore new ideas. If they entertain an unpopular idea or
theory, it can leave them extremely isolated and unpopular in a super-critical peer oriented setting where popularity means everything.
Remember Giordano Bruno?
Coniecto Responsum
Perveni
Ignem Accendere In Te
To get a better picture of some of the challenges faced by
the physicists in the early 1900’s, let's consider this fact: at
the turn of the century, there were three separate branches
of physics. The first branch was called Mechanics, intended to predict the motions of Matter as influenced by Gravity. Then there was Thermodynamics, which was rooted in
attempts to understand the relationships of heat, pressure
and temperature in relation to the potential energy within
a system.
Finally Electro/Magnetism, which defined the interactions of charging and discharging particles. Interestingly
enough, it was Maxwell who attempted to marry the Electric and Magnetic Fields. Before Maxwell, Electricity and
Magnetism was seen as separate forces but as more data
returned from experiments and observation it became
clear that these two forces were somehow interrelated.
Unfortunately, he was also responsible for proliferating
the misconception that opposite charges attract, which
has confused these issues for so many sincere and honest
scientist. When the observable truth shows us through Nature, that opposites repel each other. This reality is layered
in all that we observe.
Consider Hot and Cold water for instance, they’re the
same exact substance but operating under different motion conditions where hot water rises and cold water sinks.
The only difference in them is their charge, their spin.
The Cold water is spinning in a North Eastern direction
descending into a higher pressure condition tightening
its bundles because of its high preponderance of Electric
charge, spinning in ever tightening centripetal vortices of
ever increasing pressures.
In contrast, the Hot water is expanding out and unraveling into an array of ever widening and lowering volumes
of spinning centrifugal pressure walls with a South-Western spin, increasing it’s radiating, rarefying bands of Magnetic potential.
Like the old common sense saying,"Birds of a Feather
Flock Together”, positive charges integrate and Crystallize in mass. Whereas negatively discharging particles or
waves within a set of fields repel each other, in tumultuous
acts of resistance that we observe in Nature as explosions.
Hot and Cold are opposites and move in completely opposed directions from each other.
A discharging mass or substance discharges evenly from
its equator and so effortlessly makes spherical pressure
walls one after another, perfectly. Spheres are the product
of expansion which is under the office of Radiation, performing the work of repulsion. Light and Darkness are polar
opposites and do not commingle. Opposites do not attract
they repel, it is the positive charge in a system that seeks
out an equatorial balance between other equally charged
substances. This is determined simply by spin either clockwise or counter-clockwise and at what velocity do these
given rotations occur. These are the determining factors
that either cause things to repel or to attract.
Motion and pressure conditions!
Things with like spin and relative pressures may continue to orbit their primary axis along with similar mass
or like-substances. Another way to marry your common
sense understanding to the overly complex terms that are
used by the scientific community is to think of the simple
effects that are created by the action of spin and how it can
change the appearance of anything caught within its visual effects. Which are often more than not simple optical
illusions.
Spin is measured in Hertz, or the count of revolutions per
second. Basically, how quickly does a wave oscillate? How
fast does it rotate upon its axis? What position upon the
equatorial plane does it orbit its primary star in this quantum world?
But let’s not get sidetracked, we have millennia of accumulated mis-information to expose and to root out if we
are ever going to get to the Truth. So, let's continue into
the world of Electro-Magnetism which is the foundational
corner stone of Quantum Mechanics.
Now the word quanta means: parcel or discrete lump.
These little discrete lumps were ultimately reduced down
to a constant called Planks Constant, which is supposedly
the smallest measurable unit of energy (a fallacy that will
be corrected in just a few more pages). It was believed to
have behaved completely differently from the Macro-Euclidean based geometry expressed in Einstein's work.
General Relativity was the talk of the world and millions
upon millions of dollars and man hours both governmental and private were being poured into laboratories and
testing facilities, each trying to monopolize upon the Nuclear Age, and willing to explore any of Einstein's exotic
hypotheses.
This enlightenment regarding interactive fields ultimately
became known as the true Aether. It was known and expressed in the works of John Keeley, Walter Russell and
Nikola Tesla yet intentionally ignored by mainstream science.
These three men were visionaries, sculptors of perception, philosophers, artist who understood the mathematical symmetry expressed in the repetitive and increasingly
expanding octaves that play an essential role in the distribution and the integration of Matter.
Like the esteemed Democrates and Lucretius, the gentlemen who 2,500 years ago predicted the super symmetry
that is observed in All Things. The difference being, these
men were outsiders, unpopular misfits as it were. They
were classified as pseudo-scientist, accused of adhering to
experiments carried out in circus tents with parlor tricks as
their evidence. “This must be some slight of mind like the
eye can be confused and deceived by some slide of hand.
That must be the case.”
They exert: 'Einstein’s theory predicts that these particles and forces of gravitational attraction must exist. So
we have to show proof of that in our findings if we are
going to receive more funding.'
This is undoubtedly the motivation behind many of the
actions of the peer oriented cult of the then and now modern world of physics.
“You need funding and funding only comes to those who
play by the status-quo even if it is blatantly wrong.” Yet, all
of the premier physicist of that day poured out their life
force insisting on proving the existence of a non-existent
thing and slipped down a rabbit hole of intellectual suicide
where they were forced to break every fundamental law of
established physics in order to propagate a false mathematical assumption that 1 x 1 = 1. An assumption that has
never been observed in the Universe since the first observation was observed.((lol))
As a result of this one arbitrary assumption their theories end in either an over expanded Universe where the
force of the expansion overtakes the force of gravity and
everything expands away from every other thing and everything disappears into oblateness. Or the force of gravity over takes the radiative expansion and everything gets
compressed into a super massive black hole that is a collection of all the other gobbled up super massive black holes
and everything disappears again into the nothingness of
an infinitesimally small void of dense emptiness.
Neither one of these hypotheses have ever been observed
in the observable Universe nor will they ever be observed
in the observable Universe because their predictions simply cannot exist in a balanced Universe of equal and opposites.
Nevertheless, mainstream science with haste and with the
acceleration of a rocket propelled projectile, championed
Einstein's notions with regard to Gravity.
They overlooked the common sense and necessary explanation of CAUSE and its relationship to the myriad of Effects which Newton made so very clear in his rendition on
the ‘Nature of Things‘ by Lucretius but Newton called his
book “Principia”, where he outlined the basic guide lines
of conduct for the present day scientific community. Laying down the foundational laws that are strictly upheld to
this day by the world of modern physics. Unless it proves
to be inconvenient.
One law in particular is the law concerning...
Action and Reaction.
This is a Universal Law that is completely disregarded in
Einsteins view of Relativity. “Gravity is its own product of
Space/Time” according to Einstein. Gravity is treated like
a giant Cosmic Deity, who is Omniscient and Omnipresent. Like the theoretical cosmic soup of Electro-Magnetism that Einstein insisted is there and another product
of so-called Space/Time, that has always been and always
will be.
The soup that created itself just before or just after The
Big Bang, like Rupert Sheldrake states quoting Terrence
McKenna, “Science just asks for one miracle, ‘Give us the
Big Bang’ and we will then be able to explain the rest of
creation.” This “particular” miracle involves the spontaneous generation of the Cosmic Soup of Gravity and
Electro-Magnetism from...
(wait for it)
Nothing!
"(But if Einstein made the prediction, it must be true.
Right? We must not be looking at the equation properly,
or perhaps were just not smart enough to figure this one
out. Perhaps Einstein’s brain was wired differently than everyone else’s… You know that don’t you, right?)"
We have all heard these excuses and myth building diversions that have been used against our common senses
from the first day of our indoctrination. ‘We must raise a
God for them to worship!’ and Albert Einstein was that
man. ‘Einstein has it all figured out!’ I’m sure this sentiment must have been echoed in and out of lecture halls all
around the world.
Who would dare contradict the reigning King of Physics?
Fortunately for our species there were a few individuals
that dared to challenge many of Einsteins misinformed assumptions. Walter Russell was one of them and without
hesitation he said this regarding Einstein’s Gravitational
Hypothesis:
“One of our most celebrated physicists has advanced the idea
that gravitation is not a force of Nature, but a property of Spacetime. This is a grave error which should be corrected at this
time (1926) lest it complex our already too-complex thinking in
respect to effects of motion.”
“In the first instance it is illogical to conceive of motion without
force, or of the power to appear to attract without a force backing that power. In the second instance it is illogical to conceive
that the effects of a cause could be due to other effects of a cause
without eventually getting back to the underlying cause.”
“Effects become causes of other things but effects cannot become
the cause of their own existence nor can they subtract themselves
from their cause. Space-Time are effects of force; they are dimensions of force; just as a foot is the dimension traveled by force,
or as a temperature is the measure of a resistance generated by
force. Time is merely the measure of intervals between sequences of events, which in themselves could not be unless force acted
to cause those intervals. And what is Space? Is it anything other
than a concept? Without light and two objects in the Universe,
could there be such a thing as Space?”
A supporter of Einstein went so far as to give him the benefit of a doubt by saying:
“This is Einstein’s “Theory of Equivalence.” It shows that
gravitation may have more than one explanation. And this
leads us to his own explanation, which is an altogether
new one.”
“Einstein thinks that Gravity is not, as Newton held, a
force, but a property of Space. That all the effects of gravity may exist where there is no attraction…Einstein’s theory
explains gravitation as a distortion of the world of SpaceTime due to the presence of material objects. He does not
explain how or why a body can distort Space-Time; the
theory (attempts) to explain gravity, not as a force of nature, but as a property of Space-Time.”
Walter Russell’s response:
“The Einstein theory of the constitution of matter conceives
this Universe to be One great ocean of Electro-Magnetism, out
of which—and into which—flow the steams of gravitation, material and energy. Radiation, the equal-and-opposite mate of
gravitation, without which gravitation is impossible, is entirely
ignored in this fantastic and unnatural concept.”
“Equally fantastic is the claim of this theory that, ‘It is possible
to have gravitation without Material,’ and for Space to exist
without Gravity or without Material.”
“The conclusion arrived at by Einstein that force is not necessary in consideration of the effect of gravitation is illogical,
because gravitation is force, or rather one half of the Universal
force. On the contrary, gravitation is the cause of motion in one
direction of which there are two, and Radiation, the other half,
is the cause of motion in the opposite direction.”
Again Einstein “does not explain how or why a body can distort Space/Time.”
“The answer is simple,” said Russell. “Space-Time is not distorted. It is perfectly symmetrical. It merely appears to be distorted. In the symmetry of the sphere, we have perfection.”
“In the symmetry of many spheres we have a supposed distortion of symmetry due to the time dimension of force which Nature takes to form the spheres through the office of electric contraction and proceeds to oblate them back again into nebulosity
through the office of Magnetic Radiation. During this process,
the apparent distortions are exactly balanced by equal and opposite apparent distortions which, in the sum total, is perfect
symmetry. Any unbalanced unit of a design is balanced into
perfect symmetry of bilateral design by its repetition in a mirror
held in any relation to it whatsoever… Natures apparent distortions are due to the varying pressures of the varying densities.
There are not two laws for the same principle.” Walter Russell
Magnetism performs the work of radiation as it seeks to
disintegrate that which was integrated by the centripetal
effects caused by the Electric/Gravitative force.
Nevertheless, the vast majority of scientists followed the
trend and jumped upon the “particle” wagon that would
eventually be summed up as, “a white lie!”
Dr. David Tong in 2016 gave this very lecture at Cambridge
Hall declaring that everything that was being taught or
had ever been taught there concerning the world of particle physics were based upon theories that were based on
a lie. It was built upon an admittedly debunked theory of
the three quark, electron based particle world. A world as
confessed by Dr Tong himself that doesn’t exist. He called
it, “A White Lie” ‘A Fairy Tale,’ like Cinderella or The Princess Frog.
Yet, because of the tremendous influence that intellectual giants like Einstein, Schrödinger and Heisenberg who
believed that the quantum world at its most minute level
was much more mysterious and counterintuitive than we’d
ever imagined. These men forgot the first rule of similarities; If (A) is equal to (B) and (B) is equal to (C), then
(A) is equal to (C). Or “As above, so below.” Or even my
own mantra of, “If you know one thing about one thing,
then you know one thing about all things. Find the common denominator and either multiply it or divide.” There
exists a flawless Super Symmetry that underlies the entire
Universe and it behaves in the Macro the same way that it
behaves in the Quantum world.
They just have to stop worshiping the falling gods of science and open their hearts and minds to the true and sim-
ple interpretations demonstrated in Nature. For all of Nature and the whole of the Multi-Verse is constructed and
maintained by the same two forces of Electricity and Magnetism. One spins to the left and the other spins to the
right and these two opposing vortices are the Cause of
all observable Effects of changing Pressure Conditions and
Motion Conditions.
So, now that we’ve been given a brief understanding concerning the overall topic of Quantum Mechanics and we’ve
also become more acquainted with some of the challenges
that arise when we attempt to marry what we know about
the “Quantum World” with the Laws that govern everyday life and reflect everything that we experience in the
“Macro world.” Let me share with you some of the closing
remarks from the lecture given by Dr Tong.
He continues by declaring that after a couple of quarter
centuries of collecting data from the most respected scientist in the world and reviewing that data that they now
think that they can approximate the “first principles of the
mass of a proton.”But Hold up:
DIDN’T HE JUST SAY THAT
THE UNIVERSE WAS MADE UP OF FIELDS
AND THAT THE ELECTRON AND PARTICLE
THEORIES HAD CRASHED?
So, who gives a hot fart about how much a theoretical or
more than likely non existent proton weighs? Yet here we
see them still trying to determine the mass of an object
that all their best data says does not exist.
“We’ve got the right equations. We’re pretty sure we’re
solving the right equation. It’s simply that we’re not smart
enough to solve it.” That was Dr. Tongs final relent.
Such an honest man.
To put it simply, whatever equations that you think you
have, they're wrong! If they were right, they would not only
give you a more lucid picture of how the UNIVERSE truly
works but they would also predict the proper distribution
of All Matter! A feat that not one of their theories has ever
been able to consistently accomplish. Something that only
the absolute truth in Mathematics and the Creator can accomplish and those with whom It shares its many secrets.
(AIN’T THAT A BOLD STATEMENT?)
Dr. Tong continues, “We’ve got the right equations. We’re
pretty sure we’re solving the right equation. It’s simply
that we’re not smart enough to solve it… There are some
situations where for fairly subtle reasons we’re unable to
use computers to help us and we simply have no idea what
we’re doing.”
Can you not hear the sincere frustration that Dr. Tong is
expressing? For I believe that the Community of Scientist
as a whole are truly seeking answers to the most fundamental of questions but they have been hamstrung and
hog tied by the false postulates that mislead their predecessors and their predecessors before them.
He continues: “You are all made of quantum fields and I
don’t understand them as much as I think I should,” and
he’s right, the periodic table was a nice place to start but
what is really important, is the motion and pressure conditions under which these elements interact. Those various
motion and pressure conditions he calls, “Fields.” That’s
not all, he then goes on to introduce one more particle
called the neutrino, a particle that he says is not really relevant to our everyday life. Then he introduces another set
of particles that behave just like these initial three particles, but are larger than the electron and they are called
the muon and the tau particles and for some in-explicable reason they up and decided to square themselves twice
and modern science has no idea why. Its all chucked up as
just another one of those great mysteries that govern the Universe.
He says that there are even more of these neutrino particles, 3 in all and he adds in a few more quarks but still
stresses mainstream science and mathematics inability to
make any sense of them.
Now do you understand why I thought that Dr. Tong
would be the perfect person to introduce the most important part of this book? He is an authority on this matter. His
intentions sound pure, so let’s listen closely.
By the way, it might help if you imagine in your mind a
very kind looking, thin fellow with a thick and very refined
English diction. He really does sound rather smart as he
says this next line which seems to completely contradict
everything that he was just talking about regarding the
fundamentals of the Universe as to whether they were
made up of particle or fields.
“All right, okay. So, what I want to do in the rest of this
talk is tell you where that vision takes us. I want to tell you
about what it means that we’re not made of particles,
we’re made of fields, and I want to tell you what we can do
with that and how we can best understand the Universe
around us.”
If we are not made of particles and are made of fields then
why do they need to calculate the mass of something that
is immaterial? It appears that most of the pursuits undertaken by theoretical physicist are just mental exercises if
they’ve spent the last 4 decades trying to measure the mass
of theoretical particles that their best theorist believe
don’t even exist.
Yet, Dr. Tong openly admits: “We don’t really even know
how to begin to start understanding these kinds of ideas
in quantum field theory.” He says that, “We have these theories of physics, the best theories we’ve ever developed…
but at the same time they’re also the theories that we understand the least.” And if the scientific community wants
any forward momentum they’ll have to either graduate to
a better understanding of the Universe or find better approaches for the experiments that are being conducted.
Now, the most important part of his lecture takes form.
Dr. Tong continues, “But this is everything. This is everything in the Universe. Everything you’re made of is these
three at the top, there, and it’s only when you go to more
exotic situations like in particle colliders that we need the
others on the bottom". (as he points to the equation of
the standard model on the board). "But every single thing
we’ve ever seen can be made out of these 12 particles, these
12 fields."
"These 12 fields interact with each other and they interact through 4 different forces. Two of these are extremely
familiar, to the force of gravity and the force of electro/
magnetism, but there’s also 2 other forces, which operate
only on the smaller scales of the nucleus.”
“Again each of these forces is associated to a field so Faraday taught us about the electro/magnetic field, but theres
a field associated to this, which is called the gluon field,
and a field associated to this, which is called the W and Z
boson field.”
“So this is the Universe we live in. There are 12 fields that
give Matter, I’ll call them Matter fields, and 4 other fields
that are forces. And the world we live is these combinations of the 16 fields all interacting together in interesting ways. 
So, this is what the Universe is like. Its filled with
these fields, fluid-like substances, 12 Matter, 4 forces."
"One of the Matter fields starts to oscillate and ripple.
Say the electron field starts to wave up and down because
there’s electrons there. That will kick off one of the other
fields. It will kick off say the electro/magnetic field, which
in turn will also oscillate and ripple; there will be light,
which is emitted so that will oscillate and ripple. At some
point it’ll start interacting with the quark field, which in
turn will oscillate and ripple, and the picture we end up
with is this harmonious dance between all these fields, interlocking each other, swaying, moving this way and that
way. That’s the picture we have of the fundamental laws of
physics.”
“We have a theory, which underlies all this. It is, to put
it simply, the pinnacle of science. It’s the greatest theory
we’ve ever come up with."
"We call it The Standard Model. It should really be replaced with: THE GREATEST THEORY IN THE HISTORY OF
HUMAN CIVILIZATION!” Dr. David Tong
The End of All Theories is what you’re
about to Witness!
Go ahead,
don’t be scared.
Turn the page!
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
