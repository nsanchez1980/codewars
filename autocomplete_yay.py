def autocomplete(input_, dictionary):
    x = 0
    output = []
    amount = 0
    buffer = ""
    if not input_.isalpha():
        while x < len(input_):
            if input_[x].isalpha():
                buffer = buffer + input_[x]
            x = x + 1
    else:
        buffer = input_
    for word in dictionary:
        if word.lower().startswith(buffer.lower()) and amount<5:
            output.append(word)
            amount = amount + 1       
    return output


dictionary=[ 'abnormal',
  'arm-wrestling',
  'absolute',
  'airplane',
  'airport',
  'amazing',
  'apple',
  'ball' ]

print(autocomplete('ai', dictionary))#, ['airplane','airport'])
print(autocomplete('a', dictionary))#, ['abnormal','arm-wrestling','absolute','airplane','airport'])