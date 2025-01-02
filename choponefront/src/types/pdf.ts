export interface CompressionResult {
  originalSize: string;
  compressedSize: string;
  compressionRatio: string;
  downloadPath: string;
}

export type CompressionLevel = "HIGH" | "MEDIUM" | "LOW";

export interface QualityOption {
  value: CompressionLevel;
  label: string;
  description: string;
}
