# 构建阶段
FROM node:18.19-alpine3.18 as builder
WORKDIR /app
RUN apk add --no-cache python3 make g++
COPY package*.json ./
RUN npm install --verbose
COPY . .
RUN npm run build

# 生产阶段 - 这个阶段只包含构建产物
FROM scratch
COPY --from=builder /app/dist /dist
# 不需要 CMD，因为这个容器只用于提供构建文件 