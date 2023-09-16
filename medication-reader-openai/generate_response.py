import openai
import os

API_KEY = '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'


def generate_response(test_message, examples, guidelines):
    openai.api_key = API_KEY

    model = 'text-davinci-003'
    print("TESTTTTT")
    print(os.getcwd())
    with open(test_message) as f:
        test_message_output = f.read()
        print("TTEST")
    f.close()
    with open(examples) as f:
        examples_output = f.read()
    f.close()
    with open(guidelines) as f:
        guidelines_output = f.read()
    f.close()
     
    print(test_message_output)
    


    response_prompt = '''
        An image of a medical pill bottle and prescription was fed through an OCR package and produces the text on the label. 
        Based on these snippets of text, output a simple, straightforward description of the medicine and it's uses. 
        DO NOT include the prescription number, quantity of pills inside the bottle, etc. 
        This is an example of what the output should look like:
        
    ''' + examples_output + "\n\nUse these guidelines to create the text response: \n" + guidelines_output + "\n\nFind a response for this conversation: \n" + test_message_output
    
    print(response_prompt)
    response = openai.Completion.create(
        prompt=response_prompt,
        model=model,
        max_tokens=2000,
        temperature=0.95,
        n=1,
    )
    print(response)

    f = open('medication-reader-openai/text_files/results.txt', 'w')
    f.write('')
    f = open('medication-reader-openai/text_files/results.txt', 'a')
    # change: display to front end
    result_array = []
    for result in response.choices:
        f.write(result.text)
        result_array.append(result.text)

    # formatted_str = formatArray(result_array)
    # print(formatted_str)
    # return formatted_str
    formatted_str = ""
    for r in result_array:
        formatted_str += r
    print(formatted_str)
    return formatted_str


def txtToString(file_name):
    with open(file_name) as f:
        file = f.readlines()
    str_txt = ""
    for line in file:
        str_txt += line
    return str_txt


def formatArray(array):
    formatted_messages = []
    for element in array:
        try:
            splitstring = element.split('Person 2: ')
            formatted_messages.append(splitstring[1])
        except:
            print(element + " is not valid")
        else:
            print("continue")

    str_txt = ""
    for element in formatted_messages:
        str_txt += element + "\n"
    return str(str_txt)

generate_response('medication-reader-openai/text_files/test_message.txt', 'medication-reader-openai/text_files/examples.txt', 'medication-reader-openai/text_files/text_guidelines.txt')