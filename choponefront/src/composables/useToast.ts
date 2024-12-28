import { ref } from "vue";

interface Toast {
  message: string;
  type: "success" | "error";
  id: number;
}

const toasts = ref<Toast[]>([]);
let nextId = 0;

export function useToast() {
  const showToast = (
    message: string,
    type: "success" | "error" = "success"
  ) => {
    const id = nextId++;
    const toast = {
      message,
      type,
      id,
    };
    toasts.value.push(toast);

    // 3秒后自动移除
    setTimeout(() => {
      const index = toasts.value.findIndex((t) => t.id === id);
      if (index > -1) {
        toasts.value.splice(index, 1);
      }
    }, 3000);
  };

  return {
    toasts,
    showToast,
  };
}
