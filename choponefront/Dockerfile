# 构建阶段
FROM node:18.19-alpine3.18 as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 生产阶段
FROM nginx:alpine
COPY --from=builder /app/dist /dist
CMD ["nginx", "-g", "daemon off;"] 