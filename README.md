#Karishma-Srivastava-MedicalChatbot-LLM-Pinecone-Langchain-FastAPI-Azure

## how to run

## steps
clone the repository

''' bash
git clonehttps://github.com/Karishma-Srivastava/Karishma-Srivastava-MedicalChatbot-LLM-Pinecone-Langchain-FastAPI-Azure.git
'''

## step 1 create a conda environment after opening the repository 

'''bash
conda create -n medicalbot python=3.11 -y
'''

'''bash 
conda activate medicalbot
'''

## step 2 install requirements
'''bash
pip install -r requirements.txt
'''




Azure Deployment with GitHub Actions (CICD)
1. Login to Azure Portal

Go to https://portal.azure.com and sign in with your Azure account.

2. Create Azure Resources

We will use the following Azure services for deployment:

Azure Container Registry (ACR) – To store Docker images

Azure Web App for Containers – To host the Flask app inside a container

3. Create Azure Container Registry (ACR)

In the Azure Portal, search for Container Registry → Create

Choose:

Resource Group: medicalbot-group

Registry Name: medicalbotregistry

SKU: Basic

Once created, note down the Login Server name, e.g.

medicalbotregistry.azurecr.io
4. Build & Push Docker Image to ACR

Run these commands locally or in GitHub Actions workflow:

# Login to Azure
az login
az acr login --name medicalbotregistry


# Build Docker image
docker build -t medicalbotregistry.azurecr.io/medicalbot:latest .


# Push image to ACR
docker push medicalbotregistry.azurecr.io/medicalbot:latest
5. Create Azure Web App for Containers

Go to Create a Resource → Web App

Choose:

Publish: Docker Container

OS: Linux

Region: east us

Image Source: Azure Container Registry

Select your medicalbotregistry and medicalbot:latest image

Once created, note the Web App URL, e.g.

https://medicalbot.azurewebsites.net
6. Configure Environment Variables in Azure

In your Web App:

Go to Settings → Configuration → Application settings

Add the following keys:

PINECONE_API_KEY

OPENAI_API_KEY

Click Save and Restart.

7. Setup GitHub Secrets for CICD

In your GitHub repository, go to
Settings → Secrets and Variables → Actions → New Repository Secret

Add:

AZURE_CREDENTIALS (JSON from az ad sp create-for-rbac)

ACR_LOGIN_SERVER (e.g., medicalbotregistry.azurecr.io)

ACR_USERNAME

ACR_PASSWORD

PINECONE_API_KEY

OPENAI_API_KEY

8. Configure GitHub Actions Workflow

Create a .github/workflows/azure-deploy.yml file:

name: Deploy to Azure Web App


on:
  push:
    branches:
      - main


jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4


      - name: Log in to Azure
        uses: azure/login@v2
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}


      - name: Build and Push Docker image to ACR
        run: |
          az acr login --name medicalbotregistry
          docker build -t ${{ secrets.ACR_LOGIN_SERVER }}/medicalbot:latest .
          docker push ${{ secrets.ACR_LOGIN_SERVER }}/medicalbot:latest


      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v3
        with:
          app-name: "medicalbot"
          images: ${{ secrets.ACR_LOGIN_SERVER }}/medicalbot:latest
✅ Done!

Your Medical Chatbot Flask app is now automatically deployed to Azure Web App every time you push to the main branch.

Access it at:
👉 https://medicalbot.azurewebsites.net
