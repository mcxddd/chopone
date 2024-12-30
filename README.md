# Chopone

一个基于 Vue.js 和 Flask 的 Web 应用程序，使用 Caddy 作为反向代理。

## 项目结构

```
chopone/
├── choponefront/         # Vue.js 前端项目
├── choponeback/         # Flask 后端项目
├── docker-compose.yml   # Docker 编排配置
└── README.md
```

## 系统要求

- Docker
- Docker Compose
- Caddy (作为独立容器运行)

## 部署说明

### 1. 准备工作

1. 确保已安装 Docker 和 Docker Compose
2. 确保 Caddy 已经正确配置并运行

### 2. Caddy 配置

在 Caddy 配置文件中添加以下内容：

```
www.example.com {
    handle /api/* {
        reverse_proxy localhost:5000
    }

    handle {
        root * /srv/www
        file_server
        try_files {path} /index.html
    }
}

chopone.com {
    redir https://www.chopone.com{uri} permanent
}
```

### 3. 创建必要的 Docker 卷

```bash
docker volume create chopone_frontend_dist
```

### 4. 部署服务

1. 克隆项目：

```bash
git clone <项目仓库地址>
cd chopone
```

2. 启动服务：

```bash
docker compose down

docker compose up -d
```

3. 验证服务：

```bash
# 检查服务状态
docker compose ps

# 检查后端健康状态
curl http://localhost:5000/api/system/health
```

## 服务说明

### 前端服务 (frontend)

- 基于 Vue.js
- 构建后的静态文件存储在 `chopone_frontend_dist` 卷中
- 通过 Caddy 提供服务

### 后端服务 (backend)

- 基于 Flask
- 使用 host 网络模式运行
- 监听端口：5000
- 提供 API 服务

### 数据存储

- 上传文件存储在 `data` 卷中
- 文件会在 24 小时后自动清理

## 维护操作

### 查看日志

```bash
# 查看所有服务日志
docker compose logs

# 查看特定服务日志
docker compose logs frontend
docker compose logs backend
```

### 重启服务

```bash
docker compose restart
```

### 更新服务

```bash
# 拉取最新代码
git pull

# 重新构建并启动服务
docker compose up -d --build
```

### 停止服务

```bash
docker compose down
```

## 注意事项

1. 确保 Caddy 容器能够访问 `chopone_frontend_dist` 卷
2. 后端服务使用 host 网络模式，确保端口 5000 未被占用
3. 上传的文件会在 24 小时后自动删除
4. 确保服务器防火墙允许必要端口的访问（80/443）

## 故障排除

1. 如果无法访问 API：

   - 检查后端服务是否正常运行
   - 验证 Caddy 配置是否正确
   - 测试 `curl http://localhost:5000/api/system/health`

2. 如果前端文件无法访问：
   - 检查 `chopone_frontend_dist` 卷是否正确挂载
   - 验证前端构建是否成功
   - 检查 Caddy 的静态文件配置

## 技术栈

- 前端：Vue.js
- 后端：Flask
- 反向代理：Caddy
- 容器化：Docker
- 编排：Docker Compose
