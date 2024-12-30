import { ref } from "vue";
import type { Toast } from "@/types/pdf";

const toasts = ref<Toast[]>([]);
let nextId = 0;

export function useToast() {
  const showToast = (
    message: string,
    type: "success" | "error" = "success",
    duration: number = 5000
  ) => {
    const id = nextId++;
    const toast: Toast = {
      message,
      type,
      id,
      duration,
    };
    toasts.value.push(toast);

    // 自动移除
    setTimeout(() => {
      removeToast(id);
    }, duration);
  };

  const removeToast = (id: number) => {
    const index = toasts.value.findIndex((t) => t.id === id);
    if (index > -1) {
      toasts.value.splice(index, 1);
    }
  };

  return {
    toasts,
    showToast,
    removeToast,
  };
}
