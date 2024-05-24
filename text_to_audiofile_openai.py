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
CHALLENGING THE STATUS-QUO.
Flat vs Round.
Well, it wasn’t until the 3rd or 4th grade that this question
came up again concerning the accuracy of 1 x 1 = 1. Around
this time we were being taught in American public schools
the concept of square roots. And as I recall, it seemed like
an easy enough stretch of our reasoning faculties to accept the answer given to us by our math teachers that the
square root of 16 was 4. When my teacher used it as an
example, she helped us to appreciate its simplicity by asking, “If you think about it class, what number times itself
equals 16?”
The class became silent but my hand flew up immediately
because I had taken the time to memorize the “Times Table” forwards and backwards and I could confidently recite
it up to 20 x 20!
When she asked the class, "what was the square root of
4?” Well, that was when everyone else in the room raised
their hands because the formula was then apparent to all.
Therefore, the young man that answered that particular question didn’t receive any bragging rights when the
teacher said that the answer was the number “2.”
From that point she tried to move on to the square root of
a much larger number, I think it was 25 or was it 100? Anyway, my hand shot up like a rocket. When she called my
name thinking that I was going to answer her question, to
her chagrin, her star pupil, which I had been up until that
moment, hit her with a doozie.
I asked, “What is the square root of the number 2?”
Again the room went silent, that was perhaps one of the
most confounding question that any 3rd grader had ever
asked her. She was perhaps more equipped to answer a
question like, “where God came from?” or, “how does one
turn water into wine?” That is how uncomfortable that
moment felt and how ill-equipped she was to answer that
simple question. A question that would define the very nature of my being and set me upon a course that would hold
me captive for the rest of my life.
I still recall the resounding silence of that fateful moment.
The bell of “PURPOSE” resonated within my being! From
then, until now, till time indefinite, it shall ring on forever.
That’s what the sound of Truth does to you!
When you reach your purpose, it is like what Paolo Cohello said in the opening of his international best seller, “The
Alchemist,” “Once you seek out your own personal legend,
The Universe conspires!” That is exactly what happened to
me that day, for that moment seemed to last forever. The
second hand on the clock on the wall just ticked by...
So, I just blurted out, “Based on the formula given, the
square root of 0 was 0, the square root of 1 was supposedly
1 but that didn’t leave any numbers that could fill the spot
for the square root of 2.” I then said...
“I think that somebody made a mistake with this part
of math.”
The teacher stood there for a moment with a look of utter
confusion upon her face and I now understand that deep
down inside she wanted to say 1 x 1 couldn’t equal 2 because of the “Identity Property” but maybe she didn’t 
fully understand the concept of irrational numbers.
I’m sure that she knew the prescribed answer, but I’m
not exactly sure that she believed what she had been programmed to say. Mind you, she was a very conscious teach-
er as I remember her. She would always take whatever time
was necessary for the class to understand a complex idea
no matter how long it took. That’s why I was particularly
surprised when she answered with, “No, that question is
a bit too complicated to answer with the time we have today.”
“How complicated can it be?” I asked her, “It sits right between two very simple numbers.” I laughed for a moment
knowing that for the first time I had stumped her. Mind
you, she liked me because since the first grade I had a habit of asking her questions that I thought were challenging,
and until this very moment she was undefeated in proving
to the class that she had all the answers, but not this time. I
marveled at the thought that I had finally got her with the
simplest of questions. “My all knowing teacher!”
I remarked with a bit of smug in my tone, “I don’t understand how that can be a complicated question?” It’s not
an odd number like 3 or 5, it’s an even number. The number 2 was the easiest of all the numbers to memorize in
the multiplication table. “How and when did it become so
complicated?” I thoroughly enjoyed this moment, because
for three years she was always the one who got the last
word. Finally, I would win the day, my point was valid and
she knew it.
I suppose she mistook my out spoken curiosity as if I was
mocking her or was it the devilish smirk upon my face? I
didn’t intend for the class to start giggling at her inability
to answer such a simple question but they’d witnessed the
question and answer game that she and I had played for
years and she more than likely recognized that I was finally
at match point and she reacted.
Reflecting back on that moment, after five decades of
questioning and contemplating, I now understand the
painful look drawn upon her face. How do you explain to a
room full of third graders the concept of “Irrational numbers?” Nevertheless, my intentions were not to frustrate
her at all, even though I did slightly enjoy it. Yet, I sincerely wanted to know, but:
"The Road to Hell is Often Paved with
Good Intentions"
She thought that I was just being obstinate and that perhaps, she needed to teach me a lesson for questioning her
authority.
She told me, ‘to get the paddle,’ that hung on the wall
next to the closet door, where our coats were also hung
and to put my hands on her desk, and to bend over so that
she could swat me.
As I recall, the paddle was about an inch thick, solid oak,
four or five inches in width and about 18 inches long. It
had a handle that looked like brass knuckle grips and there
were half inch holes that were bored through the face of
the paddle to help it gain speed before it hit you. (During
the seventies in the American public school system, corporal punishment was permitted and carried out by the
teachers and school faculty.)
Well, I refused to bend over that day and as she tried to
grab my arm and force my 8 year old body to bend over, I
yelled imploringly at the top of my lungs:
“GET SWATTED FOR WHAT?!"
"If the purpose of ‘class’ is to LEARN.
Then, how was I interrupting the class by
ASKING A LEGITIMATE QUESTION?
WHAT'S THE SQUARE ROOT OF 2?
THAT'S ALL!”
In an instant her face became bright red as she became
infuriated with me and sent me to the principals office,
where I received three swats from him and a two day suspension for disrupting the math class. Which garnered an-
other whooping from my father when he returned home
from work and found that I was suspended because now,
who was going to watch me during the day?
School served then as it does now for many lower income
families as a day care center rather than a place of education. On the suspension slip, under the section titled ‘Rea-
son for Suspension’ it read; “Insubordination,” a term that
I would remember because my father struck me multiple
times for every letter of that word.
Till this day I can recall him spelling it out but it was a
word that would become synonymous with my own personal empowerment. For it would ultimately embolden
my plight to end abuse of authority especially regarding
forced doctrine, dogma and the proliferation of false and
harmful concepts that are based upon tradition alone.
I suppose, the humiliation that I endured that day of being almost swatted in front of the entire class for question-
ing the established authority and it’s so-called unbreakable rules, must have left a lasting impression on the rest
of the class. After that no one ever questioned anything
that the teacher ever said. Everyone just did as they were
told. It was the end of innocence and the end of the illusion that children could learn in a safe and comfortable
environment. From that day onward, school became like
a prison yard with barbed wire fences and harsh penalties
for anyone who would dare attempt to scale its towers.
I on the other hand never learned to fear the repercussions of asking questions and seeking the truth. I innately
understood that the truth was not being taught inside the
classrooms. The truth was self evident in all observable
and natural phenomena. Therefore, I set out to find the
answer to and the true value of 1 * 1 = x and would not
stop and until I had accomplished my goals.
That was over 4 decades ago.
Anyway, while at home on suspension I continued my search
for the answer to that simple question that had somehow became so “COMPLICATED.” I thought if anyone would know
the answer to the square root of two, Einstein would.
So, I opened up the encyclopedia and began to read
about Albert Einstein. He never once mentioned the ,
although it is one of the most prolific values used in
quantum mechanics. Yet, I do recall Albert saying,
“Everything is relative” which I understood as, “Everything is related.”
I remember thinking, “Does he mean relative as in fami-
ly, like my brothers are ‘related’ to me?” After meditating
on that thought for a while as I was watching “The Super
Friends” the next morning, even though my father said
that, 'I couldn’t watch any television because I had been
suspended and was being punished and should suffer the
consequences of my actions.'
Nevertheless, I knew that I was basically being punished
for a crime that I didn’t commit and didn’t see the need to
subject myself to more of an undeserved and unwarranted
punishment. Actually, I had already suffered three separate forms of discipline for asking a very valid question. I
felt that the days of my martyrdom was over, I had suffered
enough! Therefore, when my father went to work and left
me and my brothers at home on that fall Saturday morning, well I rewarded myself with a nice big bowl of Apple
Jack’s and sat in front of the TV so that I could watch the
"Super Friends". During that program I heard Superman
say:
“One for all, and all for One!”
Why that struck a chord in me I couldn’t tell you but
something about (One) and (All) just made me ponder. It
actually brought my mind back to what Einstein said about
relativity. I interpreted his words as meaning, “If you know
ONE thing about ONE thing, then you know ONE thing
about ALL things. Find the common factor and either
multiply or divide.”
What a rare and insightful moment that was for me still
to this day. I live for those beautiful moments when the
Universe hands you a particular piece of the puzzle that
will ultimately become the cornerstone of your purpose in
life. When it whispers the gentlest note that only you can
hear, a note that will ultimately lead to the crescendo of
your own life’s opus.
I began listening more intently to the voice that came from
within, The inner voice of truth. That same voice that led
each and every single one of us to this thing called Life
That voice is heard more clearly within the natural world.
It sings in every established system that we see, hear, feel,
and taste. This Universe was built upon truth and that truth
is apparent in all of its actions and its countless reactions.
Everything within this Universe is connected and is of the
same substance, just under different motion and pressure
conditions. Therefore, Everything is “related” and is subject to the same genetic and atomic laws. 
Everything within this Universe behaves according to a predetermined
and predictable pattern in it’s winding and it’s unwinding.
Therefore, if All systems are inescapably connected, then
All systems are tied to the same inescapable laws that govern gravitational and radiational forces. All of these forces
are subject to the same math that governs and regulates its
expansion and contractions. So, Spin is a common factor
to them All and Spin is measurable.
It appears that all three of these separate and distinct species have not only spin but a great deal more in common,
especially in the beginning stages of their development,
at the place we call the start also known as the position of
One.
Spiral Galaxies unwind into Solar systems, that unwind
into Planets, that unwind into hurricanes, that follow the
same exact rules and laws that govern the Galaxy. These
governing laws are rooted in mathematics and mathematics is rooted in the nature of the number One. Therefore,
our valuation of the number One must remain consistent
with Universal values if our understanding of Universal
phenomenon is to be factual, accurate and ultimately beneficial for our species.
Relative factors must be taken into consideration in order
for us to have a clear and objective perspective on the matter. Otherwise, we will be forever 
subjugated by an incorrect and dangerously myopic view of the Universe and as
a result our thinking and reasoning ability will be likewise
connected to antiquated ideologies which will force our
species into the category called obsolete, and we will cease
to exist. In other words, we will be EXTINCT!
The hurricane ultimately unwinds into a myriad of other
weather systems. On land one of those systems is closely related to a tornado, which has the tendency of bringing the
tip of that giant common factor right down to our small
minded perspectives. From here on out; we will be considering some of the more conspicuously obvious relative
factors one by one as we continue on our search for understanding the value and true nature of One. Why don't
we allow the true and simple nature of the Universe as a
whole to weigh in on these most important issues? I bet
that after you hear their testimony, your view concerning
these matters might make a considerable change.
Let’s see if natural phenomena either supports or contradicts the claims of the Identity Element? I believe that it is
time to gain a bit of insight and perspective from the oldest
and most reliable witness on this matter. Hell! On any MATTER for that matter, (All puns intended) because Hydrogen
is the first visible element on the periodic table that will ultimately unwind into every other element/substance that
has ever been or ever will be observed within the visible
Universe.
Why don’t we consider the case of Hydrogen and the
whole of the periodic table of elements and see how they
weigh in on these matters?
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
