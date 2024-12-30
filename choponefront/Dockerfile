FROM node:18.19-alpine3.18
WORKDIR /app
RUN apk add --no-cache python3 make g++
COPY package*.json ./
RUN npm install --verbose
COPY . .
RUN ls -la
RUN npm run build || (echo "Build failed with error code $?" && ls -la && cat $(find . -name "*.log" 2>/dev/null) && exit 1)
CMD ["tail", "-f", "/dev/null"] 