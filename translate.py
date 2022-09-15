from libretranslatepy import LibreTranslateAPI
translator = LibreTranslateAPI("https://translate.argosopentech.com/")
def hindi_to_english(text):
	return translator.translate(text,"hi","en")
def english_to_hindi(text):
	return translator.translate(text,"en","hi")

#test
print(english_to_hindi("My name is Ramesh"))
print(hindi_to_english(english_to_hindi("My name is Ramesh")))
