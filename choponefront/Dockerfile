FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --verbose
COPY . .
RUN npm run build || (echo "Build failed" && npm run build --verbose && exit 1)
CMD ["tail", "-f", "/dev/null"] 