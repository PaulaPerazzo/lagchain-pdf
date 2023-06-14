# PDF Question Answering with Lanchain AI

This is a project that uses the Lanchain AI model from OpenAI to answer questions related to a PDF file uploaded by the user. The application is built using Python and Streamlit.

## Technologies Used
 - Lanchain AI (from OpenAI)
 - Python
 - Streamlit

## Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running the following command:
  ```pip install -r requirements.txt```

## How to Run the Application
1. Ensure that you have the necessary dependencies installed.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command to start the application:
```streamlit run app.py```
5. The application will be launched in your default browser.

## How to Use
1. Once the application is running, you will see a header titled "Ask your PDF."
2. Click on the "Upload your PDF" button and select a PDF file to upload.
3. After uploading the PDF, the application will process the file and extract the text.
4. You can then enter a question about the PDF in the text input field labeled "Ask a question about your PDF."
5. Press Enter or click outside the input field to submit your question.
6. The application will use the Lanchain AI model to find the most relevant information from the PDF and provide an answer to your question.
7. The answer will be displayed below the input field.

Note: The application splits the PDF into smaller chunks for more efficient processing. The size of the chunks can be adjusted in the code if needed.

## Additional Notes
- The API key for the Lanchain AI model is loaded from a .env file. Make sure to provide your own OpenAI API key in the .env file.
- This project relies on the PyPDF2 library to extract text from the uploaded PDF file.
- The application uses the Streamlit library to create the user interface and interact with the user.
- The OpenAI library is used to work with the Lanchain AI model for question answering.
- The langchain package is used for text splitting, embedding, and similarity search.
- The FAISS library is used for creating a vector store from the text chunks.

Feel free to explore the code and make any necessary modifications to suit your specific requirements.

Credits to: https://www.youtube.com/watch?v=wUAUdEw5oxM&t=367s

