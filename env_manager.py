#=====conda virtual env=========
conda update conda  ###updates conda
conda install <package_name>
conda uninstall <package_name>
conda update <package_name>
conda --version
conda env list
conda create --name <your_env_name> python=3.6 pandas numpy scipy
activate <your_env_name>
deactivate <your_env_name>
conda env remove --name <your_env_name>

#====venv with pip===========
py -m venv your_env_name #create new environment named 'your_env_name'

....\your_env_name\scripts\activate #activate new environment

py -m pip install <file_with_dependencies> #install packages and dependencies

deactivate #leaves the environment


#=============Types of Environment Managers======================
pip venv
conda
virtual env wrapper