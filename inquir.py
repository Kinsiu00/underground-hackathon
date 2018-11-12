import inquirer

questions = [
  inquirer.Text('answer', message="where are you trying to go?")
]
answer = inquirer.prompt(questions)
if answer['answer'] != 'penn station':
    print('where is that?')
else:
    print('off we go then')
# print(answer['answer'])