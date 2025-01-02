import { ref, nextTick } from "vue";

export function useScroll() {
  const containerRef = ref<HTMLElement | null>(null);

  const scrollToBottom = async () => {
    await nextTick();
    if (containerRef.value) {
      containerRef.value.scrollTop = containerRef.value.scrollHeight;
    }
  };

  return {
    containerRef,
    scrollToBottom,
  };
}
