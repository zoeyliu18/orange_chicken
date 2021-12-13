import argparse, io, os

language_maps = {'eng':'english', 'fin':'finnish', 'ger': 'german', 'ind': 'indonesian', 'mayo': 'mayo', 'nahuatl': 'nahuatl', 'persian': 'persian', 'ru': 'russian', 'tur': 'turkish', 'wixarika': 'wixarika', 'zul': 'zulu'}

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = '*/experiments/')
	parser.add_argument('--lang', type = str, help = 'language')

	args = parser.parse_args()

	lang = args.lang
	lang_dir = language_maps[lang]

	for replacement in ['with', 'without']:
		for i in range(1, 51):
			train_data = []
			for size in os.listdir(args.input + lang_dir + '/'):


