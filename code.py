'''Using Apache 2.0 Open Source Agreement.'''
import easygui
import webbrowser
while True:
	a = easygui.choicebox('Menu','HTML Builder',('Start Build','View HTML Files'))
	print(a)
	if a == 'Start Build':
		f = open(easygui.filesavebox(),'w',encoding='utf-8')
		if easygui.choicebox('Do you want to use a background?(Picture)','HTML Builder',['Yes','No']) == 'Yes':
			bg = easygui.enterbox("Enter picture's name",'HTML Builder')
			fr = f'''
<!DOCTYPE HTML>
<html background="{bg}">
<head>
<meta charset='utf-8'>
</head>
<body>
			'''
			print(fr)
		else:
			fr = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset='utf-8'>
</head>
<body>
			'''
			print(fr)
		while True:
			d = easygui.choicebox('What do you want to add now?','HTML Builder',('Title','Texts','Finish'))
			if d == 'Title':
				input1 = easygui.enterbox('The title','HTML Builder')
				fr += f'\n<h1>{input1}</h1>'
			elif d == 'Texts':
				input1 = easygui.enterbox('The text','HTML Builder')
				fr += f'\n<p>{input1}</p>'
			elif d == 'Finish':
				fr += '''
</body>
</html>
				'''
				f.write(fr)
				f.close()
				break
	else:
		webbrowser.open_new_tab(easygui.fileopenbox('HTML Builder'))
	break

		
