import { defineStore } from "pinia";
import { ref } from "vue";
import { useNetwork } from "@vueuse/core";

export const useUserStore = defineStore("user", () => {
  const ip = ref("");
  const { isOnline } = useNetwork();

  const fetchIp = async () => {
    try {
      const response = await fetch("https://api.ipify.org?format=json");
      const data = await response.json();
      ip.value = data.ip;
    } catch (error) {
      console.error("Failed to fetch IP:", error);
      ip.value = "Unable to fetch IP";
    }
  };

  return {
    ip,
    isOnline,
    fetchIp,
  };
});
