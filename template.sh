# make structure
mkdir -p src
mkdir -p research

## creating a files

touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch env
touch src/app.py
touch src/setup.py
touch research/trails.ipynb

touch requirements.txt(
"fastapi
uvicorn
langchain
openai
pinecone-client
python-dotenv
requests
tiktoken
pydantic
jinja2
azure-ai-textanalytics")

echo="Directory and files created successfully!."