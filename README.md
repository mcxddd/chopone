# Chopone

一个在线工具集合网站，目前支持 PDF 压缩功能。

## 项目结构

```
chopone/
├── choponeback/     # 后端项目 (Python Flask)
└── choponefront/    # 前端项目 (Vue 3 + TypeScript)
```

## 功能特性

- PDF 压缩
  - 支持三种压缩级别（轻度、标准、极限）
  - 支持中文文件名
  - 自动文件清理
  - 实时压缩率显示

## 技术栈

### 前端 (choponefront)

- Vue 3.3.11
- TypeScript 5.2.2
- Vite 5.0.8
- Vue Router 4.2.5
- 原子化 CSS

### 后端 (choponeback)

- Python 3.11
- Flask 2.3.3
- PyPDF2[image] 3.0.1
- Pillow 10.1.0
- Flask-CORS 4.0.0
- Gunicorn 21.2.0

## 开发环境设置

### 前端开发

1. 进入前端项目目录：

```bash
cd choponefront
```

2. 安装依赖：

```bash
npm install
```

3. 启动开发服务器：

```bash
npm run dev
```

开发服务器默认运行在 http://localhost:5173

4. 构建生产版本：

```bash
npm run build
```

构建后的文件将生成在 `dist` 目录中

### 后端开发

1. 进入后端项目目录：

```bash
cd choponeback
```

2. 创建并激活 Python 虚拟环境：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# Linux/Mac
source venv/bin/activate
```

3. 安装项目依赖：

```bash
pip install -r requirements.txt
```

4. 创建必要的目录：

```bash
# Windows
mkdir uploads downloads
# Linux/Mac
mkdir -p uploads downloads
```

5. 运行开发服务器：

```bash
python run.py
```

开发服务器默认运行在 http://localhost:5000

## 环境要求

### 前端环境

- Node.js 18+
- npm 7+

### 后端环境

- Python 3.11+
- pip
- 虚拟环境工具 (venv)

## API 文档

### PDF 压缩 API

#### POST /api/utility/compress-pdf

压缩 PDF 文件

请求参数：

- `file`: PDF 文件 (multipart/form-data)
- `compression_level`: 压缩级别 ('HIGH'|'MEDIUM'|'LOW')
  - HIGH: 轻度压缩，保持较高质量
  - MEDIUM: 标准压缩，平衡质量和大小
  - LOW: 极限压缩，优先考虑文件大小

响应示例：

```json
{
  "success": true,
  "message": "PDF compressed successfully",
  "data": {
    "file_path": "/api/download/compressed_example.pdf",
    "original_size": 1000000,
    "compressed_size": 500000,
    "compression_ratio": "50.0%"
  }
}
```

## Docker 部署

### 前置条件

- Docker 20.10.0+
- Docker Compose 2.0.0+
- Caddy 2.0.0+（作为反向代理服务器）

### 部署步骤

1. 克隆项目到服务器：

```bash
git clone <repository-url>
cd <project-directory>
```

2. 创建必要的目录：

```bash
# 创建数据目录
mkdir -p data/uploads data/downloads
```

3. 在 Caddy 配置文件中添加反向代理规则：

```caddyfile
your-domain.com {
    # 前端静态文件（Vue 构建后的文件）
    # Docker volume 路径说明：
    # - Linux 默认路径：/var/lib/docker/volumes/chopone_frontend_dist/_data
    # - 使用 docker volume inspect chopone_frontend_dist 查看实际路径
    root * /var/lib/docker/volumes/chopone_frontend_dist/_data
    file_server
    try_files {path} /index.html

    # 后端 API 反向代理
    handle /api/* {
        reverse_proxy localhost:5000
    }
}
```

4. 启动 Docker 服务：

```bash
# 首次启动（构建镜像并启动容器）
docker-compose up -d --build

# 后续启动（直接启动容器）
docker-compose up -d
```

5. 验证服务状态：

```bash
# 检查容器状态
docker-compose ps

# 检查服务日志
docker-compose logs
```

### 目录说明

Docker 部署会创建两个数据卷：

- `chopone_frontend_dist`: 存储前端构建文件
  - 实际路径：使用 `docker volume inspect chopone_frontend_dist` 查看
- `chopone_data`: 存储 PDF 文件
  - 上传文件目录：`/app/data/uploads`
  - 下载文件目录：`/app/data/downloads`

### 环境变量配置

1. 前端环境变量
   在 `choponefront/.env` 文件中配置：

```env
# 生产环境 API 地址
VITE_API_BASE_URL=http://your-domain.com/api
```

2. 后端环境变量
   在 `docker-compose.yml` 中已配置：

- `FLASK_ENV`: 运行环境（默认：production）
- `UPLOAD_FOLDER`: 上传文件存储路径（默认：/app/data/uploads）
- `DOWNLOAD_FOLDER`: 下载文件存储路径（默认：/app/data/downloads）

### 维护操作说明

1. 查看服务日志：

```bash
# 查看所有服务日志
docker-compose logs

# 查看前端服务日志
docker-compose logs frontend

# 查看后端服务日志
docker-compose logs backend

# 实时查看日志
docker-compose logs -f
```

2. 重启服务：

```bash
# 重启所有服务
docker-compose restart

# 重启单个服务
docker-compose restart frontend
docker-compose restart backend
```

3. 更新部署：

```bash
# 1. 停止当前服务
docker-compose down

# 2. 拉取最新代码
git pull

# 3. 重新构建并启动服务
docker-compose up -d --build
```

4. 数据管理：

```bash
# 停止服务
docker-compose down

# 查看数据卷
docker volume ls | grep chopone

# 备份数据卷（如果需要）
docker run --rm -v chopone_data:/source -v $(pwd)/backup:/backup alpine tar czf /backup/data.tar.gz -C /source .

# 清理数据卷（谨慎使用）
docker volume rm chopone_data
docker volume rm chopone_frontend_dist
```

5. 故障排查：

```bash
# 检查容器状态
docker-compose ps

# 检查容器资源使用
docker stats

# 进入容器排查问题
docker-compose exec frontend sh
docker-compose exec backend sh
```

## 许可证

MIT License
