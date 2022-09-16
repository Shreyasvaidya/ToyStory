import translators as ts

def hindi_to_english(text):
	return ts.google(text,from_language = 'hi',to_language='en')
def english_to_hindi(text):
	return ts.google(text,from_language = 'en',to_language='hi')


#test
text = """the catapult, also known as a slingshot or a Gulel, is a tool which is also known as Baatul in rural areas. In the early days, the Gulel’s popularity was so widespread among Adivasi boys, that it had become their best companion.The boys always kept the Gulel with them while grazing cattle in the fields .The Gulel turned out to be very useful- the flock of birds could be easily chased away without exerting too much effort, throwing stones or shouting. A person with a Gulel and some pebbles can sit in one place and chase birds away from a distance.The Gulel is a multipurpose tool- not only is it used to chase away birds, it is also used as a toy, a sports equipment or a weapon. 
This classic Slingshot/Catapult toy from the 90's consists of a Y-shaped frame held in the off hand, with two rubber strips attached to it. The other ends of the strips lead back to a pocket which holds the projectile. The pocket is grasped by the dominant hand and drawn back and then let go, very similar to a catapult.
"""
print(english_to_hindi(text))
