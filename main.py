from fastapi import FastAPI, Depends, HTTPException, status
import pandas as pd
from pydantic import BaseModel
from typing import List, Optional
import random

#Instance de l'application
api = FastAPI (
    title = "FastAPI Evaluation",
    description= "Rendu de NELLY GUEPNANG.",
    version="1.0.0"
)

#Lecture du fichier csv
df = pd.read_csv('questions.csv')

#Conversion de mon DataFrame en liste de dictionnaires pour faciliter le filtrage
list_questions = df.to_dict('records')

#Création des modèles Pydantic pour structurer les données
class Question(BaseModel):
    question : str
    subject : str
    use : str
    correct : List[str]
    responseA : str
    responseB : str
    responseC : str
    responseD : Optional[str]
class NewQuestion(BaseModel):
    question: str
    subject: str
    correct: List[str]
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str]
class UserCredentials(BaseModel):
    username: str
    password: str
class LoginCredentials(BaseModel):
    username: str
    password: str
class AdminCredentials(BaseModel):
    admin_username: str
    admin_password: str

# Dictionnaire pour l'authentification basique
users_db = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
}

#Fonction d'authentification
def authenticate_user(credentials: UserCredentials):
    if users_db.get(credentials.username) == credentials.password:
        return True
    return False

#Endpoint de base pour verifier que l'API est fonctionnel
@api.get('/')
def get_index():
    return {
        'message' : 'Bienvenue sur mon API'
    }

#Endpoint d'authentification
@api.post("/login/")
async def login(credentials: UserCredentials):
    if authenticate_user(credentials):
        return {"message": "Connexion réussie"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Identifiants incorrects"
    )

#Endpoint pour recuperer les questions
@api.get('/questions/')
def get_questions(use: str, subject: str, number: int =10):
    #filtrage des questions en fonction de 'use' et 'subject'
    questions_filtre = [q for q in list_questions if q['use'] == use and q['subject'] == subject]
    if not questions_filtre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aucune question trouvée"
        )
    return random.sample(questions_filtre, min(number, len(questions_filtre)))

#Endpoint pour l'administration : création de nouvelles questions
@api.post("/admin/questions/")
async def create_question(question: NewQuestion, credentials: AdminCredentials = Depends()):
    if credentials.admin_username != 'admin' or credentials.admin_password != '4dm1N':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Accès refusé"
        )
    # Conversion du modèle Pydantic en dictionnaire et ajout à la liste des questions
    question_dict = question.dict()
    list_questions.append(question_dict)
    return {"message": "Question ajoutée avec succès"}

