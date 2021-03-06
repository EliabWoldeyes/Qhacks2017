import os
import indicoio

indicoio.config.api_key = '1ad4dd5e8b4acb277778d9a4451e8e89'

origDir = os.getcwd()
os.chdir("snapPics")

pics = os.listdir(".")

picFeats = []

picFeats = indicoio.fer(pics)

angry = sad = neutral = surprise = fear = happy = 0.0

for pf in picFeats :
	for p in pf :
		if p == 'Angry':
			angry += pf[p]
		elif p == 'Sad':
			sad += pf[p]
		elif p == 'Neutral':
			neutral += pf[p]
		elif p == 'Surprise':
			surprise += pf[p]
		elif p == 'Fear':
			fear += pf[p]
		elif p == 'Happy':
			happy += pf[p]

avPicFeats = {"Angry":angry,"Sad":sad,"Neutral":neutral,"Surprise":surprise,"Fear":fear,"Happy":happy}

for emotion in avPicFeats :
	avPicFeats[emotion] = avPicFeats[emotion]/len(pics)
	# print(emotion) 

maxProb = max(avPicFeats.values())

# print maxProb

for k in avPicFeats.keys() :
	if avPicFeats.get(k) == maxProb :
		maxProbKey = k

observedEmotion = {maxProbKey : maxProb}

# print avPicFeats
# print(observedEmotion)

# os.system("""
#                osascript -e 'display notification "{}" with title "{}"'
#               """.format(text, title))

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    i = '-contentImage /Users/eliab/Downloads/Screen\ Shot\ 2017-02-04\ at\ 9.49.51\ PM.png'
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, i])))
    # os.system("""
    # 	osascript -e 'display notification "{}" with title "{}"' 
    # 	""".format(message,title))

# Calling the function
notify(title    = 'Eyecalm',
		subtitle = 'We feel you man',
       message  = observedEmotion.keys()[0])

# print "You are feeling: ", observedEmotion.keys()[0]



