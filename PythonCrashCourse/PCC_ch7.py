# prompt = "\nEnter something here: "
# prompt += "\nEnter 'quit' to exit."
#
# active = True
# while active:
#     message = raw_input(prompt)
#
#     if message.lower() == 'quit':
#         active = False
#     else:
#         print message
#
# #################
# prompt = '\nEnter city: '
# prompt += "\nEnter 'quit' to exit."
#
# while True:
#     city = raw_input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print 'Destination is: ' + city.title() + '.'
########

# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
#     print (current_num)
#
# ##########
#
# unconfirmed = ['Johnny', "Bridge", "Yeti"]
# confirmed = []
#
# while unconfirmed:
#     current = unconfirmed.pop()
#     print 'verifying user: ' + current.title()
#     confirmed.append(current)
#
# print '\nThe following have been confirmed: '
# for user in confirmed:
#     print user
# print confirmed
#
#
# pets = ['dog', 'cat', 'turtle', 'rabbit', 'cat', 'cat', 'fish', 'pig']
# print pets
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print pets

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = raw_input("enter name: ")
#     response = raw_input("enter climb: ")
#
#     responses[name] = response
#
#     repeat = raw_input("add another person? (yes/no) ")
#     if repeat.lower() == 'no':
#         polling_active = False
#
# print "\n ---Poll Results---"
# for name, response in responses.items():
#     print name.title() + ' will climb ' + response.title() + "."



