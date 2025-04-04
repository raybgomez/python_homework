# Task 1

import traceback

def write_diary():
    try:
        with open("diary.txt", "a") as file:
            prompt = "What happened today?"
            while True:
                entry = input(prompt)
                file.write(entry + "\n")

                if entry.lower() == "done for now":
                    break

                prompt = "What else?"

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            for trace in trace_back
        ]

        print(f"An exception occurred: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print(f"Stack trace: {stack_trace}")

    __name__ == "_main_"
    write_diary()

    # Task 2
    