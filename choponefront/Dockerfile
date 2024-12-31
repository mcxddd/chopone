# 构建阶段
FROM node:18.19-alpine3.18 as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 生产阶段
FROM nginx:alpine
# 复制构建产物到 nginx 默认目录
COPY --from=builder /app/dist /usr/share/nginx/html
# 复制 nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf 