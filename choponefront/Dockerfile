# 构建阶段
FROM node:18.19-alpine3.18 as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 生产阶段 - 这个阶段只包含构建产物
FROM scratch
COPY --from=builder /app/dist /dist 