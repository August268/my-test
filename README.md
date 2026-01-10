# my-test
## Description
This project pulls articles using Zendesk API, convert them to markdown files, turn each file into chunks and upload them to a vector store in OpenAI

## How to set up locally
### Step 1: Clone the project

```
  git clone https://github.com/August268/my-test.git
```

### Step 2: Create a virtual environment

```
  python -m venv .venv
```

### Step 3: Activate the virtual environment

- On Windows (Command Prompt)

```
  venv\Scripts\activate
```

- On macOS and Linux

```
  source venv/bin/activate
```

### Step 4: Install packages

```
  pip install -r requirements.txt
```

### Step 5: Set up the environment variables
Here you create an OpenAI platform account and add a .env file in the project folder. This is what you need to add in the .env file:

```
  OPENAI_API_KEY=<your-openai-api-key>
  OPENAI_VECTOR_STORE_NAME=<name-of-the-vector-name-that-you-want> 
  ARTICLE_MARKDOWN_OUTPUT=files
```

### Step 5: Run main.py

```
  python main.py
```

### Step 6: Create an assistant on OpenAI playground and attach it to the created vector store
- Go to the [vector storage tab](https://platform.openai.com/storage/vector_stores/) on OpenAI platform
- Select the vector storage created by our project
- Click the create assistant button
!(<img width="1696" height="720" alt="image" src="https://github.com/user-attachments/assets/1f20610a-8e3e-4ab7-81da-ddf58915f4e0" />)

## You're done!
Now you can go to the assistant tab, click edit button and start chatting with it.

You can also give it instructions to define the the format of the assistant's answers.

## Chunking strategy

I basically split each article by the header 2 tag. After that, I have each chunk compared to the MAX_CHARS (maximum number of characters) I set.

If the chunk size is over the limit, I will try and split the chunk by paragraphs until each chunk size is below MAX_CHARS

## Playground answers from my assistant
<img width="1187" height="801" alt="image" src="https://github.com/user-attachments/assets/7dca3747-c339-44c2-a1b5-31adc2f06fae" />
