#QuizApplication
1. Quiz application has the following commands
2. quiz list - List of all the available quizzes in your library
3. quiz import <path_to_quiz_JSON> - Import a new quiz from a JSON file
4. JSON Format for Quizzes should contain the following keys
questions - List of questions in the quiz
text - Question text
options - List of options for the question
.is_answer - Parameter of an option that can be true or false. Indicates whether or not that option is the correct answer.
quiz take <quiz_name> - Start taking a new quiz
When a user takes a quiz he gets a score based on the answers he got right
