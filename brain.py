from leo_API import Leo 
# Initialize the Leo instance
leo = Leo()

def askleo(prompt):
#max_tokens_to_sample is an int : 400 to 2048
    # You can use it as Llama by explicitly leaving System Prompt empty.
    system_prompt = 'you are an ai named none0 your job is to help devolopers in solving theit problems and and help them .rules : your response should be complete and well explained , if someone asked you somthing that dont have a relation with coding and programming say " im a coding ai expert i cannot help you"'
    response = leo.ask(prompt, system_prompt=system_prompt,max_tokens_to_sample=2048)
    response = response.completion
    print(response)
    return response


askleo("hello")