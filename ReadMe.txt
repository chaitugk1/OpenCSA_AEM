(1) INITIAL SET UP

# Create clone from git
git clone -b master https://github.com/chaitugk1/OpenCSA_AEM.git

# Create environment and install necessary libraries
 python -m venv aem_env
.\aem_env\Scripts\activate
 pip install -r requirements.txt

#First time GIT push
git remote add origin https://github.com/chaitugk1/OpenCSA_AEM.git
git push -u origin master

(2) Push the local changes to repository

# Update git and push
git status
git add .
git status
git commit -m "Added view and template for detailed blog post as well as CSS for the site."
git push https://github.com/chaitugk1/OpenCSA_AEM.git

(3) Pull a branch/repository from github
#for first time
git remote add origin https://github.com/chaitugk1/OpenCSA_AEM.git
git pull origin master
 

# Converting Qt Designer 
pyside2-uic.exe layout.ui > MainWindow.py
