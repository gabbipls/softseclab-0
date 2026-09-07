#Chooses the base image for the Docker container, this is where we put nicos repo so it builds from it etc.....
FROM python:3.14-slim 

#Sets the working directory inside the container to /app. All subsequent commands will be run from this directory.
WORKDIR /app

#Copies the requirements.txt file from the host machine to the working directory inside the container. This file contains a list of Python dependencies needed for the application (like what we have in the environment here in vscode
COPY src/requirements.txt .

#Installs the Python dependencies listed in requirements.txt using pip. The --no-cache-dir option is used to prevent caching of the installed packages, which helps reduce the size of the Docker image.
RUN pip install --no-cache-dir -r requirements.txt

#Copies the application into the container. First source on the computer, then destination inside the docker image 
COPY src/ ./src/

#Exposes port 5000 on the container
EXPOSE 5000

#Starts the Flask application by running the api.py script using Python. The CMD instruction specifies the command to run when the container starts.
CMD ["python", "src/api.py"]