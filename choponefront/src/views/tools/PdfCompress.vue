<template>
  <div class="pdf-compress">
    <div class="compress-container">
      <div v-if="!compressionResult" class="compress-section">
        <div class="quality-options">
          <div
            v-for="option in qualityOptions"
            :key="option.value"
            class="quality-option"
            :class="{ active: selectedLevel === option.value }"
            @click="selectedLevel = option.value"
          >
            <div class="option-header">
              <span class="option-title">{{ option.label }}</span>
            </div>
            <p class="option-description">{{ option.description }}</p>
          </div>
        </div>

        <div
          class="upload-area"
          @drop.prevent="handleDrop"
          @dragover.prevent
          @dragenter.prevent="isDragging = true"
          @dragleave.prevent="isDragging = false"
          :class="{ dragging: isDragging }"
        >
          <div v-if="!selectedFile" class="upload-prompt">
            <div class="upload-icon">📄</div>
            <div class="text">拖放PDF文件到此处，或点击选择文件</div>
            <input
              type="file"
              accept=".pdf"
              @change="handleFileSelect"
              class="file-input"
            />
          </div>
          <div v-else class="file-info">
            <div class="file-name">{{ selectedFile.name }}</div>
            <div class="file-size">{{ formatFileSize(selectedFile.size) }}</div>
            <button @click="selectedFile = null" class="clear-btn">清除</button>
          </div>
        </div>

        <button
          @click="startCompression"
          :disabled="!selectedFile || isCompressing"
          class="compress-btn"
        >
          {{ isCompressing ? "压缩中..." : "开始压缩" }}
        </button>
      </div>

      <div v-else class="result-section">
        <div class="result-card">
          <div class="result-header">
            <div class="success-icon">✓</div>
            <h3>压缩完成</h3>
          </div>
          <div class="result-details">
            <div class="size-comparison">
              <div class="original-size">
                <div class="size-label">原始大小</div>
                <div class="size-value">
                  {{ compressionResult.originalSize }}
                </div>
              </div>
              <div class="arrow">→</div>
              <div class="compressed-size">
                <div class="size-label">压缩后大小</div>
                <div class="size-value">
                  {{ compressionResult.compressedSize }}
                </div>
              </div>
            </div>
            <div class="compression-ratio">
              <div class="ratio-label">压缩率</div>
              <div class="ratio-value">
                {{ compressionResult.compressionRatio }}
              </div>
            </div>
          </div>
          <div class="result-actions">
            <a
              :href="compressionResult.downloadPath"
              class="download-btn"
              download
              >下载压缩后的文件</a
            >
            <button @click="resetCompression" class="new-file-btn">
              压缩新文件
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useToast } from "@/composables/useToast";
import type {
  CompressionResult,
  CompressionLevel,
  QualityOption,
} from "@/types/pdf";

const { showToast } = useToast();

const showError = (message: string) => showToast(message, "error");
const showSuccess = (message: string) => showToast(message, "success");

const selectedFile = ref<File | null>(null);
const isCompressing = ref(false);
const isDragging = ref(false);
const compressionResult = ref<CompressionResult | null>(null);

const formatFileSize = (bytes: number): string => {
  if (bytes === 0) return "0 B";
  const k = 1024;
  const sizes = ["B", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${(bytes / Math.pow(k, i)).toFixed(2)} ${sizes[i]}`;
};

const qualityOptions: QualityOption[] = [
  {
    value: "HIGH",
    label: "轻度压缩",
    description: "保持较好的图片质量，文件大小适度减小",
  },
  {
    value: "MEDIUM",
    label: "标准压缩",
    description: "显著压缩文件大小，图片质量适中",
  },
  {
    value: "LOW",
    label: "极限压缩",
    description: "最大程度压缩文件大小，图片质量降低",
  },
];

const selectedLevel = ref("MEDIUM"); // 默认选择标准压缩

const handleDrop = (e: DragEvent) => {
  const files = e.dataTransfer?.files;
  if (files && files.length > 0) {
    if (files[0].type === "application/pdf") {
      selectedFile.value = files[0];
    } else {
      showError("请选择PDF文件");
    }
  }
};

const handleFileSelect = (e: Event) => {
  const input = e.target as HTMLInputElement;
  const files = input.files;
  if (files && files.length > 0) {
    if (files[0].type === "application/pdf") {
      selectedFile.value = files[0];
    } else {
      showError("请选择PDF文件");
    }
  }
};

const resetCompression = () => {
  selectedFile.value = null;
  compressionResult.value = null;
};

const startCompression = async () => {
  if (!selectedFile.value) {
    showError("请先选择要压缩的PDF文件");
    return;
  }

  isCompressing.value = true;
  const formData = new FormData();
  formData.append("file", selectedFile.value);
  formData.append("compression_level", selectedLevel.value);

  try {
    const response = await fetch("/api/utility/compress-pdf", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.message || `请求失败: ${response.status}`);
    }

    if (!result.success) {
      throw new Error(result.message || "PDF压缩失败");
    }

    compressionResult.value = {
      originalSize: formatFileSize(result.data.original_size),
      compressedSize: formatFileSize(result.data.compressed_size),
      compressionRatio: result.data.compression_ratio,
      downloadPath: result.data.file_path,
    };
    showSuccess("PDF压缩成功");
  } catch (error) {
    console.error("PDF压缩错误:", error);
    showError(
      `PDF压缩错误: ${error instanceof Error ? error.message : "未知错误"}`
    );
    compressionResult.value = null;
  } finally {
    isCompressing.value = false;
  }
};
</script>

<style scoped>
.pdf-compress {
  min-height: calc(100vh - 200px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.compress-container {
  width: 100%;
  max-width: 800px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  padding: 40px;
}

.quality-options {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  margin-bottom: 24px;
}

.quality-option {
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px;
  cursor: pointer;
  transition: all 0.3s;
}

.quality-option.active {
  border-color: #409eff;
  background: #f0f9ff;
}

.quality-option .option-header {
  margin-bottom: 8px;
}

.quality-option .option-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #2c3e50;
}

.quality-option .option-description {
  font-size: 0.8rem;
  color: #64748b;
  line-height: 1.3;
  margin-top: 4px;
}

.upload-area {
  border: 2px dashed #e2e8f0;
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  transition: all 0.3s;
  background: #f8fafc;
  margin-bottom: 24px;
}

.upload-area.dragging {
  border-color: #409eff;
  background-color: rgba(64, 158, 255, 0.05);
}

.upload-icon {
  font-size: 48px;
  margin-bottom: 16px;
  color: #64748b;
}

.upload-prompt {
  position: relative;
}

.upload-prompt .text {
  color: #64748b;
  margin-bottom: 8px;
}

.file-input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.file-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.file-name {
  font-weight: 500;
  color: #2c3e50;
}

.file-size {
  color: #64748b;
  font-size: 0.9rem;
}

.compress-btn {
  width: 100%;
  padding: 12px;
  background: #409eff;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.compress-btn:disabled {
  background: #a0cfff;
  cursor: not-allowed;
}

.result-card {
  text-align: center;
  padding: 32px;
}

.result-header {
  margin-bottom: 24px;
}

.success-icon {
  font-size: 48px;
  color: #10b981;
  margin-bottom: 16px;
}

.result-header h3 {
  color: #2c3e50;
  font-size: 1.5rem;
  margin: 0;
}

.result-details {
  margin-bottom: 32px;
}

.size-comparison {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  margin-bottom: 24px;
}

.arrow {
  color: #64748b;
  font-size: 24px;
}

.size-label,
.ratio-label {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 4px;
}

.size-value,
.ratio-value {
  color: #2c3e50;
  font-size: 1.2rem;
  font-weight: 600;
}

.compression-ratio {
  margin-top: 16px;
}

.result-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.download-btn,
.new-file-btn {
  padding: 12px;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s;
  text-align: center;
  cursor: pointer;
}

.download-btn {
  background: #10b981;
  color: white;
  text-decoration: none;
}

.download-btn:hover {
  background: #059669;
}

.new-file-btn {
  background: #f1f5f9;
  color: #64748b;
  border: none;
}

.new-file-btn:hover {
  background: #e2e8f0;
}

.clear-btn {
  padding: 4px 12px;
  border-radius: 6px;
  background: #ef4444;
  color: white;
  border: none;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s;
}

.clear-btn:hover {
  background: #dc2626;
}
</style>
