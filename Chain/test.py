student_answer = """
   Python is a high-level programming language.
   It is widely used in web development, data science,
   and artificial intelligence.
"""

def clean_ans(answer):
    return answer.strip()

clean_answer = clean_ans(student_answer)

def words(clean_ans):
    return len (clean_ans.split())

word_count = words(clean_answer)

def generate_feedback(answer,word_count): 
    return f"""
    The answer contains {word_count} words.
    The student correctly explained python and mentioned some important applicatin areas.

      """

feedback = generate_feedback(clean_answer,word_count)



def format_feedback(feedback): 
    return feedback.strip().upper()