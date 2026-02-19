import time

def test_exceptions(wait = 2):
    try:
        print('AI is thinking...')
    
        # We "try" to sleep for 2 seconds
        time.sleep(wait)
    
        # Imagine if the computer was shut down or the process was 
        # interrupted here—the 'except' block would catch it.
        print('AI is done')

    except Exception as e:
        # This is your catch(error) { console.log(error) }
        print(f"The AI process was interrupted: {e}")

    finally:
        # This runs no matter what (just like in JS)
        print("Cleanup: Closing connection to AI server.")