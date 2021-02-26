def underscore_delete(text):
	for i in text:
		if i == '_':
			new_text = text.replace(i, ' ')
			return new_text

def underscore_add(text):
	for i in text:
		if i == ' ':
			new_text = text.replace(i, '_')
			return new_text

