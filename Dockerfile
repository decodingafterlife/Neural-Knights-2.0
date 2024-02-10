# Use an official Node.js runtime as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json if they exist in the root folder
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Install Python and required Python packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install tensorflow streamlit pandas torch matplotlib google-api-python-client transformers wordcloud --break-system-packages

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["node", "index.js"]
