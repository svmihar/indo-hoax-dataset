import os 
from datetime import datetime

def push_this():

    today = datetime.now().strftime('[COLAB] generated at %H:%M:%S')
    print(today)
    with open('logger.txt', 'a') as fd:
        fd.write(f'\n{today}')
    # os.system('git push colab googlecolab')
    os.system('drive add_remote')

    print('manjiw!')
    
if __name__ == "__main__":
    push_this()