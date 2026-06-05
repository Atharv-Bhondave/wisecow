```dockerfile
# Start with a clean Ubuntu Linux system
FROM ubuntu:22.04

# Install the exact tools wisecow needs: fortune, cowsay, and netcat
RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Tell the system where to find the cowsay application
ENV PATH="${PATH}:/usr/games"

# Create a folder for our app
WORKDIR /app

# Copy the wisecow script from your computer into the container
COPY wisecow.sh .
RUN chmod +x wisecow.sh

# Open port 4499 so we can visit the app
EXPOSE 4499

# Run the app when the container starts
CMD ["./wisecow.sh"]