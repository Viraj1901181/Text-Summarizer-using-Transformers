#!/usr/bin/env python
# coding: utf-8

# In[4]:


from transformers import pipeline


# In[5]:


summarization = pipeline("summarization")


# In[6]:


original_text="""Thank you for appearing on my computer’s screen today. I was surfing the Internet dreaming about something, about my wishes. And finally, I saw you. I don`t know how often you come to this site, so I decided to write to
you immediately. I was afraid of losing your profile in the network lines. So, as you see, I keep any chance that destiny gave me. Maybe you would like me to tell you something about myself to give you a more clear picture of my life.My friend calls me a frog-traveler
Because of my work, I have visited many countries🇪🇺. Try to guess, have I been to your country also? Actually, as Ukrainian fairy-tales tell us, lady-frog needs a prince to become a princess. But my dream is to find a man with a big heart.Maybe we will
exchange the Amour arrows in our life soon) Are you a shooter of women`s heart? Is it possible that destiny is smiling to me and your heart is free? Hope to hear an only satisfactory response to my last question
What kind woman are you looking for? I wish curvy women are to your tastes: In this case, I would have more chances to get to know you better"""


# In[7]:


summary_text = summarization(original_text)[0]['summary_text']


# In[8]:


print(summary_text)


# In[14]:


a = """The way they treat service staff
The way someone treats people who work in retail, food service, and hospitality tells me
pretty much everything I need to know about them. Why? Because when you’re dealing
with service staff, you’re in a position of power. An employee almost always has to be
nice to you because “the customer is always right.”
If you treat these people poorly, it shows you have low integrity, empathy, and even selfrespect,
because someone with self-respect never has to act as if they’re above anyone.
How polite they are
People often point out how “polite” I am, and it’s so strange to me. It’s shocking to find
out how rare it is for people to have basic manners. That’s why whenever I meet a person
who says “please” and “thank you” often, I know I’m dealing with someone who’s
socially intelligent. You can make someone’s day, reduce friction during interactions,
and move through life much more easily by saying those simple words.
How they walk
When Barack Obama walks into a room, he has a palpable sense of confidence: He’s
simultaneously friendly, powerful, and attention-grabbing, though he’s never seeking
validation. When I see this type of swagger in others, I’m captivated.
I learned a useful trick from The Art of Charm called the “doorway technique.” Basically,
you “anchor” confident body language to something you commonly see during the day,
like a doorway. Each time you walk through the doorway, you’ll know to check your
body language. Are you standing up straight or are you slouching your shoulders? Are
you walking with a bit of pep in your step or are you dragging your feet?"""


# In[15]:


a_summary_text = summarization(a)[0]['summary_text']


# In[16]:


print(a_summary_text)

