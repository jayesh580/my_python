'''#to create new virtual machine
virtualenv myprojectenv
#to launch or activate virtual environment
source .\myprojectenv\Script\activate.ps1
#all packages installed in virtual machine not main machine
pip install flask
pip install pygame
pip install pandas
#it will be deactivate virtual machine and go to main machine
deactivate
#shows all packages which installed in present machine
pip freeze
#copy all packages which installed in machine and paste it in text file
pip freeze > copy.txt
#install all packages which name contains in the text file
pip install -r .\copy.txt
'''