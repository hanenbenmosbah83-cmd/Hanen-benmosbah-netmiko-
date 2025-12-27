# Mon Projet Netmiko

## Description du projet
Ce projet illustre l’utilisation de Git pour la gestion de versions et de Netmiko pour l’automatisation réseau.  
Nous avons simulé des manipulations Git classiques : création de dépôts, commits, branches, fusion, et interaction avec un dépôt distant GitHub.  
Le script Python `main.py` se connecte à un routeur Cisco via Netmiko, récupère certaines informations et les enregistre dans un fichier.

---

## Structure du projet
- `README.md` : ce fichier détaillant les commandes et explications.
- `main.py` : script Python utilisant Netmiko.
- `interfaces.txt` : fichier généré contenant les informations des interfaces réseau (après exécution de `main.py`).

---



### 1. Initialisation d’un dépôt local
```bash
mkdir hanen-benmosbah-netmiko      
cd hanen-benmosbah-netmiko         
git init   
   ```  
### 2. Ajout et commit de fichiers   
```bash         
git add README.md             
git commit -m "Ajout du fichier README" 

git add main.py               
git commit -m "Ajout du script Python principal"
```
### 3.Visualiser les commits
```bash
git log

```
### 4.Gestion des branches
```bash
git checkout -b feature/netmiko   
git checkout main            
git merge feature/netmiko        
```
### 5.Gestion d’un dépôt distant (GitHub)  
```bash
git remote add origin  https://github.com/hanenbenmosbah83-cmd/Hanen-benmosbah-netmiko-.git
git branch -M main                 
git push -u origin main          

```
### 6.Travailler avec une branche distante
```bash
git fetch origin                   
git checkout -b feature/salut origin/feature/salut  
git commit -m "Ajout de la fonction dire_salut"
git push origin feature/salut    
```
### 7.Synchronisation après fusion sur GitHub
```bash
git checkout main
git pull origin main             

```
