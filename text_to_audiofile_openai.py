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
THE WORLD'S
DEPARTURE
FROM THE
GOLD STANDARD
Money can't be multiplied, or can it? Money can be multiplied by a number, but can it be multiplied by itself?
If you can remember some of the earlier lessons from elementary school, we learned everything has a common
denominator and can be reduced to its lowest terms. In
the field of Mathematics this means that Everything has
a relative numeric value and once that value has been determined, that substance or condition of Matter can then
be made equal to All Other substances or conditions of
Matter. In other words, if the monetary value can be made
equal to the number it's being multiplied by, and you can
successfully eliminate any and all distinguishable differences between the currency and the integer, then in all
truth, money can be multiplied.
We are essentially multiplying one electronically generated number by another electronically generated number,
in theory. This process of equalizing differing values is one
of the very first lessons we are taught regarding fractions.
You must first make the things being multiplied or divided, dimensionally equal? Yet, in order to do so you must
do the work necessary to convert them. This process ofconversion is when we align the things that you are trying
to manipulate. We have to first place the values in relative
dimensional order, from that point forward the number
being multiplied or divided can then be manipulated at
will.
For instance, in order to multiply 1/5 times 3/10 either
the 1/5 fraction has to be converted to the dimension of
the 3/10 or vice versa.
The moment that you've successfully completed the conversion both fractions become 
fair game and can be multiplied or divided by each other.
This is also true concerning money or currency. You
might say that paper money or currency isn't just a collection of imaginary numbers though, nor is it a set of
virtual arbitrary fractions. One might define money as
being a convenient representation of some inconvenient
real physical asset. Therefore, how can one multiply a real
physical asset? To be perfectly honest with you, our dollar
is not linked to a real physical asset. Our paper money isn't
a convenient representation of anything except that of a
very vivid imagination because our currency is no more
valuable than the paper that it is printed upon.
Try to comprehend this simple but irrefutable fact; ever
since the U.S. dollar was taken off the Gold Standard it
has effectively been based upon a fiat monetary system, a
virtual system, an arbitrary system with imaginary values.
The dollar is no longer anchored to a real and specific asset. Therefore, there aren't any real safeguards to prevent
financial institutions from manipulating the currency that
is held within its virtual safes or anything preventing perverted governments from over printing money which is
essentially the art of multiplying money.
When the dollar was based upon the GS (Gold Standard)
it was relatively impossible to multiply money. I mean, you
couldn't just wave your hand and magically cause the gold
in your reserves or precious metals that the currency represented to instantly increase in number. The GS helped
to regulate the growth of the economy because in order
for the economy to grow the gold supply at the reserves or
banks had to likewise grow and unfortunately, gold mines
couldn't produce enough gold to satisfy Man's insatiable
greed. It also served in the capacity of a gate keeper regarding inflation because the value of the dollar was root-
ed in a solid and trustworthy foundation and couldn't balloon out of control.
Nevertheless, in 1933 when Franklin D. Roosevelt closed
down the U.S. banks and then reopened them 10 days later,
the financial world would never be the same. He issued a
mandate stating that all US citizens should turn in their
gold and gold certificates to the treasury department if
they wanted to receive a favorable exchange rate for their
value to be paid out in US dollars. From the 350,000,000dollars worth of gold that was collected from that government decree, Fort Knox was founded. From that moment
onward, the United States Government began its slow but
steady departure from the Gold Standard. By 1971 when
President Nixon signed the Executive Order officially taking the US off the Gold Standard the rest of the world
would soon follow and before long all of their respective
currencies became based upon a virtual monetary system
commonly referred to as a "Fiat" system. An electronically
fluctuating system that is represented by 0's and 1's as part
of a binary program. A potential money laundering program ensued that has more in common with a Play Station
or a Game Boy than Fort Knox because its value exists only
within the imaginary walls of a computer generated program.
Now instead of the dollar being tied to a specified quantity
of gold, silver or other precious metal the value of a dollar
is based upon fluctuations of confidence that exists within
the financial markets as prescribed and set by an "Unelected Central Banking Committee." This is why the financial
world is so vulnerable to the possibility of a dollar being
multiplied in pennies, nickels, dimes or in quarters where
each one of these currencies gives a completely different
value for the same calculation of a dollar times a dollar.
Remember, "EVERYTHING has a common denominator
and can be reduced to its lowest term."
So, now that there is literally no difference whatsoever between the dollar or the integers that it is being multiplied
by, there is nothing to prevent a dollar from being multiplied by another dollar. When the world governments
ceased to base their currencies upon hard assets, at that
moment all currency became nothing more than virtual
digital markers which represent nothing within the real
world. These digital markers can now be multiplied and
divided in the same like manner that one multiplies or
divides any other imaginary number that exists within a
computer generated program.
In all truth, this problem was brought up over 160 years ago
by Richard Dover Stater who also provided a SOLUTION
which was never incorporated. And it could have helped us
avoid this quagmire that we find ourselves in today.
Now that I've
explained one way
that money can
be multiplied and
some historical
examples, would
you like to see
what could
be possibly
taking place
behind the hidden
walls of the
financial world?
Does a penny times a penny equal one penny based upon
the rules of multiplication? Or does a penny times a penny
equal 0.0001 based upon our current decimal system. A value so small that there isn't even a currency circulated for that
amount by the US Department of Treasury. All calculations
shown here are reasonable forms of multiplication but which
one remains consistent with Observed Universal Phenomena?
How would you like your money calculated?
THE PLAIN AND SIMPLE TRUTH
As you can clearly see, for all of our unfortunate lives, and
for most of Mankind's chaotic existence upon this planet
under the false banner of a civilized society we've been,
(If I may borrow a phrase or two from the legendary civil
rights leader, Malcolm X), we've been misled, bamboozled,
we've been had, hood winked, conned, taken advantage of,
taken for a ride around the proverbial block, taken to the
cleaners and we've been taken to the bank, literally!
The British just so happen to have a phrase that they use
to describe someone who is short sighted and a tad bit slow
when it comes to finances. They call it being " Penny wise
and Pound foolish." Unfortunately, that describes 99.9%
of the past and present populations of the world.
Nevertheless, the Proverbial "Buck Stops Here!" All pun
intended.
Daniel 2:31-35
31 “You, O king, were watching, and you saw an immense image.
That image, which was huge and extremely bright, was standing
in front of you, and its appearance was terrifying. 32 The head of
that image was of fine gold, its chest and its arms were of silver, its
abdomen and its thighs were of copper, 33 its legs were of iron,
and its feet were partly of iron and partly of clay. 34 You looked on
until a stone was cut out, not by hands, and it struck the image on
its feet of iron and of clay and crushed them. 35 At that time the
iron, the clay, the copper, the silver, and the gold were, all together, crushed and became like the chaff from the summer threshing
floor, and the wind carried them away so that not a trace of them
could be found. But the stone that struck the image became a large
mountain, and it filled the whole earth.
John 16:12,13
12 “I still have many things to say to you, but you are not able to
bear them now.
13 However, when that one comes, the spirit of the truth, he will
guide you into all the truth, for he will not speak of his own
initiative, but what he hears he will speak, and he will declare
to you the things to come.
The
TRUTH
Will Set you Free
Truth: (noun)
1. a transcendent fundamental or spiritual
reality.
2. that which is Irrefutable and in accordance
with fact or reality.
COMMON SENSE AND MANKIND'S
HASTENED DEPARTURE FROM IT
In the process of writing this book I've had the pleasure of
conversing with literally thousands of people from virtually every corner of this world and from almost every walk
of life.
Categorically, 9 out of 10 persons when asked the question, "What's a dollar times a dollar?" Their initial centers
of cognitive thought, the place that is ruled by common
sense answers the question with a shy confidence of,
"Two!"
Then there's always a slight pause as the confidence in
their overall common senses begins to fade because we
were taught to ignore what is common to us. At that point
we make a desperate attempt to correct our mental mathematics, searching the visual cortices of the brain hoping to
find a mental picture of the problem written upon a chalk
board, or table, or in a publication of some kind, searching desperately out of fear that we could possibly answer a
question this basic, wrong.
You can almost hear their heart rate surge as they search
for the correct answer. Then, with a little less certainty
they seemingly whisper:
"Yeah uh ... 2."
"Right?"
"No, its 1 ?"
"Isn't it?"
"Its 1 ?"
Then they abandon the challenge with, "I don't really know
math." How sad? For this question should be the simplest
of questions. The correct answer should roll off the tongue
with certainty and authority, not insecurity and self loathing.
When you first read the cover of this book, do you recall
how your mind processed the initial question? Can you recall the conundrum that this simple question raised within
your own mind? If the question was,
"What is 1 x 1 ?"
The mind could have easily regurgitate the indoctrinated
answer that's been drilled into our subconscious throughout the course of our lives and it would have sputtered out
the prerecorded answer of "1 ".
Because this question regarding "What is 1 x 1" means nothing to you, it lacks a physical relation to you or your life
because mostly it is an imaginary calculation, but when a
monetary value is attached to it, the entire game changes.
We begin to question the end result. Instantly, the answer
that we give matters. It transforms the question from a
non-existent and irrelevant state, into an immediately relevant and almost defensive material state because cash/
currency is how most of us sustain our existence.
Remember, that knee jerk reaction that we spoke about,
that someone initially experiences when asked a question
concerning the resources that sustain their existence?
Well, Malcolm Gladwell referred to this reaction in his
book "Blink" as a 'blink' moment. That, 'gut' feeling that
screams from within telling you that, "Something smells a
bit fishy." That instinctual survival response that has been
sharpened and honed by hundreds of millions of years of
a dramatic life and death saga. A story of untold misery,
heartache and unbelievable triumph that has shaped the
selfish gene. Insuring its survival over thousands of millennia.
A determined gene whose will shall outlive our present
human form of concentrated conditioned states of Matter
and will ultimately fulfill its Universal purpose of bringing
All Things into balance. You are the present physical manifestation of that spirit like force, that gene who continues
to live and has managed to do so because of the uncompromising Nature that resides in that mental state we call
our sixth sense. A State of Being that cannot be bullied by
the dogma of consistent messaging, because this mentalstate is more of a spiritual state, an incompressible state of
Being. It is the truth from which All Life springs.
That is the part of our survival arsenal that can not be
dismantled, because it speaks from a place of truth. It is
the very instinct that guided you as a sperm racing against
hundreds of millions of your own brothers and sisters to
the egg in your mothers body and then lead you to the
most secure place in her uterus in order for you to attach
yourself and transform that uterus into a womb. As a result
of trusting that inner voice, you are here today alive and
awakening. The "gut" feeling, that instinctual response
that has been honed over hundreds of millions of years in
this continued process of evolution, in order for this
selfish gene, which you are the present representation of, can continue to survive if we
heed its warnings by listening and recognizing the truth from the lie. Malcolm Gladwell
tried to warn his readers against the pitfalls associated with ignoring our gut feeling.
He showed numerous examples of individuals who were defrauded out of millions of
dollars throughout the course of history simply because they failed to listen to their gut
feeling. With that thought in mind, I'm going to ask you to answer a series of questions:
When I ask you what is a PENNY times a PENNY ?
What was your gut reaction to that question? Did you have a moment when you had to
argue with your mind. Did you want to answer, "2 pennies?"
The answer, feels logical, like it's the common sense answer to the question, right?
It is consistent with Universal phenomena.
It doesn't violate any of the known laws of
physics.
Yet it felt as if someone was standing behind you, shaking their head, shaming you. As
if they were trying to force you to respond with "1 penny?" Right? Or you might feel like
returning back to the false idea that our modern currency is based upon a physical asset,
a hard asset? So does most of the world but unfortunately, our world economy is, as they
say, "Past the point of no return." It is virtually impossible tor us to return to the Gold
Standard short of a complete global economic collapse, followed by absolute anarchy
and then the world may hit the reset button.
Nevertheless, there is this possibility, but
this operation is illogical. For it completely violates Newton's 3rd law of "Action and Reaction." It
doesn't even look right, it feels as though we are being cheated, doesn't it? Yet, this is the programmed
response that has been seared into our minds from
infancy, based upon the
false concept of 1 x 1 = 1.
Even though the programs in our computers and calculators
gives a valuation that is much worse.
Remember: 0.01 X 0.01 = 0.0001
That is far less than the 2 cents allotted
for common sense, (all puns intended)
that's 1/1000 of a dollar.Who is that person, whispering in the back of your conscious mind, causing you to first
doubt your common-instinctual senses and then to abandon it all together for conventional thinking that leaves you at a loss? Where does that voice come from? How can
they have such a powerful influence over you?
Did that voice try to tell you that you don't have to answer that question because, "You
cannot multiply money anyway?" Remind that voice that our money is no longer based
upon a GOLD STANDARD, our money is no longer based upon A HARD ASSET, the
FIAT system that our money is rooted in is an imaginary system that is set and regulated
by fluctuations of trust and confidence within the market, overseen by an UNELECTED
CENTRAL BANKING COMMITTEE. Consequently, our money behaves and operates
according to the same rules as computer generated numbers. Therefore, money can be
multiplied.Next question, what is a dime times a dime?
Did you instinctively want to say two dimes?
But you found yourself hesitating for
some reason?
Did the voice in your head try to stop
you from responding?
Are you feeling a little anxious at this
moment?
Has your heart rate increased? Are you beginning to feel a bit defensive? Well, that
means that you are fighting back. First, against me for raising the question, then you
will redirect your anger to the imaginary person in your head, the "PAIN BODY " that
Eckhart Tolle speaks of in many of his books, most notably in "The Power of Now." That
'pain body' is the accumulated representation of all of our regrets and short comings.
The residual effects of years of ignoring our instincts. THE PAIN BODY!
Once this imaginary person is exposed to the light, as it were, this pain body dissolves
away immediately because it can only exist in a place that tolerates a lie. When the truth
becomes apparent, the "lie" evaporates like the illusion of darkness retreats when a light
bulb is turned on.
You want to know why your. first thought was 2 dimes? It is because the Universe spoke
through you and answered according to the Associative and Commutative laws which
states: "When (a) and (b) are positive integers, that (a) is to be ADDED to itself as many
times as there ·are units in (b); the ADDITION of a number to itself as often as is indicated by another number." It naturally doubled it as its first step. Then afterwards we
can begin to compare the value of the dime as being ten pennies, and from their make a
secondary calculation but your first reaction more than naught is in line with Universal
Truth and the more conscious that you become the more connected you will feel to that
Truth.
These are some of the immediate discrepancies that arise from the lack of balance that
exists between Man's methods of multiplying compared to how Nature multiplies.
Based upon a dime being worth 10 pennies:
And 10 pennies times 10 pennies equals 100 pennies, then it should follow that:
But again the programs in our calculators and our computers tells us
that a dime times a dime equals: 'one penny.'
If that's not a smack in the face
to our common sense then
I don't know what is.
Perhaps a big part of the "Pain Body" comes from this kind of
perpetuated confusion.
Nevertheless, having this new knowledge, just by virtue of you using your incredibly developed minds to begin questioning some of the dogma that has dominated our thinking
faculties, you are starting to feel a greater confidence concerning your own thinking and
reasoning abilities which is part of the journey to "Awakening". Recognizing that you are
a part of a greater community than just yourself or your circle of friends and immediate
environment. You are beginning to recognize that you have no beginning and cannot
possibly fathom having an end. This is the reward of being centered in the Truth. This is
the path of those who are not afraid of the confines of this system of things. These are the
individuals that will help the rest of our species Awaken from our slumbering thoughts of
generalities or useless Approximations.
APPROXIMATIONS
We live in a world where accuracy once played a vital role
in the advancement and overall smooth functioning of
our given society. It matters not what species is involved
in the process of summarizing information about a particular place or thing, the necessity for accuracy is still a
vital part in determining whether or not that species will
achieve sustainability.
Take a Honey Bee on a wing, a scout may travel miles in
search of meadows filled with blossoming flowers that may
sustain the pollen and nectar requirements of the hive.
Along the way of finding that meadow that particular
scout may have changed direction countless times as she
tasted the breeze and followed magnetic signatures and
indicators in the color spectrum that would signify a food
source is nearby. Now, try to imagine the excitement that
bee feels rushing to return to her hive and report that she
has located a food source before another competing hive
finds it. She has to deliver that information accurately, efficiently and expeditiously if the rest of the hive is to find
that particular meadow.
The transmission of this information is accomplished
through a particular number of gyrations of her upper
and lower abdomen. This number must be precise because
two gyrations to the left may mean the difference of 23
degrees north of the hive or 46 degrees south of the hive.
Each gyration translates into a specific vibration or frequency that is interpreted by the rest of the hive with such
accuracy that the hive is able to locate one particular flower out of millions of blossoms.
This method of communication is repeated in the processes of finding water, the location of other hives with
their colonies, along with the necessary information regarding potential threats to the colony as in the case of
certain birds or other predators. Every gyration relays a
different detail which has enabled the honey bee to thrive
and populate almost every continent upon this planet for
hundreds of millions of years.
If the Honey Bee based its relating of information on Approximations "a shake or two in this direction, maybe bob
the head to the left or to the right. It all depends on how
you feel. Antennae up or down, don't worry about it, we'll
try to figure it out along the way... ". They're extinction
would have occurred long ago.
Accuracy is the life's blood of any species seeking a prolonged existence. The model of the Honey Bee can be
applied to relatively any insect, species of bird, pod of
aquarian mammals, and even the basic DNA or RNA of
any species.
Every DNA or RNA is made up of a particular arrangement of chemical elements that combine to form complex
molecules and proteins. Each and every single strand of
connected elements are governed by one law,
"The law of PRF (Prime Resonant Frequency)."
Meaning that every element either bonds or breaks its
bonds with other elements based upon a specific number
of vibrations. An accurate number of vibrations holds all
Matter together or causes the release of collected Matter.
This is the contracting and expanding principles of the
Universe working at the smallest level. Some of that motion has been observed and classified under a term called
the "Browning Effect". Nevertheless, if any one of those atoms oscillated one time either more or less in a sequence,
the process of bonding or the breaking of bonds would
never occur. Consequently, there would be no such thing
as reproduction, nor birth, growth, aging and eventual
death, which leads to a rebirthing process. For all of these
functions that are directly reliant upon accurate oscillations of each element in order for there to be this thing
called Existence.
In all of Nature, accuracy is the hard rule of thumb and
I believe that it should be as clear as an un-muddied lake.
The relative importance that accuracy and rigor plays in
the success of All Things in existence. Why then does Academia feel that accuracy is not essential in their observations and our existence in this Universe? Is it possible
that Academia takes it for granted thinking perhaps since
the rest of the Universe is so predictably accurate we can
even tell the exact day that the next comet will pass near
the Earth's orbit hundreds of years in advance. Maybe Academia believes we can afford to take certain liberties concerning our actions and measurements.
Perhaps they feel since everything else follows the specific
rules Concerning Universal Law, perhaps the law doesn't
apply to Man. Maybe Mankind can simply adjust as he goes.
That view is certainly demonstrated in the fluctuating rules
that govern our Mathematics and our Sciences. I believe
that it is painfully clear that this last remaining species of
hominids have no intention whatsoever in prolonging its
existence, judging upon our current practices in math and
science and our overall general ideologies.THE ABSOLUTE IGNORANCE
OF ZERO
A NON THING
When was zero invented?
The first record of zero appeared in Mesopotamia around 3 B.C.
The Mayans of South America are also credited with its invention
independently of the Mesopotamians, around 4 A.D. The concept of
zero was later seen in India in the mid-fifth century, it then spread
to Cambodia around the close of the 7th century, ultimately making
its way into China and was subsequently adopted into the Islamic
countries by the end of the eighth century.
Robert Kaplan, authored "The Nothing That Is." He states,
'In Mesopotamia, several thousand years ago, a slanted
double wedge was inserted between cuneiform symbols for numbers, written positionally, to indicate the
absence of a number in a place. The (0) indicated that
there was no digit or number in the given column.
Now that we've addressed the possible origin of zero (0), let's examine how this "place holder" has become confused with an actual
value.
Once Something comes into existence, its 'EFFECTS' are forever
present. Even though the initial 'CAUSE' may have dissipated or disintegrated from being a concentrated mass or initial force, nevertheless, the 'EFFECTS' of that initial force or action perpetually unwinds centrifugally, until all its radiated manifestations are collected
together again in a positively charging, centripetal spin.
As in the case with exploding stars, we can see the effects of that
star even though it may no longer be shinning. It may have tendrils
of Hydrogen filaments that may stretch as far as 100 billion miles.
Also, the effects from the Light that it produced while still alive continues to reproduce itself and show its effects in the night sky and
in the life force. Again, once Something comes to be, it will forever
have measurable effects upon All that is. There is no such Thing as
Nothing! I challenge anyone to show me one example.
Equilibrium is the common ground and the currency for all Universal phenomena. Yet, it does not mean that there is 'No Thing' there,
it simply means that a system is in what appears to be in a "state of
balance" momentarily.
That State of balance can never be reached because of the inertia
gained through motion in the Universal process of either increasing
pressures or decreasing pressures that the wave field generated always overshoots the desired equilibrium as conditions reverse from
an electrically charging system to a magnetically discharging system. Nevertheless, everything must remain in motion. Therefore,
even that temporary state of Something appearing to be at rest is
only an illusion for if One Thing in this Universe ceased its motion,
then All Things connected to it would likewise have to cease their
motion and that would mean that the entire Universe would have to
cease its motion because All Things are connected in this Universe.
At which point the entire Universe would cease to exist because All
Energy is expressed in motion and a Universe void of motion is a
Universe void of Energy.
So, it is fair to say that the concept of zero (0) has been either misrepresented, misinterpreted or completely mis-understood. I once
had a debate with an esteemed professor of Mathematics from Chicago University concerning the notion of (0). It went as follows:
I was on a publicity tour for the release of the feature film "Red
Tails" and we just so happened to be having dinner at the Montage
Resort in Dana Point, California. I made the statement that, "There
was no such thing as zero." He looked at me with a puzzled look
upon his face for a moment and then the professor said,
"Lets say you had an apple and
I had an apple and you
gave me your apple."
"How many apples do you have?"
I said, "I have two apples."
He said, "You don't understand, you gave me your apple."
I said, "No, you don't understand. As long as you are still inside this
Universe, whatever you have, I have. Because Everything in this Universe is connected to Everything else."
"Even if you could take my apple and place it into an adjacent Universe, I would still have two apples because as long as that Universe
is touching this Universe then Everything in that Universe is still
connected to and influenced by Every single atom in this Universe."
"Therefore, my giving you my apple is paramount to me transferring
my apple from my left hand to my right hand because All Things are
One."
It may have been a bit too philosophical for him but the first law
of thermodynamics holds true here, "Energy can't be created or destroyed, it can only be transferred or transformed."
Does that help in understanding the illogical nature of our current
concept and practices associated with (0) zero?
Can you make Something truly disappear? A magician can create
the illusion of Something disappearing but it is only through some
talent regarding deception, a trick or slight of hand.
Within our current practices of mathematics we are being misled by
the illusion of Something becoming a Non Existing Thing because of
the "IDENTITY PROPERTY." Another interesting observation is the
fact that the Identity Property/Element never mentions dividing by
(0) zero. Why? Because the dividing of anything by a (0) zero value
drives the result to an infinity. What is wrong with that? You might
ask. An "Infinity" in a mathematical result is a red herring indicating
that something is 'definitely' rotten in the state of Denmark.
Simply put: if you can multiply by a zero (0) value then you should
also be able to divide by a zero (0) value. If one operation is impossible then neither operation is possible because Everything polarizes
from positive to negative by multiplying or dividing its potential and
a zero value has no stored potential.
Again the "IDENTITY PROPERTY" states that, "Anything multiplied by zero becomes a zero product". This concept is based upon
what Universal principal? Where in Nature does Something encounter Nothing and that Something completely disappears? Perhaps in
the Bermuda Triangle, Area 51 or the soon to be debunked concept
of the Black Hole, none of these aforementioned irrational and conspiratorial theories have any place in the world of a so-called fact
based system of science and mathematics.
Yet, our current system of mathematics actually subscribes to this
illogical practice which makes our calculations regarding zero as
reliable as a disappearing rabbit into a top hat at a circus sideshow.
How foolish! Even more peculiar is the fact that Nothing can be divided by (0). If it can't be divided by zero then it cannot be multiplied
either, for multiplication is the opposite of division and essential for
Universal Equilibrium.
As was reasoned upon earlier, multiplication is an exaggerated form
of addition. When a number or integer is added to zero that number
or integer goes unaffected.
Like passing your hand through the air, if there is no wind resisting
the motion or movement of your hand, the hand does not disappear.
If one is added to (0) it still remains one, and if multiplication truly
finds its roots in addition, then how can an exaggerated condition
of not being affected by a Non Thing result in a Non Thing having
so great an effect that it completely breaks the laws of experienced
Universal phenomena and the very principles of existence?
The simple truth is that this concept of multiplying by zero must
be a false concept, another mathematical fallacy . If the results of
a hypothesis or theory cannot be reproduced under natural condi-
tions then that concept must be abandoned and replaced by a more
reliable theory with reproducible results.
When Something is multiplied by Nothing that Something remains
unchanged. It does not cease to exist simply because it did not come
into contact with Something that does not exist.
Long story short, the concept of multiplying anything by zero is in
desperate need of an immediate audit. In 1926 a brilliant man by the
name of Walter Russell authored a scientific and mathematically astounding book called The Universal One. In this Masterpiece he not
only redefined the periodic table of the elements but also corrected
many of the false ideas concerning the nature of the Universe and its
functions. One such correction was the very nature of Electricity as
the contractive and gravitative force and Magnetism as the radiative
and expanding force in the Universe.
Prior to Russell's ground breaking work, all literature and understanding upon the subject along with the standing ideas and theo-
ries had these two equal and opposite forces behaving in contrary
ways to the actual work that they preformed. His ideas were so revolutionary and insightful that many of his discoveries concerning
chemistry were stolen by lesser men who went on to collect Noble
Prizes for his life's work, because he was not accredited.
Nevertheless, a free thinker by the name of Nikola Tesla became
aware of his work and the two became fast friends. It has been reported by people who knew the odd pair of friends that Tesla once
warned Russell that his insight was far too superior for the people of
that time and that he should seal up his work and place it in a times
capsule for a thousand years and perhaps a future generation would
come to appreciate his discoveries.
That was 92 years ago, and our scientific and mathematical community has yet to begin to understand or consider his beautiful and
most truthful work. Yet, Tesla did say that we have perhaps another
908 years to go before they might be ready. I personally believe that
his estimation might have been a very conservative one at that. Perhaps it will take a few millennium more. I hope that this generation
will take a firm stand on the side of truth and reform our general
understanding of Universal phenomena.
UNIVERSAL MATHEMATICS - UNIVERSAL RATIOS
Walter here offers extraordinary insight concerning zero:
"Let us add to the pressure laws a dimension law. All dimensions contract
in the direction of electric force and expand in the direction of magneticforce
in universal ratio.
Equilibrium of motion-in-inertia is represented by zero. Zero in sex, force
and motion means an equilibrium of pressures. Four means maximum pressure opposition.
The intermediate twos and threes, plus and minus, are the comings and
goings between the cold zero of expansion in the violet of inertia and the hot
four of contraction in the yellow of opposed motion.
Zero in force does not represent nothingness, nor does plus mean more than
nothing nor minus mean less than nothing.
Such a concept of mathematics is not in accord with a Universe of the illusion
of motion.
The One substance is a tangible substance. It is SOMETHING.
This is not an empty Universe. It is not a void. Non-dimension does not mean
nothingness.
The Universe of the One thinking substance is not one of quantity or dimension. It is a substance capable of causing an appearance of quantity through
the life principle of the substance which we term "energy."
The universal constant of energy is an X quantity.
An X quantity is apparently divisible.
This divisibility of quantity and its dimensions are relative and measurable.
The relations of its dimensions are in fixed ratios.
These ratios are simple and absolute, but their apparent variability is complex.
The universal constant may be added to or multiplied by, but its accumulation never varies in its relative dimensions.
The dimension X is unimportant for it represents the illusion of a total of
apparent motion which disappears in the equilibrium of inertia.
The dimensions of relative ratios are important, for by knowledge of these
relations one will be enabled to assemble divided quantities in any desired
multiple to produce any desired effect. All dimensions are relative.
All dimensions are either more or less than equilibrium.
This is a Universe of more and less.
Every effort of motion which is added to must be equally subtracted from.
Mathematics are bounded by the absolute limits of effects of motion measured
by adding to or by subtracting from in universal ratio.
Mathematics cannot transcend universal limitations.
Multiplication and division are but ratios of more and less."
Walter Russell, The Universal One. Published 1926
THE MOTION AND PRESSURE CONDITIONS
THAT GOVERN SPACE/TIME
My Mother and Father also taught me that, "If you break
something, you have the responsibility to fix it."
Also, "If you tear something down, You must replace it
with something better."
I have spent the majority of this book, reviewing many of
the laws that have helped countless others including myself reason upon the foundation of logic, which should always be anchored in truth.
I have also pulled at some of the loose threads leaving the
fabric of our standard model of the Universe tattered and
full of holes.
I believe that the Lynchpin (a new geometry) will help
Mankind to have faith in the value of the number 1 once it
is fully understood and embraced by a reluctant world that
seems resistant to change now that we have entered the
winter of our species. Yet spring is near and with it comes
New Light and a fresh perspective to help raise the number One and the Children of Light to their proper place.
I have likewise spent a considerable amount of time breaking down and tearing apart the foundations of the Platonic Solids.
In view of the karmic responsibility instilled in me by my
parents I would also like to share with Mankind the wave
dynamics and structures that I have discovered. They redefine our understanding of our Multi-Dimensional Universe.
This is a subject for an entirely different book but for now,
here are a few insights into the true Nature of what physicists have been calling "Dark Matter" or more directly conceived as "I don't know" Matter or "some kind of invisible"
Matter although it is the source of all visible light.
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
